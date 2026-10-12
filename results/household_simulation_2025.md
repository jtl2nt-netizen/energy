---
ontology: true
type: reference
domain: research
summary: Year-long simulation of how much a forecast-driven controller saves a PV + battery (+ EV) home in Lisbon and Madrid on 2025 prices and 2026 tariffs
tags: [simulation, home-battery, ev, portugal, spain, mpc, value-per-home]
status: active
discovered: 2026-10-12
related: [prospects_iberia, 01_brief_critique_and_steering]
---

# Value of smart home-energy control in Portugal and Spain, 2025 data

## What was simulated

One home in Lisbon and one in Madrid, hour by hour through 2025, with 5 kWp of solar,
a 10 kWh / 5 kW battery and, in half the runs, an EV (60 kWh, 3.7 kW home charger,
commuting on weekdays). Each home is run under four controllers:

| Controller | What it does |
|---|---|
| Default | What a hybrid inverter does out of the box: solar to the house, surplus into the battery, battery covers deficits. The EV charges at full power as soon as it is plugged in. |
| Simple rules | Default battery, plus a smart EV charger that follows solar surplus and tops up in the cheapest known hours before departure. |
| Optimiser | Our controller: re-plans the next 36 hours every hour with forecasts and executes the first hour. |
| Perfect foresight | The same optimiser with perfect knowledge of the whole year; an upper bound nobody can reach. |

The optimiser's forecasts are deliberately weak and use only past data: solar from
clear-sky output scaled by recent and 30-day cloudiness, household load from the
same hour on recent similar days, and prices only once OMIE has published them.
A real weather forecast should capture more of the gap to perfect foresight.

## Results (EUR per home per year, including 0.02 EUR/kWh battery wear)

Lower cost is better. "Saving" columns compare the optimiser with each baseline.

### Homes with solar, battery and EV

| Country | Import tariff | Export paid at | Default | Simple rules | Optimiser | Perfect | Saving vs default | Saving vs rules |
|---|---|---|---|---|---|---|---|---|
| PT | Simple | Hourly market | 333 | 290 | 256 | 177 | 77 | 34 |
| PT | Two-period | Hourly market | 342 | 238 | 195 | 103 | 147 | 43 |
| PT | Three-period | Hourly market | 340 | 232 | 182 | 101 | 158 | 50 |
| PT | Hourly indexed | Hourly market | 387 | 260 | 234 | 131 | 153 | 26 |
| PT | Simple | 0.01 fixed | 365 | 325 | 284 | 236 | 81 | 41 |
| PT | Two-period | 0.01 fixed | 374 | 272 | 263 | 177 | 111 | 9 |
| PT | Three-period | 0.01 fixed | 372 | 267 | 253 | 176 | 119 | 14 |
| PT | Hourly indexed | 0.01 fixed | 419 | 291 | 293 | 197 | 126 | -2 |
| ES | PVPC | Hourly market | 317 | 181 | 131 | 51 | 186 | 50 |
| ES | Fixed offer | Hourly market | 276 | 177 | 110 | 9 | 166 | 67 |
| ES | PVPC | 0.04 fixed | 262 | 134 | 137 | 81 | 125 | -3 |
| ES | Fixed offer | 0.04 fixed | 221 | 126 | 136 | 95 | 85 | -10 |

### Homes with solar and battery, no EV

| Country | Import tariff | Export paid at | Default | Optimiser | Perfect | Saving vs default | Most that could be saved |
|---|---|---|---|---|---|---|---|
| PT | Simple | Hourly market | 13 | -33 | -94 | 46 | 107 |
| PT | Two-period | Hourly market | 11 | -38 | -115 | 49 | 126 |
| PT | Three-period | Hourly market | 10 | -50 | -116 | 60 | 126 |
| PT | Hourly indexed | Hourly market | 20 | -34 | -93 | 54 | 113 |
| PT | any | 0.01 fixed | 53–64 | 57–66 | 44–59 | -7 to 0 | 0–10 |
| ES | PVPC | Hourly market | 25 | -71 | -111 | 96 | 136 |
| ES | Fixed offer | Hourly market | 19 | -79 | -174 | 98 | 193 |
| ES | any | 0.04 fixed | -65 to -59 | -65 to -59 | -74 | 0 | 9–15 |

