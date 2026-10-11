---
type: note
status: complete
tags: [energy-startup, regulation, REMIT-II, EnWG, MsbG, NIS2, DL-15-2022, EXIST, FLUEGGE, EIC-Accelerator, Eurostars, StartUP-Voucher, Portugal-Ventures, go-to-market, public-procurement, CCP-2026, cross-border-employment, UG-GmbH-vs-Lda, Munich, Lisbon]
relatedTo: [european-energy-flexibility-startup-wedges]
---

# Funding, regulation and go-to-market for a DE–PT energy forecasting/optimisation software startup (research date: 11 October 2026)

Scope note: evidence note for a two-founder team (technical founder in Munich; Portuguese co-founder resident in Portugal; no capital, no industry network) planning to start a software-only energy-market forecasting/optimisation company in late 2026. All amounts in EUR; VAT treatment stated where relevant. "Legal fact" = statute/regulator/official programme text; "interpretation" = my reading, flagged. Every item that needs a lawyer/tax adviser is marked **[ADVISER]**.

Method note: web search budget for this session was exhausted after the first ~35 queries (shared limit), so later evidence comes from direct fetches of primary pages/PDFs. Several primary pages were unreachable (ACER open letters: HTTP 503; regelleistung.net prequalification page: 404; IAPMEI programme pages and startupportugal.com: rate-limited; Thüga/E.ON/EnBW innovation pages: 404/403). These are listed as gaps with the page to check.

---

## A1. Germany: which activities need a licence/registration/market role, and does a software vendor need any?

### Takeaway
In Germany the regulated roles are tied to *contractual* positions in the market (supplying customers, being responsible for a balance group, selling into balancing markets, operating metering points), not to producing forecasts or dispatch recommendations. The sources found confirm the §5 EnWG supplier notification scope and the MsbG list of parties entitled to meter data (which explicitly allows a vendor to act as an Art. 28 GDPR processor for an entitled party); I could not fetch the prequalification and Bilanzkreisvertrag pages, so those remain partly uncited. No source found imposes a registration on a pure software/analytics vendor — but this is an absence of evidence, not a regulator statement **[ADVISER]**.

