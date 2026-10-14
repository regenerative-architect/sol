# U.S. Military Peace & Civilian Protection Research OS — Edition 03

**Fact freeze:** October 14, 2026. **Publisher/attribution:** Foster + Navi / Planetary Restoration Archive. **Status:** independent, unofficial public-interest prototype; not endorsed by, connected to or authorized by the U.S. military, Department of Defense, UN, FBI, CIA or Secret Service.

## Mission and safety

Non-tactical, nonviolent, offline-capable workspace for public evidence, civilian-harm mitigation policy, lawful assistance/end-use transparency, ceasefire verification concepts, humanitarian protection, resilience and reconstruction. **No military targeting, troop tracking, operational maps, surveillance, offensive cyber, classified data handling, intelligence collection or automatic enforcement.** Live interoperability nodes are not present. Humanitarian organizations retain neutral mandates.

## Quick start

Extract the ZIP, then open `us_military_peace_os/index.html` directly. 15 separate index.html files are available in modules. All have no-JavaScript reading fallback. Vanilla HTML/CSS/JS, no external dependencies and no login.

Optional hosted PWA: host the folder on HTTPS or localhost with e.g. `python3 -m http.server 8000` from its parent, then open `http://localhost:8000/us_military_peace_os/`. The service worker precaches the same-origin 15-page shell and JSON reference files; official external source pages and dynamic material are **not** offline. File URL sessions cannot register service workers and may restrict local persistence. Hosted and file origins do not share data automatically.

## Folder tree

```text
us_military_peace_os/
  index.html
  modules/{sitrep,doctrine,casebook,register,evidence,compliance,framework,cyber,humanitarian,ceasefire,metrics,premortem,nodes,governance}/index.html
  assets/{app.js,styles.css,icon.svg}
  data/{sources.json,actions.json,scope_matrix.json,handoff_schema_v1.json}
  service_worker.js; site.webmanifest
  LICENSE; README.md; TESTING.md; tests/verify_structure.py
```

## UX and data sovereignty

Canonical route registry generates header navigation, sidebar and breadcrumb; mobile drawer uses Escape and focus trap, skip link, contrast styles, reduced motion, page search, printing and dark/light. Public-source notes can be saved, searched, revised and deleted in IndexedDB where available (memory fallback if unavailable). Encrypted storage **is not provided**. Up to 200 local notes. Import accepts military local backup v1, FBI local backup v1, predecessor Secret Service backup v1/v2, and compatible v1 single public handoff; previews collision options. Validated source URLs must be HTTPS. JSON backup and manual handoff are local downloads; they are not sent. SHA-256 is local file fingerprinting when Web Crypto is supported, not a provenance signature. All input is escaped prior to display. No analytics, telemetry, network sync or remote fetches.

## Interaction restrictions

No sensitive information of any kind. Do not enter classified/controlled materials, operational plans, unpublicized force positions, protected refugee data, credentials, informants or private financial records. Files selected for hash are only read in memory; digest may be attached as metadata to public notes. We do not claim legal or official chain of custody.

## Interoperability

`pra.reciprocal_public_handoff/v1` with `sender_node='us_military_concept'`, `handling='PUBLIC_ONLY'`, `submitted=false`, and no authentication. Recipient suggestions include USSS, FBI, CIA, UN, State, and BIS. The future CIA edition is **not built by this bundle**; no agency has authenticated, received or consented to data. Real integrations require legal authorization, dedicated classification boundaries, verified digital signatures, agency endpoints, data minimization, access controls and formal human approval.

## Governance and evidence caveats

Fact, party claim, legal finding, inference and unknown remain distinct. UN August 2026 reported at least 372 killed and 2,349 injured—verified minimums in that publication, not live or immutable totals. The 2022 DoD CHMR action plan and 2023 DoDI 3000.17 are publicly documented policies; confirm current revision before official application. All intervention plans and monitoring protocols are **proposals**, not actions taken.

## Attribution & licensing

Original software MIT license. Original concept and implementation: Foster + Navi / Planetary Restoration Archive. Architectural continuity with USSS/FBI earlier prototypes; original government and UN material linked by source. No proprietary source code or official seals included.
