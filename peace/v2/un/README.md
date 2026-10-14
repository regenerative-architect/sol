# UN Peace Assurance & Civilian Protection Commons — Edition 05

**Version:** 2026-10-14 · **Attribution:** Foster + Navi / Planetary Restoration Archive · **License:** MIT for original code. **Not affiliated with or endorsed by the UN** or any government, court, humanitarian actor, the ICRC or OSCE.

## What it is
A 15-page standalone HTML/vanilla JavaScript/CSS public-source research OS connecting civilian protection, international law, humanitarian access, proposed ceasefire monitoring, diplomatic incentives, recovery and evidence review. Contains a dated SITREP, nine phased action concepts, evidence/uncertainty ledger, source registry, 24-month premortem, local backup/import and five-gate legal safeguards. No operational field capability.

## Quick start
1. Extract ZIP keeping folder layout; open `un_peace_assurance_os/index.html`. Each of 15 modules has its own `index.html` and a static noscript navigation index.
2. Use top search, theme switch, print, and sidebar. Add only public-source notes and HTTPS references in Local Evidence Ledger.
3. Export a JSON backup before resets; import after review and choose conflict handling. Storage is IndexedDB where available, or explicitly labeled memory-only. No automatic synchronization.
4. Online links open original sources on demand; linked reports are NOT bundled or available offline automatically.
5. Optional localhost/HTTPS PWA: from parent folder run `python3 -m http.server 8000`, visit `http://localhost:8000/un_peace_assurance_os/`. Service worker caches only same-origin static shell, not online articles or local record database. Service workers do not work from file://.

## Structure
```text
un_peace_assurance_os/
  index.html; modules/{sitrep,doctrine,casebook,register,evidence,compliance,framework,cyber,humanitarian,ceasefire,metrics,premortem,nodes,governance}/index.html
  assets/{app.js,styles.css,icon.svg}
  data/{sources.json,actions.json,scope_matrix.json,handoff_schema_v1.json}
  service_worker.js; site.webmanifest
  SITREP.md; RUNBOOK.md; MANDATE_AND_SAFEGUARDS.md; README.md; TESTING.md; LICENSE
  file_manifest_sha256.json; tests/verify_structure.py
```

## Interoperability
Supports `pra.reciprocal_public_handoff/v1`. Import from this and prior Secret Service, FBI, U.S. Military and CIA public-note backups via existing normalized constraints. Handoffs are **unsigned, unsubmitted, manual local drafts** with no recipient delivery. No live integrations or institutional consent implied. The ICRC and OSCE remain institutionally distinct, not UN subordinate nodes.

## Safeguards and limits
No private records, confidential testimonies, military targeting, offensive cyber, surveillance, influence operations, covert/forced contact, humanitarian data harvesting or mission deployment. Be cautious with public document sensitivity and remove precise real-time aid or energy vulnerabilities.

License-respecting concepts: UN Charter, UN Peacekeeping, OCHA, OHCHR, ICRC and other external references are linked, not reproduced wholesale; rights belong to their publishers. Prior prototype code from this project's earlier editions was adapted and original code is MIT licensed.
