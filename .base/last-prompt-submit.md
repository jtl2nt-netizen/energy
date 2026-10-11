<context-bracket>[CRITICAL] (prompt 2)</context-bracket>

[base rules · topic: research]
  - Every current-rule or market claim in reports must carry a dated 2025-2026 source; where none was found, say so explicitly rather than asserting.

<base-context name="Research" kind="domain" hops="2">
  decision  Research round 1 treats Portugal (and Spain via MIBEL) as a first-market candidate on par with Germany, not a second market. — hasDecision
  decision  Treat the ChatGPT research brief (research/brief/00_original_brief.md) as a scope document, not a template to answer line by line. Prioritise the primary decision (1-2 first wedges from Munich) and depth on top wedges over 13 full deliverables. — hasDecision
  decision  Use basemode (base CLI v0.16.0) as the shared memory layer for the energy-trading startup research project; workspace scaffolded at repo root, project slug 'energy'. — hasDecision
  note      Brief critique: prioritise Germany + DACH and upstream buyers (Stadtwerke, BRPs, Direktver — hasDomain
  note      Founding team: technical founder in Munich (ML/software/optimisation) plus a Portuguese co — hasDomain
  note      Research round 1 decomposed into 10 parallel evidence tracks: DE small-asset flexibility;  — hasDomain
  research  Every current-rule or market claim in reports must carry a dated 2025-2026 source; where n — hasRule
</base-context>

<base-context name="Energy" kind="domain" hops="2">
  task      Critique brief and set research plan — hasDomain
  task      Install basemode and scaffold workspace — hasDomain
  task      Run country/wedge screening with web evidence — hasDomain
  task      Write feasibility report and commit — hasDomain
  milestone Research round 1: wedge selection report — hasDomain
  project   energy — hasDomain
  workspace energy — belongsTo
</base-context>
