"""Forecasts available to the controller at each hour, with no look-ahead.

PV: clear-sky PV scaled by a clear-sky index that blends the last few hours
(for the next hours) with yesterday and the 30-day average (for later hours).
It needs no weather-forecast subscription and is deliberately weak;
a numerical weather forecast should do better, so results are conservative.
Load: mean of the same local hour over the last four days of the same type
(weekday or weekend), using only data before the decision hour.
Prices: OMIE publishes next-day prices around 13:00 CET. Before that, hours of
the next day are filled with the same hour of the latest known day.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def pv_forecasts(pv: pd.Series, pv_clear: pd.Series, start: pd.Timestamp, horizon: int) -> list:
    idx = pv.index
    a, c = pv.values, pv_clear.values
    t0 = idx.get_loc(start)
    out = []
    for t in range(t0, len(idx)):
        lo = max(0, t - 24)
        cs_day = c[lo:t].sum()
        k_day = a[lo:t].sum() / cs_day if cs_day > 0.5 else 1.0
        # last three hours with meaningful clear-sky output
        recent = [i for i in range(t - 1, max(-1, t - 7), -1) if c[i] > 0.3][:3]
        k_now = a[recent].sum() / c[recent].sum() if recent else k_day
        # 30-day climatology of the clear-sky index (past data only)
        lo30 = max(0, t - 720)
        cs30 = c[lo30:t].sum()
        k_clim = a[lo30:t].sum() / cs30 if cs30 > 1.0 else k_day
        h = np.arange(horizon)
        w = np.exp(-h / 3.0)
        k_later = 0.4 * k_day + 0.6 * k_clim  # yesterday has little skill a day ahead
        k = np.clip(w * k_now + (1 - w) * k_later, 0, 1.2)
        seg = c[t:t + horizon]
        f = np.zeros(horizon)
        f[:len(seg)] = seg * k[:len(seg)]
        out.append(np.minimum(f, a.max()))
    return out


def load_forecasts(load: pd.Series, tz: str, start: pd.Timestamp, horizon: int, recency: bool = False) -> list:
    """Seasonal mean of recent same-type days, optionally corrected by the latest reading.

    With recency=True the log-ratio between the last observed hour and its
    seasonal estimate is carried forward with a decay phi**(h+1), where phi is
    the lag-1 autocorrelation of those log-ratios over the trailing 30 days.
    phi is re-estimated every day from past data only.
    """
    idx = load.index
    local = idx.tz_convert(tz)
    weekend = (local.dayofweek >= 5)
    hour = local.hour
    v = load.values
    t0 = idx.get_loc(start)
    out = []
    for t in range(t0, len(idx)):
        f = np.zeros(horizon)
        for h in range(horizon):
            j = t + h
            if j >= len(idx):
                break
            # same local hour, same day type, strictly before t
            cands = []
            back = j - 24
            while back >= 0 and len(cands) < 4:
                if back < t and hour[back] == hour[j] and weekend[back] == weekend[j]:
                    cands.append(v[back])
                back -= 24
            f[h] = np.mean(cands) if cands else v[t - 1]
        out.append(f)
    if not recency:
        return out
    # seasonal estimate for every hour, using only earlier days
    seas = np.full(len(v), np.nan)
    for j in range(len(v)):
        cands, back = [], j - 24
        while back >= 0 and len(cands) < 4:
            if weekend[back] == weekend[j]:
                cands.append(v[back])
            back -= 24
        if cands:
            seas[j] = np.mean(cands)
    lr = np.log(np.maximum(v, 0.05) / np.maximum(seas, 0.05))
    phi = 0.0
    for k, t in enumerate(range(t0, len(idx))):
        if k % 24 == 0:
            past = lr[max(0, t - 720):t]
            past = past[np.isfinite(past)]
            if len(past) > 48:
                a, b = past[:-1] - past[:-1].mean(), past[1:] - past[1:].mean()
                phi = float(np.clip((a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum()), 0, 0.95))
        r = lr[t - 1] if np.isfinite(lr[t - 1]) else 0.0
        out[k] = out[k] * np.exp(phi ** (np.arange(horizon) + 1) * r)
    return out


def price_forecasts(price: pd.Series, start: pd.Timestamp, horizon: int, dayahead: bool = True) -> list:
    """Known-price windows for day-ahead-linked prices; fixed tariffs are fully known."""
    idx = price.index
    v = price.values
    t0 = idx.get_loc(start)
    cet = idx.tz_convert("Europe/Madrid")
    day_start = np.array([(ts.normalize()) for ts in cet])
    out = []
    for t in range(t0, len(idx)):
        seg = np.zeros(horizon)
        n = min(horizon, len(idx) - t)
        seg[:n] = v[t:t + n]
        if dayahead:
            known_days = 1 if cet[t].hour < 13 else 2
            limit = day_start[t] + pd.Timedelta(days=known_days)
            for h in range(n):
                if cet[t + h] >= limit:
                    k = h
                    while cet[t + k] >= limit:
                        k -= 24
                    seg[h] = v[t + k]
        out.append(seg)
    return out
