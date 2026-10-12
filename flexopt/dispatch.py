"""Dispatch optimisation for a home with PV, a stationary battery and an EV.

A linear programme decides, for each hour of a horizon, grid import and export,
battery charge and discharge, EV charging and PV curtailment, minimising the
energy bill plus a battery wear cost. The same model serves as the
perfect-foresight benchmark (actual data, whole year) and as the planner
inside the model-predictive controller (forecasts, rolling 36-hour horizon).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog

from .household import System

N_FLOW = 6  # imp, exp, bch, bdis, ev, curt
IMP, EXP, BCH, BDIS, EV, CURT = range(N_FLOW)


@dataclass
class Plan:
    imp: np.ndarray
    exp: np.ndarray
    bch: np.ndarray
    bdis: np.ndarray
    ev: np.ndarray
    curt: np.ndarray
    soc_b: np.ndarray
    soc_ev: np.ndarray
    cost: float


def solve(
    pv: np.ndarray,
    load: np.ndarray,
    p_imp: np.ndarray,
    p_exp: np.ndarray,
    ev_home: np.ndarray,
    ev_trip: np.ndarray,
    ev_need: np.ndarray,
    soc_b0: float,
    soc_ev0: float,
    sysm: System,
    deg_cost: float = 0.02,
    term_b: float = 0.0,
    term_ev: float = 0.0,
) -> Plan:
    """Solve the dispatch LP over len(pv) hourly steps.

    term_b / term_ev value the energy left in each battery at the end of the
    horizon (EUR/kWh) so a short planning window does not empty them.
    """
    T = len(pv)
    nf = N_FLOW * T
    nb = T + 1
    nv = nf + 2 * nb
    ib = nf  # first soc_b index
    ie = nf + nb  # first soc_ev index

    def f(k, t):
        return k * T + t

    c = np.zeros(nv)
    # Tiny preference for importing later rather than now breaks ties between
    # "import now, discharge later" and "discharge now" on flat tariffs.
    c[IMP * T:(IMP + 1) * T] = p_imp + 1e-4 * (T - np.arange(T)) / T
    c[EXP * T:(EXP + 1) * T] = -p_exp
    c[BDIS * T:(BDIS + 1) * T] = deg_cost
    c[CURT * T:(CURT + 1) * T] = 1e-4  # prefer exporting at zero price over curtailing
    c[ib + T] = -term_b
    c[ie + T] = -term_ev

    rows, cols, vals, rhs = [], [], [], []
    r = 0
    # Power balance: imp + bdis - curt - ev - bch - exp = load - pv
    for t in range(T):
        for k, v in ((IMP, 1), (BDIS, 1), (CURT, -1), (EV, -1), (BCH, -1), (EXP, -1)):
            rows.append(r); cols.append(f(k, t)); vals.append(v)
        rhs.append(load[t] - pv[t]); r += 1
    eta = sysm.batt_eta
    # Battery state: soc[t+1] - soc[t] - eta*bch + bdis/eta = 0
    for t in range(T):
        rows += [r, r, r, r]; cols += [ib + t + 1, ib + t, f(BCH, t), f(BDIS, t)]
        vals += [1, -1, -eta, 1 / eta]; rhs.append(0.0); r += 1
    rows.append(r); cols.append(ib); vals.append(1); rhs.append(soc_b0); r += 1
    # EV state: soc[t+1] - soc[t] - eta_ev*ev = -trip
    for t in range(T):
        rows += [r, r, r]; cols += [ie + t + 1, ie + t, f(EV, t)]
        vals += [1, -1, -sysm.ev_eta]; rhs.append(-ev_trip[t]); r += 1
    rows.append(r); cols.append(ie); vals.append(1); rhs.append(soc_ev0); r += 1
    A_eq = sp.csr_matrix((vals, (rows, cols)), shape=(r, nv))

    lb = np.zeros(nv)
    ub = np.full(nv, np.inf)
    ub[IMP * T:(IMP + 1) * T] = sysm.grid_import_kw
    ub[EXP * T:(EXP + 1) * T] = sysm.inverter_kw
    ub[BCH * T:(BCH + 1) * T] = sysm.batt_kw
    ub[BDIS * T:(BDIS + 1) * T] = sysm.batt_kw
    ub[EV * T:(EV + 1) * T] = sysm.ev_kw * ev_home if sysm.has_ev else 0.0
    ub[CURT * T:(CURT + 1) * T] = pv
    lb[ib:ib + nb] = 0.0
    ub[ib:ib + nb] = sysm.batt_kwh
    if sysm.has_ev:
        lb[ie:ie + nb] = sysm.ev_soc_min
        ub[ie:ie + nb] = sysm.ev_soc_max
        need = np.append(ev_need, 0.0)
        lb[ie:ie + nb] = np.maximum(lb[ie:ie + nb], need)
        # the starting state is given; never let a bound make it infeasible
        lb[ie] = min(lb[ie], soc_ev0)
        ub[ie] = max(ub[ie], soc_ev0)
    else:
        ub[ie:ie + nb] = 0.0
    lb[ib] = min(lb[ib], soc_b0)
    ub[ib] = max(ub[ib], soc_b0)

    res = linprog(c, A_eq=A_eq, b_eq=np.array(rhs), bounds=np.column_stack([lb, ub]), method="highs")
    if res.status != 0:
        raise RuntimeError(f"LP failed: {res.message}")
    x = res.x
    g = lambda k: x[k * T:(k + 1) * T]  # noqa: E731
    return Plan(g(IMP), g(EXP), g(BCH), g(BDIS), g(EV), g(CURT), x[ib:ib + nb], x[ie:ie + nb], float(res.fun))
