---
type: note
status: complete
tags: [entso-e, smard, energy-charts, netztransparenz, rebap, aep-schaetzer, omie, esios, ren-datahub, e-redes, elia, tennet, apg, open-meteo, dwd, ecmwf, era5, mastr, wpuq, htw-berlin, paragraph-14a-modul-3, dynamic-tariff, battery-arbitrage, imbalance-cost, price-forecasting, perfect-foresight, mpc, experiment-design, data-licensing, germany, portugal, spain, mibel]
relatedTo: [european-energy-flexibility-startup-wedges]
---

# Public data, licences and quantitative evidence for backtesting European electricity-flexibility and forecasting models (DE, PT/ES, then NL/BE/AT)

Research date: 11 October 2026. Method note: ~45 primary pages/PDFs were fetched directly; the web-search budget was exhausted after the first round, so several portals (ENTSO-E terms page, EPEX fee pages, OMIE legal notice, REE/ESIOS PVPC page, ElaadNL, Pexapark) could not be retrieved (403/404/503) and are listed explicitly as gaps rather than filled from memory. Where a figure is my own estimate or design choice it is labelled "[estimate]" or "[design]".

## Key Question 1: Price, imbalance and balancing data — exact sources, granularity, lag, licence (Germany, MIBEL, NL/BE/AT)

### Takeaway
Germany is the best-served market: SMARD (CC BY 4.0, explicit attribution string), Energy-Charts (CC BY 4.0 with a documented exception that DE-LU and most day-ahead price zones are "private and internal use" unless sourced from SMARD), and netztransparenz.de (reBAP published by the 20th working day of the following month; a real-time AEP-Schätzer 30 min after each quarter-hour; ID-AEP at D+1) cover everything the three experiments need. Iberia is accessible (OMIE files, ESIOS token API, E-REDES CC BY 4.0) but licence text for OMIE/ESIOS/REN could not be retrieved and must be confirmed before commercial use; REN's Data Hub API exposes only daily/monthly electricity aggregates and no imbalance (desvios) or reserve prices.

### Cited Findings

