# Architecture and extension contract — EIE + Trystero v2.2

## File tree

```text
peace/
├─ index.html                       # Complete master shell, CSS, logic, embedded dated registry
├─ service_worker.js                # HTTPS-only, versioned static-resource cache
├─ site.webmanifest, icon.svg
├─ data/
│  ├─ public_handoff_example.json   # Prior interoperable handoff
│  └─ integrated_public_records.json# Audit copy of exact embedded public registry
├─ usmc/, usss/, cia/, fbi/, un/     # FULL retained editions, each with module pages and assets
├─ tests/                           # Regression + new integration tests
├─ README.md, GUIDED_PLAYBOOK.md, ARCHITECTURE.md
├─ DEPLOYMENT.md, TESTING.md, ATTRIBUTIONS_AND_LICENSES.md
└─ file_manifest_sha256.json
```

## Primary user journey (v2.1)

`renderFlow()` is now the default overview route. It hosts an introductory card followed by a four-step learning journey inside `#flowScene`. `flowSetStep()` updates only this panel, preserving the current page and original user state. All steps are optional; original advanced routes still use the shared router. The left navigation becomes an on-demand drawer on the home screen and stays available on advanced routes. Three low-friction changes preserve backward compatibility: existing IndexedDB schema, original quest XP accounting, and unsigned public handoff schema. Reduced-motion preferences are respected.

## Shared route registry

`ROUTES` in the master drives main navigation, breadcrumbs and client-side search. New `atlas` and `campaign` views use the same route system as the existing `overview`, `quests`, `skills`, `workshop`, `commons`, `vault` and `help` views. Unknown hashes revert to the overview.

## Public archive model

`ARCHIVE = {usmc:{routes, sources, cases, actions, checks}, ...}` is injected into the master from the supplied sub-edition JavaScript registries. The USSS edition stores `interventions` rather than `actions`; its values are merged when displaying interventions. Source citations, event dates and gaps remain visible. `data/integrated_public_records.json` provides a structured mirror for review by other tools.

## Save/portability model

`pra.sol_peace_master` backup v1 remains the live character/project state model **to preserve compatibility** with the previous master. Public handoffs remain `pra.reciprocal_public_handoff/v1`, unsigned, marked `PUBLIC_ONLY`, and require explicit export. Peer records enter `inbox` pending independent review, never the verified ledger. Class/quest/skill/project state is local IndexedDB, with memory-only fallback. Small theme/motion/journey preference values use localStorage. There is no hidden remote sync.

## Multiplayer (v2.1 historical behavior; superseded below)

Trystero 0.25.3 is dynamically imported only by a user-approved Join action; no automatic peer discovery. Long randomly generated room codes are invitations, **not** credentials or identity proof. No backend is bundled and no guarantee of two-device connectivity is made. Future authentication should rely on reviewed digital signatures, never on unverified room aliases or public-service logos.

## Security and legal boundary

All incoming public-source links must be HTTPS. Imported JSON is schema and length validated. Dynamic display strings are HTML-escaped; user content is not executed. No agency identity verification or privileged capability exists. New modules should add their IDs, domain, source, dates, confidence, lawful mandate, non-sensitive public data, capability constraints, initialization and failure fallback. Do not let optional integrations contaminate independent offline work. External AI or APIs need clear opt-in, explicit endpoint configuration and network disclosure.

## Verification pipeline

Physical/source fact → manufacturer/product identity → commercial transfer → end-use linkage → proof of knowing wrongdoing. Failure to verify one gate must not automatically turn it into a confirmed claim. A SHA-256 hash verifies equality of bytes; it does not prove authorship or authenticity.

## v2.2 extension: default visible Trystero and EIE

The preceding v2.1 descriptions of **optional peer discovery** are superseded by this section and `PEER_RUNBOOK.md`: user-requested public-room discovery starts automatically on online HTTP(S) pages unless disabled. A visible HUD control disconnects and disables future auto-join; manual invite rooms remain possible. No application data is sent upon connection. The selected public proposal payload omits private gate notes. Incoming proposals are rate-limited and quarantined.

`renderHud()` now contains an embedded `#earthEngine` disclosure panel. `eieAnalyze()` locally retrieves over the embedded public archive, returning sources, a historical intervention concept, alternative hypotheses, explicit uncertainty, next verification steps, and private save/export actions. It is not an AI model or external actor. `st.eieNotes` is the only added optional property in the preserved `pra.sol_peace_master` version 1 schema. The `pra.reciprocal_public_handoff/v1` transfer contract is unchanged. Public source data is frozen; no dynamic new factual findings are inferred from model overlap scores.

PWA cache name v5 invalidates the old public shell cache, while leaving the local database intact. No external CDN, peer traffic or private data is cached. Automatic connections are unavailable on file URLs and offline, with local EIE and manual JSON fallback retained.
