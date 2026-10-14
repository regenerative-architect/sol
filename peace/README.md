# SOL Peace Commons — Master Coordination OS (Edition 06)

**Build date:** 2026-10-14 · **Version:** 1.0.0 · **Author:** Foster + Navi / Planetary Restoration Archive · **Status:** independent public-interest prototype. **Not operated by or affiliated with the U.S. Secret Service, FBI, CIA, U.S. military, United Nations or their staff.**

## Purpose

An accessible, optional-multiplayer, offline-first master `index.html` unifying **five existing public research portals** through an educational collaboration experience. This is a cross-disciplinary training and public-research layer, not a government command system or an intelligence platform.

| Existing node | URL supplied by project |
|---|---|
| U.S. Military edition (`usmc`) | https://regenerative-architect.github.io/sol/peace/usmc/ |
| U.S. Secret Service (`usss`) | https://regenerative-architect.github.io/sol/peace/usss/ |
| CIA (`cia`) | https://regenerative-architect.github.io/sol/peace/cia/ |
| FBI (`fbi`) | https://regenerative-architect.github.io/sol/peace/fbi/ |
| UN (`un`) | https://regenerative-architect.github.io/sol/peace/un/ |

**Live availability and deployed contents of the five URLs could not be verified from the current environment.** This master uses the exact URLs supplied by the user. It does not fetch or scrape them. A visit to an external URL requires network access.

## Fast start

1. Extract `sol_peace_master_bundle.zip` without changing folder layout.
2. **Offline local mode:** open `sol_peace_master/index.html` in a browser. Static reading, navigation, classes, quests, co-op drafting and JSON export work without hosting. IndexedDB behavior under `file://` depends on your browser. If IndexedDB is unavailable, the UI will explicitly indicate **memory only · export JSON**. To prevent losing work, export a backup regularly.
3. **Recommended hosted mode:** copy the contents into the GitHub repository's `/sol/peace/` directory, alongside the existing subfolders, so the master resolves at `https://regenerative-architect.github.io/sol/peace/`. Hosting on HTTPS enables service-worker shell caching and the best chance of working WebRTC. No deployment has been performed by this assistant.
4. Choose a class, complete a cited quest, unlock a skill and draft a co-op project with two or more represented domains.
5. Optional peer rooms: generate a long random invitation code, explicitly join, and share selected public proposals. Rooms require internet access. If peers do not connect, exchange public-only JSON files manually instead.

## File tree

```text
sol_peace_master/
├── index.html                      # ALL core HTML, CSS, app code and data; standalone
├── service_worker.js               # optional hosted same-origin shell cache
├── site.webmanifest                # optional hosted installability
├── icon.svg                        # original icon
├── data/
│   └── public_handoff_example.json  # public-only interoperability example
├── tests/
│   ├── smoke_browser.py            # isolated Chromium smoke tests
│   ├── verify_structure.py         # packaging/JS syntax/JSON integrity checks
│   └── app_syntax.mjs              # generated inline JS for Node syntax check
├── README.md
├── TESTING.md
├── DEPLOYMENT.md
├── ATTRIBUTIONS_AND_LICENSES.md
├── LICENSE
└── file_manifest_sha256.json        # package integrity, not authorship
```

## What is genuinely implemented

- Single route registry powers **10 visible modules**, deep links, breadcrumb and side navigation, plus a search route; an accessible mobile drawer closes on Escape.
- **8 opt-in classes** reflecting evidence, diplomacy, humanitarianism, civilian protection, finance integrity and reconstruction. Classes are learning preferences, never an assertion of real agency membership.
- **16 public-source quests**, 4 learning tiers, one-time local XP per completed quest, completion evidence gates (HTTPS citation + ≥25-character description) and reversible completions.
- **5 trait practices** and **15 progressive skill unlocks**, with prerequisite checking and earned points. These scores measure self-reported activity, not competence or moral worth.
- **Five co-op review gates per project** (evidence audit, civilian impact, lawful mandate, strongest dissent, independent metrics); local notes must cite an HTTPS public source. Peer-provided gate claims are never considered automatically verified.
- Co-op workshop stores proposals locally; each requires at least two institutional *research domains*. A reviewer can fork an incoming unverified public proposal without importing other participants' review approvals.
- Manual public-only JSON drafts follow `pra.reciprocal_public_handoff/v1` and support import of public sourced notes from previous Secret Service, FBI, CIA, U.S. military and UN local research formats.
- Quarantined/unverified inbox; explicit consent and validation for both full backup replacement and imported records; basic file size and record count limits.
- Structured local IndexedDB (when available); localStorage is used only for the small UI theme preference. No remote database, account, hidden telemetry or auto-mail.
- Consent-triggered Trystero `0.25.3` Nostr WebRTC module, plus optional experimental MQTT strategy. Trystero is not bundled: it is retrieved via `esm.sh` **only on user-initiated room join**, and this functionality is unavailable offline. The 0.25 action-object interface uses `room.makeAction('public-proposal-v1')`, `action.send(...)`, `action.onMessage`, `room.onPeerJoin` and `room.onPeerLeave`.
- Random invitation code via Web Crypto random bytes; aliases are not verified identities; peers may learn each other's network address through WebRTC. No promise of anonymity.
- SHA-256 local file hashing where WebCrypto is available on a secure origin; printed/JSON portable backups; light/dark mode, print styles, accessible labels, reduced-motion fallback.
- Optional PWA install using same-origin versioned shell service worker. **No service worker is available for `file://`.** It does not cache external institutional sites or Trystero CDN modules, and does not ensure they work offline.

## Public handoff contract

`data/public_handoff_example.json` illustrates the exact public-only v1 schema used in existing prototypes. The master can add optional `collaborating_nodes` and `review_gates` to the `lead` object. Earlier editions generally ignore unknown extra fields; formal cross-edition acceptance of these extensions is not guaranteed. Handoff files are **unsigned, unsubmitted local drafts**, require explicit user download/import, and cannot establish recipient acknowledgement. No automatic peer-to-agency connection exists.

### Threat and privacy boundaries

1. Do not enter private-person identifiers, contact details, confidential case records, classified material, precise real-time sensitive sites, targeting data or other operational military information.
2. Peer rooms have no verified membership or authorization. Any peer can send misleading claims; their proposals are put into an **UNVERIFIED** review queue. The app **never automatically awards XP or merges peer opinions as facts**.
3. When joined, Trystero Nostr/MQTT signaling relies on third-party discovery infrastructure. WebRTC browser-to-browser channels provide transport encryption; anonymity, data sovereignty on the network path and authorization are not guaranteed. Use long room codes and share out of band.
4. Manual exports are local downloads, not security signatures. SHA-256 checks byte integrity, not authorship or accuracy.
5. Proposal co-op review gates are local self-attestations. They are not evidence of real peacebuilding outcomes.

## Attributions and modifications

See `ATTRIBUTIONS_AND_LICENSES.md`. Original code is MIT-licensed. Trystero is MIT-licensed (copyright belongs to its maintainers) and is referenced by the package loader rather than redistributed here. The external agency-themed sites are linked, not copied into the bundle.

## Next development milestones

A deployed-origin persistence/SW test, actual two-device Trystero handshake, authenticated peer invitations (without implying agency identity), schema-migration regression tests, community-led accessible translations and optional end-to-end signed public review records—each subject to independent security/legal review. These are **future tasks, not features claimed as working**.