### Cited Findings
- §5 EnWG notification duty applies to "Energielieferanten, die Haushaltskunden mit Energie beliefern" (suppliers of household customers); BNetzA publishes the list of notified suppliers. Text version labelled valid as of 23 Dec 2025 — [lexetius §5 EnWG](https://lexetius.com/EnWG/5); [Gesetze/BNetzA page](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/HandelundVertrieb/Lieferantenanzeige/start)
- BNetzA FAQ: the duty covers electricity/gas suppliers that supply household customers via the public grid (also foreign-seated suppliers); exemptions for supply inside a Kundenanlage, closed distribution networks; commercial customers >10,000 kWh/yr do not trigger it; charging-point operators are not obliged, "wer den Ladepunkt mit Strom beliefert" is the supplier; BNetzA may prohibit activity if "wirtschaftliche Leistungsfähigkeit oder Zuverlässigkeit nicht gewährleistet ist"; notify "unverzüglich nach Aufnahme der Tätigkeit"; cessation ≥3 months in advance — [BNetzA Lieferantenanzeige FAQ](https://bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/HandelundVertrieb/Lieferantenanzeige/start.html)
- Balance-group settlement: 50Hertz settles forecast deviations "mit den verantwortlichen Marktteilnehmern" — the Bilanzkreisverantwortliche — as part of Bilanzkreiskoordination — [50Hertz Bilanzkreise](https://www.50hertz.com/de/Markt/Bilanzkreise)
- MsbG §49(1)–(2): personal metering data may be processed only by the listed "berechtigte Stellen": Messstellenbetreiber, Netzbetreiber, Bilanzkoordinatoren, Bilanzkreisverantwortliche, Direktvermarktungsunternehmen, Energielieferanten, Aggregationsverantwortliche, Messwertweiterverarbeiter, and any party holding Art. 7 GDPR-compliant consent of the connection user. §49(3): entitled parties may use a processor under Art. 28 GDPR. §49(5): supply/tariff access may not be conditioned on unnecessary personal data — [buzer.de MsbG §49](https://www.buzer.de/s1.htm?a=49&g=MsbG&dorg=1)
- BSI develops (on behalf of BMWE) requirements for the Smart-Meter-Gateway with security module, CLS components and the Smart Metering PKI under the MsbG; "Die Einhaltung der Vorgaben werden im Rahmen eines Zertifizierungsverfahrens durch das BSI überprüft"; CLS = control boxes / energy management systems that can be added to control and switch devices — [BSI Smart Metering](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Smart-metering/smart-metering_node.html)
- German NIS2 implementation (NIS2UmsuCG) entered into force 6 Dec 2025 with no transition period; covered: ≥50 employees or ≥€10m turnover/balance sheet in 13 (some sources: 18) sectors incl. energy; two categories (besonders wichtige / wichtige Einrichtungen); registration via "Mein Unternehmenskonto" then BSI portal; "Lieferkettensicherheit" is among required measures but the page describes no direct flow-down to vendors — [usd.de](https://www.usd.de/nis2umsucg-offiziell-in-kraft/); [Scheja & Partners](https://scheja-partners.de/en/2026/01/07/nis2-implementation-act-new-cybersecurity-obligations-since-5-december-2025); registration generally within 3 months of entry into force — [DQS](https://www.dqsglobal.com/de/entdecken/blog/nis2-und-nis2umsucg)

### Inferences
- (Interpretation) A vendor that only delivers forecasts, bid/dispatch recommendations or even sends setpoints *within the client's own systems* is not an Energielieferant (§5 EnWG), not a BKV (no Bilanzkreisvertrag), not a balancing-service provider (the Rahmenvertrag/prequalification is held by the party that bids), not a Direktvermarkter (no EEG marketing contract with plant operators) and not a Messstellenbetreiber. None of the cited texts attach a registration to the analytics function itself.
- (Interpretation) For meter data the clean construction under MsbG §49(3) is: the entitled party (supplier, Direktvermarkter, Aggregationsverantwortlicher, BKV) remains controller; the startup is Auftragsverarbeiter under an Art. 28 GDPR contract. Direct access as "Messwertweiterverarbeiter" or via consumer consent is possible but heavier.
- (Interpretation) A 2-person startup is far below NIS2 size thresholds; exposure comes contractually (client supply-chain clauses, security questionnaires), not statutorily.

### Gaps
- Could not fetch §4 StromNZV (gesetze-im-internet returned 503), the standard Bilanzkreisvertrag, or the TSO prequalification conditions (regelleistung.net pages returned 404). Check: gesetze-im-internet.de/stromnzv/__4.html; regelleistung.net → "Präqualifikation"; 50hertz.com → Bilanzkreiskunden.
- §10b EEG (Fernsteuerbarkeit/Direktvermarktung) could not be fetched (503). Check gesetze-im-internet.de/eeg_2014/__10b.html.
- "Energy sharing" operator role under the 2025 EnWG amendments: no source retrieved. Check EnWG §42c (gesetze-im-internet) and BNetzA pages.
- BSI "externer Marktteilnehmer (EMT)" role and whether third-party steering software needs certification: BSI overview page does not say; check BSI TR-03109-1/-6 and "Administration und Betrieb" subpage **[ADVISER / BSI]**.
- No BNetzA guidance or legal commentary explicitly stating "software vendors need no registration" was found; this remains an inference **[ADVISER]**.

---

## A2. Portugal: comercializador, agregador, agente de mercado — what a software vendor needs

### Takeaway
Under DL 15/2022 (SEN regime), retail supply and *independent aggregation* are registration activities with DGEG (aggregation of last resort needs a licence); registered retailers are automatically allowed to aggregate after notifying DGEG. ERSE's register (updated 17 Jul 2026) lists separate categories for market agents (ADM), aggregators (AGR) and retailers (COM). No source describes any registration for a software/analytics provider; DGEG's activity page lists only market roles.

### Cited Findings
- DL 15/2022 of 14 Jan 2022 transposes Directive (EU) 2019/944 and consolidates the former DL 29/2006 and DL 172/2006 regime — [MLGTS legal alert](https://www.mlgts.pt/xms/files/site_2018/Newsletters/2022/Novo_regime_juridico_da_organizacao_e_funcionamento_do_Sistema_Eletrico_Nacional_-_Legal_Alert_-PT-.pdf)
- SRS Legal note on DL 15/2022: independent aggregation is "exercida em regime de livre concorrência e está sujeita a registo junto da DGEG"; aggregation of last resort "está sujeita a licença"; "Os comercializadores registados estão dispensados da obtenção do registo de agregador, ficando automaticamente habilitados a exercer a atividade de agregação após notificação à DGEG"; peer-to-peer trading introduced; the switching operator (OLMC) role now also covers switching of aggregator — [SRS Legal nota informativa](https://www.srslegal.pt/xms/files/Nota_Informativa_Novas_regras_de_organizacao_e_funcionamento_do_Sistema_Eletrico_Nacional.pdf)
- ERSE register of entities (Diretiva 16/2019, "Atualizado a 17 de julho de 2026") has categories: ADM "Entidades com estatuto de Agente de Mercado", AGR "Agregadores em regime de mercado", AUR "Agregador de último recurso", COM "Comercializadores em regime de mercado", CUR, OLM, OPC etc.; e.g. Gold Energy appears as AGR0121EE, COM0121EE and OPC0121EE — [ERSE registo (PDF)](https://www.erse.pt/media/radffdkh/cria_atualizado.pdf)
- DGEG "Atividades e Profissões" page lists "Comercializador de Energia Elétrica" as a regulated activity but gives no requirements; it mentions a 2026 decree on production (DL 100/2026) — [DGEG](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/atividades-e-profissoes/); DGEG's electricity page also highlights "Decreto-Lei n.º 130/2026" amending the SEN regime — [DGEG comercialização](https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/comercializacao-de-energia-eletrica/)
- DGEG Despacho 30/2026 (published 20 Apr 2026, in force 21 Apr 2026) concerns counting of deadlines in Arts. 14 and 58 of DL 15/2022 "na sua redação atual" (licensing of generation) — [Pérez-Llorca](https://www.perezllorca.com/pt/atualidade/nota-juridica/despacho-n-o-30-2026-da-direcao-geral-de-energia-e-geologia-suspensao-dos-prazos-de-licenciamento-de-centros-electroprodutores/)
- Portugal NIS2: Decreto-Lei n.º 125/2025 of 4 Dec 2025 replaces Lei 46/2018; in force 3 Apr 2026; 17 sectors + public administration incl. energy and ICT services (managed services, cloud); registration with CNCS April–May 2026; cybersecurity officer by May 2026; 12-month fine grace until April 2027 for organisations with a structured adaptation process; supply-chain risk assessment is a covered-entity obligation — [Forbes PT](https://www.forbespt.com/?p=183152); entry into force 3 Apr 2026 also per [RISI tracker](https://www.risidata.com/regulations/nis2/countries/pt)

### Inferences
- (Interpretation) A software vendor whose Portuguese client is the registered comercializador/agregador/agente de mercado needs no DGEG registration; if the startup itself wanted to contract flexibility from customers and sell it, it would need the agregador registration (and a market-agent relationship with OMIE/REN for settlement) — i.e., it would become the regulated party **[ADVISER]**.
- (Interpretation) DL 130/2026 is a 2026 amendment of DL 15/2022 whose content I could not retrieve; it must be checked before relying on the 2022 aggregator rules.

### Gaps
- Documents/fees/timing for DGEG registration of comercializador or agregador not found (DGEG page gives none). Check DGEG "No Setor Elétrico Nacional" tab and the consolidated DL 15/2022 on diariodarepublica.pt (Arts. on comercialização/agregação).
- Content of DL 130/2026 not retrieved.
- OMIE/REN market-agent admission requirements (collateral, fees) not researched.

---

## A3. REMIT II (Regulation (EU) 2024/1106): algorithmic trading, PPAETs, DEA, and the status of a model vendor

### Takeaway
REMIT II obligations on algorithmic trading (Art. 5a) sit on *market participants*; ACER's guidance (as relayed by Nord Pool) explicitly says those requirements also apply when the MP uses "stand-alone vendor algorithms by third parties", and that MPs are "fully responsible" for algorithm behaviour — so a vendor's practical exposure is contractual (documentation, kill-switch, vendor questionnaire), not a REMIT registration. PPAET duties (surveillance, STOR reporting of suspicious orders) attach to persons "professionally arranging or executing transactions"; whether a vendor that actually places orders on an OMP for a client crosses into PPAET territory is unresolved in the sources retrieved **[ADVISER]**.

### Cited Findings
- REMIT II entered into force 7 May 2024; Art. 5a: all market participants must report use of algorithmic trading; NRAs may request strategies/parameters; firms must maintain effective risk controls (resiliency, capacity, functioning, compliance). Art. 15: PPAETs must alert ACER/NRAs on reasonable suspicion of insider trading/manipulation and set up detection mechanisms; non-EU MPs needed a representative by 8 Nov 2024; NRAs remain the sanctioning bodies — [Cleary Gottlieb](https://www.clearygottlieb.com/news-and-insights/publication-listing/eu-adopts-new-measures-against-market-manipulation-on-the-wholesale-energy-market)
- PPAETs must now report suspicious *orders* as well as transactions — [Unyer](https://www.unyer.com/remit-ii-enters-into-force-important-changes-for-energy-trading/)
- ACER open letter on algorithmic trading and DEA dated 30 Jul 2024 is addressed to firms that "engage in algorithmic trading, and/or provide direct electronic access (DEA) to an organised marketplace (OMP)"; notification obligation in force since 7 May 2024 — [VERT summary of ACER news](https://vert.lt/en/Pages/2024-08/Revised-REMIT-brings-new-obligations-for-market-participants-ACER-addresses-algorithmic-trading-notifications.aspx)
- BNetzA: notification of algorithmic trading/DEA is made by updating CEREMP entries; "Mit Aktualisierung der Angaben in CEREMP kommen Marktteilnehmende ihren REMIT-Meldepflichten nach"; MPs that neither trade algorithmically nor offer DEA need not provide these details; updated ACER Guidance was announced for end-2024 — [BNetzA](https://bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/HandelundVertrieb/REMIT/3Aktuelles/Open_Letter_algorth-Handel.html?nn=1024066)
- BNetzA REMIT page lists a new REMIT implementing regulation "(EU) Nr. 2026/256" (dated 30 Jan 2026) covering RRMs and IIPs — [BNetzA REMIT](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/HandelundVertrieb/REMIT/start.html)
- Nord Pool Market Surveillance (Dec 2024), citing ACER REMIT guidance chapter 7: Art. 5a requirements "apply to internal (market participant's) algorithms, external (OMP's) 'execution algorithms' without human intervention and to stand-alone vendor algorithms by third parties"; "MPs are fully responsible for the behaviour of the algorithms they use"; recommends kill switch, pre-/post-trade controls, documentation of "how forecasts are incorporated and generated and the specifics of any AI models used", and a "questionnaire for the vendor" when purchasing third-party algorithms; inside information must not be fed to algorithms; MPs "do need to know and be able to show documentation of the underlying logic and assumptions" — [Nord Pool newsletter Dec 2024 (PDF)](https://nordpoolgroup.com/48cc74/globalassets/download-center/market-surveillance/market-surveillance-newsletter---december-2024.pdf)
- ACER 3rd open letter (25 Sep 2024) covers third-country representatives and PPAETs; a practitioner summary says ACER recommends PPAETs extend MAR-style monitoring to REMIT Arts. 3–5 — [ACER PDF (not readable, 503 on fetch)](https://www.acer.europa.eu/sites/default/files/REMIT/Guidance%20on%20REMIT%20Application/Open%20Letters%20on%20REMIT%20Policy/25092024_3rd_Open_Letter_Third_Countries_PPAETs.pdf); [Bird & Bird](https://www.twobirds.com/en/insights/2024/global/are-you-ready-for-remit-ii) (page returned 402 on fetch; snippet only)

### Inferences
- (Interpretation) Advisory-only delivery (forecasts, recommended schedules, bid curves the client submits) keeps the startup outside REMIT: it is neither an MP nor a PPAET. The client must still document the vendor model under Art. 5a, so the startup should expect to supply model documentation, change logs, test evidence and a vendor questionnaire response as part of any contract.
- (Interpretation) If the startup's software is given credentials to submit orders to an OMP (EPEX/OMIE/regelleistung) on the client's behalf without human intervention, the *client* is doing algorithmic trading using a vendor algorithm and must notify; the startup may be viewed as "executing transactions professionally" (PPAET) or as a DEA user — this is the line where legal advice is required before go-live **[ADVISER]**.
- (Interpretation) The German implementation is procedural (CEREMP update), not a separate licence; the Portuguese NRA route (ERSE; CMVM for financial instruments) was not found and must be checked.

### Gaps
- The ACER open letters themselves (algorithmic trading 30 Jul 2024; PPAET 25 Sep 2024) and the current edition of the ACER Guidance on REMIT could not be fetched (acer.europa.eu returned 503 repeatedly). Check acer.europa.eu → REMIT → "Guidance on REMIT application" for the edition in force in 2026 and any 2025–2026 Q&A on vendor algorithms.
- No ERSE/CMVM statement on national REMIT II implementation in Portugal found.
- No source found on whether a vendor placing orders via a client's DEA is itself a PPAET **[ADVISER]**.

---

## A4. Data (GDPR/MsbG/E-REDES), NIS2, BSI/CLS, liability and insurance

### Takeaway
Germany's MsbG §49 gives a statutory basis to receive smart-meter data as a processor for an entitled party; NIS2 is in force in both countries (DE 6 Dec 2025; PT 3 Apr 2026) but hits only organisations of ≥50 staff/€10m and flows to a small vendor only via client supply-chain clauses; standard German IT professional-indemnity cover (Vermögensschadenhaftpflicht) explicitly covers "Fehlberatung" and programming errors, with typical sums €0.5–1m and small-firm premiums in the tens of euros per month. E-REDES data-access rules for Portugal were not retrieved.

### Cited Findings
- MsbG §49 entitled parties and Art. 28 processor route — see A1 ([buzer.de](https://www.buzer.de/s1.htm?a=49&g=MsbG&dorg=1))
- NIS2 DE: in force 6 Dec 2025, thresholds ≥50 employees or ≥€10m; BSI can ban components/manufacturers; planned manufacturer guarantee declaration for critical components was dropped — [usd.de](https://www.usd.de/nis2umsucg-offiziell-in-kraft/)
- NIS2 PT: DL 125/2025, in force 3 Apr 2026; ICT service providers incl. managed services/cloud are a covered sector; supply-chain risk assessment is a covered-entity duty — [Forbes PT](https://www.forbespt.com/?p=183152)
- Hiscox IT-Berufshaftpflicht: covers professional errors "etwa bei Projektverzug, der Verletzung von Rechten Dritter oder Fehlberatung"; programming errors and client data loss are named claims; many customers choose sums "zwischen 500.000 und 1.000.000 Euro"; example tariff €50.52/month for €1m cover (IT freelancer, €150k revenue); entry prices quoted from €10.10 or €15.21/month plus VAT — [Hiscox](https://www.hiscox.de/geschaeftskunden/it-haftpflichtversicherung)
- Bitkom updated its standard data-processing (Auftragsverarbeitung) model annex in 2025; accompanying guide v1.2 published Nov 2025 — [Bitkom Praxisleitfäden](https://www.bitkom.org/Themen/Praxisleitfaeden-zur-Auftragsverarbeitung)

### Inferences
- (Interpretation) Household 15-minute consumption data is personal data; for B2B pilots the startup should contract as processor (Bitkom AV template) and avoid becoming controller. Aggregated plant/portfolio data from utilities is usually not personal data, so the heavier obligations arise only in residential-flexibility use cases.
- (Interpretation) Liability for an "errant dispatch" is a contract matter: cap liability at fees, exclude consequential loss, and carry Vermögensschadenhaftpflicht of €1m; insurers' standard IT wording appears to cover financial loss from wrong recommendations, but whether automated dispatch of physical assets is covered must be confirmed with the insurer **[ADVISER/insurer]**.

### Gaps
- E-REDES / ERSE data-access rules (Portugal smart meter data, "dados de consumo", DSO data hub) not retrieved.
- BSI TR-03109 CLS/EMT role and certification for steering software: not retrieved.
- No insurer quote specific to energy-dispatch software; Hiscox figures are generic IT.
- Bitkom AI contract templates: none found on the publications page; Bitkom has AV templates only. Check bitkom.org → Publikationen → "Vertrag".

---

## A5. Cross-border selling (DE, PT, AT, NL, BE, ES, IT), VAT, and public-procurement thresholds

### Takeaway
B2B software/services can be sold across EU borders without local establishment; VAT is reverse-charged to the business customer. For public-sector/municipal-utility buyers, the EU thresholds from 1 Jan 2026 are €432,000 (sector entities) and €216,000 (other authorities) net; Portugal's reformed CCP (DL 177/2026, in force 1 Oct 2026) raises direct award for services to <€75,000 and consulta prévia to <€130,000, adds startup-reserved procedures, free IT trial periods and "spontaneous initiatives". German sub-threshold (UVgO/Bavarian) direct-award limits were not retrieved.

### Cited Findings
- EU B2B services: "you don't usually need to charge your customers VAT"; the customer accounts for VAT under the reverse charge at its own country's rate; supplier keeps input-VAT deduction — [Your Europe](https://europa.eu/youreurope/business/taxation/vat/cross-border-vat/index_en.htm)
- EU thresholds from 1 Jan 2026 (net, Regulations (EU) 2025/2150–2152 of 22 Oct 2025): supplies/services, sector entities €432,000 (was €443,000); outside sectors €216,000; top federal authorities €140,000; works and concessions €5,404,000; social/special services €750,000 (sector €1m) unchanged — [IHK Bodensee-Oberschwaben](https://www.ihk.de/bodensee-oberschwaben/recht/vertraege-schliessen/oeffentliche-ausschreibung-vergabe/neue-schwellenwerte-europaweite-ausschreibungen-5989678); valid until 31 Dec 2027 per [WKO](https://www.wko.at/wirtschaftsrecht/schwellenwerte-eu-weite-ausschreibungen)
- Portugal CCP reform: Decreto-Lei n.º 177/2026 of 4 Sept 2026, in force 1 Oct 2026, applies to procedures started after that date; services/goods: ajuste direto <€75,000 (was €20,000), consulta prévia <€130,000 (was €75,000); works: ajuste direto <€150,000, consulta prévia <€1m; new "consulta prévia especial" (≥5 invitees) for contracts below EU thresholds and <€2m; Art. 54.º-A(1)(d) allows reserving procedures for startups recognised under Lei 21/2023 for goods/services below EU thresholds "sem interesse transfronteiriço certo"; Art. 35.º-C allows free temporary provision of IT systems for technical evaluation before a procurement; Art. 35.º-B "iniciativa espontânea" (operator submits a technical study; entity has 90 days; no preference right, cost reimbursement if not awarded) — [PLMJ nota informativa Sept 2026](https://www.plmj.com/xms/files/03_Novidades_legislativas/2026/NI_CCP_2026.pdf); ajuste direto simplificado €5,000 goods/services, €10,000 works — [dnoticias 30 Sep 2026](https://www.dnoticias.pt/2026/9/30/507344-contratos-publicos-ate-dois-milhoes-com-convite-directo-a-cinco-empresas/)
- Austria (for AT sales): Vergaberechtsgesetz 2026 (BGBl I 8/2026), in force 1 Mar 2026; sector entities direct award supplies/services €150,000 net, with publication €200,000 — [WKO](https://www.wko.at/wirtschaftsrecht/highlights-vergaberechtsgesetz-2026)

### Inferences
- (Interpretation) Pilots of €5k–€30k with Stadtwerke are far below EU thresholds; the binding limit is the national/Land direct-award rule (not retrieved for Bavaria). In Portugal, a paid diagnostic ≤€5,000 fits ajuste direto simplificado and anything <€75,000 fits ajuste direto from 1 Oct 2026.
- (Interpretation) Invoices to EU business customers: no VAT, customer VAT-ID, "reverse charge" note, and an EC Sales List (Zusammenfassende Meldung) in Germany; for private persons or non-business buyers VAT applies — confirm filing duties **[ADVISER]**.
- (Interpretation) Freedom to provide services means no local company is needed in AT/NL/BE/ES/IT for B2B software; a permanent establishment can arise from local staff or a dependent agent (see C3).

### Gaps
- German/Bavarian sub-threshold direct-award limits (UVgO §14; Bavarian Wertgrenzen 2026) not retrieved. Check IHK München "Vergabe Wertgrenzen Bayern 2026".
- Whether many Stadtwerke are "Sektorenauftraggeber" for software purchases depends on their activity; not researched.

---

## B1. Germany/Bavaria funding (rules as of 2026)

### Takeaway
EXIST-Gründungsstipendium (Richtlinie 11 Apr 2023, applications until 31 Dec 2027) is the natural fit: €2,500/month per graduate (€3,000 PhD) for up to 3 people for 12 months, up to €30,000 material costs, requires a German university/research host with a Gründungsnetzwerk, degree not older than 5 years, and the company must *not* be founded before project start; nationality is not restricted. EXIST-Forschungstransfer requires a research-project origin and host employment (up to 4 FTE, €250k, 18 months; deadlines 31 Mar/31 Aug/30 Nov). FLÜGGE (Bavaria, €2,500/month, once-a-year call) requires the founders to belong to a Bavarian state university. INVEST runs to 31 Dec 2026 with no successor confirmed. Gründungszuschuss requires ≥150 days of remaining ALG I.

### Cited Findings
- EXIST-Gründungsstipendium (Förderdatenbank, Richtlinie dated 11 Apr 2023, valid to 31 Dec 2029, applications until 31 Dec 2027): applicants "Hochschulen und Forschungseinrichtungen in Deutschland"; host must have a Gründungsnetzwerk, mentor, free infrastructure; degree or last university employment "darf nicht länger als fünf Jahre zurückliegen"; company formation "ist zulässig, darf jedoch bei Projektbeginn noch nicht erfolgt sein"; max 3 persons; stipends €1,000 (students) / €2,000 (vocational) / €2,500 (graduates) / €3,000 (PhD) per month + €150 per child; material costs up to €10,000 (solo) / €30,000 (team); coaching €5,000; network consulting €10,000 (+€2,500 diverse team, +€2,500 mentor); up to 12 months (+3 months for childbirth); submission via easy-Online + paper to PtJ Berlin; project may start 3 months after complete application; diversity by "Herkunft oder Nationalität" earns a bonus — [Förderdatenbank](https://www.foerderdatenbank.de/FDB/Content/DE/Foerderprogramm/Bund/BMWi/exist-gruendungsstipendium.html); no other stipend and no job >5 h/week — [selbststaendig.de](https://www.selbststaendig.de/wissen/exist-gruenderstipendium); founders need not have studied at the network university — [deutsche-startups](https://www.deutsche-startups.de/lexikon/exist-grunderstipendium/)
- TUM route: project sketches monthly via TUM Gründungsberatung; idea paper ≥6 weeks before submission — [TUM Finanzierung](https://www.tum.de/innovation/entrepreneurship/fuer-gruenderinnen-start-ups/finanzierung)
- EXIST-Forschungstransfer Richtlinie (BAnz AT 18.04.2023 B2, valid to 31 Dec 2029, applications until 31 Dec 2027): Phase I applicants are German HEIs/research institutes that employ the team; team members need at least Diplom/Master (one may be Bachelor/vocational); work must originate from a research project with team participation, "Ausgangspunkt ist immer eine technische Basisinnovation", proof of principle shown; founding before project start not allowed ("dürfen jedoch bei Projektbeginn noch nicht erfolgt sein"); Phase I up to 18 months (36 with jury consent); Phase II: company must be a Kapitalgesellschaft with seat in Germany, ≥€25,000 share capital paid in, >50% owned by active founders, grant max €180,000, own funds 1:3, ≤18 months — [Bundesanzeiger Richtlinie (PDF)](https://www.bundesanzeiger.de/pub/publication/w7ttUSCiuBuormB6OJn/content/w7ttUSCiuBuormB6OJn/BAnz%20AT%2018.04.2023%20B2.pdf)
- EFT Handbook 2026 (PtJ, created 18 Aug 2026): "steht Gründerinnen und Gründern aller Nationalitäten offen"; collection dates 31 Mar, 31 Aug, 30 Nov; up to 4 FTE; up to €250,000 Sachmittel incl. €10,000 coaching; "Die Gründerinnen und Gründer sind bei der antragstellenden Hochschule angestellt"; "Alle Teammitglieder müssen bei der antragstellenden Hochschule angestellt sein"; host gets €20,000 incentive premium; timetable: deadline 31.03 → jury June → start 01.09; 31.08 → Nov → 01.03; 30.11 → March → 01.06; Phase II selection sessions roughly every two months — [EFT Handbuch 2026 (PDF)](https://exist.de/wp-content/uploads/2026/08/260818_Handbuch_EFT_barrierefrei.pdf)
- FLÜGGE (BayVV 7070-W-10427-0, text valid from 31 Dec 2025 to 31 Dec 2029): applicants are Bavarian state universities in a founder-support network; founders must belong to the applying university (staff ≤50%); stipend €2,500/month + €150 per child; university material costs up to 50% of stipends; up to 6 months (sustainable business models) or 12 months (technical hurdles / rejected EXIST); +6 months extension possible; company may be founded during but not before the project; separate validation projects up to €300,000/18 months — [gesetze-bayern.de](https://www.gesetze-bayern.de/Content/Document/BayVV_7070_W_10427-0); eligibility includes students, staff and graduates of a Bavarian state university, at least one founder must hold rights to the idea, stacking with other stipends "ausgeschlossen" — [OTH Regensburg](https://www.oth-regensburg.de/studieren/nach-dem-studium/existenzgruendung-start-up-center/gruendungsberatung/fluegge); applications once a year — [TUM](https://www.tum.de/innovation/entrepreneurship/fuer-gruenderinnen-start-ups/finanzierung); a grant portal lists the last window as closed 31 Dec 2025 (page updated 6 May 2026) — [grantbite](https://www.grantbite.com/de/funding/bayern-foerderung-forschung-existenzgruendung)
- INVEST (BAFA): Richtlinie extended to 31 Dec 2026; acquisition grant 25% (raised from 20%) incl. convertibles per IWW; min investment €10,000; grant only for first investment; federal portal still shows 20% — [IWW](https://www.iww.de/bbp/unternehmensberatung/foerdermittelberatung-invest--zuschuss-fuer-wagniskapital-bis-2026-verlaengert-und-erwerbszuschuss-auf-25-erhoeht-n151534); [verwaltung.bund.de](https://verwaltung.bund.de/leistungsverzeichnis/DE/leistung/99148136017000)
- Gründungszuschuss: §93 SGB III — remaining ALG entitlement "mindestens 150 Tage", Tragfähigkeit via "Stellungnahme einer fachkundigen Stelle" (IHK etc.), discretionary ("kann"); §94: ALG + €300/month for 6 months, then €300/month for up to 9 more months — [dejure §93](https://dejure.org/gesetze/SGB_III/93.html); [dejure §94](https://dejure.org/gesetze/SGB_III/94.html)
- HTGF: initial pre-seed/seed "sweet spot … €800,000+", lead investor, companies ≤3 years old, HQ in Germany (or German base) — [HTGF](https://www.htgf.de/en/)
- Bayern Kapital: "Mit Tickets von 250.000 Euro bis 50 Millionen Euro", pre-seed to scale-up, €1.3bn under management, Bavarian startups — [Bayern Kapital](https://www.bayernkapital.de/)
- BayStartUP: investor network placing >€50m/year early-stage; regional business-plan competitions (Munich, Northern Bavaria, Swabia); no fees/deadlines on homepage — [BayStartUP](https://www.baystartup.de/)
- UnternehmerTUM Accelerator (formerly XPRENEURS): Batch #20 3 Sep–10 Dec 2026; Batch #21 Mar–Jun 2027, applications Dec 2026–Jan 2027; deep-tech teams from across Europe; Batch #19: 18 startups, 12% acceptance; funding/equity terms not stated — [accelerator.unternehmertum.de](https://accelerator.unternehmertum.de/)
- TUM Venture Labs: labs incl. Climate/Circular and Software & AI; support "from idea generation to seed-capital"; open to students, researchers, professionals, existing teams; no amounts — [TUM Venture Labs](https://www.tum-venture-labs.de/)
- SET Award (dena Start Up Energy Transition): annual SET100 list + 5 category awards; no 2027 deadline on homepage — [SET](https://www.startup-energy-transition.com/)

### Inferences
- (Interpretation) The Munich founder's EXIST eligibility hinges on (a) a degree/university employment ≤5 years old and (b) a host (TUM, LMU, HM/SCE) willing to sign; the Portuguese co-founder can be a team member (no nationality restriction) but the host must provide a workplace and the stipend contract is with the host — residence abroad is not addressed in the Richtlinie and should be asked of PtJ/host before applying **[host/PtJ]**.
- (Interpretation) Because EXIST and FLÜGGE both prohibit founding before project start, incorporating in late 2026 would disqualify the team from both; sequence: apply first, found during the grant.
- (Interpretation) EXIST-Forschungstransfer is unrealistic unless the technical founder's work stems from a university research project and both founders can be employed by the German host.
- (Interpretation) INVEST's 2027 status is unknown; angels in a 2027 round should not assume the 25% grant.

### Gaps
- BayTOU, LMU IEC, SCE (HM), EnBW/E.ON/Vattenfall/EWE/Thüga/Bayernwerk/SWM startup programmes: pages not reachable or not searched after budget exhaustion. Check: bayern-innovativ.de (BayTOU), lmu.de/iec, sce.de, eon.com/innovation, enbw.com/innovation, thuega.de.
- FLÜGGE 2026/2027 call window not confirmed.
- INVEST post-2026 continuation not found; check bafa.de → INVEST.
- Whether EXIST hosts accept a co-founder living abroad: no source.

---

## B2. Portugal funding (rules as of 2026)

### Takeaway
Portugal's public early-stage instruments found are narrow for this team: StartUP Voucher 4th edition (€900/month, age ≤29, North/Centro/Alentejo, not employed; closed 30 Jan 2026) and Portugal Ventures (€50k–€1.5m tickets, Portuguese registered office, via Ignition Partners; no 2026 pre-seed call found). The startup law (Lei 21/2023) gives a 14% effective stock-option tax but excludes ≥20% holders/board members unless the issuer is a certified startup/micro/small company. Company formation via Empresa na Hora costs €360. IAPMEI's Vale Incubação and Startup Visa pages could not be fetched.

### Cited Findings
- StartUP Voucher Innovate (4th edition): graduates ≤29 (down from 35), resident in Norte/Centro/Alentejo, not studying/working/with other income, Portuguese nationality or residence, tax/social-security regularised; €900/month, max 2 grants per project; €1,500 at start of phases 2 and 3; €2,000 completion prize; 9 months in 3 phases; IAPMEI selects; funded by Compete 2030/FSE+; applications closed 30 Jan 2026 (extended from 3 Jan) — [ECO 23 Jan 2026](https://eco.sapo.pt/2026/01/23/candidaturas-ao-startup-voucher-terminam-a-30-de-janeiro/); €5m budget — [Governo](https://portugal.gov.pt/gc25/comunicacao/comunicados/pt2030-5-m-do-startup-voucher-para-jovens-criarem-emprego-proprio-em-areas-de-base-tecnologica)
- Portugal Ventures: tickets "between 50k€ and 1.5M€", pre-seed/seed/Series A, startups "with registered offices in Portugal", sectors Digital & Technology etc.; applications via Ignition Partners Network — [Portugal Ventures strategy](https://www.portugalventures.pt/en/about-us/investment-strategy-2/); Call INNOV-ID 2025 €150,000 per project, axes incl. decarbonisation/energy efficiency, closed 2 Mar 2025 — [ANI](https://ani.pt/en/portugal-ventures-launches-5th-edition-of-call-innov-id-to-support-startups/); Call FIT (tourism) closed 19 Jan 2026 — [Portugal Ventures](https://www.portugalventures.pt/en/news/portugal-ventures-launches-new-edition-of-call-fit-to-support-pre-seed-tourism-projects/)
- Startup law stock options (Lei 21/2023 of 25 May, EBF Art. 43-C): taxation deferred to liquidity; 50% of gain taxed at 28% → effective 14%; excludes holders of ≥20% capital/votes or governing-body members "except where the granting entity qualifies as a start-up or as a micro or small company"; one-year holding; exit tax on loss of residency criticised — [VdA, ITR Feb 2026 (PDF)](https://www.vda.pt/xms/files/05_Publicacoes/2026/ITR-Local_insight_VdA-February_2026.pdf); same mechanics — [Startup Portugal Legal Bites (30 Jul 2025)](https://startupportugal.com/?p=5927)
- Empresa na Hora: €360 (standard); €200 if a trademark in one class is included, +€44 per extra class; deed + commercial registration + social-security number issued; capital to be deposited within 5 working days; all partners must attend a desk; ID + NIF required — [registo.justica.gov.pt](https://registo.justica.gov.pt/Empresas/Empresa-na-Hora); a vendor claims minimum capital €1 per partner — [Zunapro (vendor, unverified)](https://www.zunapro.com/portugal/pt/blog/criar-lda-portugal-guia-completo)
- IRC 2026: standard 19%; 15% on first €50,000 for SMEs/small mid-caps; derrama municipal up to 1.5%; state surtax from €1.5m profit (reviewed 24 Jul 2026) — [PwC Portugal](https://taxsummaries.pwc.com/portugal/corporate/taxes-on-corporate-income)
- Portuguese social security: employer 23.75% / employee 11%; managers/administrators same; self-employed 21.4% (plus 10%/7% from economically dependent client) (reviewed 3 Oct 2026) — [PwC Portugal](https://taxsummaries.pwc.com/portugal/individual/other-taxes)
- Startup-reserved public procurement and free IT trial periods under the 2026 CCP (see A5) — [PLMJ](https://www.plmj.com/xms/files/03_Novidades_legislativas/2026/NI_CCP_2026.pdf)
- Web Summit Lisbon 9–12 Nov 2026 — [Web Summit](https://websummit.com/)
- Free Electrons: the programme domain freeelectrons.co now redirects to an unrelated site (madnest.in), so the programme's 2026 status is unclear — [redirect observed](https://www.freeelectrons.co/)

### Inferences
- (Interpretation) StartUP Voucher is only usable if the Portuguese co-founder is ≤29, lives in Norte/Centro/Alentejo (not Lisbon) and has no job; the next edition (if any) would be late 2026/early 2027 — check iapmei.pt.
- (Interpretation) A Portuguese Lda is needed for Portugal Ventures and for startup certification; a German UG/GmbH would not qualify for these, while a Portuguese entity would not qualify for EXIST Phase II / HTGF (German HQ required). See C3.

### Gaps
- IAPMEI Vale Incubação, Startup Visa (relevant only to non-EU founders), ANI, Portugal 2030 and PRR energy/digital calls: pages rate-limited/404; check iapmei.pt, ani.pt, portugal2030.pt, recuperarportugal.gov.pt.
- Startup certification criteria (age ≤10 years, <250 staff, turnover ≤€50m, etc.) not retrieved from a primary source; check Lei 21/2023 Art. 2 on diariodarepublica.pt.
- EDP Starter (403), Galp and REN programmes, Startup Lisboa, UPTEC, IPN: not retrieved.
- No 2026 Portugal Ventures pre-seed call found.

---

## B3. EU funding (EIC, Eurostars, Horizon Europe Cluster 5, LIFE CET, EIT InnoEnergy)

### Takeaway
All remaining 2026 EU deadlines relevant to a startup are: EIC Accelerator 4 Nov 2026 and EIC Pathfinder Challenges 28 Oct 2026; Eurostars Call 11 (10 Sep 2026) and LIFE CET 2026 (16 Sep 2026) have passed; the next Eurostars window is expected spring 2027 (unconfirmed). German Eurostars terms: up to €500k per participant, SMEs fund 50%. These instruments require either a research-grade proposal (EIC/Horizon) or a cross-border consortium (Eurostars), and none pays out in less than ~6–9 months from deadline.

### Cited Findings
- EIC 2026 Work Programme: Accelerator budget €634m, grants up to €2.5m + investments €0.5–10m; cut-offs 7 Jan, 4 Mar, 6 May, 8 Jul, 2 Sep, 4 Nov 2026; full proposal template cut from ~50 to 20 pages; evaluations every 2 months; Pathfinder Open 12 May 2026, Challenges 28 Oct 2026 (grants up to €4m); Transition 16 Sep 2026 (up to €2.5m); STEP Scale-Up €10–30m with cut-offs 11 Feb, 6 May, 9 Sep, 25 Nov 2026; Advanced Innovation Challenges pilot stage 2 closes 18 Jun 2027 — [Hezelburcht](https://www.hezelburcht.com/en/news/eic-launches-2026-work-programme-an-overview-of-the-eic-instruments-for-2026/); one secondary source gives the last cut-off as 4 Oct 2026 (likely error) — [eufordigital](https://eufordigital.eu/horizon-europe-eu-simplifies-application-process-for-eic-accelerator/)
- Eurostars: Call 11 open 9 Jul 2026, deadline 10 Sep 2026 14:00 CET; consortium led by innovative SME; no participant/country >70% of budget; rates set nationally — [EUREKA](https://www.eurekanetwork.org/?p=1673); March 2026 call closed 19 Mar 2026; German participants via DLR-PT up to €500k, max 3 years, SMEs cover 50% of costs, German universities 100% + flat rate when a German SME participates; two cut-offs per year (spring/autumn) — [TU Dresden EPC](https://tu-dresden.de/forschung-transfer/services-fuer-forschende/european-project-center/news/eurostars-startet-mit-erstem-call-in-2026)
- Horizon Europe Cluster 5 2026–27 WP: e.g. HORIZON-CL5-2026-02-D4-02 "Smarter buildings as part of the energy system for increased efficiency and flexibility – Societal Readiness Pilot" (IA, lump sum) deadline 17 Feb 2026; calls open Dec 2025–Aug 2027 with closings Mar 2026–Dec 2027; later 2027 battery storage topics (HORIZON-CL5-2027-05-D2-08, Sept 2027) — [IUK Business Connect](https://iuk-business-connect.org.uk/opportunities/horizon-europe-2026-27-climate-energy-and-mobility-cluster-5/); draft WP >47 topics — [accelopment](https://accelopment.com/blog/funding/draft-horizon-europe-cluster-5-2026-27/)
- LIFE Clean Energy Transition 2026: €85.5m, 13 topics, up to 95% funding, deadline 16 Sep 2026 (FFG/EY/Confindustria) vs 22 Sep 2026 (CoR) — [FFG](https://www.ffg.at/en/europa/life-call2026-CET); [EY](https://www.ey.com/en_be/technical/tax/tax-alerts/2026/life-2026-calls-open-601-million-for-climate-and-environment); results expected Feb–Apr 2027
- EIT InnoEnergy: invests in clean-tech teams with at least proof of concept/prototype, mainly Europe; rolling online application; 1,400+ partners; no ticket sizes published — [InnoEnergy](https://www.innoenergy.com/for-innovators/); older IEA record: Highway programme, apply any time, dilutive equity (page updated Jun 2025) — [IEA](https://www.iea.org/policies/15240-eit-innoenergy-highway); directory lists €200k–$500k — [incubatorlist](https://incubatorlist.com/kic-innoenergy)

### Inferences
- (Interpretation) For a late-2026 start, the realistic EU path is a Eurostars spring-2027 proposal with a German SME lead and a Portuguese partner (university or utility), cash no earlier than late 2027; EIC Accelerator is a 2028 ambition after traction.
- (Interpretation) Reporting burden rises in order EXIST < Eurostars < LIFE/Horizon consortia; co-funding of 50% (Eurostars SME) must be financed from revenue or equity.

### Gaps
- EIC 2027 Work Programme and cut-offs not yet found.
- Portuguese Eurostars funding rate/ceiling (ANI as national body) not found.
- Interreg (SUDOE/Atlantic, Bavaria-Austria) not researched.
- Horizon 2027 flexibility/demand-response topics not confirmed.

---

## B4. Angels, pre-seed and seed in DACH and Iberia (2025–2026 evidence)

### Takeaway
Comparable German energy-flexibility software companies raised €0.5m (neXtract, Sep 2025), €2.2m (Einklang, Feb 2026, Vireo-led) and €6.3m seed (encentive, Sep 2025, General Catalyst-led with named industrial customers); specialist pre-seed/seed funds publish initial tickets of €1–2m (Vireo) and up to €2.5m (Faber, Southern Europe); HTGF's sweet spot is €800k+. Seed rounds in this niche show deployed customers (logistics/industrial sites) rather than consulting revenue.

### Cited Findings
- encentive (founded 2020; flexOn industrial energy control centre): €6.3m seed announced 15 Sep 2025, led by General Catalyst with Summiteer, SIVentures, Vireo Ventures, HelloWorld and angels; total raised €9m; technology in use at Metro Logistics, Dachser, Klingele — [Vestbee](https://vestbee.com/insights/articles/encentive-raises-6-3-m)
- Einklang (Cologne, Energy-as-a-Service: battery + dynamic tariffs + control for SMEs): €2.2m, article dated 26 Feb 2026, led by Vireo Ventures with SI Ventures, Saxovent, Angel Invest, Heimatboost, DnA Ventures; target 100 customer sites by 2026 — [parsers.vc](https://parsers.vc/news/260226-einklang-secures-2-2m-to-revolutionize-sme/)
- neXtract energy (Berlin): €500k, Sep 2025, software for IPPs to run optimised storage schedules — [tech.eu funding](https://funding.tech.eu/companies/9338D37F-BEAD-45FA-8E81-5DA1FF98F1BC)
- Podero (Vienna): round led by Planet A Ventures; CB Insights lists €5.5m seed — [CB Insights](https://www.cbinsights.com/company/podero)
- node.energy: €15m Series B, Apr 2025 — [Seedtable](https://seedtable.com/companies/nodeenergy/funding-rounds/series-b-2025-04)
- Vireo Ventures: pre-seed and seed, initial ticket €1–2m, themes "Electrification & Sovereignty", "AI × Energy"; Invertix (AI for renewables portfolios) €1.7m, 19 May 2026 — [Vireo](https://vireo.vc/)
- Faber (Lisbon): pre-seed/seed, first ticket up to €2.5m, Southern Europe, deep tech incl. Climate & Ocean Tech — [Faber](https://www.faber.vc/)
- HTGF: €800k+ initial, ≤3 years old, German HQ — [HTGF](https://www.htgf.de/en/)
- Bayern Kapital €250k–€50m — [Bayern Kapital](https://www.bayernkapital.de/)
- World Fund: climate-tech VC; energy-related portfolio (ENERKII, hyperscale power, Anaphite, CYLIB); no ticket sizes published — [World Fund](https://worldfund.vc/)
- INVEST angel grant 25% until 31 Dec 2026 — see B1

### Inferences
- (Interpretation) A model-as-a-service company with 2–3 paid pilots and one recurring contract is the typical bar for a €0.5–2m pre-seed in this niche; a consulting-first business (paid diagnostics) is not venture-backable on its own but is the cheapest way to earn the traction those funds cite.
- (Interpretation) None of the cited funds requires a German HQ except HTGF and Bayern Kapital (Bavaria); Faber/Portugal Ventures require Southern Europe/Portugal; this constrains entity choice (C3).

### Gaps
- Extantia, Planet A, Speedinvest Climate, 2150, Picus, UVC Partners, Übermorgen, Indico, Shilling, Seaya Andromeda, Kibo, Suma Capital: ticket sizes not retrieved (search budget exhausted). Check each fund's site.
- No systematic 2025–2026 round list; Dealroom/tech.eu query recommended.

---

## B5. Three financing scenarios: cost inputs and burn (Munich vs Lisbon/Porto)

### Takeaway
Cited inputs: single-person living cost excl. rent €1,075/month in Munich, €760 Lisbon, €719 Porto; 1-bed rents €1,124–1,500 Munich, €1,063–1,425 Lisbon, €852–1,153 Porto (Numbeo, Oct 2026); Empresa na Hora €360; IT liability insurance ≈€50/month for €1m cover; Portuguese employer social charges 23.75%; German combined corporate tax ≈33% in Munich vs 19%/15% IRC in Portugal. Scenario burn figures below are my arithmetic on those inputs plus unsourced placeholders (flagged).

### Cited Findings
- Munich: €1,074.6/month single excl. rent; 1-bed €1,500.24 centre / €1,123.76 outside (updated 8 Oct 2026) — [Numbeo Munich](https://www.numbeo.com/cost-of-living/in/Munich)
- Lisbon: €760.4/month excl. rent; 1-bed €1,425.00 / €1,062.73 (updated 11 Oct 2026) — [Numbeo Lisbon](https://www.numbeo.com/cost-of-living/in/Lisbon)
- Porto: €719.0/month excl. rent; 1-bed €1,153.33 / €851.79 (updated 6 Oct 2026) — [Numbeo Porto](https://www.numbeo.com/cost-of-living/in/Porto)
- Lda via Empresa na Hora €360 — [registo.justica.gov.pt](https://registo.justica.gov.pt/Empresas/Empresa-na-Hora)
- IT-Berufshaftpflicht example €50.52/month for €1m (no deductible) — [Hiscox](https://www.hiscox.de/geschaeftskunden/it-haftpflichtversicherung)
- Germany: KSt 15% + Soli = 15.825%; Gewerbesteuer 3.5% × Hebesatz; Munich overall ≈33%; KSt falls to 14% in 2028 and 1 pt/year to 10% from 2032 (reviewed 30 Jun 2026) — [PwC Germany](https://taxsummaries.pwc.com/germany/corporate/taxes-on-corporate-income)
- Portugal IRC 19% / 15% on first €50k; social security 23.75%+11% — [PwC PT corporate](https://taxsummaries.pwc.com/portugal/corporate/taxes-on-corporate-income); [PwC PT other taxes](https://taxsummaries.pwc.com/portugal/individual/other-taxes)
- EXIST stipend €2,500/month per graduate, €30k team material costs — [Förderdatenbank](https://www.foerderdatenbank.de/FDB/Content/DE/Foerderprogramm/Bund/BMWi/exist-gruendungsstipendium.html)

### Inferences (arithmetic on cited inputs; items marked * are unsourced placeholders to be replaced with quotes)
- Founder subsistence (rent outside centre + living): Munich ≈ €2,200/month; Lisbon ≈ €1,820; Porto ≈ €1,570 (Numbeo). Over 12 months, two founders split Munich/Lisbon ≈ €48k.
- Scenario 1 — solo/two-founder research, no entity (pre-EXIST or on EXIST): burn ≈ founder subsistence (€2.2k + €1.8k) + cloud/data/tools *€300–800* + insurance €50 ≈ **€4.4–5.0k/month**; EXIST at 2 × €2,500 + €30k material covers ~100% of this for 12 months; without EXIST, €30k savings ≈ 6–7 months.
- Scenario 2 — 2–3 person team with paid pilots, UG/GmbH or Lda: add accountant *€150–400/month*, formation (Lda €360; UG notary/register *€300–1,000*; GmbH €25k capital of which €12.5k paid in), one developer/working student *€2–4k/month gross* (+23.75% in PT), compute/data *€500–1,500*, travel to E-world/conferences *€500*: ≈ **€9–14k/month**, i.e. €110–170k/year; covered by 2–3 pilots of €15–30k plus EXIST or a €300–500k pre-seed.
- Scenario 3 — hardware-involved demo (battery/EMS testbed, CLS/SMGW control): add hardware *€10–40k one-off*, lab/space *€500–1,500/month*, certification/BSI-related consulting *€10–30k*: **€15–25k/month plus €30–70k one-off**; realistically requires a Eurostars/FLÜGGE validation grant (FLÜGGE validation projects up to €300k) or a partner's test site.
- VAT: founder subsistence is private (no VAT); business costs net of VAT for a VAT-registered entity; B2B EU sales reverse-charged (A5).

### Gaps
- No sourced quotes for UG/GmbH notary and register fees, German accountant fees, compute costs or developer salaries (firma.de/gründerplattform pages returned 404/403). Check notar.de GNotKG calculator, IHK München UG guide, and a Steuerberater quote.
- Minimum Lda share capital not stated on the official page.

---

## C1. How utilities, Stadtwerke, direct marketers and Iberian retailers buy from startups; contract forms; IP/data norms

### Takeaway
Primary evidence on procurement mechanics is strongest for Portugal (new CCP: free IT trial periods before procurement, startup-reserved procedures, spontaneous initiatives, direct award <€75k) and for the EU public sector (MCC-AI model clauses, which deliberately exclude IP and liability terms). Comparable German startups reached seed stage with named industrial/logistics customers rather than utilities. Specific PoC budgets, sales-cycle lengths, €/MW pricing and Stadtwerke examples were not found in retrievable sources and remain gaps.

### Cited Findings
- Portugal CCP 2026: Art. 35.º-C lets contracting entities accept "disponibilização gratuita e temporária" of IT systems for technical/functional/interoperability/security evaluation before a procurement; Art. 35.º-B spontaneous initiatives (technical study, 90-day review, cost reimbursement if not awarded); Art. 54.º-A(1)(d) startup-reserved procedures; direct award services <€75,000, consulta prévia <€130,000 from 1 Oct 2026 — [PLMJ](https://www.plmj.com/xms/files/03_Novidades_legislativas/2026/NI_CCP_2026.pdf)
- EU Model Contractual AI Clauses (MCC-AI, published 29 Sep 2023, updated version of April 2023 clauses): voluntary, for public buyers; high-risk and non-high-risk versions; they "do not contain any conditions concerning intellectual property" and exclude liability, payment, acceptance and applicable law — [EU Public Buyers Community](https://public-buyers-community.ec.europa.eu/communities/procurement-ai/resources/eu-model-contractual-ai-clauses-pilot-procurements-ai)
- Bitkom: updated Auftragsverarbeitung model annex (2025; guide v1.2 Nov 2025); no AI/software contract template found on the publications page — [Bitkom](https://www.bitkom.org/Themen/Praxisleitfaeden-zur-Auftragsverarbeitung); [Bitkom Publikationen](https://www.bitkom.org/Bitkom/Publikationen)
- Comparable traction at seed: encentive's flexOn used at Metro Logistics, Dachser, Klingele before its €6.3m seed (Sep 2025) — [Vestbee](https://vestbee.com/insights/articles/encentive-raises-6-3-m); Einklang sells Energy-as-a-Service with "No upfront investment" for SMEs — [parsers.vc](https://parsers.vc/news/260226-einklang-secures-2-2m-to-revolutionize-sme/)
- REMIT Art. 5a documentation expectations on the client side (model logic, parameters, testing, kill switch, vendor questionnaire) — [Nord Pool](https://nordpoolgroup.com/48cc74/globalassets/download-center/market-surveillance/market-surveillance-newsletter---december-2024.pdf)
- German procurement: sector threshold €432,000 net from 1 Jan 2026 — [IHK](https://www.ihk.de/bodensee-oberschwaben/recht/vertraege-schliessen/oeffentliche-ausschreibung-vergabe/neue-schwellenwerte-europaweite-ausschreibungen-5989678)

### Inferences
- (Interpretation) First-contract ladder that fits the cited rules: (1) free or €5k "technical evaluation" (PT Art. 35.º-C / DE Direktauftrag) → (2) paid diagnostic €10–30k under direct award → (3) 6–12-month pilot → (4) SaaS or €/MW/year; keep each contract below the national direct-award limit and avoid splitting one need into several contracts (PLMJ warns the higher thresholds make aggregation/fractionation rules stricter).
- (Interpretation) Because REMIT puts algorithm responsibility on the client, utilities will insist on documentation, audit rights and a kill switch; offering these proactively is a sales asset.
- (Interpretation) IP: EU model clauses leave IP to the parties, so the startup should set its own default (vendor owns model/IP; client owns its data; client gets a licence to outputs; no exclusivity or time-boxed exclusivity) — contract templates must be drafted with a lawyer **[ADVISER]**; Werkvertrag (defined deliverable, acceptance, warranty) vs Dienstvertrag (effort-based) choice affects liability for forecast accuracy and should be decided per contract **[ADVISER]**.

### Gaps
- No retrievable evidence on Stadtwerke/direct-marketer PoC budgets, innovation-department processes, sales-cycle lengths, or €/MW/year pricing norms (search budget exhausted; Thüga/E.ON/EnBW pages 404/403). Sources to check: Thüga "Innovationsplattform", E.ON "Innovation", EnBW New Ventures, BDEW/VKU startup initiatives, press releases of Podero/encentive/Einklang for contract forms.
- Bitkom AI contract templates: not found; Bitkom "Vertragsgestaltung" search needed.

---

## C2. Channels beyond cold outreach (associations, fairs, research networks, open source, advisors)

### Takeaway
Dated channel facts found: E-world 2027, Essen, 16–18 Feb 2027 (2026 edition >1,100 exhibitors, 90% of 2027 space booked by Oct 2026); The smarter E Europe / ees / EM-Power 2027, Munich, 8–10 Jun 2027 (conference 7–8 Jun) with a start-up stage; Web Summit Lisbon 9–12 Nov 2026; OpenEMS Association (~70 members incl. FENECON, Consolinno, Fraunhofer ISE; annual conference 27 Oct 2026); dena SET Award (SET100); UnternehmerTUM Accelerator batch #21 applications Dec 2026–Jan 2027; BayStartUP investor network. Portuguese associations (APREN, APE, ENERGYIN) and Handelsblatt Energy Summit were not retrievable.

### Cited Findings
- E-world energy & water 2027: 16–18 Feb 2027, Essen; 2026 edition had >1,100 exhibitors in six halls; 90% of 2027 space booked (news 6 Oct 2026) — [E-world](https://www.e-world-essen.com/en/)
- The smarter E Europe 2027: exhibitions 8–10 Jun 2027 Messe München, conferences 7–8 Jun 2027 ICM; Start-up Stage and exhibitor start-up offer listed — [The smarter E](https://www.thesmartere.de/home)
- Web Summit Lisbon 9–12 Nov 2026 — [Web Summit](https://websummit.com/)
- OpenEMS: open-source EMS platform; OpenEMS Association e.V. with ~70 members; chairs from FENECON and Consolinno; Fraunhofer ISE co-develops EEBus reference implementation; hackathon 6–8 Oct 2026 (France); members' meeting 26 Oct 2026, conference 27 Oct 2026; promoted as basis for an open-source HEMS for small/mid-sized utilities — [OpenEMS](https://openems.io/)
- SET Award (dena): annual SET100 + five category awards, 4,500+ applications over 10 years — [SET](https://www.startup-energy-transition.com/)
- UnternehmerTUM Accelerator: "300+ partners" incl. corporates/family offices; Batch #21 application Dec 2026–Jan 2027 — [accelerator.unternehmertum.de](https://accelerator.unternehmertum.de/)
- BayStartUP: investor network >€50m/year, Startup Demo Nights (Nürnberg 21 Oct 2026) — [BayStartUP](https://www.baystartup.de/)
- TUM Venture Labs Climate/Circular events (e.g. "Moonshot Insights: Deep-Tech Climate Ventures", 20 Oct 2026) — [TUM Venture Labs](https://www.tum-venture-labs.de/)
- Portuguese startup-reserved procurement and spontaneous initiatives as an inbound route to public utilities — [PLMJ](https://www.plmj.com/xms/files/03_Novidades_legislativas/2026/NI_CCP_2026.pdf)

### Inferences
- (Interpretation) For a late-2026 start, the time-ordered channel plan is: OpenEMS conference (27 Oct 2026, Germany) → Web Summit (Nov 2026, Lisbon) → UnternehmerTUM batch #21 application (Dec–Jan) → E-world (Feb 2027) → The smarter E (Jun 2027); publishing open analyses (e.g. OpenEMS contributions, public backtests on ENTSO-E/OMIE data) is the low-cost inbound lever given no network.
- (Interpretation) A sector advisor (ex-Stadtwerke/direct-marketer trading head) is the substitute for a missing network; typical compensation (advisor equity 0.25–1%) is unsourced.

### Gaps
- BDEW, VKU, bne, dena networks, Handelsblatt Energy Summit (403), FfE/TUM research networks, Bayern Innovativ energy cluster, APREN, APE, ENERGYIN, Portugal energy summits: not retrieved.

---

## C3. Company setup: German UG/GmbH vs Portuguese Lda vs dual structure; paying a co-founder in the other country

### Takeaway
Legal facts found: EXIST Phase II/HTGF/Bayern Kapital require a German-seated company (Phase II: Kapitalgesellschaft, ≥€25k capital, >50% founder-owned); Portugal Ventures and the startup-law benefits require a Portuguese-registered company; a managing director working from a fixed place abroad can create a management permanent establishment (§12 AO); under EU Regulation 883/2004 an employee resident in Portugal doing ≥25% of work there is insured in Portugal, which obliges the German employer to register and pay Portuguese contributions (23.75%); A1 certificates cover only temporary postings. All of this needs a cross-border tax/social-security adviser **[ADVISER]**.

### Cited Findings
- EXIST-Forschungstransfer Phase II: company must be a Kapitalgesellschaft "mit Unternehmenssitz in Deutschland", €25,000 capital paid in, >50% owned by active founders, at least one Phase I founder in management — [Bundesanzeiger Richtlinie](https://www.bundesanzeiger.de/pub/publication/w7ttUSCiuBuormB6OJn/content/w7ttUSCiuBuormB6OJn/BAnz%20AT%2018.04.2023%20B2.pdf); EXIST-Gründungsstipendium: founding before project start not allowed — [Förderdatenbank](https://www.foerderdatenbank.de/FDB/Content/DE/Foerderprogramm/Bund/BMWi/exist-gruendungsstipendium.html)
- HTGF requires German HQ or base; ≤3 years old — [HTGF](https://www.htgf.de/en/)
- Portugal Ventures requires registered office in Portugal — [Portugal Ventures](https://www.portugalventures.pt/en/about-us/investment-strategy-2/)
- Portuguese stock-option regime excludes ≥20% holders/board members unless issuer is a certified startup or micro/small company; exit tax on leaving residency — [VdA](https://www.vda.pt/xms/files/05_Publicacoes/2026/ITR-Local_insight_VdA-February_2026.pdf)
- Social security coordination (German tax-adviser blog): place-of-work principle; posting keeps home system "bis zu 24 Monate"; multi-state work: residence-state system applies if >25% of work is done there; A1 needed; DVKA can grant Art. 16(1) exceptions; home office abroad may trigger host-country employment law; employee home office generally no PE, but a managing director working from a fixed place abroad "may create a management permanent establishment under § 12 sentence 2 no. 1 AO"; dependent agents concluding business abroad can create a PE; 183-day rule does not apply to managing directors (salary split) — [steuerberaten.de](https://www.steuerberaten.de/blog/554/mitarbeiter-im-ausland-beschaeftigen-steuerliche-und-sozialversicherungsaspekte/)
- Foreign employer of a Portugal-resident employee: duties include registering as employer in Portugal, local payroll, Portuguese social contributions, local labour law, PE risk; EOR offered as alternative — [Parakar](https://parakar.eu/de/knowledge/portugal-de/in-portugal-fuer-ihren-niederlaendischen-arbeitgeber-arbeiten-ein-traum-der-tatsaechlich-wirklichkeit-werden-kann)
- Portuguese contribution rates: employer 23.75% / employee 11%; managers same; self-employed 21.4% (+10% employer charge if ≥80% of income from one client) — [PwC PT](https://taxsummaries.pwc.com/portugal/individual/other-taxes)
- Empresa na Hora €360, all partners present, NIF required — [registo.justica.gov.pt](https://registo.justica.gov.pt/Empresas/Empresa-na-Hora)
- Corporate tax: Germany ≈33% (Munich); Portugal 19% (15% first €50k) — [PwC DE](https://taxsummaries.pwc.com/germany/corporate/taxes-on-corporate-income); [PwC PT](https://taxsummaries.pwc.com/portugal/corporate/taxes-on-corporate-income)

### Inferences
- (Interpretation) Option A — German UG/GmbH, PT co-founder as remote employee: cleanest for EXIST/HTGF/Bayern Kapital; but the GmbH must register as employer in Portugal and pay 23.75% on top of salary; if the PT co-founder is a Geschäftsführer working from Portugal, a management PE in Portugal is a real risk — mitigate by making only the Munich founder Geschäftsführer or by appointing the PT founder as Prokurist/employee **[ADVISER]**.
- (Interpretation) Option B — PT co-founder as self-employed contractor (recibos verdes) invoicing the GmbH: avoids employer registration but the 21.4% + possible 10% "economic dependence" charge and the risk of false self-employment make it a stop-gap only **[ADVISER]**.
- (Interpretation) Option C — Portuguese Lda as the company: cheap (€360), 19%/15% IRC, startup-law stock options, Portugal Ventures/Faber eligibility, startup-reserved procurement; but it forfeits EXIST Phase II, HTGF, Bayern Kapital and may complicate selling to German Stadtwerke that prefer German contracting entities; the Munich founder would then be the cross-border worker.
- (Interpretation) Option D — dual structure (German GmbH + Portuguese Lda subsidiary or vice versa) solves eligibility on both sides but doubles accounting/compliance; worth it only after a first round.
- (Interpretation) Sequencing that respects the grant rules: no incorporation until EXIST/FLÜGGE decision; found the GmbH/UG during the grant in Germany if the Munich host route works; set up the Portuguese payroll registration (or EOR) at that point.

### Gaps
- No source on EXIST's treatment of a team member resident abroad (ask PtJ/host).
- No sourced EOR pricing or Portuguese employer-registration procedure (Segurança Social "entidade empregadora sem sede em Portugal").
- Germany–Portugal double-tax treaty specifics for director salaries not researched **[ADVISER]**.
- UG/GmbH formation fees (notary, register) not sourced; see B5.
