# Architecture and extension contract

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

## Shared route registry

`ROUTES` in the master drives main navigation, breadcrumbs and client-side search. New `atlas` and `campaign` views use the same route system as the existing `overview`, `quests`, `skills`, `workshop`, `commons`, `vault` and `help` views. Unknown hashes revert to the overview.

## Public archive model

`ARCHIVE = {usmc:{routes, sources, cases, actions, checks}, ...}` is injected into the master from the supplied sub-edition JavaScript registries. The USSS edition stores `interventions` rather than `actions`; its values are merged when displaying interventions. Source citations, event dates and gaps remain visible. `data/integrated_public_records.json` provides a structured mirror for review by other tools.

## Save/portability model

`pra.sol_peace_master` backup v1 remains the live character/project state model **to preserve compatibility** with the previous master. Public handoffs remain `pra.reciprocal_public_handoff/v1`, unsigned, marked `PUBLIC_ONLY`, and require explicit export. Peer records enter `inbox` pending independent review, never the verified ledger. Class/quest/skill/project state is local IndexedDB, with memory-only fallback. Small theme/motion/journey preference values use localStorage. There is no hidden remote sync.

## Multiplayer, optional

Trystero 0.25.3 is dynamically imported only by a user-approved Join action; no automatic peer discovery. Long randomly generated room codes are invitations, **not** credentials or identity proof. No backend is bundled and no guarantee of two-device connectivity is made. Future authentication should rely on reviewed digital signatures, never on unverified room aliases or public-service logos.

## Security and legal boundary

All incoming public-source links must be HTTPS. Imported JSON is schema and length validated. Dynamic display strings are HTML-escaped; user content is not executed. No agency identity verification or privileged capability exists. New modules should add their IDs, domain, source, dates, confidence, lawful mandate, non-sensitive public data, capability constraints, initialization and failure fallback. Do not let optional integrations contaminate independent offline work. External AI or APIs need clear opt-in, explicit endpoint configuration and network disclosure.

## Verification pipeline

Physical/source fact → manufacturer/product identity → commercial transfer → end-use linkage → proof of knowing wrongdoing. Failure to verify one gate must not automatically turn it into a confirmed claim. A SHA-256 hash verifies equality of bytes; it does not prove authorship or authenticity.
