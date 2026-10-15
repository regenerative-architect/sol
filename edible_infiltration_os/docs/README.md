# Global Fruit-Grafting & Edible Cities Archive OS

**Version:** 1.0.0 · **Date:** 14 October 2026 · **Credits:** Foster + Navi / Planetary Restoration Archive

A working, source-linked, offline-capable static educational archive. Includes 42 city-specific `index.html` briefs, a conservative fruit-tree graft-pair explorer, a botanical field guide, a local pilot planner, policy safeguards, voluntary Trystero peer notes, evidence, and a self-reported skill tree.

## Open it

- **Immediately / offline (`file://`):** Unzip and double-click the top-level `index.html`. Follow relative links between pages. Search, compatibility, local planner, skill progression, import and export work in a modern browser if browser storage is allowed. Browser policies may restrict IndexedDB under `file://`; code falls back to localStorage, and will warn if storage is unavailable. No network is required for the core UI.
- **Hosted (`https://`):** Upload the **entire extracted folder tree** to a static host root (or into a dedicated subfolder). Serve under HTTPS. `sw.js` installs a same-origin service worker and precaches the site. The first successful load must complete online before the app is genuinely offline-ready in that browser; installation may fail if hosting misconfigures MIME types or permissions. Avoid changing relative directory structure.
- **Optional local test server:** Run `python -m http.server 8000` from the extracted folder, then visit `http://localhost:8000/`. Service workers work on localhost; open in two tabs to check persistent data handling.

## Interlinked page tree

```text
index.html
compatibility/index.html
cities/index.html
cities/<42_city_slugs>/index.html
field-guide/index.html
planner/index.html
commons/index.html
governance/index.html
academy/index.html
research/index.html
assets/styles.css
assets/data.js
assets/core.js
assets/favicon.svg
manifest.webmanifest
sw.js
LICENSE
docs/README.md
docs/data_schema.json
```

No build pipeline or account is required. Each city-specific page contains meaningful, independently readable HTML content and links to the shared engine and policy modules.

## Domain scope / important limits

- Grafting is **not** universally possible across tree species. An apple will not reliably graft onto maple, pine or oak; cherry is not generally a rootstock for peach or plum. The pairing direction (existing host *to* scion) matters. Pyrus onto quince and many Prunus combinations are cultivar-specific. Always confirm with local horticultural expertise before grafting.
- All city briefs are **illustrative feasibility hypotheses**, not verified species inventories, food-insecurity rankings, municipal legal opinions or proof that public trees may be grafted. Mature canopy trees require professional assessment, and modifying trees without owner consent is prohibited by this archive's safeguards.
- A graft can remain initially alive and fail years later. Biological compatibility is not sufficient evidence for long-term safety, food quality or net ecological benefit.
- Urban soil, road dust, pesticide history, fruit fall, access, community consent, maintenance and irrigation must be addressed before eating or distributing fruit.
- Importing live scionwood across borders is regulated. Source clean, certified, locally permitted scionwood.

## Offline and local-data architecture

- Shared shell and all route navigation: build-time semantic HTML and ordinary relative anchors; JavaScript enhances search and modules.
- Botanical dataset: static `assets/data.js` (no remote data retrieval). To update, rebuild/revise the file and cite your sources. Change schema/version carefully when adding compatibility codes.
- Project records: IndexedDB `edible_grafting_os_v1`, object store `projects` keyed by `id`; fallback localStorage `eg_os_projects_fallback_v1` if IDB is unavailable. Storage is local to that browser/origin and not synced.
- Theme and milestones: localStorage. Skill XP is intentionally self-reported and not validation of safe practice.
- Backup: project planner → Export JSON / Import JSON; schema version 1; imported project fields validated and duplicate IDs upserted after explicit confirmation. Exports also include milestones.
- Service worker: *same-origin only*. Versioned precache of 51 HTML pages and support assets. Installation must complete on an eligible HTTPS/localhost origin to use cache offline. The `file://` archive does **not** rely on a service worker.

## Peer-to-peer notes (optional)

The commons uses the current documented Trystero action API, with Nostr public relay signaling; the explicit Connect action dynamically imports `https://esm.sh/trystero@0.26.0`. Runtime module loading was **not verified here** because this build environment has no outbound network. The application gives an error and retains all offline tools if the CDN, relays, ICE negotiation or cross-origin modules fail. Users enter a room code (6–64 alphanumeric, `_`, `-`) and voluntarily send notes. No automatic broadcast, hidden IPFS upload or persistence. Connected peers may learn network identifiers; rooms are **not** authenticated identity groups, and the decentralized transport has **no moderation guarantees**. Please do not transmit people's identity, precise private addresses or sensitive tree sites.

Optional hardening before public rollout: bundle an audited permitted MIT-licensed Trystero version locally (and include its license), sign releases, pin CDN integrity where technically feasible, add rate limits/authentication/abuse controls, and consider your own signaling infrastructure and TURN if real deployment justifies it.

## Quality and tests

Static integrity tests check all relative links and referenced local assets. JS syntax and smoke tests can be run as part of verification. Do not infer that live P2P or field grafts have been validated by those checks. Accessibility target is WCAG 2.2 AA, with keyboard support, focus outlines, meaningful headings, reduced motion and print rules; this is a best-effort implementation, not an independent accessibility audit.

## Zero-harm / anti-inversion

Any request to use the system for unauthorized tree tampering, ecological introduction without approvals, covert profiling or extraction of sensitive site or participant data falls outside its permitted field protocols. Record outcomes transparently (including failure); consent and living canopy outrank engagement scores or first-mover novelty.

## Credits and licensing

Original OS code, data summaries and illustrations: MIT License, © 2026 Foster + Navi / Planetary Restoration Archive. Research is linked and paraphrased; source works retain their original licenses/copyright. Trystero is by Dan Motzenbecker and contributors, MIT-licensed, with external source available at https://github.com/dmotz/trystero. Research anchors are listed inside `research/index.html` and `assets/data.js`.
