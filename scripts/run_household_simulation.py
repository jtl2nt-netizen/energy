"""Year-long household simulation for Portugal (Lisbon) and Spain (Madrid), 2025.

Usage: .venv/bin/python scripts/run_household_simulation.py
Writes results/household_simulation_2025.csv and prints a summary.
"""
from __future__ import annotations

import itertools
import sys
import time
from dataclasses import replace
from multiprocessing import Pool
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flexopt.controllers import run_mpc, run_perfect, run_rule_based  # noqa: E402
from flexopt.data import load_nasa_power, load_omie_dayahead  # noqa: E402
from flexopt.forecast import load_forecasts, price_forecasts, pv_forecasts  # noqa: E402
from flexopt.household import LISBON, MADRID, System, ev_schedule, home_load, pv_output  # noqa: E402
from flexopt.tariffs import es_import, export_price, pt_import  # noqa: E402

H = 36
START = pd.Timestamp("2025-01-01", tz="UTC")
END = pd.Timestamp("2025-12-31 22:00", tz="UTC")  # last OMIE hour (CET delivery day)
DEG = 0.02  # EUR per kWh discharged, battery wear (assumption)

SCENARIOS = (
    [("PT", imp, exp) for imp in ("simple", "bi", "tri", "indexed") for exp in ("indexed", "fixed_low")]
    + [("ES", imp, exp) for imp in ("pvpc", "fixed") for exp in ("indexed", "fixed_mid")]
)
HOUSEHOLDS = {"pv_battery_ev": System(), "pv_battery": replace(System(), has_ev=False)}


def run_one(args, pv_plan_factor=1.0):
    country, imp_kind, exp_kind, hh = args
    site = LISBON if country == "PT" else MADRID
    sysm = HOUSEHOLDS[hh]
    w = load_nasa_power(site.name)
    pv = pv_output(w, site, sysm)
    pvc = pv_output(w, site, sysm, clear_sky=True)
    ld = home_load(w, site, sysm, seed=1 if country == "PT" else 2)
    ev = ev_schedule(w.index, site, sysm)
    omie = load_omie_dayahead(country).tz_convert("UTC")
    p_imp = pt_import(imp_kind, omie) if country == "PT" else es_import(imp_kind, omie)
    p_exp = export_price(exp_kind, omie)
    sl = slice(START, END)
    df = pd.DataFrame({
        "pv": pv[sl], "load": ld[sl], "p_imp": p_imp[sl], "p_exp": p_exp[sl],
        "ev_home": ev.home[sl], "ev_trip": ev.trip_kwh[sl], "ev_need": ev.need_kwh[sl],
    })
    dayahead_imp = imp_kind in ("indexed", "pvpc")
    fc = pd.DataFrame({
        "pv_fc": pv_forecasts(pv[:END], pvc[:END], START, H),
        "load_fc": load_forecasts(ld[:END], site.tz, START, H),
        "p_imp_fc": price_forecasts(p_imp[:END], START, H, dayahead=dayahead_imp),
        "p_exp_fc": price_forecasts(p_exp[:END], START, H, dayahead=(exp_kind == "indexed")),
    })
    rows = [
        run_rule_based(df, sysm, smart_ev=False, deg_cost=DEG),
        run_rule_based(df, sysm, smart_ev=True, deg_cost=DEG),
        run_mpc(df, fc, sysm, DEG, H, pv_plan_factor=pv_plan_factor),
        run_perfect(df, sysm, DEG),
    ]
    meta = {"country": country, "import_tariff": imp_kind, "export_tariff": exp_kind, "household": hh,
            "pv_kwh": float(df.pv.sum()), "load_kwh": float(df.load.sum()),
            "ev_kwh": float(df.ev_trip.sum())}
    return [{**meta, **r} for r in rows]


def main():
    jobs = [(c, i, e, hh) for (c, i, e), hh in itertools.product(SCENARIOS, HOUSEHOLDS)]
    t0 = time.time()
    with Pool(4) as pool:
        out = pool.map(run_one, jobs)
    res = pd.DataFrame([r for rows in out for r in rows])
    Path("results").mkdir(exist_ok=True)
    res.to_csv("results/household_simulation_2025.csv", index=False)
    piv = res.pivot_table(index=["country", "household", "import_tariff", "export_tariff"],
                          columns="controller", values="total_eur").round(0)
    piv = piv[["default", "smart_rules", "mpc", "perfect"]]
    piv["save_vs_default"] = piv["default"] - piv["mpc"]
    piv["save_vs_rules"] = piv["smart_rules"] - piv["mpc"]
    piv["ceiling_vs_default"] = piv["default"] - piv["perfect"]
    pd.set_option("display.width", 200)
    print(piv.to_string())
    print(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
