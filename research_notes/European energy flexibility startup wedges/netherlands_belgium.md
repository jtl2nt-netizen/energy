---
type: note
status: complete
tags: [netherlands, belgium, tennet, elia, acm, gopacs, fluvius, imbalance-market, picasso, regeltoestand, home-battery, salderingsregeling, congestion-management, capaciteitssturingscontract, capacity-tariff, aggregators, flexibility-market-entry, research-2026-10]
relatedTo: [european-energy-flexibility-startup-wedges, netherlands-energy-market, belgium-energy-market]
---

# Netherlands and Belgium as target markets for a software-only flexibility forecasting/dispatch vendor (as of October 2026)

Research date: 11 October 2026. Method note: web search budget for this session was exhausted after the first ~12 queries, so most evidence below comes from direct fetches of primary/vendor pages identified in those searches. TenneT.eu and Elia.be pages are behind a Cloudflare JavaScript challenge and could not be read directly; where I cite them, the claim comes from search-result snippets of those pages and is flagged. VREG/VNR (vreg.be), Octopus Belgium, Energy Storage Belgium and Luminus pages returned HTTP 503/404 at research time.

Terminology: "VREG" was renamed "Vlaamse Nutsregulator (VNR)"; 2026 Fluvius/Powerland sources use VNR, older ones VREG. "CBC" (capaciteitsbeperkingscontract) is being replaced by "CSC" (capaciteitssturingscontract) in NL since May 2026.

---

## NL-1. Imbalance-based optimisation: TenneT settlement, passive balancing, 2025–2026 reforms, and what home batteries actually earn

### Takeaway
The Dutch household imbalance ("onbalans") trade is real, paid, and large (tens of thousands of steered devices at Frank Energie alone), but per-battery returns have visibly compressed since PICASSO (Oct 2024) and the 2025–2026 TenneT publication changes, and TenneT is now openly treating synchronised battery reactions to its public balance-delta signal as a system-stability problem (regeltoestand 2 at ~40% of time in 2026 versus a <10% obligation). The value is captured by retailer/BRP-aggregators (Frank, Zonneplan, Eneco, Tibber etc.) that run their own in-house steering stacks and lock the customer to their supply contract.

### Cited Findings