**Market structure change relevant to all backtests**
- The 15-minute market time unit went live in Single Day-Ahead Coupling on trading day 30 September 2025 for delivery day 1 October 2025 "in all European bidding zones and across bidding zone borders" (APG, 1 Oct 2025) — [APG](https://markt.apg.at/en/news-press/sdac-go-live-of-15-minute-market-time-unit-in-day-ahead-market-coupling-successful-as-of-september-30-2025/); the Market Coupling Steering Committee confirmed readiness on 12 Sep 2025 after a >1-year test campaign — [OTE](https://www.ote-cr.cz/en/about-ote/ote-news/market-coupling-steering-committee-confirms-go-live-of-15-minute-mtu-in-sdac-on-trading-day-30-september-2025-for-delivery-day-1-october-2025); the original 11 June 2025 date was postponed in May 2025 — [HUPX](https://hupx.hu/2025/05/14/market-coupling-steering-committee-aligns-revised-go-live-date-15-minute-mtu-sdac).
- Consequence for backtests: German day-ahead series are hourly up to 30 Sep 2025 and 15-min from 1 Oct 2025; Modo's German benchmark methodology explicitly models "hourly until Oct 2025 and 15-minute after" — [Modo Energy methodology, updated 20 May 2026](https://modoenergy.com/benchmarking/methodology/germany).

**ENTSO-E Transparency Platform (all bidding zones)**
- The live Terms & Conditions page returned HTTP 400/403 to both fetch tools on 11 Oct 2026; the token how-to and rate-limit articles on transparencyplatform.zendesk.com returned 403. What is documented in secondary ENTSO-E sources: a Data Policy "approved at the end of 2017" was implemented on the TP in 2018 to increase data re-use — [ENTSO-E Annual Report 2018](https://annualreport2018.entsoe.eu/transparency-and-trust/); the TP terms cover data from TSOs and from capacity allocators, and "Joint Allocation Office data can be re-used by TP users without any restriction" (2020) — [ENTSO-E Annual Report 2020](https://annualreport2020.entsoe.eu/transparency-regulation).
- A modelling-community critique (undated, likely pre-2020) states the TP T&Cs "do not provide a proper licence; data users must check with all relevant primary data owners in order to re-use data" — [nworbmot.org](https://www.nworbmot.org/energy/brown-entsoe.pdf).
- Practical route used by the German regulator: SMARD states its data "comes directly from ENTSO-E" and republishes it under CC BY 4.0 (see next item) — [SMARD Datennutzung](https://www.smard.de/home/datennutzung).
- ACER's 2024 opinion on the third update of the TP Manual of Procedures is the authoritative reference for what must be published — [ACER Opinion 01-2024](https://www.acer.europa.eu/sites/default/files/documents/Official_documents/Acts_of_the_Agency/Opinions/Opinions/ACER_Opinion_01-2024_third_update_MoP_ENTSO-E_Transparency_Platform.pdf).

**SMARD.de (Bundesnetzagentur, Germany)**
- Market data in "Marktdaten visualisieren" and "Daten herunterladen" are licensed under "Creative Commons Namensnennung 4.0 International" (CC BY 4.0); required attribution string: "Bundesnetzagentur | SMARD.de"; data "dürfen in Teilen genutzt, zusammengefügt und verändert werden"; data provided under § 111d EnWG "für die Öffentlichkeit zur freien Verfügung und Verwendung"; no API is described on the page (download only); liability for correctness excluded — [SMARD Datennutzung](https://www.smard.de/home/datennutzung).

**Energy-Charts (Fraunhofer ISE) API**
- API v2.0 released 2026-07-20; "Unless stated otherwise, data is licensed under CC BY 4.0"; "Proper attribution to Energy-Charts.info as the source is required". Day-ahead price endpoint is the exception: some zones (e.g., AT, FR, NL, PL) are CC BY 4.0 "from Bundesnetzagentur | SMARD.de", while other zones are "restricted to private and internal use". Rate limits: default 2 requests/min (burst 4) per IP per endpoint; `/price` 2/min (burst 2); `/signal` 20/min; HTTP 429 with Retry-After; "Higher limits for commercial use" via a named Fraunhofer ISE contact. Endpoints include `/v2/public_power`, `/v2/public_power_forecast` (load only as `forecast_type=day-ahead`), `/v2/installed_power`, `/v2/frequency` (1-s since 2022-05-01), `/v2/price` (bzn default DE-LU, ~50 zones), `/v2/cbet`, `/v2/cbpf` — [Energy-Charts openapi.json](https://api.energy-charts.info/openapi.json).

**netztransparenz.de (German TSOs: 50Hertz, Amprion, TenneT, TransnetBW)**
- reBAP is a symmetric quarter-hourly price (€/MWh, 15-min Balancing Time Unit) that can be positive or negative; published as reBAP_pos/reBAP_neg (identical except when Kapazitätsreserve is used); "Qualitätsgesicherte Daten: Spätestens am 20. Werktag des Folgemonats"; csv-Download and API-Download — [Netztransparenz Erläuterungen, 10 July 2023, §2.1](https://www.netztransparenz.de/xspproxy/api/staticfiles/ntp-relaunch/dokumente/regelenergie/regelenergie%20(%C3%BCs)/rl-erlaeuterungen_ntp_20230710.pdf).
- AEP-Schätzer: "eine Prognose des reBAP auf Basis betrieblicher Daten... spätestens 30 Minuten nach der jeweiligen Viertelstunde veröffentlicht"; computed as max(AEP1, AEP2, AEP3) for positive NRV-Saldo and min for negative — same document §2.4.
- ID-AEP: volume-weighted average of the last intraday trades totalling 500 MW for that quarter-hour, EPEX SPOT data only; published D+1 — same document §2.5.
- RZ-Saldo/NRV-Saldo: 15-min MW averages per TSO, operational and quality-assured versions; "Der RZ-Saldo entspricht dem umgekehrten Vorzeichen des ACE_open-loop" published on ENTSO-E as "total imbalance" — same document §3.1. Tender results remain on regelleistung.net — same document §1.
- Imbalance price construction (Amprion explainer): since June 2022 the AEP is built from modules — Module 1 base price from aFRR/mFRR platform prices (PICASSO/MARI); Module 2 couples to the ID-AEP with a minimum gap of 25% (at least €10/MWh) when |NRV balance| ≥ 500 MW, rising linearly between 0 and 500 MW; Module 3 scarcity component is a parabolic function of the NRV balance applying from 80% of dimensioned FRR; earlier caps (IP1/IP2/IP20) and the 3%/€3 price-correction were dropped in June 2022 — [Amprion, Important Information on the balancing energy price](https://www.amprion.net/Energy-Market/Balancing-Groups/Balancing-Group-Price/Important-Information.html).
- Price corrections after publication go into the following month's reBAP via pass-through so an already published reBAP is not changed — [BDEW](https://www.bdew.de/media/documents/Umgang-mit-Preiskorrekturen-nach-Veroeffentlichung-des-reBAP.pdf).
- Web-API: netztransparenz.de/de-de/Web-API redirects to https://api-portal.netztransparenz.de/ which returned "An error has occurred. Please reload." at fetch time; registration details and licence could not be verified — [API portal](https://api-portal.netztransparenz.de/).

**regelleistung.net (FCR/aFRR/mFRR tenders)**
- Page title "Datacenter FCR/aFRR/mFRR/ABLA" at [regelleistung.net datacenter](https://www.regelleistung.net/apps/datacenter/tenders/); it is a JavaScript application and no terms-of-use or format text could be extracted. Modo lists "Regelleistung" among the public inputs of its German index — [Modo methodology](https://modoenergy.com/benchmarking/methodology/germany).

**EPEX SPOT**
- Site navigation shows "Market data", "Market Data Services", "Dynamic Pricing Licence for Electricity Retailers", "Fees", and "General Conditions EPEX SPOT Market Data" — [EPEX market data](https://www.epexspot.com/en/market-data). All pages returned 403 to the fetch tool; no fee figures could be verified (see Gaps). The ID-AEP used in German imbalance pricing "basiert nur auf den Handelsdaten der EPEX-SPOT" — [Netztransparenz Erläuterungen §2.5](https://www.netztransparenz.de/xspproxy/api/staticfiles/ntp-relaunch/dokumente/regelenergie/regelenergie%20(%C3%BCs)/rl-erlaeuterungen_ntp_20230710.pdf).

**OMIE (MIBEL day-ahead and intraday, Spain and Portugal)**
- Public file families: Day-ahead "Prices (hourly, Spain and Portugal)", Programmes, Curves, Bids; Intraday Auction (IDAs since 13 June 2024) prices/curves/bids; Continuous Intraday (max/min/weighted prices per period); Settlements zips. Repository covers "the last 6 mobile years"; older files via the assistance portal; footer "© 2019-2026 - All rights reserved"; file formats described in a separate document (omie.es/en/publicaciones/64) — [OMIE file access list](https://www.omie.es/en/file-access-list). The legal notice page (omie.es/en/legal-notice, /aviso-legal) returned 403/404; no reuse licence verified.
- A community Python package downloads OMIE day-ahead and intraday price/volume files — [OMIEData on PyPI](https://pypi.org/project/OMIEData).

**ESIOS / REE (Spain)**
- API index at [api.esios.ree.es](https://api.esios.ree.es/): generic indicator endpoints ("Getting a specific indicator filtering values by a date range", "Search indicators by name") with time groupings five-minute, ten-minute, fifteen-minute, hourly, daily, monthly, yearly; personal token request at esios.ree.es/es/token. No licence or rate-limit text on the page.
- Settlement files are a separate route requiring "a card issued by REE or by OMEL and access to the subjects website" — [REE PDF](https://www.ree.es/sites/default/files/12_CLIENTES/Documentos/Acceso_a_ficheros_de_liquidaciones_desde_esios_.pdf).
- Community clients: pyesios ("You need a personal token in order to use the ESIOS API") — [pyesios](https://pypi.org/project/pyesios); esiosapy describes itself as unofficial — [esiosapy](https://pypi.org/project/esiosapy).

**REN Data Hub (Portugal)**
- Website: electricity production breakdown, consumption with expected-consumption forecast, wind and solar forecasts, daily average OMIE price; "Electricity: updated every 15 minutes"; downloads and iframe embedding; licence not stated — [REN Data Hub](https://datahub.ren.pt/en/).
- API: base `https://servicebus.ren.pt/datahubapi/` + `electricity/` or `gas/`; JSON; no authentication mentioned; electricity endpoints are daily energy balance, production breakdown, monthly balance and installed power, yearly consumption variation, daily/monthly market prices. "Not covered on this page: forecasts, imbalances (desvios), and reserves"; no licence stated — [REN API instructions](https://datahub.ren.pt/en/api-instructions/). The REN terms-of-use URL returned 404.

**TenneT NL**
- Developer portal lists APIs: Settlement prices (imbalance prices per balancing time unit), Reconciliation Prices, Merit Order List Incident Reserve (mFRRda), Merit Order List aFRR & mFRRsa (capacity bids per PTU), FRR activations, "Balance Delta High Res" (name only), Available Border Capacity, Settled imbalance volumes, Metered injections; Register/Login links; a "Fair use policy" link; no licence or history stated — [developer.tennet.eu](https://developer.tennet.eu/).

**Elia (Belgium)**
- Catalogue (API call on 11 Oct 2026): 110 datasets, every one tagged "Elia Open Data Licence". Relevant IDs: ods133 imbalance price per minute (as of 22/05/2024), ods134 imbalance prices per quarter-hour (as of 22/05/2024), ods046/ods047 the same up to 22/05/2024, ods162 near-real-time imbalance price, ods136/ods147 system imbalance forecast (current/next QH), ods126 current system imbalance, ods125/ods207 individual aFRR capacity bids, ods055/ods206 individual mFRR capacity bids, ods156/ods157 individual incremental/decremental balancing energy bids, ods031/ods032 wind and PV estimation and forecast, ods001 measured and forecast total load, ods057 frequency and FCR demand per 10 s; new "[Simulated] Imbalance prices per minute (Live updates as of 24/11/2026 conditional on CREG approval)" (ods211/ods212) — [Elia catalogue API](https://opendata.elia.be/api/explore/v2.1/catalog/datasets?limit=100). The licence text itself redirects to elia.be/en/disclaimer which returned 403; terms not verified.

**APG (Austria)**
- Transparency page lists load/forecast, generation by type and forecast, installed capacity, PRR/SRR/TRR (FCR/aFRR/mFRR) awarded capacity and energy bids, imbalance energy prices and balance, day-ahead prices; "public REST API for market transparency data" (access requested through the site); data from 01.01.2023 via API and visualisations, data up to 31.12.2022 only in download area; only a liability disclaimer, no CC licence stated — [APG Transparenz](https://markt.apg.at/transparenz/).

### Inferences
- For a commercial product, the lowest-risk German price stack is SMARD (CC BY 4.0) + netztransparenz (statutory publication) + Energy-Charts for non-price series; do not rely on Energy-Charts `/price` for DE-LU in a product without written consent, because the API marks most price zones as private/internal use.
- The AEP-Schätzer (T+30 min) and ID-AEP (D+1) make a realistic "information available at decision time" protocol possible for German imbalance experiments: the final reBAP is only known ~4 weeks later, so any intraday re-dispatch decision must use the Schätzer or ID-AEP, not the final price.
- Iberia: OMIE + ESIOS supply all wholesale prices needed, but the Portuguese imbalance (desvios) prices are not on REN's API; they would have to be obtained from REN's market/settlement pages or ESIOS (Spain) with licence confirmation.

### Gaps
- ENTSO-E TP Terms & Conditions text, token procedure and rate limits could not be fetched (HTTP 400/403 on 11 Oct 2026); commercial redistribution rules for TP data remain unverified beyond the 2020 statement that JAO data is unrestricted.
- EPEX SPOT market-data fee schedule, continuous-intraday order-book data cost and the "General Conditions EPEX SPOT Market Data" and "Dynamic Pricing Licence for Electricity Retailers" terms: pages returned 403; no figures.
- OMIE legal notice, ESIOS terms of use, REN Data Hub terms, Elia Open Data Licence text, TenneT fair-use policy, APG API terms: not retrievable or not stated on the pages fetched.
- regelleistung.net download formats, history depth and terms: SPA page, nothing extractable.
- Portuguese desvios/secondary-reserve price series location and licence: not found.
- Netztransparenz API registration process: portal errored.

## Key Question 2: Load, generation, weather and registry data (ENTSO-E/TSO, DWD, ECMWF, Open-Meteo, ERA5, PVGIS, OPSD, MaStR)

### Takeaway
Weather is the main no-look-ahead hazard: ECMWF Open Data and DWD only keep the latest runs (ECMWF: last 12 runs), so historical issue-time forecasts must come from Open-Meteo's Historical Forecast API (ICON-D2/EU/Global archived since 2022-11-24, IFS 0.25° since 2024-02-03) or Previous Runs API (fixed day-1..day-7 lead times, most models since Jan 2024), which require a paid Professional plan for commercial use. DWD and ECMWF open data are CC BY 4.0; MaStR is Datenlizenz Deutschland – Namensnennung 2.0; OPSD's own page still says funding ended in 2020.

### Cited Findings
- ECMWF Open Data: "may be redistributed and used commercially, subject to appropriate attribution" (CC BY 4.0 plus ECMWF Terms of Use); 0.25° GRIB2; IFS runs 00/06/12/18 UTC, 0–144 h in 3-h steps then 150–360 h in 6-h steps for 00/12z; AIFS 0–360 h in 6-h steps; "Rolling archive. The most recent 12 forecast runs are kept, about 2–3 days of forecasts. Full historical access requires a Service Agreement" — [ECMWF Open Data](https://www.ecmwf.int/en/forecasts/datasets/open-data).
- DWD: "Es gelten die Bedingungen der Lizenz Creative Commons BY 4.0" (Stand Mai 2024) — [DWD CDC Nutzungsbedingungen](https://opendata.dwd.de/climate_environment/CDC/Nutzungsbedingungen_German.pdf); the DWD Act change effective 25 July 2017 gives DWD a mandate to provide data "mostly free of charge"; "service and availability levels cannot be guaranteed for this service" — [DWD Open Data](https://www.dwd.de/EN/ourservices/opendata/opendata.html); NWP directories available: icon, icon-d2, icon-d2-eps, icon-eps, icon-eu, icon-eu-eps; no README on retention — [opendata.dwd.de/weather/nwp](https://opendata.dwd.de/weather/nwp/).
- Open-Meteo pricing: free/open-access tier "for non-commercial use only", 10,000 calls/day (600/min, 5,000/h, 300,000/month); API Standard 1M calls/month, Professional 5M, Enterprise 50M+; "Historical, Climate, Ensemble, and Satellite Radiation APIs" require Professional or higher per the FAQ; open data licensed CC BY 4.0 and "attribution is a requirement under this licence" even for commercial use — [Open-Meteo pricing](https://open-meteo.com/en/pricing). Prices from Open-Meteo's own newsletter: Standard $29/month (1M calls), Professional $99/month — [Open-Meteo Substack](https://openmeteo.substack.com/p/api-subscriptions-for-commercial) (date of post not confirmed; verify current price).
- Open-Meteo Historical Forecast API: archived forecasts where "Each run's first few hours are joined into one continuous hourly series" (i.e., a stitched best-available series, not fixed lead time); archive starts: ICON Global/ICON-EU/ICON-D2 from 2022-11-24; ECMWF IFS 0.25° from 2024-02-03; IFS HRES 9 km from 2017-01-01; AIFS 0.25° from 2025-02-20; GFS from 2021-03-23; ARPEGE Europe from 2022-11-13; KNMI/DMI HARMONIE from 2024-07-01 — [Historical Forecast API](https://open-meteo.com/en/docs/historical-forecast-api).
- Open-Meteo Previous Runs API: "Requesting temperature_2m_previous_day1 returns the value predicted 24 hours before valid time"; offsets day 1–7; most models archived from January 2024 (exceptions: GFS 2 m temperature from March 2021, JMA from 2018); "Older history may be reconstructed on request" — [Previous Runs API](https://open-meteo.com/en/docs/previous-runs-api).
- ERA5: 0.25° atmosphere; "updated daily with a latency of about 5 days"; ERA5T early release may differ from the final release 2–3 months later; CC-BY licence listed — [CDS ERA5 single levels](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview).
- PVGIS API v5_3: `https://re.jrc.ec.europa.eu/api/v5_3/{PVcalc|seriescalc|tmy|...}`; 30 calls/s per IP (HTTP 429 beyond), HTTP 529 when overloaded; GET only, no AJAX; licence not stated on the page — [PVGIS API](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/getting-started-pvgis/api-non-interactive-service_en).
- Open Power System Data: homepage still says "actively maintained (current funding until 2020)"; code MIT; data: the team "would like to publish all data under CC BY 4.0, but several data owners do not allow us to do so" — [OPSD](https://open-power-system-data.org/).
- Marktstammdatenregister Gesamtdatenexport: XML in ZIP of ~3,155,463 KB (~3.2 GB); updated "in der Regel um 5:00 Uhr"; export version changed 01.10.2025; licence "Datenlizenz Deutschland – Namensnennung – Version 2.0"; bulk download only on that page (no API described) — [MaStR Datendownload](https://www.marktstammdatenregister.de/MaStR/Datendownload).
- Energy-Charts offers load as a `production_type` in `/v2/public_power_forecast` with `forecast_type=day-ahead`, plus PV/wind shares measured and forecast — [Energy-Charts openapi.json](https://api.energy-charts.info/openapi.json).
- Elia publishes wind and PV "estimation and forecast on Belgian grid (Historical)" (ods031/ods032) and measured/forecast total load (ods001) under the Elia Open Data Licence — [Elia catalogue](https://opendata.elia.be/api/explore/v2.1/catalog/datasets?limit=100).
- REN publishes mainland Portugal wind and solar generation forecasts and an expected-consumption forecast on its site (15-min updates) — [REN Data Hub](https://datahub.ren.pt/en/).

### Inferences
- A rigorous no-look-ahead weather feature set for 2024-onward German/Iberian backtests is feasible with Open-Meteo Previous Runs (fixed lead-time) at Professional tier; for 2022–2023 only the stitched Historical Forecast API exists, which slightly flatters short-lead accuracy and should be disclosed as a limitation.
- ERA5's ~5-day latency and ERA5T revisions mean reanalysis may be used for training targets/proxies but never as a decision-time input in a backtest.
- MaStR's daily 3.2 GB XML is sufficient to build DSO-level and postcode-level PV/battery/EV-charger counts for portfolio scaling without an API.

### Gaps
- DWD ICON run retention time on opendata.dwd.de and the existence/cost of a DWD archive of past NWP runs: not verified.
- Copernicus/ERA5 licence wording (commercial use) beyond the "CC-BY" label on the dataset page: not verified.
- PVGIS data licence/reuse terms: not stated on the API page.
- OPSD time_series package last-update date: not on the homepage.
- IPMA (Portugal) and AEMET (Spain) open-data terms: not researched (search budget exhausted).

## Key Question 3: Household, EV and heat-pump metered profiles, and tariff formulas (DE, PT, ES, NL/AT)

### Takeaway
Freely usable metered residential data exists at research scale: WPuQ (38 German households with heat pumps, 10-s, 2018–2020, CC BY 4.0), HTW Berlin 74-household 1-s load profiles ("frei verfügbar", no licence named), London Low Carbon dToU trial (5,567 households, half-hourly, CC BY), E-REDES hourly consumption by postal code and hourly EV-mobility consumption (CC BY 4.0). Tariff-side, Germany's §14a Modul 3 schedules are published per DSO (790 DSOs analysed; HT–NT spread 1.82–22.47 ct/kWh; median correlation with day-ahead prices only 0.22), while Portugal's regulated tariff tables are Excel files per ERSE Directive 1/2026.

### Cited Findings

**Metered profiles**
- WPuQ v2.0 (Zenodo, 5 Nov 2021): "Electric load of 38 households measured in a small village in Lower Saxony, Germany", 2018–2020, 10-s files plus 1-min/15-min/60-min aggregates, separate heat-pump and household measurements plus transformer; 33.8 GB; CC BY 4.0; DOI 10.5281/zenodo.5642902 — [Zenodo](https://zenodo.org/records/5642902).
- HTW Berlin: "74 Stromverbrauchsprofile von Privathaushalten" at 1-s resolution, collected by IZES; "frei verfügbar"; download via HTW cloud (password "profile"); DOI 10.13140/RG.2.1.5112.0080/1; no licence or commercial-use statement; no PV data — [HTW Lastprofile](https://solar.htw-berlin.de/elektrische-lastprofile-fuer-wohngebaeude/).
- HTW's 2026 poster simulations use "Reale Lastprofile von 27 deutschen Privathaushalten" (data: ISFH) — [HTW Meissner 2026 poster](https://solar.htw-berlin.de/wp-content/uploads/MEISSNER-2026-Poster-Einfluss-dynamischer-Stromtarife-und-zeitvariabler-Netzentgelte-auf-Haushalte-mit-PV-Batteriespeichersystem.pdf).
- LoadProfileGenerator: synthetic residential electricity/hot-water profiles at 1 h to 1 min, "completely free of charge", latest listed version 10.10, licence not stated, footer "all rights reserved" — [loadprofilegenerator.de](https://www.loadprofilegenerator.de/).
- London Low Carbon smart-meter data: ~5,567 households, Nov 2011–Feb 2014, half-hourly kWh; ~1,100 on dynamic ToU (High 67.20 p/kWh, Low 3.99 p/kWh, Normal 11.76 p/kWh during 2013; flat 14.228 p/kWh for others); CC BY 4.0; ~10 GB CSV — [London Datastore](https://data.london.gov.uk/dataset/smartmeter-energy-use-data-in-london-households).
- SERL (UK): "only accredited researchers working on approved projects can gain access"; commercial use not addressed — [SERL data](https://serl.ac.uk/data/).
- ACN-Data (Caltech/JPL/office EV charging): per-session fields incl. connectionTime, doneChargingTime, kWhDelivered, pilot/current time series, user inputs (kWhRequested, requestedDeparture); API with registration token; no licence stated, citation requested — [ACN-Data](https://ev.caltech.edu/dataset).
- ElaadNL open data moved to https://data.elaad.nl/ (301 redirect; 503 at fetch time).
- E-REDES (Portugal DSO) open-data catalogue (70 datasets, 11 Oct 2026): "Hourly Consumption by Postal Code" series (4-digit and 7-digit), "Hourly Consumption of Electric Mobility" by district groups, "Electricity Consumption by Municipality by Tariff Period", "Number of low voltage delivery points with collection of Load Diagrams", substation load diagrams, "Total de unidades de produção para autoconsumo", "Energy Communities" — all CC BY 4.0 — [E-REDES catalogue API](https://e-redes.opendatasoft.com/api/explore/v2.1/catalog/datasets?limit=100).

**German tariff components and §14a**
- Tibber "Smart Dynamic": energy billed "zu den aktuellen 15-Minuten-Preisen" plus "the usual taxes and levies"; a 5.99 €/month fee appears in the FAQ; no ct/kWh component values on the page — [Tibber](https://tibber.com/de/stromtarif).
- §14a EnWG modules (Yello explainer, 24 Feb 2026): Modul 1 flat annual grid-fee reduction "zwischen 110 € und 190 € brutto im Jahr"; Modul 2 (separate meter) reduces the network charge "auf 40 % je verbrauchter kWh"; Modul 3 since 1 April 2025 as add-on to Modul 1, requires an intelligentes Messsystem, three tiers ST/HT/NT; devices >4.2 kW on low voltage; curtailment floor 4.2 kW — [Yello](https://www.yello.de/wissen/energiemarkt/14a-enwg-netzentgelt/).
- Modul 3 schedules in practice (ZfK, 12 June 2026, citing a Rabot Energy analysis of 790 DSOs ≈ 92% of DSOs in MaStR, Q1 2026, 35,040 quarter-hours): HT–NT difference 1.82 to 22.47 ct/kWh; lowest NT examples Bayernwerk 0.47, EWE 0.32, LEW 0.41 ct/kWh; 452 DSOs (57%) effectively flat in summer; 338 (43%) have HT/NT year-round; 255 DSOs use a night-low model, 55 a midday "solar" low model; median correlation between grid-fee signal and day-ahead price 0.22; up to 674 €/a impact for a 3,000 kWh heat pump; Rabot is a dynamic-tariff seller (conflict of interest noted) — [ZfK June 2026](https://www.zfk.de/energie/strom/variable-netzentgelte-14a-enwg-modul-3-dynamische-tarife).
- Modul 3 HT levels: 10–17 ct/kWh in 2025 vs 6–16 ct/kWh in 2026 for the same quarter (ZfK) — [ZfK 2026](https://www.zfk.de/politik/regulierung/zeitvariable-netzentgelte-modul-3-netzbetreiber).
- Example DSO price sheets for Modul 3 (Q1/Q4 HT/ST/NT, summer flat): [Röttingen 2026](https://www.roettingen.de/fileadmin/Dateien/Dateien/Versorgungsbetriebe/Netzentgelte/2026_Netzentgelt_f%C3%BCr_steuerbare_Verbrauchseinrichtungen.pdf), [Burgbernheim 2025](https://erdgas.burgbernheim.de/_obj/B92742C0-B882-4DCA-A09D-07397235B25C/outline/Preisblatt-14a-EnWG-vorlaeufige-Netzentgelte-ab-01.01.2025.pdf).
- Dynamic-tariff add-on costs used by a 2026 German study: SMGW 60–100 €/a plus HEMS 20–60 €/a, "zusammen konservativ rund 120 €/Jahr" (= 3.4 ct/kWh at 3,500 kWh/a, 1.5 ct/kWh at 8,000 kWh/a); average dynamic all-in price ~36 ct/kWh "seit April 2025"; intra-day spot spreads typically 5–15 ct/kWh; incumbent fixed tariffs 31–40 ct/kWh, new-customer fixed 24–27 ct/kWh — [BürgerNetzwerkSolar study 2026 (hosted by Stadt Worms)](https://www.worms.de/neu-de-wAssets/docs/zukunft-gestalten/klima-umwelt/Energie/BuergerSolarBeratung/_BNS_3_Studie_A_Effizienz_von_Batteriespeichersystemen_mit_dynamischen_Stromtarifen-Fachstudie_2026_mit_Querverweisen-final.pdf).

**Portugal / Spain tariffs**
- ERSE Directive No. 1/2026 of 7 January approves 2026 tariffs and the 2026–2029 regulatory parameters; "Electricity Tariff Tables effective from 1 January 2026" and "Regulated Price Tables" are published as Excel; Directive No. 4/2026 of 15 September adjusts the supplier-of-last-resort energy tariff from 1 October 2026; normal LV (≤41.4 kVA) can choose simple, bi-hourly (peak/off-peak) or tri-hourly (peak/mid-peak/off-peak) network-access tariffs; nothing on indexed tariffs on that page — [ERSE tariffs and prices](https://www.erse.pt/en/activities/market-regulation/tariffs-and-prices-electricity/).

### Inferences
- For Experiment 2 the cleanest licence path is WPuQ (CC BY 4.0, includes heat pumps) for German loads and E-REDES postal-code hourly data (CC BY 4.0, aggregated) for Portuguese shape calibration; HTW's 74 profiles are usable for research but the missing licence must be clarified before product use.
- The weak correlation (median 0.22) between Modul 3 schedules and day-ahead prices means a residential optimiser faces two partially conflicting signals; this is itself a measurable experiment outcome (value of co-optimising both vs. price-only).

### Gaps
- Portuguese indexed-tariff formula (OMIE + losses + adjustment services + margin) and ERSE guidance: not found on the pages fetched.
- Spanish PVPC formula and ESIOS indicator IDs: REE/ESIOS PVPC pages returned 404 or were JS shells; not verified.
- Dutch and Austrian dynamic-tariff/grid-fee equivalents: not researched (search budget).
- Octopus/Rabot German tariff component formulas: not fetched.
- ElaadNL dataset contents and licence: portal unavailable at fetch time.
- Spanish/Portuguese individual smart-meter datasets (i-DE, Endesa): not found; E-REDES publishes only aggregated postal-code/substation series.
- Liander (NL) open data status and OpenEMS datasets: not researched.

## Key Question 4: What public data cannot prove, and which partnership unlocks each

### Takeaway
Public data supports price-taker, perfect-information-about-prices backtests only. It cannot prove execution quality in continuous intraday, real imbalance exposure of a specific balancing group, asset availability or control rights, or settlement economics.

### Cited Findings
- Order books and realised trades: OMIE publishes aggregated curves and "Bids" files, but EPEX continuous order-book data sits behind "Market Data Services" and the "General Conditions EPEX SPOT Market Data" (fee pages not retrievable) — [EPEX market data](https://www.epexspot.com/en/market-data); Modo's German index substitutes a "centred 2-hour rolling mean" for actual ID3 execution and applies a flat 0.80 calibration factor "anchored to observed Great Britain fleet capture" because "Germany has no public per-asset battery data" — [Modo methodology](https://modoenergy.com/benchmarking/methodology/germany).
- Individual balancing-group positions: the reBAP is published as a DE-wide value only; RZ/NRV-Saldo are TSO-level — [Netztransparenz Erläuterungen](https://www.netztransparenz.de/xspproxy/api/staticfiles/ntp-relaunch/dokumente/regelenergie/regelenergie%20(%C3%BCs)/rl-erlaeuterungen_ntp_20230710.pdf).
- Settlement files in Spain require an REE/OMEL card and subject-website access — [REE](https://www.ree.es/sites/default/files/12_CLIENTES/Documentos/Acceso_a_ficheros_de_liquidaciones_desde_esios_.pdf).
- Individual meters: SERL access is restricted to accredited researchers — [SERL](https://serl.ac.uk/data/); E-REDES publishes only aggregates (postal-code/substation) — [E-REDES catalogue](https://e-redes.opendatasoft.com/api/explore/v2.1/catalog/datasets?limit=100).
- Control events: as of April 2026 "no § 14a control intervention was recorded on VNBdigital" (ZfK) — [ZfK](https://www.zfk.de/energie/strom/variable-netzentgelte-14a-enwg-modul-3-dynamische-tarife).
- Prequalification/availability: Modo clips aFRR capacity bids at 50 EUR/MW/h and sets cycles/efficiency by assumption rather than measurement — [Modo methodology](https://modoenergy.com/benchmarking/methodology/germany).

### Inferences (partnership map, [design])
- Realised execution/slippage in continuous intraday → a trading-desk or direct-market-access partner (or paid EPEX order-book data).
- Balancing-group imbalance exposure, actual reBAP invoices → one supplier/BRP data-sharing agreement (anonymised 15-min schedule vs. allocation series).
- Individual household/EV/heat-pump meters with control rights → a HEMS/battery OEM or utility pilot (HTW's 2025 energy-management test lists Fenecon, KOSTAL, sonnen, RCT Power as participating OEMs) — [HTW Inspektion 2025](https://solar.htw-berlin.de/wp-content/uploads/HTW-Stromspeicher-Inspektion-2025.pdf).
- Asset availability, SoC telemetry, degradation, prequalification constraints → a BESS owner/optimiser (the Modo page names "enspired"-style optimisers only indirectly; no public per-asset data exists in Germany).
- Aggregator fees and revenue-share terms → term sheets from flexibility aggregators; not public.

### Gaps
- No public source quantifies aggregator fee levels or revenue-share percentages for DE/PT residential flexibility; treat any figure as a term-sheet input.

## Key Question 5: Value of forecasting improvements (imbalance cost of forecast error; price-forecast skill; does price skill translate into money?)

### Takeaway
Quantified, recent (2025–2026) German/Iberian studies converting load/PV/wind forecast error into €/MWh of imbalance cost were not found; the best available numbers are older (wind balancing cost 1.7–2.5 €/MWh in Germany 2010–2012). Price-forecast skill is well benchmarked: a pan-European XGBoost study over Jan 2025–Mar 2026 finds DE-LU among the most predictable zones (rMAE 0.566–0.612) and no systematic deterioration after the 15-min switch; a 2026 Hirsch–Ziel paper shows that ranking forecasters by battery-trading profit can be gamed and is not a proper scoring rule, so price skill alone is a weak proxy for money.

### Cited Findings
- Historical wind balancing cost, Germany: "balancing costs between 1.7 and 2.5 €/MWh wind energy in Germany during the period 2010-2012" (Hirth & Ziegenhagen) — [Balancing Power and Variable Renewables (PDF)](https://opus4.kobv.de/opus4-hsog/files/2285/Balancing+Power+and+Variable+Renewables.pdf) (figure taken from the search snippet of this document; verify page).
- The reBAP "is not meant as a penalty for balancing-group forecast deviations, but reflects the price of the activated reserves"; incentive Module 2 forces a ≥25%/≥€10/MWh gap to the intraday index at |NRV| ≥ 500 MW — [Amprion](https://www.amprion.net/Energy-Market/Balancing-Groups/Balancing-Group-Price/Important-Information.html).
- Pan-European day-ahead benchmark (IAEE abstract, Semmelmann/KIT, PDF generated 26 May 2026): XGBoost with SHAP across all 31 bidding zones, Jan 2025–Mar 2026, hourly and 15-min products; DK, FI, DE-LU most predictable with "rMAE 0.566–0.612"; Nordic hydro zones and CH hardest (rMAE 1.361–1.651); weather features 68.7% of importance; auxiliary load/generation predictions improve accuracy by 15.6% on average; "The October 2025 transition from hourly to 15-minute products does not produce systematic forecast deterioration"; Portugal benefits "substantially from neighboring zone fundamentals" — [IAEE abstract 487](https://app.iaee.org/abstract/abstract-487.pdf).
- Open benchmark toolbox and datasets (Lago, Marcjasz, De Schutter, Weron; Applied Energy 2021): LEAR and DNN baselines; the EPEX-DE test window in the open dataset is 04.01.2016–31.12.2017 — [arXiv 2008.08004](https://arxiv.org/abs/2008.08004).
- Hirsch & Ziel (arXiv 2604.19580, 21 April 2026; Univ. Duisburg-Essen / Statkraft): German day-ahead case study, data 2015–2023 (test 2018-12-27 to 2023-12-31), 10 MWh storage, round-trip efficiency 0.95², durations 1/2/4 h, 1–2 cycles/day, DP and MILP, risk-neutral and CVaR objectives; "quantile-based trading strategies (QBTS) do not reward honest probabilistic forecasting"; "an overdispersed forecast can lead to higher expected profits than the perfect forecast"; "ranking forecasting models by battery trading performance can be misleading" — [arXiv 2604.19580](https://arxiv.org/abs/2604.19580).
- Kath & Ziel (Energy Economics 2018): German quarter-hourly intraday continuous and call-auction prices, elastic-net forecasts, "even simple electricity trading strategies can have substantial economic impact" (no €/MWh figure in abstract) — [arXiv 1811.08604](https://arxiv.org/abs/1811.08604).
- Quarter-hourly forecast-error pass-through: a German quarter-hourly study found higher wind/solar forecast errors increase absolute imbalance volumes and can pass into spot prices (snippet of [IAEE proceedings](https://www.iaee.org/en/publications/proceedingsabstractdoc.aspx?id=7948)).
- Commercial definition of "imbalance cost" for PPAs: difference between revenue with a perfect day-ahead forecast and actual revenue; in single-price systems such as Germany the sign depends on direction relative to system imbalance (Pexapark help page; fetch was rate-limited, from search snippet) — [Pexapark](https://help.platform.pexapark.com/en/articles/11172380-imbalance-costs).
- Forecast-based home-storage charging became a tested feature in 2025: HTW/KIT developed a new energy-management test; "3 Systeme eine Internetverbindung zum Bezug der Wetterprognosen benötigen" while 3 forecast locally — [HTW Inspektion 2025, p.7](https://solar.htw-berlin.de/wp-content/uploads/HTW-Stromspeicher-Inspektion-2025.pdf).

### Inferences
- The imbalance value of a load/PV forecast improvement in Germany must be computed from public series rather than cited: cost = Σ_t (reBAP_t − P_DA/ID_t) × error_t, with sign depending on whether the balancing group is short/long against the NRV-Saldo. Because Module 2 enforces a ≥25% gap to ID-AEP when |NRV| ≥ 500 MW, the expected penalty per MWh of error is bounded below by ~25% of the intraday index in high-imbalance quarter-hours, which gives a reproducible lower-bound metric [inference].
- Semmelmann's rMAE ~0.57–0.61 for DE-LU with XGBoost sets a defensible baseline: a founder's model must beat ~0.6 rMAE out of sample on 2025–2026 data to claim state-of-the-art day-ahead skill.
- Hirsch–Ziel implies the right experimental metric is realised net value under a fixed, published dispatch policy (MILP with the forecast as input) plus proper scoring rules (CRPS/energy score), not profit alone.

### Gaps
- No 2022–2026 study found giving €/MWh imbalance cost per MWh of load/PV/wind forecast error for German suppliers/BRPs (Fraunhofer, FfE, TUM, Energy Brainpool) — the Fraunhofer document surfaced by search was a 2012 ISI slide deck on RE cost-benefit, not relevant.
- No Iberian (REN desvios / ESIOS desvíos) imbalance-cost-of-forecast-error study found.
- Numeric profit tables from Hirsch & Ziel's Figures 14–15 are graphical; not extracted.
- Lago et al. 2021 EPEX-DE MAE/rMAE values: table is graphical in the PDF; not extracted.

## Key Question 6: Battery arbitrage value (home, C&I/grid-scale DE, Iberia, NL) and the perfect-foresight-vs-rolling-forecast gap

### Takeaway
Home batteries on German dynamic tariffs are worth little once PV is present: HTW's 2026 simulation of 27 real households finds price-optimised control saves on average 233 €/a without PV but only 64 €/a with PV, and most PV-battery households lose ~4 €/a on a dynamic tariff alone; combining §14a Modul 1+3 was best. Grid-scale: German day-ahead spreads widened from ~€30/MWh (2019) to ~€130/MWh (2024); Iberian day-ahead TBx benchmarks are ~€80k/MW (2024) and ~€130k/MW (2025); Modo's German index applies a flat 0.80 realisation factor to perfect-foresight revenue. Academic MPC studies capture 50–90% of perfect-foresight arbitrage (NYISO), >80% for >2 h batteries.

### Cited Findings

**Residential, Germany**
- HTW Berlin (Meissner, Bergner, Kerlinski, Quaschning; KLIMTEC project, poster 2026): Simbat model, threshold-based price control, DWD irradiance/temperature, 27 real household load profiles (ISFH), synthetic Tibber-style dynamic tariff on 2024 SMARD prices, time-variable grid fees from 14 DSOs; "Ein PV-Generator senkt die potentielle Kosteneinsparung durch die preisoptimierte Steuerung in allen untersuchten Haushalten von durchschnittlich 233 €/a auf 64 €/a"; "Ein Großteil der Haushalte mit PV-Batteriespeichersystem muss bei der alleinigen Nutzung des dynamischen Stromtarifs sogar Mehrkosten zahlen, im Durchschnitt 4 €/a"; "Die Kombination von Modul 1 und 3 nach §14a des EnWG stellt die beste Option für alle untersuchten Haushalte dar" — [HTW poster](https://solar.htw-berlin.de/wp-content/uploads/MEISSNER-2026-Poster-Einfluss-dynamischer-Stromtarife-und-zeitvariabler-Netzentgelte-auf-Haushalte-mit-PV-Batteriespeichersystem.pdf).
- HTW Stromspeicher-Inspektion 2025 (Feb 2025): 17 manufacturers, 22 systems; mean battery efficiency 95.7% (20 of 22 above 95%); worst hybrid inverter loses 46% at 100 W output ("Der Batteriespeicher muss folglich 186 W bereitstellen, damit 100 Watt ... ankommen"), best 14–24%; reference fully-electrified household 9,363 kWh/a with 3,745 €/a bill; 10 kW PV cuts bill by 1,677 €/a; adding a high-efficiency 10 kWh battery raises self-supply to 56% and total saving to "fast 2500 €/a" — [HTW Inspektion 2025](https://solar.htw-berlin.de/wp-content/uploads/HTW-Stromspeicher-Inspektion-2025.pdf).
- BürgerNetzwerkSolar study (2026, uses HTW 2025 measurements): LCOS = investment/(capacity × cycles): 5 kWh cheap 2,500 €/6,000 cycles = 8.3 ct/kWh; 10 kWh quality 6,000 €/10,000 cycles = 6.0 ct/kWh; effective cost per discharged kWh = (LCOS + charge price)/η; 10 kWh quality storage reaches ≤30 ct/kWh effective only at spreads ≥15 ct/kWh and η ≥ 86%; with 10 kWp PV + 10 kWh storage and 3,500 kWh/a, dynamic tariff saves ~35 €/a without and 60–100 €/a with optimisation versus a 40 ct/kWh legacy fixed tariff, but costs ~79 €/a more than a 24 ct/kWh new-customer tariff; typical real savings 7–12% of residual grid purchase, "etwa 80–250 € pro Jahr" — [BNS study PDF](https://www.worms.de/neu-de-wAssets/docs/zukunft-gestalten/klima-umwelt/Energie/BuergerSolarBeratung/_BNS_3_Studie_A_Effizienz_von_Batteriespeichersystemen_mit_dynamischen_Stromtarifen-Fachstudie_2026_mit_Querverweisen-final.pdf). (Non-academic citizen-network study; use as a sanity range, not as evidence.)
- Verbraucherzentrale Niedersachsen (1 July 2026) gives no € figures; savings "gering" if consumption cannot be shifted — [VZ Niedersachsen](https://www.verbraucherzentrale-niedersachsen.de/node/123774).

**Grid-scale / C&I, Germany**
- Modo ME BESS DE methodology (20 May 2026; first publication May 2026): markets stacked = DA (EPEX DE-LU), IDA2 auction, ID3 continuous, FCR (symmetric), aFRR capacity (pos/neg), aFRR energy; mFRR, capacity payments, imbalance, grid fees excluded; perfect foresight in DA and IDA steps; ID3 and aFRR energy use a "centred 2-hour rolling mean"; "a flat 0.80 multiplier applies to all simulated per-timestep revenues ... anchored to observed Great Britain fleet capture"; aFRR capacity price clipped at 50 EUR/MW/h; 88% AC-AC round-trip; 1.5 cycles/day (custom 1–5); 100% DoD; SoC reset 50% at midnight; degradation disabled; index values not public ("unauthorised reproduction or redistribution requires Modo's prior written consent") — [Modo methodology](https://modoenergy.com/benchmarking/methodology/germany).
- Modo Germany explainer: day-ahead highest-to-lowest spreads "from about €30/MWh in 2019 to €130/MWh in 2024"; FCR ~3 GW procured continentally of which ~570 MW for Germany, ~800 MW qualified; aFRR ~2 GW with "€400 million of TSO spend in 2024", ~550 MW qualified; fleet 2.5 GW operational end-2025; a related teaser mentions "~€215k/MW/yr for September 2026 ... fell 40% on the year" (annualisation basis unclear); grid-forming inertia product €8–17k/MW/yr in 2026 — [Modo Germany explainer](https://modoenergy.com/research/en/germany-explained-how-europes-most-liquid-power-market-really-works-for-bess).
- Fleet: Germany added 842 MW of grid-scale batteries in 2025, reaching 2.4 GW by year-end (Modo, Feb 2026, from search snippet) — [Modo buildout](https://modoenergy.com/research/en/de-germany-bess-batteries-buildout-capacity-growth-installation-grid-scale-february-2026).

**Iberia**
- Modo ME BESS ES (6 July 2026): day-ahead sub-line validated against "publicly available Iberian BESS TBx benchmarks (~€80k/MW for 2024; ~€130k/MW for 2025)"; modelled asset 50 MW/4 h, 88% RTE, max 2 cycles/day, backtest Jan 2024–Jun 2026; per-stream values only in charts — [Modo ES benchmark](https://modoenergy.com/research/es-bess-me-benchmark-revenue-stack). Search snippets of the same family of articles state Spanish daily spreads hit a record €94/MWh in 2025, the benchmark discharged at ~€90/MWh vs €60/MWh average, and a July 2026 forecast of total revenue falling to €152k/MW/yr by 2028 from €219k/MW/yr in April — [Modo ES (en)](https://modoenergy.com/research/en/es-bess-me-benchmark-revenue-stack) (snippet-sourced; verify).
- University of Seville (Energy Reports, article dated 20 Jan 2026): with 2024 Spanish data, raising storage to the planned 30 GWh cuts the average daily peak-trough differential from €70.68/MWh to €32.56/MWh; beyond 32 GWh revenues no longer cover variable costs; ~130 idle days/year for marginal capacity; an incremental 6 GWh at €109,000/MWh capex yields ~4% — [ESS News](https://www.ess-news.com/2026/01/20/battery-storage-in-spain-becomes-unviable-beyond-32-gwh-of-cumulative-capacity-study-finds/).
- European Commission approved Spain's capacity market on 29 May 2026 (Modo snippet) — [Modo ES](https://modoenergy.com/research/en/es-bess-me-benchmark-revenue-stack).

**Perfect foresight vs. forecast-driven dispatch**
- Zheng, Jaworski, Xu (NYISO real-time arbitrage, 2021/22): MPC with price forecasts "captures 50% to 90% of arbitrage profit compared to perfect price forecasts" and ">80%" in three of four zones for batteries over two hours with realistic degradation cost — [arXiv 2108.06000](https://arxiv.org/abs/2108.06000).
- Opportunity-value-function prediction (NYISO): 65–90% of perfect-foresight profit (ar5iv) and up to 90% (PDF) — [arXiv 2211.07797](https://arxiv.org/pdf/2211.07797).
- Modo's 0.80 realisation factor is a calibration constant, not a German measurement — [Modo methodology](https://modoenergy.com/benchmarking/methodology/germany).
- Hirsch & Ziel's setup (10 MWh, 1/2/4 h, 1–2 cycles, MILP/DP, CVaR) is the closest German-market template for a forecast-to-dispatch experiment — [arXiv 2604.19580](https://arxiv.org/abs/2604.19580).

**Netherlands**
- TenneT exposes settlement (imbalance) prices and "Balance Delta High Res" via its developer API (registration required) — [developer.tennet.eu](https://developer.tennet.eu/); no Dutch €/MW/yr battery-revenue publication was retrieved.

### Inferences
- A German 1 MW/2 MWh C&I battery perfect-foresight DA-only bound can be computed directly from SMARD prices; with the 2024 spread of ~€130/MWh and 1.5 cycles/day the gross DA-only upper bound is on the order of 130 €/MWh × 2 MWh × 1.5 × 365 × 0.88 ≈ €125k/MW-yr before fees [estimate from cited spread; actual varies strongly by day].
- The practically relevant question for a startup is not "ML vs heuristic" on perfect-foresight, but what fraction of the 10–50% gap between perfect foresight and realistic MPC is recoverable; published evidence puts simple forecasters at ~80–90% capture for ≥2 h batteries, leaving a thin margin for ML.

### Gaps
- No enspired, Entrix, Flexpower, Montel or Aurora publications with €/MW/year for 2024–2026 could be retrieved (search budget); Modo index values are paywalled.
- No Portuguese BESS revenue estimate found; Seville study is Spain-only.
- No published German study quantifying MPC-with-forecast capture vs perfect foresight on EPEX DE 15-min prices (post-Oct-2025).
- Dutch imbalance-arbitrage revenue benchmarks: not found.

## Key Question 7: Three concrete experiment designs, tooling and cost

### Takeaway
All three experiments can be built on CC-BY or statutory-public data (SMARD/netztransparenz/ENTSO-E via SMARD, Open-Meteo Previous Runs, WPuQ, E-REDES/OMIE/ESIOS for Iberia) with a walk-forward, decision-time-only protocol; the data cost is roughly $100/month (Open-Meteo Professional) and compute is laptop-scale. The designs below are my specification [design], anchored to the cited constraints.

### Cited Findings (constraints that shape the designs)
- German day-ahead clears at 12:00 CET for next-day delivery (Hirsch & Ziel) — [arXiv 2604.19580](https://arxiv.org/abs/2604.19580).
- Final reBAP available only by the 20th working day of the following month; AEP-Schätzer at T+30 min; ID-AEP at D+1 — [Netztransparenz](https://www.netztransparenz.de/xspproxy/api/staticfiles/ntp-relaunch/dokumente/regelenergie/regelenergie%20(%C3%BCs)/rl-erlaeuterungen_ntp_20230710.pdf).
- Open-Meteo Previous Runs provides fixed-lead forecasts (day1..day7) since Jan 2024 for most models — [Previous Runs API](https://open-meteo.com/en/docs/previous-runs-api).
- Modul 3 schedules: HT/ST/NT by quarter and DSO, HT–NT spread 1.82–22.47 ct/kWh — [ZfK](https://www.zfk.de/energie/strom/variable-netzentgelte-14a-enwg-modul-3-dynamische-tarife); Modul 1 110–190 €/a; Modul 3 only with iMSys and >4.2 kW device — [Yello](https://www.yello.de/wissen/energiemarkt/14a-enwg-netzentgelt/).
- Measured home-storage efficiency: mean battery efficiency 95.7%, but system (inverter) losses dominate at part load (46% loss at 100 W for the worst system) — [HTW Inspektion 2025](https://solar.htw-berlin.de/wp-content/uploads/HTW-Stromspeicher-Inspektion-2025.pdf).
- Grid-scale assumptions used by an industry benchmark: 88% AC-AC RTE, 1.5 cycles/day, aFRR capacity bids clipped at 50 €/MW/h, SoC 50% at midnight — [Modo methodology](https://modoenergy.com/benchmarking/methodology/germany).
- Price-forecast baseline to beat: XGBoost rMAE ~0.57–0.61 for DE-LU over Jan 2025–Mar 2026 — [IAEE 487](https://app.iaee.org/abstract/abstract-487.pdf).
- Profit-based model ranking is gameable; use proper scoring rules alongside realised value — [arXiv 2604.19580](https://arxiv.org/abs/2604.19580).
- Energy-Charts rate limit 2 req/min (cache aggressively); SMARD bulk download is the licence-clean price source — [Energy-Charts](https://api.energy-charts.info/openapi.json), [SMARD](https://www.smard.de/home/datennutzung).

### Inferences — the three designs [design]

**Experiment 1 — Supplier/BRP short-term load (or PV) forecasting and imbalance cost reduction (DE balancing group; PT/ES variant)**
- Target: 15-min net load (or PV feed-in) of a synthetic balancing group built from WPuQ households (38 HH, CC BY 4.0) scaled with MaStR postcode counts; alternatively ENTSO-E/SMARD actual load for a bidding zone as a "large BRP" proxy.
- Decision interval and information: day-ahead forecast issued at 11:00 D-1 (inputs: Open-Meteo `previous_day1` weather, calendar, lagged load up to D-1 10:00); intraday re-forecast every hour with `previous_day0`/live-run proxies and lagged actuals up to T-1 h. Never use ERA5 or stitched historical-forecast data as a decision input for ≥2024 windows.
- Baselines: (a) seasonal-naive (same quarter-hour, same weekday last week); (b) standard-load-profile-style scaled profile; (c) statsforecast MSTL/ETS; (d) LightGBM/XGBoost with weather. Perfect-foresight bound: zero error.
- Walk-forward: train on rolling 365 days, re-fit weekly, test Jan 2024–Sep 2026 (hourly DA up to Sep 2025, then 15-min).
- Net-value formula (German balancing group): ImbalanceCost_t = e_t × (reBAP_t − P_ref,t) where e_t = forecast − actual (MWh per 15 min), P_ref = the price at which the position was procured (DA price for the DA forecast; ID-AEP for the intraday-corrected part). Report €/MWh of portfolio and € per MWh of absolute error, separately for quarter-hours with |NRV-Saldo| ≥ 500 MW (Module 2 floor). Intraday correction value = Σ_t (e_DA,t − e_ID,t) × (reBAP_t − IDAEP_t) minus trading fees [fee input needed from EPEX; not public here].
- Iberian variant: same with OMIE hourly/15-min DA price as P_ref and the Portuguese desvios price as settlement price (source to be confirmed; see Gaps); ESIOS indicators for Spain.
- Sensitivity: portfolio size (1 MW to 100 MW), weather model (ICON-D2 vs IFS), re-forecast cadence (1 h vs 4 h), post-Oct-2025 15-min regime vs hourly.
- Buyer claim supported: "€X/MWh lower imbalance cost per MWh supplied vs the supplier's current method, measured on public prices with a decision-time protocol."
- Limitations: synthetic portfolio; reBAP is DE-wide so no portfolio-specific price impact; aggregated WPuQ/E-REDES data understates individual-meter volatility.

**Experiment 2 — Residential 10 kWh battery dispatch on a German dynamic tariff with §14a Modul 3 vs self-consumption-first (PT indexed-tariff variant; 500-home portfolio extension)**
- Data: WPuQ household + heat-pump loads (10-s → 15-min), PVGIS seriescalc or SMARD-weighted PV profile, SMARD DE-LU DA prices (CC BY 4.0), one DSO's Modul 3 price sheet per region (e.g., Bayernwerk, LEW), Tibber-style tariff = (DA price + levies + taxes + grid fee) with a 5.99 €/month fee.
- Decision interval: 15 min; horizon 24–36 h; DA prices known from ~13:00 D-1 (so from 13:00 the horizon extends to 24:00 D+1); PV forecast from Open-Meteo `previous_day1` irradiance; load forecast from Experiment-1 model.
- Baselines: (a) self-consumption-first greedy; (b) rule "charge from grid in NT window when DA price < daily median", (c) perfect-foresight MILP (upper bound); candidate: rolling-horizon MILP (pyomo + HiGHS) with forecasts; optional ML residual on forecast.
- Physics: 10 kWh, 5 kW, usable DoD 90%, charge/discharge efficiency from HTW part-load curves (use ~0.92 one-way at ≥500 W, lower at 100 W), standby 10–20 W, degradation cost = LCOS proxy 6.0 ct/kWh throughput (BNS) as a sensitivity.
- Net-value formula: Saving = Σ_t [P_tariff,t × (g_base,t − g_opt,t)] − Σ_t [FIT × (f_base,t − f_opt,t)] − 12 × fee_dyn − SMGW/HEMS (≈120 €/a sensitivity) − deg_cost × throughput; with P_tariff,t = DA_t × (1+VAT) + grid_fee_tier(t) + levies/taxes; Modul 1 flat −110…−190 €/a and Modul 3 tier prices as scenario switches.
- Walk-forward: no training needed for MILP; forecasts re-fit monthly; evaluate 2024 and 2025 separately (HTW used 2024 prices; show robustness).
- Expected magnitude from the literature: 64 €/a mean with PV, 233 €/a without PV (HTW 2026); your result must be reported against those.
- PT variant: replace DA with OMIE PT price, grid tariff with ERSE 2026 bi/tri-hourly BTN access tariff from the Excel tables; indexed-tariff formula must be sourced (gap).
- 500-home portfolio extension: aggregate 500 bootstrapped WPuQ/HTW homes; introduce an aggregator fee (scenario 20–40% of gross savings [assumption]) and imbalance exposure by settling the portfolio's forecast-vs-actual deviation at reBAP (Experiment 1 engine).
- Buyer claim supported: "Our dispatcher captures Y% of the perfect-foresight saving and beats self-consumption-first by Z €/home-year under tariff T and DSO D."
- Limitations: no control-right or latency modelling; OEM inverter behaviour (SoC reserves, response time) unknown; Modul 3 schedules change yearly; levies/taxes change (document the exact 2025/2026 values used).

**Experiment 3 — 1 MW/2 MWh C&I battery in Germany: DA + ID + FCR/aFRR stacking vs rule-based dispatcher**
- Data: SMARD DA (hourly→15-min from 1 Oct 2025), ID-AEP and AEP-Schätzer (netztransparenz, D+1/T+30 min), FCR and aFRR capacity/energy tender results (regelleistung.net CSV via UI), reBAP for penalty modelling. Continuous intraday execution cannot be modelled from public data; use ID-AEP or IDA auction prices as a conservative proxy and state it.
- Decision cadence: D-1 08:00 FCR/aFRR capacity bids (4-h blocks) → D-1 12:00 DA → D-1 afternoon IDA → intraday re-optimisation every 15 min against ID-AEP proxy. Information set must exclude any price published after the decision time (final reBAP excluded entirely; only Schätzer at T+30 min).
- Baselines: (a) rule "DA two-cycle: charge 2 cheapest hours, discharge 2 dearest"; (b) FCR-only; (c) perfect-foresight MILP over all markets (upper bound); candidate: rolling MILP with statsforecast/LightGBM price forecasts and a probabilistic variant (quantile LightGBM → CVaR objective as in Hirsch & Ziel).
- Physics/constraints: 88% RTE, ≤1.5–2 cycles/day, SoC band 10–90% during FCR hours (symmetric reserve requires headroom), aFRR capacity price clipped at 50 €/MW/h, prequalification lead-time handled by committing capacity before DA.
- Net-value formula: Rev = Σ DA + Σ ID + Σ FCR_cap + Σ aFRR_cap + Σ aFRR_energy − exchange/clearing fees [input] − grid fees (assume 0 for pure storage per German exemption as scenario; add as sensitivity) − degradation (throughput × c_deg, c_deg scenario 20–60 €/MWh [assumption]) − imbalance penalties Σ |schedule − actual| × |reBAP − DA|. Report €/MW/yr and capture ratio = Rev_forecast / Rev_perfect.
- Walk-forward: monthly re-fit, evaluate 2024, 2025 and Oct 2025–Sep 2026 (15-min regime) separately.
- Expected ranges to compare against: Modo's 0.80 calibration; academic 50–90% capture (NYISO); DA spread ~€130/MWh (2024).
- Iberian equivalent would need: OMIE DA/IDA prices (available), ESIOS secondary/tertiary reserve prices (token API), Portuguese reserve/desvio prices (not found), and capacity-market rules (approved May 2026); no public per-asset data exists.
- Buyer claim supported: "On public prices, our stacked optimiser captures X% of perfect foresight vs Y% for a rule-based dispatcher, i.e., +€Z/MW/yr."
- Limitations: no order-book execution; FCR/aFRR acceptance assumed at clearing price; aFRR energy activation volumes not modelled per asset; results are price-taker and will degrade with fleet growth (Seville study shows spread compression at scale).

**Tooling and cost [design/estimate]**
- Python: `entsoe-py` (ENTSO-E RESTful API; token needed; terms unverified), direct CSV download for SMARD and netztransparenz, `openmeteo-requests` + `requests-cache` (Open-Meteo), `pandas`/`polars`, `statsforecast` (MSTL/ETS/ARIMA baselines), `lightgbm`/`xgboost` (benchmark used by Semmelmann), `pyomo` + `highspy` (HiGHS, free MILP), `ortools` as alternative, `epftoolbox` for LEAR/DNN price baselines — [epftoolbox paper](https://arxiv.org/abs/2008.08004).
- Data cost: Open-Meteo Professional ($99/month per the Open-Meteo newsletter; verify) for commercial use of historical/previous-runs APIs — [Open-Meteo pricing](https://open-meteo.com/en/pricing); ERA5/DWD/ECMWF open data/SMARD/E-REDES/WPuQ free with attribution; EPEX order-book data and Modo index paid (prices not retrieved).
- Compute [estimate]: a 15-min MILP with a 36-h horizon for one battery solves in well under a second with HiGHS; 1,000 rolling days × 3 experiments × 10 sensitivities is a few CPU-hours on a laptop; weather pulls for ~50 sites × 3 years at hourly resolution are within a 5M-call monthly budget.

### Gaps
- Exchange/clearing fees (EPEX), aggregator fee levels, degradation cost per MWh and German grid-fee treatment of storage are inputs that must be assumed or obtained from partners; none were verified from public pages in this research.
- Portuguese desvios price series and indexed-tariff formula remain unsourced; the PT variants of Experiments 1–2 cannot be finalised without them.
- ENTSO-E API licence for commercial redistribution unverified; use SMARD for any product-facing German price series until confirmed.
