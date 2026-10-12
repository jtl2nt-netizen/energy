"""Tests for the dispatch model, controllers and data loaders."""
import numpy as np
import pandas as pd
import pytest

from flexopt.controllers import run_rule_based, run_perfect
from flexopt.dispatch import solve
from flexopt.household import System
from dataclasses import replace


def _toy(T=48, ev=False):
    h = np.arange(T) % 24
    pv = np.where((h >= 8) & (h < 18), 3.0, 0.0)
    load = np.full(T, 0.5) + np.where((h >= 18) & (h < 22), 1.5, 0.0)
    p_imp = np.where((h >= 18) & (h < 22), 0.30, np.where(h < 8, 0.10, 0.20))
    p_exp = np.full(T, 0.02)
    home = np.ones(T); trip = np.zeros(T); need = np.zeros(T)
    if ev:
        home = np.where((h >= 8) & (h < 19), 0.0, 1.0)
        trip = np.where(h == 19, 7.0, 0.0)
        need = np.where(h == 8, 30.0, 0.0)
    return pv, load, p_imp, p_exp, home, trip, need


def test_energy_balance_and_bounds():
    s = System()
    pv, load, pi, pe, home, trip, need = _toy(ev=True)
    plan = solve(pv, load, pi, pe, home, trip, need, 5.0, 40.0, s, deg_cost=0.02)
    bal = pv - plan.curt + plan.imp + plan.bdis - load - plan.ev - plan.bch - plan.exp
    assert np.allclose(bal, 0, atol=1e-6)
    assert plan.soc_b.min() >= -1e-6 and plan.soc_b.max() <= s.batt_kwh + 1e-6
    assert plan.soc_ev.min() >= s.ev_soc_min - 1e-6
    # departure requirement met at every 08:00
    for t in np.where(need > 0)[0]:
        assert plan.soc_ev[t] >= need[t] - 1e-6
    assert plan.imp.max() <= s.grid_import_kw + 1e-6


def test_optimiser_not_worse_than_default_with_perfect_information():
    s = replace(System(), has_ev=False)
    pv, load, pi, pe, home, trip, need = _toy(T=24 * 7)
    df = pd.DataFrame(dict(pv=pv, load=load, p_imp=pi, p_exp=pe, ev_home=home, ev_trip=trip, ev_need=need))
    d = run_rule_based(df, s, smart_ev=False, deg_cost=0.0)
    p = run_perfect(df, s, deg_cost=0.0)
    assert p["bill_eur"] <= d["bill_eur"] + 1e-6


def test_battery_shifts_cheap_energy_to_peak():
    s = replace(System(), has_ev=False)
    T = 24
    h = np.arange(T)
    plan = solve(np.zeros(T), np.where(h >= 18, 2.0, 0.2), np.where(h >= 18, 0.30, 0.10), np.zeros(T),
                 np.zeros(T), np.zeros(T), np.zeros(T), 0.0, 0.0, s, deg_cost=0.0)
    assert plan.bch[h < 18].sum() > 1.0  # charges in cheap hours
    assert plan.bdis[h >= 18].sum() > 1.0  # discharges at peak


def test_omie_columns_match_published_annual_averages():
    from flexopt.data import load_omie_dayahead
    pt = load_omie_dayahead("PT")
    es = load_omie_dayahead("ES")
    # ERSE Relatorio Anual Mercados 2025: PT 66.19 EUR/MWh; ES ~65.28 EUR/MWh
    assert abs(pt.mean() - 66.19) < 1.0
    assert abs(es.mean() - 65.28) < 1.0
    assert pt.isna().sum() == 0
