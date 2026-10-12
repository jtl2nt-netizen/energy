"""Controllers simulated hour by hour against actual PV and load.

- default: what an installed hybrid inverter does out of the box: solar to the
  house first, surplus charges the battery, battery covers deficits, rest to or
  from the grid. The EV charges at full power as soon as it is plugged in.
- smart_rules: the default battery, plus a smart EV charger that follows solar
  surplus and tops up in the cheapest known hours before departure (what
  simple charger apps already sell).
- mpc: the optimiser. Every hour it re-plans the next 36 hours with forecasts
  and executes the first hour, letting the battery absorb forecast errors
  around the planned grid exchange.
- perfect: the optimiser with perfect knowledge of the whole year (upper bound).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .dispatch import solve
from .household import System


def _bill(imp, exp, p_imp, p_exp):
    return float(np.sum(imp * p_imp) - np.sum(exp * p_exp))


def _result(name, imp, exp, bdis, p_imp, p_exp, deg_cost, extra=None):
    out = {
        "controller": name,
        "bill_eur": _bill(imp, exp, p_imp, p_exp),
        "import_kwh": float(imp.sum()),
        "export_kwh": float(exp.sum()),
        "batt_throughput_kwh": float(bdis.sum()),
        "wear_eur": float(bdis.sum() * deg_cost),
    }
    out["total_eur"] = out["bill_eur"] + out["wear_eur"]
    if extra:
        out.update(extra)
    return out


def _battery_follow(net, soc, sysm):
    """Self-consumption battery step. net>0 means deficit (kW). Returns (bch, bdis, soc)."""
    eta = sysm.batt_eta
    if net < 0:
        bch = min(-net, sysm.batt_kw, (sysm.batt_kwh - soc) / eta)
        return bch, 0.0, soc + bch * eta
    bdis = min(net, sysm.batt_kw, soc * eta)
    return 0.0, bdis, soc - bdis / eta


def run_rule_based(df: pd.DataFrame, sysm: System, smart_ev: bool, deg_cost: float) -> dict:
    """df columns: pv, load, p_imp, p_exp, ev_home, ev_trip, ev_need (hourly)."""
    n = len(df)
    pv, load = df.pv.values, df.load.values
    p_imp, p_exp = df.p_imp.values, df.p_exp.values
    home, trip, need = df.ev_home.values, df.ev_trip.values, df.ev_need.values
    soc_b, soc_ev = sysm.batt_kwh * 0.5, (sysm.ev_soc_max if sysm.has_ev else 0.0)
    imp = np.zeros(n); exp = np.zeros(n); bdis_a = np.zeros(n)
    next_need_idx = np.full(n, -1)
    j = -1
    for t in range(n - 1, -1, -1):
        if need[t] > 0:
            j = t
        next_need_idx[t] = j
    for t in range(n):
        soc_ev -= trip[t]
        ev = 0.0
        if sysm.has_ev and home[t] > 0:
            room = (sysm.ev_soc_max - soc_ev) / sysm.ev_eta
            if not smart_ev:
                ev = min(sysm.ev_kw, room)
            else:
                surplus = max(0.0, pv[t] - load[t])
                ev = min(sysm.ev_kw, room, surplus)
                k = next_need_idx[t]
                if k >= 0:
                    deficit = need[k] - (soc_ev + ev * sysm.ev_eta)
                    if deficit > 1e-6:
                        window = np.arange(t, k)
                        window = window[home[window] > 0]
                        hours_needed = int(np.ceil(deficit / (sysm.ev_kw * sysm.ev_eta)))
                        cheapest = window[np.argsort(p_imp[window], kind="stable")][:hours_needed]
                        if t in cheapest:
                            ev = min(sysm.ev_kw, room)
            soc_ev += ev * sysm.ev_eta
        net = load[t] + ev - pv[t]
        bch, bdis, soc_b = _battery_follow(net, soc_b, sysm)
        grid = net + bch - bdis
        imp[t] = max(grid, 0.0)
        exp[t] = min(max(-grid, 0.0), sysm.inverter_kw)
        bdis_a[t] = bdis
    name = "smart_rules" if smart_ev else "default"
    return _result(name, imp, exp, bdis_a, p_imp, p_exp, deg_cost)


def run_perfect(df: pd.DataFrame, sysm: System, deg_cost: float) -> dict:
    plan = solve(df.pv.values, df.load.values, df.p_imp.values, df.p_exp.values,
                 df.ev_home.values, df.ev_trip.values, df.ev_need.values,
                 sysm.batt_kwh * 0.5, sysm.ev_soc_max if sysm.has_ev else 0.0, sysm, deg_cost,
                 term_b=float(np.median(df.p_imp)) * sysm.batt_eta * 0.5,
                 term_ev=float(np.median(df.p_imp)) * 0.5)
    return _result("perfect", plan.imp, plan.exp, plan.bdis, df.p_imp.values, df.p_exp.values, deg_cost)


def run_mpc(df: pd.DataFrame, fc: pd.DataFrame, sysm: System, deg_cost: float, horizon: int = 36, trace: bool = False,
            pv_plan_factor: float = 1.0) -> dict:
    """Rolling-horizon controller.

    fc must hold, for each hour t, forecast arrays made at t for t..t+horizon-1:
    columns 'pv_fc', 'load_fc', 'p_imp_fc', 'p_exp_fc' with object (array) values.
    """
    n = len(df)
    pv, load = df.pv.values, df.load.values
    p_imp, p_exp = df.p_imp.values, df.p_exp.values
    home, trip, need = df.ev_home.values, df.ev_trip.values, df.ev_need.values
    soc_b, soc_ev = sysm.batt_kwh * 0.5, (sysm.ev_soc_max if sysm.has_ev else 0.0)
    imp = np.zeros(n); exp = np.zeros(n); bdis_a = np.zeros(n)
    eta = sysm.batt_eta
    tr = []
    for t in range(n):
        H = min(horizon, n - t)
        sl = slice(t, t + H)
        pv_f = fc.pv_fc.iat[t][:H]; load_f = fc.load_fc.iat[t][:H]
        pi_f = fc.p_imp_fc.iat[t][:H]; pe_f = fc.p_exp_fc.iat[t][:H]
        soc_ev_start = soc_ev - trip[t]
        need_h = need[sl].copy()
        # keep the plan feasible if the car came home emptier than required
        if sysm.has_ev:
            reach = soc_ev_start + np.cumsum(np.append(0, home[sl][:-1] * sysm.ev_kw * sysm.ev_eta))[:H]
            need_h = np.minimum(need_h, np.maximum(reach, 0))
        trip_h = trip[sl].copy(); trip_h[0] = 0.0  # already applied
        # Energy left at the end of the window is valued at no more than the
        # cheapest import price in the window, so the planner never buys
        # energy just to hold it past the horizon.
        floor = float(np.min(pi_f))
        # Planning against an optimistic solar forecast stops the controller
        # from pre-buying grid energy that a sunny day would make worthless;
        # the execution step still stores real surplus and covers real deficits.
        pv_plan = np.minimum(pv_f * pv_plan_factor, sysm.inverter_kw)
        plan = solve(pv_plan, load_f, pi_f, pe_f, home[sl], trip_h, need_h,
                     soc_b, max(soc_ev_start, sysm.ev_soc_min if sysm.has_ev else 0.0), sysm, deg_cost,
                     term_b=floor * eta * 0.9, term_ev=floor * 0.9)
        # Execute hour t with actual PV and load.
        soc_ev = soc_ev_start
        ev = plan.ev[0] if sysm.has_ev else 0.0
        ev = min(ev, (sysm.ev_soc_max - soc_ev) / sysm.ev_eta) if sysm.has_ev else 0.0
        soc_ev += ev * sysm.ev_eta
        b_plan = plan.bch[0] - plan.bdis[0]
        # Guardrail on buying battery energy from the grid: keep enough room for
        # the solar surplus a bright day could bring in the next 12 hours.
        grid_charge = min(plan.bch[0], plan.imp[0])
        if grid_charge > 1e-6:
            opt_surplus = float(np.clip(1.5 * pv_f[:12] - load_f[:12], 0, None).sum()) * eta
            max_soc = max(0.0, sysm.batt_kwh - opt_surplus)
            allowed = max(0.0, (max_soc - soc_b) / eta)
            b_plan -= grid_charge - min(grid_charge, allowed)
        deviation = (pv[t] - pv_plan[0]) - (load[t] - load_f[0])
        g_plan = plan.imp[0] - plan.exp[0]
        # Is a clearly more expensive hour coming within the horizon?
        cheap_now = H > 1 and p_imp[t] < 0.97 * float(np.max(pi_f[1:H]))
        flat = (np.ptp(pi_f) < 1e-6) and (np.ptp(pe_f) < 1e-6)
        if flat:
            # No price signal in the horizon: plain self-consumption is optimal.
            b = -(load[t] + ev - pv[t])
        elif g_plan > 0.05 and cheap_now:
            # Plan buys from the grid this hour (cheap enough): the grid absorbs
            # extra demand; any surplus that would be exported charges the battery.
            grid_if_plan = load[t] + ev + b_plan - pv[t]
            b = b_plan + max(0.0, -grid_if_plan)
        else:
            # Plan self-consumes or exports: the battery absorbs surprises.
            b = b_plan + deviation
        b = min(b, sysm.batt_kw, (sysm.batt_kwh - soc_b) / eta)
        b = max(b, -sysm.batt_kw, -soc_b * eta)
        if b >= 0:
            bch, bdis = b, 0.0
            soc_b += bch * eta
        else:
            bch, bdis = 0.0, -b
            soc_b -= bdis / eta
        grid = load[t] + ev + bch - bdis - pv[t]
        # Never discharge the battery into the grid to honour a planned export
        # that was meant to come from solar; only planned battery exports stand.
        planned_batt_export = plan.bdis[0] > 1e-6 and plan.exp[0] > 1e-6
        if bdis > 0 and grid < 0 and not planned_batt_export:
            cut = min(bdis, -grid)
            bdis -= cut; soc_b += cut / eta; grid += cut
        # Solar surplus about to be exported while export pays little: store it
        # locally (battery headroom first, then the EV), as a buffer against
        # forecast errors. Planned battery-to-grid exports are left untouched.
        unplanned = -grid if bdis == 0 else 0.0
        if unplanned > 1e-6 and p_exp[t] < 0.5 * p_imp[t]:
            extra_b = min(unplanned, sysm.batt_kw - bch, (sysm.batt_kwh - soc_b) / eta) if bdis == 0 else 0.0
            if extra_b > 0:
                bch += extra_b; soc_b += extra_b * eta; grid += extra_b; unplanned -= extra_b
            if unplanned > 1e-6 and sysm.has_ev and home[t] > 0:
                extra_ev = min(unplanned, sysm.ev_kw - ev, (sysm.ev_soc_max - soc_ev) / sysm.ev_eta)
                if extra_ev > 0:
                    ev += extra_ev; soc_ev += extra_ev * sysm.ev_eta; grid += extra_ev
        imp[t] = max(grid, 0.0)
        exp[t] = min(max(-grid, 0.0), sysm.inverter_kw)
        bdis_a[t] = bdis
        if trace:
            tr.append((plan.imp[0], plan.exp[0], plan.bch[0] - plan.bdis[0], soc_b, pv_plan[0], load_f[0]))
    res = _result("mpc", imp, exp, bdis_a, p_imp, p_exp, deg_cost)
    if trace:
        res["trace"] = pd.DataFrame(tr, columns=["plan_imp", "plan_exp", "plan_b", "soc_b", "pv_f", "load_f"], index=df.index)
        res["imp"] = imp; res["exp"] = exp
    return res
