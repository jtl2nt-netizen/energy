"""Data loaders for public inputs: OMIE day-ahead prices, Open-Meteo weather.

All functions return pandas objects indexed by tz-aware hourly timestamps in
Europe/Lisbon (PT) or Europe/Madrid (ES) local time as requested.
"""
from __future__ import annotations

import glob
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

# OMIE marginalpdbc columns: year;month;day;period;price_PT;price_ES (EUR/MWh).
# Column order verified against ERSE's 2025 PT annual average (see tests).
OMIE_COLS = ["year", "month", "day", "period", "PT", "ES"]

# Market time unit switch: hourly until 30 Sep 2025, 15-minute from 1 Oct 2025.
MTU15_START = pd.Timestamp("2025-10-01")


def load_omie_dayahead(zone: str, pattern: str = "marginalpdbc_2025*.1") -> pd.Series:
    """Hourly day-ahead price in EUR/MWh for zone 'PT' or 'ES', indexed in CET/CEST.

    OMIE delivery days run in Central European time. 15-minute periods are
    averaged to hourly so the whole year has one resolution.
    """
    frames = []
    for f in sorted(glob.glob(str(RAW / "omie" / pattern))):
        rows = []
        with open(f, encoding="latin-1") as fh:
            for line in fh:
                parts = line.strip().split(";")
                if len(parts) < 6 or not parts[0].isdigit():
                    continue
                rows.append(parts[:6])
        df = pd.DataFrame(rows, columns=OMIE_COLS)
        if df.empty:
            continue
        df[["year", "month", "day", "period"]] = df[["year", "month", "day", "period"]].astype(int)
        df[["PT", "ES"]] = df[["PT", "ES"]].astype(float)
        n = len(df)
        # 23/24/25 periods = hourly day (DST days); 92/96/100 = quarter-hourly.
        minutes = 60 if n <= 25 else 15
        day = pd.Timestamp(year=df.year[0], month=df.month[0], day=df.day[0])
        start = day.tz_localize("Europe/Madrid")
        idx = pd.date_range(start, periods=n, freq=f"{minutes}min")
        frames.append(pd.Series(df[zone].values, index=idx))
    s = pd.concat(frames).sort_index()
    s = s.resample("1h").mean()
    s.name = f"omie_{zone}_eur_mwh"
    return s


def fetch_openmeteo_archive(lat: float, lon: float, start: str, end: str, cache: str) -> pd.DataFrame:
    """Hourly ERA5-based weather from the Open-Meteo archive API (non-commercial use).

    Variables: global horizontal (GHI), direct normal (DNI), diffuse (DHI)
    irradiance in W/m2 and 2 m temperature in C. Indexed in UTC.
    """
    path = RAW / "weather" / cache
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        url = "https://archive-api.open-meteo.com/v1/archive"
        params = dict(
            latitude=lat, longitude=lon, start_date=start, end_date=end, timezone="GMT",
            hourly="shortwave_radiation,direct_normal_irradiance,diffuse_radiation,temperature_2m,cloud_cover",
        )
        r = requests.get(url, params=params, timeout=120)
        r.raise_for_status()
        path.write_text(r.text)
    js = json.loads(path.read_text())
    h = js["hourly"]
    df = pd.DataFrame(
        {
            "ghi": h["shortwave_radiation"],
            "dni": h["direct_normal_irradiance"],
            "dhi": h["diffuse_radiation"],
            "temp": h["temperature_2m"],
            "cloud": h["cloud_cover"],
        },
        index=pd.to_datetime(h["time"]).tz_localize("UTC"),
    )
    # Open-Meteo radiation is the mean over the preceding hour; shift to hour-start labels.
    df = df.shift(-1).ffill()
    return df


def load_nasa_power(name: str) -> pd.DataFrame:
    """Hourly NASA POWER radiation (W/m2) and temperature (C), indexed in UTC.

    Files: data/raw/weather/nasa_<name>_2025.json, fetched from
    https://power.larc.nasa.gov/api/temporal/hourly/point (public domain).
    Columns: ghi, dni, dhi, ghi_clear, temp.
    """
    js = json.loads((RAW / "weather" / f"nasa_{name}_2025.json").read_text())
    p = js["properties"]["parameter"]
    keys = {
        "ALLSKY_SFC_SW_DWN": "ghi",
        "ALLSKY_SFC_SW_DNI": "dni",
        "ALLSKY_SFC_SW_DIFF": "dhi",
        "CLRSKY_SFC_SW_DWN": "ghi_clear",
        "T2M": "temp",
    }
    df = pd.DataFrame({v: pd.Series(p[k]) for k, v in keys.items()})
    df.index = pd.to_datetime(df.index, format="%Y%m%d%H").tz_localize("UTC")
    df = df.where(df > -900).interpolate(limit=3).fillna(0.0)
    return df.sort_index()