**Rules and reforms in force / proposed**
- TenneT joined the European aFRR platform PICASSO in October 2024; since then average imbalance prices are lower but extremes larger: pre-PICASSO lowest ~-€1,500/MWh; recent Dutch extremes nearly -€4,000/MWh and nearly +€4,400/MWh (article 6 June 2026) — [Solar & Storage Magazine, "Het dilemma", 6 Jun 2026](https://solarmagazine.nl/nieuws-zonne-energie/i43941/het-dilemma-picasso-minder-negatieve-onbalansprijzen-goed-voor-de-onbalansmarkt)
- Share of time in "regeltoestand 2" (shortage and surplus activations within the same ISP, i.e. the state in which single-direction imbalance trading breaks): ~8% average 2016–2023, ~16.8% in 2024, 27.3% in 2025, ~40% in 2026 year-to-date with monthly peaks near 50%; TenneT is obliged to keep it below 10%. Quote (Jan Willem Zwang, Stratergy): "Dat is gewoon een PICASSO-effect" and "Voor batterijen geldt dat daar minder mee kan worden verdiend op de onbalansmarkt." — [Solar & Storage Magazine, 6 Jun 2026](https://solarmagazine.nl/nieuws-zonne-energie/i43941/het-dilemma-picasso-minder-negatieve-onbalansprijzen-goed-voor-de-onbalansmarkt)
- Balance-delta publication history: end-2024 TenneT lengthened the publication delay from 2 to 5 minutes to damp fluctuations ("not to satisfaction"); 18 June 2025 shortened back to 2 minutes; from 25/27 November 2025 TenneT publishes the balance delta every 12 seconds (was every minute) plus a "Hi Res" API; from 3 February 2026 the regeltoestand is determined on the 12-second series; the imbalance price itself is still based on 4-second activations — [Solar & Storage Magazine, 27 Nov 2025](https://solarmagazine.nl/nieuws-zonne-energie/i42301/tennet-publiceert-balansdelta-voortaan-om-de-12-seconden)
- (Search-snippet only, TenneT page blocked) TenneT's Q1 balancing market update: the old minute-based balance-delta publication stopped in May 2026; TenneT has drafted a code change for a "scarcity component" in the balancing-energy/imbalance price with shadow-running in 2027 — [TenneT, "In één oogopslag: marktupdate balancing Q1"](https://www.tennet.eu/nl/nieuws/een-oogopslag-marktupdate-balancing-q1)
- PROPOSAL, not in force: on 5 June 2026 TenneT presented (webinar on ACE oscillations) a last-resort measure to delay the *price component* of the balance delta by 15 minutes when predefined ACE-oscillation thresholds are exceeded; no introduction date, no formal consultation described. Parties steering purely on the public balance delta would be hit hardest; parties with own forecasting/market data less so — [Solar365, 5 Jun 2026](https://www.solar365.nl/nieuws/tennet-overweegt-vertraging-van-onbalansprijs-met-15-minuten-wat-betekent-dat-voor-batterijen-en-energiesturing-67A7B1B0.html)
- Market structure for a household battery: it cannot be a BSP; BSP qualification requires ≥1 MW controllable aggregated capacity and aFRR bids are in ≥1 MW steps, so a 5–10 kW home battery is pooled with roughly 100–200 others. Two routes: (a) "passive" — the supplier/BRP lets its portfolio deviate against the imbalance price (no aFRR contract needed); (b) "active" — a BSP steers the pool on TenneT setpoints every 4 s — [VOLL Energie, page sourced Sept 2026 (vendor source, hostile to pools)](https://voll-energie.nl/bsp-en-afrr-bij-een-thuisbatterij-wat-betekent-dat-eigenlijk/)
- Political/regulatory: on 19 Feb 2025 the minister said rules "voor thuisbatterijen over de handel op de onbalansmarkt" were expected before summer 2025; on 8 July 2025 ACM reported "honderden klachten" about home-battery selling practices; ACM's 2026 plan confirms it warned consumers about misleading battery sales in 2025 — [Echt Susteren Energie news archive](https://www.echtsusterenenergie.nl/tennet-verwacht-alsnog-6-7-gigawatt-batterijen-in-2030/); [ACM Focus op Energie, Feb 2026 (PDF)](https://www.acm.nl/system/files/documents/focus-op-energie-2026-opgemaakt.pdf)

**What is actually earned per home battery (2024 → 2026)**
- Measured by the Mijnbatterij platform on "ruim 400" batteries: average €73.87 per 10 kW in February 2026 and €178.16 per 10 kW in June 2026 (2.4× spread between months); the site states returns "staan structureel onder druk", "elke nieuwe batterij die meedoet maakt de koek per batterij kleiner", and that PICASSO/IGCC close gaps before home batteries are dispatched (published 5 Aug 2026) — [Thuisbatterijnederland.nl](https://thuisbatterijnederland.nl/onbalansmarkt-thuisbatterij/)
- Historical trajectory reported by an installer/comparison site: €150–200 per month in 2023/early-2024, €80–120 per month in 2025; table range €500–1,500/yr marked "dalend"; FCR/aFRR via pool indicatively €100–300/yr for 5–10 kWh; TenneT itself says a 6-year payback via imbalance trading offers "geen garanties" — [Thuisbatterijenhulp.nl (2026)](https://thuisbatterijenhulp.nl/kennisbank/verdienmodellen-van-een-thuisbatterij/)
- VOLL cites one "large aggregator": a 20 kWh battery earned €291.79 in August 2024; by early 2025 ~€100/month with the aggregator itself warning of saturation — [VOLL Energie, Sept 2026](https://voll-energie.nl/bsp-en-afrr-bij-een-thuisbatterij-wat-betekent-dat-eigenlijk/)
- Marketing claims of "tot bijna €2.900 per jaar" stem from 2024/2025 conditions; in 2026 "de opbrengst per batterij daalt"; above ~€1,800/yr of trading revenue the Belastingdienst may treat the household as an economic activity with VAT consequences; two payout models exist (fixed monthly amount vs variable share of actual result); battery wear from aggregator cycling may not be covered by warranty (6 July 2026) — [Stroomvoorspeller.nl](https://www.stroomvoorspeller.nl/kennisbank/thuisbatterij-onbalansmarkt)
- Frank Energie (retailer-aggregator) official estimate for a 10 kW / 20 kWh battery "based on 2025 results and 1.3 cycles/day": self-consumption €0, EPEX-only optimisation €841/yr, "Slim Handelen" (hybrid incl. imbalance) €1,298/yr, up to €1,985/yr when stacked with other smart services; results paid as monthly bonus incl. VAT; no fee or revenue-share percentage disclosed; a Frank dynamic contract is mandatory; purchase mark-ups are set to zero under a fair-use policy — [Frank Energie, Slim Handelen](https://www.frankenergie.nl/nl/slimme-diensten/slim-handelen)
- Frank's battery comparison lists "Resultaat per kW in 2025" per model from €37.52/kW (5 kWh Midea, 5 kW) to €170.93/kW (38.5 kWh AlphaESS, 10 kW, 3-phase); 90 battery models listed; open brand support (AEG, Anker, AlphaESS, Bliq, Enphase, GivEnergy, GoodWe, Sessy, Sigenergy, SolarEdge, …) — [Frank Energie, Thuisbatterij 2026](https://www.frankenergie.nl/thuisbatterij)
- Frank steered "meer dan 30.000 huishoudelijke apparaten" (3 May 2026) and "over 35,000" (21 July 2026) incl. batteries, EVs, heat pumps, AC and PV; its quarterly reports say its hybrid (multi-market) strategy beat EPEX-only every month of Q1 and Q2 2026, but the per-battery €-figures are only in chart images — [Frank Q1 '26](https://www.frankenergie.nl/nl/nieuws/ontwikkeling-sturingsopbrengsten-q1-26); [Frank Q2 '26](https://www.frankenergie.nl/nl/nieuws/ontwikkeling-sturingsopbrengsten-q2-26)
- Zonneplan (retailer + own battery): six-month average returns of ~€300 (10 kWh), €475 (15 kWh), €606 (20 kWh) — i.e. roughly €600–1,200/yr annualised; Zonneplan itself writes returns are lower than in 2024 "omdat prijspieken sinds de aansluiting op het Europese PICASSO-platform (oktober 2024) sneller worden afgevlakt"; most earnings come from the imbalance market and are paid via the energy bill; steering only works with a Zonneplan Energie contract (lock-in); fees €0.02/kWh incl. VAT over spot plus €6.25/product/month; battery prices after VAT refund €4,690 (10 kWh) / €7,290 (20 kWh) / €9,090 (35 kWh) (review 6 May 2026, updated 5 Oct 2026) — [Duurzaam Thuis Lab review](https://duurzaamthuislab.nl/posts/zonneplan-thuisbatterij-review-2026/); Zonneplan's own page: 11 kW, stackable to 35 kWh, "ruim 150.000 installaties" (all products) — [Zonneplan](https://www.zonneplan.nl/thuisbatterij)
- Hardware/other channels: Sessy (5/10/15 kWh at €3,550/€5,500/€9,400 incl. VAT; 2.2 kW charge/1.7 kW discharge; no subscription; imbalance-trading mode; partners Eneco and Bright; KVK Innovation Top 100 2026) — [Sessy](https://www.sessy.nl/); HomeWizard Plug-In Battery (€1,195, 2.7 kWh, dynamic-price steering only, no imbalance trading, payback claims 4–6 yrs) — [HomeWizard](https://www.homewizard.com/nl/plug-in-battery/); VOLL sells third-party control at €5/month — [VOLL](https://voll-energie.nl/bsp-en-afrr-bij-een-thuisbatterij-wat-betekent-dat-eigenlijk/)
- Volume context: 423,000 consumers had a dynamic electricity contract on 1 Jan 2025; grid operators registered 20,596 new batteries in 2025 and a record 30,856 in H1 2026 (May 2026: 5,152), while only 30–40% of installed home batteries are believed to be registered; TenneT raised its 2030 battery forecast from 4.9 GW to 6.7 GW (May 2025) and to 8.6 GW (June 2026, Monitor Voorzieningszekerheid 2026); negative-price hours hit a record 463 by 10 Aug 2025 — [Echt Susteren Energie news archive](https://www.echtsusterenenergie.nl/tennet-verwacht-alsnog-6-7-gigawatt-batterijen-in-2030/)

### Inferences
- The household imbalance wedge is a *retailer* wedge: all major players monetise via their own supply contract (Frank, Zonneplan, Eneco/Sessy, Tibber) and publish no revenue split. A third-party model vendor would sell to these retailers/BRPs, not to households.
- Returns compression is now documented by three independent-ish sources (Mijnbatterij measurement, Zonneplan's own PICASSO statement, the "large aggregator" saturation warning). A realistic 2026 planning range is ~€900–2,100/yr per 10 kW for an actively traded battery on a good aggregator (Mijnbatterij annualised), ~€600–1,300/yr for Zonneplan/Frank-type offers, and several hundred €/yr for simpler dynamic-price steering.
- Regulatory direction is against naive balance-delta chasing: the proposed 15-minute price delay and 2027 scarcity component reward parties with their own imbalance *forecasts* — which is exactly the product a forecasting vendor sells. That is the clearest software wedge in this niche, but the buyers (Frank, Zonneplan, Dexter-served BRPs) already build this in-house.

### Gaps
- TenneT primary pages (imbalance settlement design, BSP lists, aFRR/mFRR volumes) could not be fetched (Cloudflare). I found no source on MARI (mFRR platform) go-live status for NL in 2025–2026 or on specific 2025–2026 ACM decisions targeting household imbalance trading; the Feb-2025 ministerial promise of "rules" has no confirmed outcome in my sources.
- No published revenue-share percentages for any Dutch aggregator; Frank/Zonneplan figures are gross to the customer (incl. VAT), net of unknown vendor margin.
- No independent (TenneT/ACM) statistics on how many MW of household batteries are in BSP pools.

---

## NL-2. End of net metering (salderingsregeling) on 1 Jan 2027, feed-in charges, and whether this is a software or hardware/retailer wedge

### Takeaway
Net metering ends in one step on 1 January 2027 with a 50%-of-supply-tariff floor on feed-in payments until end-2029; this is driving record home-battery sales and a shift to dynamic contracts, but the economic surplus accrues to hardware sellers and retailers, and a double energy-tax issue (~€0.11/kWh on grid-charged cycles) is unresolved.

### Cited Findings
- Net metering ends 1 Jan 2027 in a single step (no phase-out). From 2027 through 2029 suppliers must pay at least 50% of the bare supply tariff (ex VAT and energy tax) for fed-in electricity; the legal minimum lapses 1 Jan 2030 with ACM overseeing "reasonableness". Suppliers may charge feed-in costs (terugleverkosten) only for actual processing costs; several suppliers have charged them since 2024 to heavy net exporters — [Thuisbatterijenhulp, salderingsregeling](https://thuisbatterijenhulp.nl/kennisbank/salderingsregeling/); [Thuisbatterij.nl](https://thuisbatterij.nl/thuisbatterij-capaciteit/salderen/)
- Indicative self-consumption value after 2027: €300–700/yr for 8–12 panels + 10 kWh battery; dynamic charging adds €200–600/yr; feed-in sometimes <€0.05/kWh vs offtake €0.25–0.40/kWh — [Thuisbatterijenhulp](https://thuisbatterijenhulp.nl/kennisbank/verdienmodellen-van-een-thuisbatterij/)
- From 2027 each grid charge/discharge cycle may carry ~€0.11/kWh energy tax that cannot be reclaimed, which VOLL argues "can erase" thin imbalance margins; in July 2026 the Tweede Kamer adopted a motion for further research into the double energy tax on stored electricity; on 14 Feb 2025 the minister saw no short-term fix — [VOLL](https://voll-energie.nl/bsp-en-afrr-bij-een-thuisbatterij-wat-betekent-dat-eigenlijk/); [Echt Susteren Energie archive](https://www.echtsusterenenergie.nl/tennet-verwacht-alsnog-6-7-gigawatt-batterijen-in-2030/)
- Demand signals: half of PV owners consider a dynamic contract when net metering ends (Independer, 7 Jun 2025); ~149,000 PV owners registered for a compensation claim (Salderingsclaim.nl, 6 May 2025); record H1-2026 battery registrations (30,856); from 29 May 2026 fixed home batteries ≥5 kWh count toward the energy label — [Echt Susteren Energie archive](https://www.echtsusterenenergie.nl/tennet-verwacht-alsnog-6-7-gigawatt-batterijen-in-2030/)
- Sales channel reality: Frank's battery comparison (90 models), Zonneplan's battery-plus-contract bundle, Sessy's Eneco/Bright partnerships and HomeWizard's plug-in battery all bundle steering software with hardware or a supply contract — [Frank](https://www.frankenergie.nl/thuisbatterij); [Zonneplan](https://www.zonneplan.nl/thuisbatterij); [Sessy](https://www.sessy.nl/); [HomeWizard](https://www.homewizard.com/nl/plug-in-battery/)
- Consumer-protection overhang: ACM received hundreds of complaints about aggressive/misleading battery sales (July 2025) and warned consumers in 2025 — [ACM Focus op Energie 2026 PDF](https://www.acm.nl/system/files/documents/focus-op-energie-2026-opgemaakt.pdf)

### Inferences
- The 2027 cliff is primarily a hardware + retailer wedge. The software opportunity is indirect: retailers/BRPs that must now forecast and settle hundreds of thousands of PV-plus-battery households at 15-minute granularity, and manage feed-in costs, need better load/PV/imbalance forecasts — a B2B sale to the BRP, not a consumer product.
- The unresolved energy-tax treatment of stored electricity is a material downside risk to the imbalance-trading business case for grid-charged household batteries from 2027.

### Gaps
- No 2026 primary sales statistics (CBS/Netbeheer Nederland) for home batteries; registration counts understate installations. No source found on actual terugleverkosten levels per supplier in 2026.

---

## NL-3. Grid congestion: GOPACS, CBC/CSC, time-dependent tariffs, non-firm ATO, energy hubs — is FSP a real paid market?

### Takeaway
Congestion services in NL are a real, regulated, paid market but gated at ≥100 kW flexible capacity, large connections (>3x80 A) and a certified Congestion Service Provider (CSP); GOPACS traded 228–364 GWh/yr in 2021–2023 (2024–2026 totals not retrievable), the product set was overhauled in 2025–2026 (CSC replaces CBC, GTO for energy hubs, TDTR), and household time/volume-dependent network tariffs are only expected from 2028/2029. Households are not yet paid for congestion flexibility.

### Cited Findings
- Eligibility: congestion management requires a large connection (>3x80 A, >55 kW) and ≥100 kW flexible capacity; parties with >1 MW contracted transport capacity can be obliged by the grid operator to investigate/offer flexibility (suppliers and hospitals excepted); redispatch requires a CSP; "since May 2026 the CSC largely replaces the CBC"; existing group-CBCs stay valid (page checked 28 July 2026) — [RVO, Flexibel contract](https://www.rvo.nl/onderwerpen/netcongestie/flexibel-contract)
- Product set per RVO: CSC with call-off (monthly availability fee), CSC with time blocks, redispatch (bid-obligation or free via GOPACS), blokstroom/time-bound transport right (ATR) on LV/MV, time-duration transport right (TDTR: ≥85% of hours firm, only on TenneT HV grid), group transport agreement (Groeps-TO), group CBC/CSC — [RVO](https://www.rvo.nl/onderwerpen/netcongestie/flexibel-contract)
- GOPACS mechanics: bids via certified CSPs on ETPA, EPEX SPOT and "soon Nord Pool" (cross-platform activation, XPA); CSP recognition for connections with ≥0.1 MW contracted capacity; "in many cases the flexible capacity must be at least 100 kW"; grid operator pays the spread between matched inside/outside orders; CSC-A pays availability + activation, CSC-T fixed compensation; products listed: CSC-A, CSC-T, Redispatch, TDTR, Mandatory Bidding — [GOPACS FAQ](https://www.gopacs.eu/en/frequently-asked-questions/)
- GOPACS volumes (historical): ~288,571 MWh (2021), ~363,917 MWh (2022), ~228,461 MWh (2023) per an ETPA whitepaper (page now 404; figures from search snippet) — [ETPA whitepaper](https://www.etpa.nl/en/whitepapers/gopacs); EPEX SPOT at Flexcon (Oct 2024): "360+ MW of flexibility from six service providers", volumes down in 2024 — [EPEX/Flexcon PDF](https://flexcon.energy/wpcms/wp-content/uploads/2024/10/Day1_EPEX-Spot-Local-Flexibility.pdf); Feb 2025 GOPACS introduced an algorithm combining bids across platforms; May 2025 API rate limits (2,000 calls/min) — [GOPACS release notes](https://www.gopacs.eu/en/product-release-notes/)
- Academic use of GOPACS order-book data (May 2023–Jun 2024, >96% of cleared volume): buy prices in redispatch were "on average still negative" in the studied windows; CLC/RC introduced 2022; minimum redispatch bid 0.1 MW (Sept 2025 paper) — [arXiv 2509.15354](https://arxiv.org/html/2509.15354v1)
- Non-firm ATO: about 50% discount on the connection/transport tariff in exchange for non-guaranteed transport; non-firm customers still entitled to compensation if redispatched; ACM proposal states an NFA "is nadrukkelijk niet een soort capaciteitsbeperkingscontract" — [ACM code-change proposal non-firm ATO (PDF)](https://www.acm.nl/system/files/documents/codewijzigingsvoorstel-non-firm-ato-openbaar.pdf); [Dirkzwager](https://www.dirkzwager.nl/kennis/artikelen/blogreeks-juridische-oplossingen-netcongestie-1-alternatieve-transportrechten)
- ACM 2025 record and 2026 plan: ordered grid operators to produce an improvement plan on congestion instruments; introduced the group transport agreement (GTO) for energy hubs and the CSC "with grid users such as battery operators"; will not pursue location-dependent tariffs for now; expects the time-dependent tariff for large connections to enter into force in 2028 and for small connections "shortly thereafter"; decision on TenneT's future-flexibility-needs report in H2 2026; Energiewet in force 1 Jan 2026 — [ACM Focus op Energie, Feb 2026 (PDF)](https://www.acm.nl/system/files/documents/focus-op-energie-2026-opgemaakt.pdf)
- Draft code decision (published 8 Oct 2026, case ACM/24/193312, proposer Netbeheer Nederland): for connections ≤3x80 A, about two-thirds of the transport tariff becomes volume- and time-dependent; 6-week consultation from Staatscourant publication; no start date on the page — [ACM draft decision](https://www.acm.nl/nl/publicaties/ontwerp-codebesluit-volume-en-tijdsafhankelijke-tarieven-voor-kleine-aansluitingen); news reporting says consumer tariffs with 4 price levels and 5 time blocks from 2028 (Oct 2025) and >2/3 volume/time-dependent from 2029 with the deadline possibly missed (May 2026) — [Echt Susteren Energie archive](https://www.echtsusterenenergie.nl/tennet-verwacht-alsnog-6-7-gigawatt-batterijen-in-2030/)
- Standard congestion compensation for wind/solar parks: ACM (6 May 2026) allows grid operators to keep offering it after a 2-year experiment; "the number of signed congestion-management contracts is still low" and smaller parks often cannot be remotely curtailed — [Energienieuws, 6 May 2026](https://www.energienieuws.info/2026/05/acm-netbeheerders-mogen-blijven-werken.html)
- Energy hubs: GTO described as "In voorbereiding (ontwerp-codebesluit ACM)" by an industry site (updated 29 Jul 2026) whereas ACM says it was introduced in 2025 — status partly conflicting; cable pooling allowed for up to four nearby parties with ≥100 kVA; Liander got a 5-year ACM exemption (Dec 2024) for an energy-volume transport-right experiment; group CBC pays compensation per call-off, amounts not published — [Energiehubs.nl](https://energiehubs.nl/kennisbank/contractvormen-individueel-en-collectief); [ACM Focus 2026](https://www.acm.nl/system/files/documents/focus-op-energie-2026-opgemaakt.pdf)
- Energy Storage NL (2026): reaction to a parliamentary letter on congestion says "the business case for flexibility is under pressure"; National Action Agenda for battery systems published; BESS Apeldoorn reached COD April 2026 — [Energy Storage NL](https://www.energystoragenl.nl/)

### Inferences
- The paid congestion niche is C&I/utility-scale: ≥100 kW, CSP-certified, GOPACS- or CSC-based. For a software vendor, the routes are (a) supply dispatch/forecast models to an existing CSP/aggregator, or (b) to an EMS/battery vendor (iwell-type) that handles CSC availability windows. Households are only reachable through retailers until time-dependent tariffs land (2028+).
- Compensation levels (€/kW/yr) for CSC/CBC are negotiated and not public; the only quantified public evidence is the ~50% tariff discount for non-firm ATO.

### Gaps
- GOPACS 2024–2026 annual volumes/expenditures: the public dashboards (app.gopacs.eu) are JavaScript apps and returned no data; no 2025 annual report found.
- No public €/kW/yr CSC/CBC compensation levels; no count of active CSPs/FSPs in 2026; no verified data on the congestion wait-list size in 2026.

---

## NL-4. Balancing services (FCR, aFRR, mFRR/noodvermogen): minimum sizes, aggregator rights, BSP registration, small-asset aggregators

### Takeaway
Access to TenneT's balancing products requires BSP status with ≥1 MW aggregated controllable capacity and 1-MW bid steps (aFRR); independent aggregation of small assets exists in practice via retailer-BRPs and specialised BSPs, but I could not retrieve TenneT's own product terms or BSP list.

### Cited Findings
- BSP must deliver ≥1 MW controllable power; aFRR bids in ≥1 MW steps; aFRR setpoints every 4 s with delivery within a minute; capacity auctioned daily and paid whether or not activated; energy settled per 15 minutes — [VOLL (Sept 2026)](https://voll-energie.nl/bsp-en-afrr-bij-een-thuisbatterij-wat-betekent-dat-eigenlijk/)
- Indicative pooled FCR/aFRR revenue for a 5–10 kWh household battery: €100–300/yr — [Thuisbatterijenhulp](https://thuisbatterijenhulp.nl/kennisbank/verdienmodellen-van-een-thuisbatterij/)
- Flexcity (Veolia) states 3.5 GW flexible power under management, 300 MW contracted BESS, 200+ steered assets across BE/FR/IT/ES/NL/UK; 2026 case: optimising "Amsterdam's largest" BESS (Giraffe); 2025 case: S4 Energy 4-hour battery in NL; clients include Giga Storage, FrieslandCampina — [Flexcity](https://www.flexcity.energy/en)
- Sympower: "Symbalance" real-time activation/imbalance-cost reduction/congestion relief, BESS optimisation, demand response and a BRP platform; no country or MW figures on the page (placeholders show "0GW+") — [Sympower](https://sympower.net/)
- Dexter Energy (Amsterdam): €23 m Series C (10 Jul 2025, led by Klima/Alantra, with Mirova; existing ETF Partners, Newion, PDENH); AI forecasting + optimisation across day-ahead, intraday and imbalance for "energiebedrijven" and producers; battery optimisation "starts in the Netherlands, then other European markets" — [Emerce, 10 Jul 2025](https://www.emerce.nl/nieuws/dexter-energy-haalt-23-miljoen-euro-aigedreven-optimalisatie-energie)

### Inferences
- A software-only vendor cannot be a BSP without a licensed partner; the natural partner is a retailer-BRP (Frank/Eneco/Vattenfall), a BSP-aggregator (Flexcity, Sympower, Next Kraftwerke) or a BESS owner/optimiser (Giga Storage, S4 Energy). All named NL BSPs already have in-house optimisation teams.

### Gaps
- TenneT product terms (FCR 1 MW, aFRR, mFRR/noodvermogen minimums, prequalification), BSP register, and 2025–2026 procurement volumes/prices could not be fetched. Noodvermogen (mFRRda) specifics are unverified in this note.

---

## NL-5. Energy communities/hubs rules and ACM "independent aggregator" framework status (2026)

### Takeaway
The Energiewet entered into force on 1 January 2026, and ACM's 2026 work plan details energy-hub instruments (GTO, CSC, TDTR) and time-dependent tariffs, but contains no reference at all to an independent-aggregator (BRP-compensation) framework; I found no 2026 ACM decision on independent aggregation.

### Cited Findings
- Energiewet in force 1 Jan 2026; ACM advised the minister on the Invoeringsregeling Energiewet; new model contracts in force 1 Jan 2026; ACM introduced GTO (energy hubs) and CSC in 2025; 2026 decisions planned on time-dependent tariffs (large and small), connection deadlines for small connections, TDTR rules and "validation thresholds" for congestion services — a full-text search of the 18-page document for "aggregat" returned no hits — [ACM Focus op Energie, Feb 2026 (PDF)](https://www.acm.nl/system/files/documents/focus-op-energie-2026-opgemaakt.pdf)
- Fluvius-style community data access is not the NL model; in NL the retailer owns the customer relationship: Zonneplan steering requires a Zonneplan contract; Frank's Slim Handelen requires a Frank dynamic contract; VOLL notes "pool participation is usually tied to one supplier's contract" — [Duurzaam Thuis Lab](https://duurzaamthuislab.nl/posts/zonneplan-thuisbatterij-review-2026/); [Frank](https://www.frankenergie.nl/nl/slimme-diensten/slim-handelen); [VOLL](https://voll-energie.nl/bsp-en-afrr-bij-een-thuisbatterij-wat-betekent-dat-eigenlijk/)
- Energy-hub contracts: GTO, group CBC/CSC, cable pooling (≤4 parties, ≥100 kVA), closed distribution systems (GDS) need ACM exemption — [Energiehubs.nl, updated 29 Jul 2026](https://energiehubs.nl/kennisbank/contractvormen-individueel-en-collectief)

### Inferences
- Absent an independent-aggregator compensation regime, flexibility of small assets in NL is monetised through the supplier/BRP that holds the connection, which structurally favours retailers with in-house stacks and makes a "software-only independent aggregator" model dependent on a retailer partnership.

### Gaps
- Status of any ACM/ministry independent-aggregator (ToE-style) framework under the Energiewet in 2026: not found (search budget exhausted before this could be verified). Number of operating energy hubs: not found.

---

## NL-6. Competition: how many software vendors already sell battery optimisation, and do Dutch BRPs/retailers buy external models?

### Takeaway
The Dutch stack is crowded and vertically integrated: retailers (Frank, Zonneplan, Eneco/Sessy, Tibber, Vattenfall) run their own steering; BESS/EMS vendors (iwell, Flexcity, Sympower, Yuso) run their own optimisation; and Dexter Energy (€23 m raised, 2025) is the reference third-party AI forecasting/optimisation vendor selling to energy companies — proving BRPs do buy external models, but also occupying that slot.

### Cited Findings
- Dexter Energy: €23 m Series C (Jul 2025), sells forecasting/optimisation to energy companies and producers; battery optimisation launched in NL first — [Emerce](https://www.emerce.nl/nieuws/dexter-energy-haalt-23-miljoen-euro-aigedreven-optimalisatie-energie)
- iwell: own EMS + modular BESS, "350+ systemen in 4 landen", offices NL/DE/BE/UK; partners Vattenfall, Eneco, Groendus, Sunrock, Prologis, DAF; projects 2 MW/4 MWh (Leeuwarden), 1.75 MW/4.5 MWh (Horizon Flower Family) — [iwell](https://iwell.eu/nl/)
- Frank Energie: >35,000 devices steered with in-house "hybrid" multi-market strategy; Product Owner Smart Services publishes quarterly results — [Frank Q2 '26](https://www.frankenergie.nl/nl/nieuws/ontwikkeling-sturingsopbrengsten-q2-26)
- Zonneplan: in-house app steering on own spot prices and consumption pattern; closed ecosystem (no open API/Home Assistant) — [Duurzaam Thuis Lab](https://duurzaamthuislab.nl/posts/zonneplan-thuisbatterij-review-2026/)
- Flexcity (Veolia): 300 MW contracted BESS incl. NL (Giraffe, S4 Energy) — [Flexcity](https://www.flexcity.energy/en); Sympower: BESS optimisation + BRP platform — [Sympower](https://sympower.net/); Yuso: 1.2 GW AUM, holds supplier/BRP/BSP licences, battery steering & PV curtailment, Belgian-based — [Yuso](https://yuso.com/)
- Third-party EMS in the consumer space: Bliq Powerflow (energy manager from €679 incl. VAT sold via Frank), Tesla Autobidder, Sigenergy/AlphaESS native VPP software — [Thuisbatterijenhulp](https://thuisbatterijenhulp.nl/kennisbank/verdienmodellen-van-een-thuisbatterij/); [Frank](https://www.frankenergie.nl/thuisbatterij)

### Inferences
- The viable entry for a new forecasting/dispatch vendor is a narrow, measurable improvement sold to a BRP/aggregator (e.g. imbalance-price or regeltoestand forecasting, 15-min household load/PV forecasting for settlement), not a competing consumer app.

### Gaps
- Lyv (lyv.energy did not resolve) and "Ampere" could not be verified; no source on Tibber Homevolt NL economics (page 404). No evidence found on which external vendors Eneco/Essent/Vandebron use.

---

## BE-1. Flanders: capacity tariff, digital meter rollout, end of reverse-running meter, supplier battery/EV offers, dynamic-contract uptake

### Takeaway
Flanders has the structural ingredients (capacity tariff since 1 Jan 2023, 80% digital-meter penetration, prosumer tariff abolished 2026, no battery subsidy since 2023), but the quantified household value is modest and self-consumption-led (peak shaving ~€80–200/yr; dynamic arbitrage ~€250–450/yr per installer estimates), supplier offers are mostly EV smart-charging and dynamic tariffs rather than paid battery flexibility, and I could not retrieve regulator data on dynamic-contract uptake.

### Cited Findings
- Capacity tariff effective 1 Jan 2023 (Fluvius) — [Fluvius capaciteitstarief](https://www.fluvius.be/nl/thema/factuur-en-tarieven/capaciteitstarief)
- Digital meters installed: 80% (goal 100% by end-2029); Fluvius investment plan 2026–2035 €11 bn with ~€200 m shifted from LV to MV because residential electrification (heat pumps, EVs) is "progressing slower than anticipated" while industry, battery parks and data centres accelerate; data-management plan 2026–2035 built on 15-minute digital-meter data with a "market for active end consumers" layer (40 initiatives, €30 m/yr) (Feb 2026) — [Fluvius investor presentation, Feb 2026 (PDF)](https://over.fluvius.be/sites/fluvius/files/2026-02/fluvius-investor-presentation-february-2026.pdf)
- Flemish battery premium stopped for inspections after 1 April 2023; last payouts 1 Dec 2024; ~60 municipalities paid €100–750 locally in 2025; prosumer network tariff abolished from 2026 (~€120/yr saving); installer's value stack (May 2026): self-consumption €350–500/yr, capacity-tariff peak shaving €80–150/yr, dynamic-contract arbitrage €250–450/yr; feed-in €0.03–0.08/kWh vs offtake €0.18–0.28/kWh; payback 7.5 yrs for 10 kWh with smart control + dynamic (€1,000/yr) vs 15 yrs on fixed contract (€500/yr) — vendor data, not independent — [Solarnation, 8 May 2026](https://solarnation.be/het-laatste-nieuws/premie-thuisbatterij-gestopt-2026-rendabel)
- Other installer estimates (search snippets): capacity-tariff saving ~€100–200/yr — [Bollen Energy](https://bollen-energy.be/thuisbatterij/thuisbatterij-kostprijs/); 10 kWh + 6 kWp ~€650/yr, 20 kWh with dynamic tariff ~€1,200/yr (model calcs) — [Energy-Village](https://www.energy-village.be/nl/thuisbatterij/prijs/)
- ENGIE Belgium: Smart Charge pays "±1€ per slimme laadsessie" for Empower/Easy/Flow customers; new "Empower Flextime" tariff compared with dynamic prices; "Smart Battery" and "Solar Surplus" products exist but no figures — [ENGIE BE](https://www.engie.be/nl/)
- Bolt: local-producer model (125 producers added this year, 500+ injection points, ~209 GWh), "best feed-in compensation"; no battery-steering product on the page — [Bolt](https://www.boltenergie.be/nl)
- Plug-in batteries must be registered with Fluvius within 30 days if ≥800 W — [Plug-in Solar Energy](https://pluginsolarenergy.be/en/blogs/nieuws/stekkerbatterij-in-belgie-regels-synergrid-en-fluvius)

### Inferences
- Belgian residential flexibility value today is a bill-optimisation story (capacity peak + dynamic spread), not a market-revenue story; there is no evidence of households being paid for imbalance or aFRR via aggregators at scale, unlike NL.
- The slower-than-expected residential electrification noted by Fluvius reduces near-term addressable volume for EV/heat-pump optimisation in Flanders.

### Gaps
- VREG/VNR pages (capacity tariff mechanics, €/kW/yr level, dynamic-contract counts, reverse-meter timeline) returned 503; Octopus Belgium and Luminus pages failed; Ecopower and Dats24 not researched. No official count of Flemish home batteries or dynamic contracts in 2026 found.

---

## BE-2. Elia transfer-of-energy, aFRR/mFRR access for small assets, Fluvius/ORES flexibility market, consumer-centric design — who is paid and how much

### Takeaway
Belgium's institutional design is more aggregator-friendly than NL (Elia opened aFRR to aggregators in 2020, LV delivery-point groups exist in the aFRR terms, Fluvius buys flexibility on NODES from 10 kW aggregated since Jan 2025), but published remuneration for small assets is absent, Fluvius' own flex purchases are opaque, and the biggest live flexibility topic is connection-linked curtailment (Fall-Back Flex / FAO) for >1 MVA C&I and ~500 stalled battery projects — unpaid.

### Cited Findings
- (Search snippet; Elia pages blocked) Current T&C BSP aFRR in force "as of 04/05/2026"; Elia's aFRR design note (Sept 2025) says evolutions were to be discussed in the WG Balancing end-2025/early-2026; aFRR energy may be offered on aggregated DP SU within one technical facility; delivery points ≤1 kV "need to be included in an aFRR Low-Voltage Delivery Point Group" — [Elia aFRR page](https://www.elia.be/en/electricity-market-and-system/system-services/keeping-the-balance/afrr); [Elia aFRR design note Sept 2025 (PDF)](https://www.elia.be/-/media/project/elia/elia-site/electricity-market-and-system/system-services/keeping-the-balance/afrr/202509_design_note_afrr.pdf)
- Historical: Elia opened aFRR to aggregators in autumn 2020 with a two-step auction (24 h symmetric; 4 h asymmetric); full activation within 7.5 min, setpoints every 4 s; CREG halted step-2 auctions in Oct 2020 after price spikes, reopened Dec 2020 — [Next Kraftwerke blog, 10 Mar 2021](https://www.next-kraftwerke.com/energy-blog/opening-afrr-market-belgium)
- Watts.happening aFRR simulator (Elia-data based, updated 14 May 2025; calculation period 1 May 2023–30 Apr 2024, explicitly "historical … market context has evolved"): capacity remuneration is pay-as-bid, modelled at max(70% of average price, bid price); minimum 4-hour CCTU blocks; example 4 MW/12 MWh battery with only 50% of power usable due to reserve assumptions — [Watts.happening aFRR model (PDF)](https://www.wattshappening.be/assets/pdf/aFRR_140525.pdf)
- Fluvius local flexibility market on NODES: opened 1 Jan 2025 (purchases from Dec 2024); products ShortFlex (activation), LongFlex and MaxUsage (reservation); demand turn-down and generation turn-up; minimum 0.01 MW (10 kW) "may be delivered by aggregated assets"; FSP onboarding via NODES + BOSA eProcurement; partners Smappee, Powernaut, Companion Energy, Thermovault, IMBY; pricing and volumes not public — [NODES, Fluvius market](https://nodesmarket.com/fluvius-market/)
- Connection-linked flexibility (unpaid): Fall-Back Flex gives full requested capacity in congestion zones with Fluvius remote-curtailment rights; the structural Flexible Connection Agreement (FAO) decree was approved Oct 2025 for new connections/upgrades >1 MVA; VNR relaxed the investment condition in April 2026; as of 30 Apr 2026: 883 flex requests awaiting offers, 423 battery files stalled pending policy, 106 battery files awaiting a new flex contract; telecontrol mandatory from 1 MVA with a proposal to lower to 100 kW for batteries; banks want worst-case curtailment guarantees; "no payment, compensation or remuneration" mentioned — [Powerland (data as of 30 Apr 2026)](https://www.powerland.be/en/blog/artikel/flexible-grid-connection-fluvius-fall-back-flex-bess); Fluvius press 24 Apr 2026: 760 applications can be connected flexibly; ~500 industrial battery applications awaiting bids; VREG decision on the battery connection contract pending — [Fluvius press, 24 Apr 2026](https://pers.fluvius.be/grid-congestion-solution-for-nearly-800-companies-seeking-grid-connection)
- Fluvius data strategy explicitly targets "the market for active end consumers" on 15-minute meter data (2026–2035) — [Fluvius IR Feb 2026](https://over.fluvius.be/sites/fluvius/files/2026-02/fluvius-investor-presentation-february-2026.pdf)

### Inferences
- Belgium offers a formally open route (LV delivery-point groups in aFRR, 10 kW aggregated minimum at Fluvius) that a software vendor could exploit via a BSP/FSP partner, but there is no public evidence of €/battery/yr being paid to households, so the near-term revenue pool is C&I/BESS.
- The ~500-file industrial battery queue plus mandatory telecontrol/EMS-RTU requirements create demand for dispatch software that can honour DSO curtailment constraints while optimising market revenue — a plausible B2B wedge once the VNR battery-contract decision lands (expected 2026).

### Gaps
- Elia consumer-centric market design, transfer-of-energy compensation rules, 2025–2026 aFRR/mFRR auction prices (€/MW/h) and BSP counts: not retrievable (Cloudflare; Elia open-data API queries failed on field names). ORES/Wallonia flexibility market not researched. No published €/kW/yr or €/battery/yr for Belgian residential flexibility.

---

## BE-3. Active aggregators/vendors in Belgium

### Takeaway
Belgium's flexibility market is served by a small set of established, licensed aggregators (Flexcity/Veolia, Centrica (ex-REstore), Next Kraftwerke, Yuso, Sympower) plus home-energy platforms partnered with Fluvius (Smappee, Powernaut, Companion Energy, Thermovault, IMBY); all hold BRP/BSP/FSP roles that a software vendor would need to partner with.

### Cited Findings
- Flexcity (Veolia, Belgian-origin): 3.5 GW under management, 300 MW contracted BESS, Belgium CRM article 2025 — [Flexcity](https://www.flexcity.energy/en)
- Next Kraftwerke Belgium: group figures 15,541 MW networked, 14,375 units (Q4 2025); batteries listed among asset types; no Belgian MW split — [Next Kraftwerke BE](https://www.next-kraftwerke.be/)
- Yuso (Waregem): 1.2 GW AUM; licences as supplier, BRP, BSP, scheduling agent, outage-planning agent, voltage-service provider; battery steering, PV curtailment, utility-scale BESS — [Yuso](https://yuso.com/)
- Centrica (ex-REstore/FlexPond): Belgian site now redirects to Centrica Energy; the group page lists BESS, heat & power and renewable flexibility services but no Belgian detail — [Centrica Energy](https://centricaenergy.com/)
- Fluvius NODES partners: Smappee, Powernaut, Companion Energy, Thermovault, IMBY, Alpro, Cogen Vlaanderen — [NODES](https://nodesmarket.com/fluvius-market/)
- iwell has a Belgian office — [iwell](https://iwell.eu/nl/)

### Inferences
- Belgium's aggregator layer is mature and consolidated at the C&I/BESS level; residential-flex platforms (Smappee, Powernaut) are the likelier partners for a small-asset forecasting vendor.

### Gaps
- Sympower's Belgian presence and Elia pilot participants in 2025–2026 unverified; Energy Storage Belgium site unavailable (503).

---

## X-1. Market-access routes for a software vendor via a licensed partner (NL and BE)

### Takeaway
In both countries every monetisation route runs through a licensed role — BRP/supplier (imbalance), BSP (FCR/aFRR/mFRR), CSP/FSP (congestion) — with hard size floors (NL: 1 MW BSP, 100 kW congestion; BE: 10 kW aggregated at Fluvius, LV delivery-point groups at Elia); the software vendor's product must therefore be an input (forecasts, dispatch schedules, bidding signals) to those partners' systems.

### Cited Findings
- NL BSP ≥1 MW, aFRR 1 MW steps, household pooling via supplier/BRP — [VOLL](https://voll-energie.nl/bsp-en-afrr-bij-een-thuisbatterij-wat-betekent-dat-eigenlijk/)
- NL congestion: ≥100 kW, CSP certification for ≥0.1 MW connections, bids via ETPA/EPEX/Nord Pool — [GOPACS FAQ](https://www.gopacs.eu/en/frequently-asked-questions/); [RVO](https://www.rvo.nl/onderwerpen/netcongestie/flexibel-contract)
- BE Fluvius FSP: 10 kW aggregated; registration via NODES + BOSA — [NODES](https://nodesmarket.com/fluvius-market/); BE Elia aFRR LV delivery-point groups — [Elia aFRR page (snippet)](https://www.elia.be/en/electricity-market-and-system/system-services/keeping-the-balance/afrr)
- NL household steering is contract-bound to the supplier (Frank, Zonneplan) — [Frank](https://www.frankenergie.nl/nl/slimme-diensten/slim-handelen); [Duurzaam Thuis Lab](https://duurzaamthuislab.nl/posts/zonneplan-thuisbatterij-review-2026/)
- Dexter demonstrates BRPs/energy companies buying external AI forecasting/optimisation in NL — [Emerce](https://www.emerce.nl/nieuws/dexter-energy-haalt-23-miljoen-euro-aigedreven-optimalisatie-energie)

### Inferences
- Candidate partner types, by niche: NL retailer-BRPs (Frank, Eneco, Vattenfall, Essent) for household batteries/EV/heat pumps; NL/BE BSP-aggregators (Flexcity, Sympower, Next Kraftwerke, Yuso) and BESS owners (Giga Storage, S4 Energy) for utility/C&I batteries; BE home-energy platforms (Smappee, Powernaut) for Fluvius flex.

### Gaps
- No public price lists or partnership terms from any partner type.

---

## X-2. Accessibility for a Munich-based English-speaking founder plus a Portuguese co-founder

### Takeaway
B2B energy-market selling in NL and BE is feasible in English and remotely (the relevant counterparties are international aggregators, BRPs and investors; Dexter, Flexcity, Sympower, Yuso, Next Kraftwerke all publish in English), but consumer-facing and regulatory material is overwhelmingly Dutch (NL) and Dutch/French (BE), and the Belgian market is split by region (Flanders/VNR-Fluvius vs Wallonia/CWaPE-ORES).

### Cited Findings
- English-language vendor sites and press: Flexcity (6 countries) — [Flexcity](https://www.flexcity.energy/en); Sympower — [Sympower](https://sympower.net/); Yuso (EN/NL site) — [Yuso](https://yuso.com/); Next Kraftwerke BE — [Next Kraftwerke](https://www.next-kraftwerke.be/); NODES Fluvius market documentation in English — [NODES](https://nodesmarket.com/fluvius-market/); GOPACS documentation in English — [GOPACS](https://www.gopacs.eu/en/frequently-asked-questions/)
- Regulatory and consumer materials are Dutch-only: ACM draft decision and Focus op Energie — [ACM](https://www.acm.nl/nl/publicaties/ontwerp-codebesluit-volume-en-tijdsafhankelijke-tarieven-voor-kleine-aansluitingen); RVO — [RVO](https://www.rvo.nl/onderwerpen/netcongestie/flexibel-contract); Frank/Zonneplan pages — [Frank](https://www.frankenergie.nl/nl/slimme-diensten/slim-handelen)
- Belgian institutional split: Fluvius (Flanders DSO) with VNR as regulator; Fluvius registration for FSPs runs through BOSA eProcurement (federal) — [NODES](https://nodesmarket.com/fluvius-market/); [Powerland](https://www.powerland.be/en/blog/artikel/flexible-grid-connection-fluvius-fall-back-flex-bess)
- Licensed roles (BRP, BSP, supplier, CSP) are held by partners; no evidence that a pure software vendor needs a local legal entity to supply models to a licensed partner (none of the fetched sources imposes one), but Fluvius FSP registration is a Belgian public-procurement process — [NODES](https://nodesmarket.com/fluvius-market/)

### Inferences
- A Munich/Lisbon team can sell to NL/BE aggregators and BRPs in English without a local entity, provided the partner holds the licences. Reading Dutch is a practical requirement for tracking TenneT/ACM/VNR rule changes, which are frequent (five balance-delta/regeltoestand changes between end-2024 and Feb-2026).

### Gaps
- No source on establishment requirements for CSP certification by a foreign entity or on language requirements in TenneT/Elia BSP contracts.

---

## X-3. Judgment: does NL/BE beat Germany or Portugal as a first or second market for this team?

### Takeaway
On the NL/BE evidence alone: the Netherlands is the deepest, most liquid flexibility market in the pair (tens of thousands of steered household devices, 8.6 GW battery forecast for 2030, functioning congestion products) but is also the most contested and regulatorily unstable niche for household-battery imbalance trading; Belgium is structurally open but thin in paid residential flexibility and stuck in a C&I battery connection backlog. Neither looks like a first market for a software-only forecasting vendor; NL is a credible *second* market for a B2B imbalance-/regeltoestand-forecasting or 15-minute settlement-forecasting product sold to BRPs and BSP-aggregators, and Belgium a later third market via Fluvius-partnered platforms or BESS optimisers.

### Cited Findings
- NL demand depth: Frank >35,000 devices (Jul 2026) — [Frank Q2 '26](https://www.frankenergie.nl/nl/nieuws/ontwikkeling-sturingsopbrengsten-q2-26); TenneT 8.6 GW batteries by 2030 (Jun 2026), 30,856 battery registrations H1 2026 — [Echt Susteren Energie archive](https://www.echtsusterenenergie.nl/tennet-verwacht-alsnog-6-7-gigawatt-batterijen-in-2030/)
- NL contestation: Zonneplan/Frank/Dexter/Flexcity/Sympower/iwell all run proprietary optimisation — [sources above]; returns compressing (Mijnbatterij, Zonneplan) — [Thuisbatterijnederland](https://thuisbatterijnederland.nl/onbalansmarkt-thuisbatterij/); [Duurzaam Thuis Lab](https://duurzaamthuislab.nl/posts/zonneplan-thuisbatterij-review-2026/)
- NL regulatory instability: regeltoestand 2 at ~40% of 2026, TenneT considering 15-min price delay, scarcity component shadow-run 2027, energy-tax question unresolved — [Solar & Storage Magazine](https://solarmagazine.nl/nieuws-zonne-energie/i43941/het-dilemma-picasso-minder-negatieve-onbalansprijzen-goed-voor-de-onbalansmarkt); [Solar365](https://www.solar365.nl/nieuws/tennet-overweegt-vertraging-van-onbalansprijs-met-15-minuten-wat-betekent-dat-voor-batterijen-en-energiesturing-67A7B1B0.html)
- NL evidence that forecasting beats signal-chasing: parties "with their own forecasting, market data, weather information or advanced algorithms" are expected to be less affected by the proposed delay — [Solar365](https://www.solar365.nl/nieuws/tennet-overweegt-vertraging-van-onbalansprijs-met-15-minuten-wat-betekent-dat-voor-batterijen-en-energiesturing-67A7B1B0.html)
- BE thinness: residential value €80–450/yr per stream (installer estimates), no published small-asset remuneration, Fluvius sees residential electrification slower than planned; C&I battery backlog ~500 files pending regulator decision — [Solarnation](https://solarnation.be/het-laatste-nieuws/premie-thuisbatterij-gestopt-2026-rendabel); [Fluvius IR](https://over.fluvius.be/sites/fluvius/files/2026-02/fluvius-investor-presentation-february-2026.pdf); [Fluvius press](https://pers.fluvius.be/grid-congestion-solution-for-nearly-800-companies-seeking-grid-connection)

### Inferences
- Where money is paid in NL in 2026, ranked by accessibility to a model vendor: (1) BRP imbalance/settlement optimisation for household portfolios (buyer: retailers; product: forecasts); (2) utility/C&I BESS multi-market dispatch (buyer: BSP-aggregators/BESS owners; highly contested); (3) congestion CSC/GOPACS (buyer: CSPs; ≥100 kW; opaque pricing); (4) household time-dependent tariffs (not before 2028/29).
- Where money is paid in BE in 2026: (1) C&I/BESS aFRR/mFRR and CRM via established aggregators; (2) Fluvius NODES flex from 10 kW (prices opaque); (3) household bill optimisation (capacity peak + dynamic spread), not market revenue.
- Comparison with Germany/Portugal is outside this note's evidence base (covered by other researchers); the NL-specific comparative advantage is liquidity and sophistication of buyers, its disadvantage is incumbent in-house capability and rule churn; Belgium's comparative advantage is formal openness to aggregation at small sizes, its disadvantage is scale and regional fragmentation.

### Gaps
- No German or Portuguese data was collected here; the final relative ranking must combine this note with the DE/PT notes.
- Quantitative size of the NL BRP-forecasting buyer market (number of BRPs steering household assets, their external software spend) is not available from public sources found.
