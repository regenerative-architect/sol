# CIA Foreign Analysis & Peace Assurance OS — Edition 04

**Dated fact freeze:** October 14, 2026. **Author:** Foster + Navi / Planetary Restoration Archive. **Status:** independent, unofficial, public-source-only prototype. It is NOT a CIA tool, and is not connected to or endorsed by the CIA, FBI, Secret Service, DoD, State Department, BIS, UN or other institutions.

## Purpose

Comprehensive offline-reading and local analytical workspace for foreign-source assessment of the Russia–Ukraine conflict, security guarantees, contested ceasefire claims, procurement-ecosystem evidence, humane recovery, and dissenting explanations. Designed to resemble the *discipline* of objective intelligence analysis, not intelligence collection or operations. No targeting, private-person surveillance, covert action, agent recruitment, offensive cyber, disinformation, intrusive network access or actual interagency handoffs.

## Start

1. Extract `cia_peace_analysis_os_bundle.zip` and open `cia_peace_analysis_os/index.html` in a current browser.
2. Use responsive top search and sidebar; each of 15 module pages is a standalone `index.html` with static noscript reading index.
3. Research notes are stored in IndexedDB if permitted; otherwise they are transient memory-only. Export backups deliberately. Import is validated, previewed and collision-aware.
4. Optional HTTPS or `http://localhost` deployment: serve the entire directory with a static server (e.g. `python3 -m http.server 8000` from its parent). On supported origins the service worker precaches *only same-origin shell and source registry*. External sources, live current affairs and user-created notes are NOT service-worker offline assets.

## Layout

```text
cia_peace_analysis_os/
  index.html
  modules/{sitrep,doctrine,casebook,register,evidence,compliance,framework,cyber,humanitarian,ceasefire,metrics,premortem,nodes,governance}/index.html
  assets/{app.js,styles.css,icon.svg}
  data/{sources.json,actions.json,scope_matrix.json,handoff_schema_v1.json}
  service_worker.js; site.webmanifest
  SITREP.md; RUNBOOK.md; ANALYTIC_STANDARDS.md; README.md; TESTING.md; LICENSE
  tests/verify_structure.py
```

## Interoperability and privacy

`pra.reciprocal_public_handoff/v1` only. This edition exports `sender_node=cia_public_concept`, `handling=PUBLIC_ONLY`, `submitted=false`, `authenticity=UNSIGNED_LOCAL_DRAFT`. Imports accepted: this edition's schemaVersion-1 records, prior US Military and FBI schemaVersion-1 backups, previous USSS schemaVersion-1/2 leads, and single supported public handoff records. **Do not enter confidential records, classified information, U.S.-person data, informant data, troop locations, sensitive infrastructure, operational plans, passwords or private financial data.** Local storage is not encrypted and is not automatically synchronized across devices or file/hosted origins.

An actual partnership would require validated institution-controlled endpoints, recipient approval, legal authorities, authenticated signed exchange, access control, minimization and independent review; nothing of that kind is included. Non-governmental aid partners must not be turned into intelligence sources.

## Fact and uncertainty methods

Cite primary sources; distinguish VERIFIED FACT, OFFICIAL ALLEGATION, PARTY CLAIM, LEGAL FINDING, INFERENCE and UNKNOWN. Negative claims about intent require direct evidence. Branded-product origin does not prove knowing illicit export. CIA publicly states it is a foreign-intelligence analysis agency, not a policy-setting or law-enforcement body. ICD 203 supplies standards of objectivity, independence, uncertainty and alternatives. See `ANALYTIC_STANDARDS.md`.

## Licenses and attribution

The original application's source code is MIT licensed. Foster + Navi / Planetary Restoration Archive contributed this independent concept and implementation. Public agency/UN materials remain with their publishers and are only linked, not copied. No government seals or licenses of third-party code are implied.
