# Critique of the brief and how the research is steered

Date: 2026-10-11. Author: Claude (coordinator), recorded in basemode under domain `research`.

## Verdict on the brief

The brief is unusually good for a ChatGPT-written prompt. Its strongest parts are the
end-to-end monetisation chain (signal → decision → asset → market → rights → settlement →
net value → startup share), the insistence on distinguishing legislation from money
actually paid, and the explicit permission to recommend not starting.

Its weaknesses, and what this round does about them:

1. **Too much surface area for one pass.** It asks for 13 deliverables, 30 numbered
   questions, a 10–15 country screen, 25+ verified prospects and runnable notebooks.
   Answering everything at equal depth produces a long, shallow document. This round
   optimises for the *primary decision* (one or two first wedges from Munich) and treats
   the remaining deliverables as supporting material at the depth the decision needs.

2. **It under-weights Germany.** The country hypotheses (PT, ES, IT, PL, GR, RO, HU, BG)
   assume the opportunity is abroad, while the founder is in Munich with no network and no
   local language elsewhere. Germany in 2026 has several things those markets lack:
   mandatory dynamic tariffs from every supplier, §14a EnWG controllable loads with
   time-variable grid fees, the Solarspitzengesetz (no feed-in payment at negative prices
   for new PV, pushing small PV and batteries toward direct marketing), 15-minute
   day-ahead products, roughly 2 million home batteries, ~900 Stadtwerke and hundreds of
   balance-responsible parties that pay imbalance costs. The research therefore screens
   Germany as a first-class candidate rather than only a benchmark, and tests the
   southern/eastern hypotheses against it.

3. **It assumes the buyer is downstream of the anecdote (asset aggregators and
   communities).** The buyer class most consistent with "an individual sold model
   development" is upstream: regional suppliers, Stadtwerke, direct marketers
   (Direktvermarkter) and balance-group managers who carry forecast risk every quarter
   hour and already buy forecasts from vendors. The research adds this class explicitly.

4. **It spends a lot of words on V2G.** Bidirectional charging is unlikely to be relevant
   to a software-first first customer in 2026. The hardware workstream is kept, but
   scoped to answer "what is controllable by third-party software today" rather than
   modelling V2G economics in depth.

5. **Energy communities are probably the wrong first buyer.** Low budgets, slow
   governance and heterogeneous national rules. They are screened, but the hypothesis
   going in is that their software/management vendors are the better buyer, if any.

6. **Date discipline.** The brief is dated October 2026. The coordinator's own knowledge
   ends mid-2026, so every current-rule claim must come from a dated web source; where a
   researcher could not find a 2025–2026 source the report must say so.

## Working hypotheses to be tested (not conclusions)

- H1: The most sellable first product from Munich is a narrow forecasting or dispatch
  model sold to a German or Austrian regional supplier/Stadtwerk/direct marketer with a
  measurable imbalance or trading cost, not a residential aggregation platform.
- H2: Residential battery/EV/heat-pump aggregation in Germany is already heavily
  contested by vertically integrated players (1KOMMA5°, Enpal, sonnen, Lichtblick,
  Tibber, Octopus) and is a poor independent software wedge.
- H3: Large and C&I battery optimisation in Germany is lucrative but served by well-funded
  specialists (Entrix, Flexpower, Terralayr, enspired, suena); a newcomer needs a niche
  (e.g. small C&I, co-located PV+storage in direct marketing) to enter.
- H4: Netherlands and Belgium are the most attractive non-German markets because
  imbalance-based home battery optimisation and congestion products already pay, but
  they are also the most contested.
- H5: Spain, Italy, Poland and the rest of the brief's list have real structural
  opportunities but weak software-only access for a foreign founder; they are second
  markets, not first.

## Deliverables of this round

- `reports/European energy flexibility startup wedges.md`: the feasibility report
  answering the primary decision, with the brief's structure where useful.
- `research_notes/…`: per-topic evidence notes with sources.
- basemode graph: decisions, rules and open questions, so later sessions start from
  the same state.
