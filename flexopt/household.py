"""Household model: PV generation, home load and EV usage.

Every series is hourly (kW averaged over the hour = kWh per hour), indexed in UTC.
Assumptions are explicit module constants so the report can cite them.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
import pvlib

# ---------------------------------------------------------------------------
# Site and system definitions
# ---------------------------------------------------------------------------


@dataclass
class Site:
    name: str
    lat: float
    lon: float
    tz: str
    zone: str  # OMIE zone: "PT" or "ES"
    summer_cooling: bool = False  # adds air-conditioning load on hot days


LISBON = Site("lisbon", 38.72, -9.14, "Europe/Lisbon", "PT")
MADRID = Site("madrid", 40.42, -3.70, "Europe/Madrid", "ES", summer_cooling=True)


@dataclass
class System:
    pv_kwp: float = 5.0
    tilt: float = 30.0
    azimuth: float = 180.0
    pv_losses: float = 0.14  # wiring, soiling, mismatch
    inverter_kw: float = 5.0  # AC limit for PV output and for export
    batt_kwh: float = 10.0  # usable capacity
    batt_kw: float = 5.0
    batt_eta: float = 0.95  # one-way; round trip ~0.90
    grid_import_kw: float = 6.9  # contracted power
    has_ev: bool = True
    ev_kwh: float = 60.0
    ev_kw: float = 3.7  # 16 A single-phase home charger
    ev_eta: float = 0.90
    ev_soc_min: float = 6.0
    ev_soc_max: float = 54.0  # 90 % of 60 kWh
    ev_departure_min: float = 30.0  # energy in the car when it leaves on a weekday
    home_kwh_year: float = 3500.0


# ---------------------------------------------------------------------------
# PV
# ---------------------------------------------------------------------------


def pv_output(weather: pd.DataFrame, site: Site, sysm: System, clear_sky: bool = False) -> pd.Series:
    """AC PV output in kW per hour from hourly GHI/DNI/DHI (PVWatts-style model).

    NASA POWER hourly values are averages over the hour that starts at the
    timestamp, so the sun position is taken at the middle of the hour.
    """
    times_mid = weather.index + pd.Timedelta(minutes=30)
    loc = pvlib.location.Location(site.lat, site.lon)
    sp = loc.get_solarposition(times_mid)
    if clear_sky:
        cs = loc.get_clearsky(times_mid, model="simplified_solis")
        ghi, dni, dhi = cs["ghi"].values, cs["dni"].values, cs["dhi"].values
    else:
        ghi, dni, dhi = weather["ghi"].values, weather["dni"].values, weather["dhi"].values
    poa = pvlib.irradiance.get_total_irradiance(
        sysm.tilt, sysm.azimuth, sp["apparent_zenith"].values, sp["azimuth"].values,
        dni=dni, ghi=ghi, dhi=dhi, albedo=0.2,
    )["poa_global"]
    poa = np.nan_to_num(np.asarray(poa, dtype=float), nan=0.0).clip(min=0)
    temp = weather["temp"].values
    t_cell = temp + poa / 800.0 * 25.0
    pdc = sysm.pv_kwp * poa / 1000.0 * (1 - 0.004 * (t_cell - 25.0))
    pac = pdc * (1 - sysm.pv_losses) * 0.96
    pac = np.clip(pac, 0, sysm.inverter_kw)
    return pd.Series(pac, index=weather.index, name="pv_kw")


# ---------------------------------------------------------------------------
# Home load
# ---------------------------------------------------------------------------

# Weekday shape for local hours 0..23, built to match E-REDES's description of the
# official BTN class C household profile for 2025: minimum 4-6 h, steep rise to 8 h,
# plateau with a local maximum at 13 h, dip at 16-17 h, daily maximum at 20-21 h.
# Source: E-REDES, "Documento Justificativo dos Perfis de Consumo e Injeção 2025",
# Dec 2024 (charts only; values here are a modelling assumption).
_WEEKDAY = np.array([
    0.030, 0.025, 0.022, 0.021, 0.020, 0.021, 0.026, 0.036, 0.042, 0.043, 0.043, 0.044,
    0.048, 0.046, 0.041, 0.038, 0.038, 0.043, 0.050, 0.058, 0.064, 0.060, 0.050, 0.040,
])
# Monthly weights: winter months heavier (Jan, Feb, Dec), per the same document.
_MONTH = np.array([1.30, 1.20, 1.05, 0.95, 0.88, 0.85, 0.90, 0.90, 0.85, 0.92, 1.10, 1.30])


def _day_shape(weekend: bool) -> np.ndarray:
    s = _WEEKDAY.copy()
    if weekend:
        s[9:16] *= 1.15  # more daytime use at home
        s[12:14] *= 1.25  # stronger lunch peak on weekends
    return s / s.sum()


def home_load(weather: pd.DataFrame, site: Site, sysm: System, seed: int = 1) -> pd.Series:
    """Hourly household consumption in kW for one home.

    Daily energy follows month weights, temperature (heating below 15 C, cooling
    above 24 C where enabled) and day-to-day noise; hourly values carry
    autocorrelated noise and random appliance spikes so that a single home is
    as hard to forecast as a real one.
    """
    rng = np.random.default_rng(seed)
    idx_utc = weather.index
    local = idx_utc.tz_convert(site.tz)
    days = pd.DatetimeIndex(sorted(set(local.normalize())))
    t_daily = weather["temp"].groupby(local.normalize()).mean()
    out = pd.Series(0.0, index=local)
    for d in days:
        mask = local.normalize() == d
        hours = local[mask].hour
        weekend = d.dayofweek >= 5
        base = _MONTH[d.month - 1] * (1.05 if weekend else 1.0)
        t = t_daily.get(d, 15.0)
        base *= 1 + 0.025 * max(0.0, 15.0 - t)
        if site.summer_cooling:
            base *= 1 + 0.04 * max(0.0, t - 24.0)
        base *= rng.lognormal(0.0, 0.12)
        out[mask] = base * _day_shape(weekend)[hours]
    # Hourly AR(1) multiplicative noise and appliance spikes.
    n = len(out)
    eps = np.zeros(n)
    for i in range(1, n):
        eps[i] = 0.6 * eps[i - 1] + rng.normal(0, 0.25)
    vals = out.values * np.exp(eps - 0.5 * 0.25**2 / (1 - 0.36))
    hrs = local.hour
    spike_p = np.where((hrs >= 7) & (hrs <= 22), 0.05, 0.005)
    spikes = (rng.random(n) < spike_p) * rng.uniform(0.8, 2.0, n)
    vals = vals + spikes
    for _ in range(3):  # cap at 5.5 kW (6.9 kVA contract) and renormalise the annual total
        vals = np.minimum(vals, 5.5)
        vals = vals / vals.sum() * sysm.home_kwh_year * (n / 8760.0)
    return pd.Series(vals, index=idx_utc, name="load_kw")


# ---------------------------------------------------------------------------
# EV usage
# ---------------------------------------------------------------------------


def ev_schedule(index_utc: pd.DatetimeIndex, site: Site, sysm: System) -> pd.DataFrame:
    """Availability, trip energy and departure requirement per hour.

    Commuter pattern in local time: weekdays away 08:00-19:00 using 7 kWh;
    Saturdays away 11:00-17:00 using 10 kWh; Sundays at home.
    Columns: home (0/1), trip_kwh (deducted in the first hour back home),
    need_kwh (minimum battery energy required at the start of that hour).
    """
    local = index_utc.tz_convert(site.tz)
    h, dow = local.hour, local.dayofweek
    away_wd = (dow < 5) & (h >= 8) & (h < 19)
    away_sat = (dow == 5) & (h >= 11) & (h < 17)
    home = ~(away_wd | away_sat)
    trip = np.where((dow < 5) & (h == 19), 7.0, 0.0) + np.where((dow == 5) & (h == 17), 10.0, 0.0)
    need = np.where((dow < 5) & (h == 8), sysm.ev_departure_min, 0.0)
    need = need + np.where((dow == 5) & (h == 11), sysm.ev_departure_min * 0.6, 0.0)
    if not sysm.has_ev:
        home[:] = False
        trip[:] = 0.0
        need[:] = 0.0
    return pd.DataFrame({"home": home.astype(float), "trip_kwh": trip, "need_kwh": need}, index=index_utc)
