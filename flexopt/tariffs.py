"""Household import and export prices in EUR/kWh, hourly, indexed in UTC.

Import prices include VAT (and the Spanish electricity tax); export prices are
what the household is paid. Values are 2026 tariff rules applied to 2025
wholesale prices. Sources are cited per constant; where a value is a modelling
assumption it says so.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

# --- Portugal ---------------------------------------------------------------
# ERSE regulated BTN energy prices for 2026 before VAT (reported by Doutor
# Financas, https://www.doutorfinancas.pt/?p=196422): simple 0.1654;
# bi-horario vazio 0.1087 / fora de vazio 0.1988; tri-horario vazio 0.1087,
# cheias 0.1690, ponta 0.2495 EUR/kWh.
PT_VAT = 0.23  # marginal rate above the 6 % reduced block (assumption: PV+EV homes exceed it)
PT_SIMPLE = 0.1654
PT_BI = {"vazio": 0.1087, "fora": 0.1988}
PT_TRI = {"vazio": 0.1087, "cheias": 0.1690, "ponta": 0.2495}
# Indexed offer (EDP "Oferta Indexada"-style): (OMIE + spread) x losses + access.
# Spread, loss factor and access term are calibrated so that the time-average
# equals the simple tariff (assumption).
PT_IDX_SPREAD = 0.010
PT_IDX_LOSSES = 1.15


def _pt_tri_period(local: pd.DatetimeIndex) -> np.ndarray:
    """ERSE daily cycle for BTN tri-horario. Vazio 22:00-08:00 all year.

    Winter (legal winter time): ponta 09:00-10:30 and 18:00-20:30.
    Summer (legal summer time): ponta 10:30-13:00 and 19:30-21:00.
    Hourly resolution: half hours are assigned to the period covering most of
    the hour (assumption).
    """
    h = local.hour
    summer = np.array([bool(t.dst()) for t in local])
    vazio = (h >= 22) | (h < 8)
    ponta_w = (h == 9) | (h == 18) | (h == 19)
    ponta_s = (h == 11) | (h == 12) | (h == 20)
    ponta = np.where(summer, ponta_s, ponta_w)
    return np.where(vazio, "vazio", np.where(ponta, "ponta", "cheias"))


def pt_import(kind: str, omie_pt: pd.Series) -> pd.Series:
    idx = omie_pt.index
    local = idx.tz_convert("Europe/Lisbon")
    h = local.hour
    if kind == "simple":
        p = np.full(len(idx), PT_SIMPLE)
    elif kind == "bi":
        p = np.where((h >= 22) | (h < 8), PT_BI["vazio"], PT_BI["fora"])
    elif kind == "tri":
        per = _pt_tri_period(local)
        p = np.vectorize(PT_TRI.get)(per)
    elif kind == "indexed":
        energy = (omie_pt.values / 1000.0 + PT_IDX_SPREAD) * PT_IDX_LOSSES
        access = PT_SIMPLE - energy.mean()
        p = energy + access
    else:
        raise ValueError(kind)
    return pd.Series(p * (1 + PT_VAT), index=idx, name=f"pt_{kind}")


# --- Spain ------------------------------------------------------------------
# 2.0TD energy-term peajes 2026 (CNMC resolution of 18 Dec 2025) plus cargos
# 2026 (Orden TED/1524/2025), EUR/kWh, from
# https://www.miteco.gob.es/en/energia/energia-electrica/electricidad/peajes.html
ES_PEAJES = {"P1": 0.033261, "P2": 0.016409, "P3": 0.000077}
ES_CARGOS = {"P1": 0.064292, "P2": 0.012858, "P3": 0.003215}
ES_IEE = 0.0511  # electricity tax
ES_VAT = 0.21
# PVPC 2026 energy: 45 % day-ahead spot and 55 % forward products. The forward
# share is approximated by the monthly mean of spot; 0.015 EUR/kWh covers
# adjustment services, capacity and losses (assumption).
ES_PVPC_SPOT_SHARE = 0.45
ES_PVPC_ADDERS = 0.015
# Fixed-price free-market offer, energy term before taxes (assumption close to
# published 2026 three-period offers net of network terms).
ES_FIXED_ENERGY = 0.075


def es_period(local: pd.DatetimeIndex) -> np.ndarray:
    """2.0TD periods: P1 10-14 & 18-22, P2 8-10, 14-18 & 22-24, P3 0-8 on weekdays; P3 all weekend.

    National holidays are treated as weekdays (simplification).
    """
    h, dow = local.hour, local.dayofweek
    p1 = ((h >= 10) & (h < 14)) | ((h >= 18) & (h < 22))
    p3 = h < 8
    per = np.where(p1, "P1", np.where(p3, "P3", "P2"))
    return np.where(dow >= 5, "P3", per)


def es_import(kind: str, omie_es: pd.Series) -> pd.Series:
    idx = omie_es.index
    local = idx.tz_convert("Europe/Madrid")
    per = es_period(local)
    network = np.vectorize(lambda x: ES_PEAJES[x] + ES_CARGOS[x])(per)
    spot = omie_es.values / 1000.0
    if kind == "pvpc":
        monthly = omie_es.groupby(local.to_period("M")).transform("mean").values / 1000.0
        energy = ES_PVPC_SPOT_SHARE * spot + (1 - ES_PVPC_SPOT_SHARE) * monthly + ES_PVPC_ADDERS
    elif kind == "fixed":
        energy = np.full(len(idx), ES_FIXED_ENERGY)
    else:
        raise ValueError(kind)
    p = (energy + network) * (1 + ES_IEE) * (1 + ES_VAT)
    return pd.Series(p, index=idx, name=f"es_{kind}")


# --- Export -----------------------------------------------------------------


def export_price(kind: str, omie: pd.Series) -> pd.Series:
    """Payment for exported kWh.

    'indexed': OMIE minus 10 EUR/MWh, floored at zero (market-indexed surplus
    purchase; PT offers quote OMIE minus a fee, ES PVPC compensation is close to
    the hourly market price).
    'fixed_low': 0.01 EUR/kWh (PT worst case observed on an EDP self-billing invoice).
    'fixed_mid': 0.04 EUR/kWh (PT comparator average) / typical ES fixed offers.
    """
    if kind == "indexed":
        v = np.maximum(omie.values / 1000.0 - 0.010, 0.0)
    elif kind == "fixed_low":
        v = np.full(len(omie), 0.01)
    elif kind == "fixed_mid":
        v = np.full(len(omie), 0.04)
    else:
        raise ValueError(kind)
    return pd.Series(v, index=omie.index, name=f"export_{kind}")
