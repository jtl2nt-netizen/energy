# energy — feasibility research for a European energy-flexibility software startup

Founder context: Munich-based, strong ML/software/optimisation skills, no industry
network, no capital. Question: is there a capital-light, software-first wedge selling
forecasting or dispatch-optimisation models into European electricity flexibility, and
if so which one or two should be tested first?

## Layout

- `research/brief/00_original_brief.md` — the original research brief (written with ChatGPT).
- `research/brief/01_brief_critique_and_steering.md` — critique of the brief and the
  hypotheses this round tests.
- `research_notes/<title>/` — per-topic evidence notes with dated sources, one file per
  research track.
- `reports/<title>.md` — the synthesised feasibility report.
- `.base/` — basemode workspace (decisions, rules, tasks). Run `base recall --domain research`
  or `base decision search --keyword wedge` to see what was decided and why.

## Tooling

[basemode](https://basemode.ai) (`base` CLI) is installed as the shared memory layer for
agent sessions on this project. Install with
`curl -fsSL https://raw.githubusercontent.com/ChristopherKahler/base/main/install.sh | sh`,
then `base doctor` in this directory.

## Home-energy optimisation model (`flexopt/`)

Forecast-driven controller for homes with solar, a battery and an EV, plus a year-long
simulation for Portugal and Spain.

- `flexopt/dispatch.py`: linear programme that plans grid import/export, battery and EV charging.
- `flexopt/controllers.py`: inverter default, simple smart-charging rules, the rolling optimiser, and a perfect-foresight bound.
- `flexopt/forecast.py`: solar, load and price forecasts using only data available at decision time.
- `flexopt/household.py`, `flexopt/tariffs.py`, `flexopt/data.py`: household model, 2026 PT/ES tariffs, data loaders.
- `results/household_simulation_2025.md`: results and assumptions.
- `outreach/`: prospect list, email drafts, one-page PDF for prospects.

Setup and run (input data downloads to `data/raw/`, which is not committed):

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
.venv/bin/python scripts/run_household_simulation.py
```

Raw data sources: OMIE day-ahead files (marginalpdbc), NASA POWER hourly radiation for
Lisbon and Madrid (2024-12-01 to 2025-12-31). The download commands are in
`flexopt/data.py` docstrings.
