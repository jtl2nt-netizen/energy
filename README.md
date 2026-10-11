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