Simple rules equal the default for homes without an EV, because the rules only change EV charging.

## What the numbers say

1. **The value depends on how exports are paid.** Where the household is paid the hourly
   market price for exports, the optimiser saves 46–60 EUR a year per battery home in
   Portugal and about 96 EUR in Spain, and 145–190 EUR per EV home on time-of-use or hourly tariffs against the default (77 EUR on a flat tariff).
   Where exports earn a fixed price, a battery-only home has almost nothing to gain
   (at most 0–15 EUR even with perfect foresight). This matches a Spanish academic
   result found by the prospect research: about 5 EUR a year from optimal battery
   scheduling under fixed compensation.
2. **EVs are where most of the money is, but simple rules capture much of it.** A smart
   charger that follows the sun and the cheapest hours gets two thirds of the way. The
   optimiser adds 26–67 EUR a year on top in market-paid homes, and little in fixed-paid ones.
3. **Our weak forecasts already capture about 40–70% of the perfect-foresight saving.**
   The remaining gap is the room for better forecasting, which is what a real ML and
   weather-forecast pipeline would target.
4. **Target customers:** installers and retailers whose customers (a) have EVs and/or
   (b) are paid market prices for exports (Goldenergy buys surplus at the 15-minute OMIE
   price; Lumio and Spanish PVPC homes are paid hourly prices), and (c) currently run
   inverter defaults. Fixed-price "virtual battery" customers are the weakest segment.

Fleet arithmetic (illustrative): 10,000 EV homes paid market prices for exports save
about 1.5–1.9 million EUR a year against inverter defaults, or 0.3–0.7 million EUR a
year against simple smart-charging rules.

## Assumptions and limitations

- Prices: OMIE day-ahead 2025 for PT and ES (column order checked against ERSE's 2025 annual averages). Tariff rules: 2026 values.
  - Portugal: ERSE 2026 regulated energy prices, simple 0.1654, two-period 0.1087 / 0.1988, three-period 0.1087 / 0.1690 / 0.2495 EUR/kWh, plus 23% VAT. The hourly indexed tariff is calibrated to the simple tariff's average.
  - Spain: 2.0TD network charges and cargos for 2026 from MITECO. PVPC is modelled as 45% spot plus 55% monthly average plus 0.015 EUR/kWh, with 5.11% electricity tax and 21% VAT.
- Export prices: hourly market (OMIE minus 10 EUR/MWh, floored at zero), or fixed 0.01 EUR/kWh (PT) or 0.04 EUR/kWh (ES).
  - Spain's monthly cap on simplified compensation is not modelled. Spanish battery-only savings on hourly export are therefore an upper bound.
- Solar: NASA POWER 2025 hourly radiation and a PVWatts-style model, 30° south. Lisbon yields 1,503 kWh/kWp and Madrid 1,410 kWh/kWp, which is probably slightly low.
- Household load: 3,500 kWh/yr. The shape follows E-REDES's description of the official BTN class C household profile. Weather effects, noise and appliance spikes are a modelling assumption, not metered data. The same shape is used for Spain.
- EV: 2,347 kWh/yr of driving, weekday commuter away 08:00–19:00. A car at home during the day would favour solar charging.
- Battery: 90% round trip, 0.02 EUR/kWh wear cost. Contracted import power 6.9 kW. Hourly resolution: Portugal settles surplus per 15 minutes, which this model does not resolve.
- One synthetic home per country. Real fleets vary widely. A shadow pilot on real installation data is needed before quoting figures to a customer as fact.

## Reproduce

```
.venv/bin/python scripts/run_household_simulation.py   # about 5 minutes on 4 cores
.venv/bin/python -m pytest -q tests
```

Raw results: `results/household_simulation_2025.csv`. Code: `flexopt/`.
