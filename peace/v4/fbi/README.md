# FBI Financial Integrity & Peace-Support Research OS — Edition 02

**Date of public-source snapshot:** 2026-10-14. **Author/credit:** Foster + Navi / Planetary Restoration Archive. **Status:** unofficial, public-interest prototype; no FBI, DOJ, or other agency affiliation, credential, authorization, or connection.

## Purpose and boundary

An interoperable, nonviolent public-source research system for lawfully evaluating illegitimate procurement and sanctions evasion related to the Russia–Ukraine war while avoiding unsupported attribution. The FBI module addresses domestic national-security and federal criminal investigations *conceptually*, not as an official FBI tool. Export controls: BIS/OEE; cross-border cases: HSI; prosecution: DOJ; sanctions and financial guidance: Treasury; USSS: distinct financial protection/financial-fraud scope. CIA, military and UN are future governed nodes only. No offensive cyber, intelligence collection, operational targeting, nonconsensual surveillance, enforcement actions, or classified information tools.

## Launch instructions

- **Extract complete ZIP.** Open `fbi_integrity_os/index.html` directly (`file://`) for a zero-dependency offline local reader. All 11 pages are independently loadable and have no-JavaScript source summaries. IndexedDB may not persist under some file/browser privacy policies; app visibly falls back to in-memory records.
- **Optional hosted PWA:** serve the extracted folder on HTTPS or localhost. Example from its parent: `python3 -m http.server 8000`; open `http://localhost:8000/fbi_integrity_os/`. A same-origin service worker precaches the local shell and records a version. It does not make external DOJ/FBI/BIS/ICRC websites available offline. In-hosted browser storage is per-origin and does not automatically migrate from file:// origins.
- **No install/build commands or accounts are required.** Embedded content, script, CSS and local data are self-contained; external links only open if clicked.

## Directory map

```text
fbi_integrity_os/
  index.html                             Shared registry/home
  modules/{sitrep,casebook,register,evidence,compliance,framework,cyber,humanitarian,nodes,governance}/index.html
  assets/{app.js,styles.css,icon.svg}    Vanilla JS, responsive accessible CSS, original icon
  data/{sources.json,handoff_schema_v1.json,scope_matrix.json}
  service_worker.js                      Optional static precache for localhost/HTTPS
  site.webmanifest
  LICENSE                                MIT license for original sample software
  README.md; TESTING.md
```

## User controls

- Shared top and sidebar, derived from one `ROUTES` registry; mobile drawer with Escape and Tab focus cycling, active state, skip link, theme button (including on mobile), page search, print CSS, high-contrast focus and reduced-motion support.
- Research register: add, update, delete, search/filter up to 200 public-source notes in IndexedDB (memory-only fallback). Fields explicitly preserve alternate explanations. No actual confidential case data.
- Local SHA-256 fingerprints are calculated for selected files up to 25 MiB when Web Crypto is available. Files are never uploaded or retained. A hash proves neither authenticity nor evidentiary chain-of-custody.
- Local backup/export/import uses JSON schemaVersion 1. Import accepts this edition, prior USSS `pra_financial_integrity_os` backups (v1/v2) and a single `pra.reciprocal_public_handoff` v1 record, with preview and collision choices. No automatic device or agency sync.
- Optional progress HUD reflects only checklist completion; no points, XP or external tracking.
- Sample dated SITREP, public DOJ casebook, legal/provenance gates, corporate compliance guidance, lawful implementation register, defensive cyber, humanitarian safeguards and reciprocal draft nodes.

## Security and privacy

All data input is displayed with HTML escaping and URLs must be HTTPS with no embedded credentials. No external dependencies, analytics, network calls, telemetry or covert export. Official source links are opened only through deliberate clicks. Do not enter confidential SAR information, personal dossiers, classified or protected files, credentials, private financial records or nonpublic investigative information. Browser IndexedDB is **not encrypted by this application** and should not be treated as secure storage. Browser local history is editable; it is not forensic logging. Exports remain local until the user explicitly transfers them.

`pra.reciprocal_public_handoff/v1` is reused from the earlier USSS prototype, with `sender_node="fbi_concept"` and `submitted=false`. User-selected JSON exports are unsigned public-only drafts. Authentic cross-agency transfer requires organizational approval, proper encryption, data classification, mutually authenticated endpoints, purpose limits, logs, human rights review, formal agreements and actual receipt verification. None are available.

## Fact policy and zero-harm / anti-inversion

Treat court adjudications, guilty pleas, sanctions designations, party allegations, third-party reporting and inference as different classes. Verify source effective dates and distinguish manufacturer, exporter, importer and knowing illicit facilitator. A component brand or a paid transaction alone proves no intent. Preserve legitimate Ukrainian self-defense, humanitarian exceptions, due process and civilian protection. Never repurpose this system into targeting, covert surveillance or deception. If material legal scope or evidence uncertainty arises, pause escalation and consult qualified professionals.

## Attribution and license

Original concepts, editorial synthesis and implementation: Foster + Navi / Planetary Restoration Archive. The code is distributed under MIT; third-party research is cited by URL and not copied as proprietary code. The app is not officially approved or sponsored by any government agency.

## Validation and deployment protections

Run `python3 tests/verify_structure.py` for a standard-library static integrity test. The optional browser validation uses an isolated Chromium harness and does not imply access to any government systems. See `TESTING.md` for the exact performed checks and limitations. For a hosted deployment, server operators should consider HTTPS, `X-Content-Type-Options: nosniff`, suitable CSP, strict referrer policy, secure update reviews and regular backups. No server is required for a local file launch. Local browser data is origin-scoped and does not migrate automatically to a new host.
