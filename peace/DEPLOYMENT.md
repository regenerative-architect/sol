# Deployment and offline matrix — Guided Constellation v1.1 — Guided Constellation v1.1

1. Place all files in `/sol/peace/` in the GitHub Pages source repository. Preserve the sibling `usmc/`, `usss/`, `cia/`, `fbi/` and `un/` directories. Your desired master route is `https://regenerative-architect.github.io/sol/peace/`.
2. Commit/publish the files; do **not** publish local JSON backups containing user notes. The demo handoff contains only illustrative public information.
3. Load the HTTPS master, check that all five portal links work, verify page navigation and mobile menu, and load once online for service-worker shell precaching.
4. Test `#/commons` peer connection with **two browsers/devices** that share a randomly generated room code. Confirm room presence and explicit proposal transfer. A Trystero relay/network or browser policy may prevent connections; avoid claiming peer transfer success until independently observed.
5. Export backup, reload, import back, and check project gates. Test offline after the shell is cached in a controlled browser. External research pages and remote dependencies do not magically become available offline.

| Feature | Local `file://` | Hosted HTTPS |
|---|---|---|
| Static routes, quest data, skill trees | Yes, self-contained | Yes |
| IndexedDB structured state | Browser-dependent; labeled fallback | Generally yes, subject to browser/storage policy |
| JSON import and export | Browser permitting file inputs/downloads | Yes |
| SHA-256 local file hashing | Depends on secure-context availability | Yes with WebCrypto |
| Hosted service-worker cache | **No** | Yes after successful shell installation |
| Nostr Trystero 0.25.3 | Network and origin dependent; not guaranteed | Available if CDN, signaling and WebRTC succeed |
| Offline peer-to-peer cross-device sync | **No** | **No** without active connectivity |
| Manual offline exchange using JSON files | Yes | Yes |
| Five external sites | Only if online | Only if online |

## Upgrade / migration policy

The master exports `pra.sol_peace_master` version 1 state. Keep a JSON backup before changing the application; future schema migrations should check version, validate constraints, preserve backup recovery and provide explicit conflict resolution. The current code has no cross-device auto-merge or signed identity.

## Zero-harm / anti-inversion

Design efforts aim to reduce civilian risk, not increase coercive reach. The app has no target mapping, no covert influence, no surveillance, no private case-management, no official institutional access and no automated dispatch. Public research must remain contestable and reversible.

## Upgrading an existing master

1. **Export the existing master local backup first.**
2. Replace the master root `index.html`, `service_worker.js`, `site.webmanifest`, documentation and public assets. Leave the five institutional edition directories untouched.
3. The service-worker cache is incremented to `sol-peace-master-shell-v2`, allowing the new shell to replace the prior cache on a secure hosted origin. Service-worker update propagation should be verified on each device.
4. Open the master; the existing `pra.sol_peace_master` v1 IndexedDB record is retained. New journey and optional motion preferences use localStorage only.
5. Use the HUD `Guided flow` and the five steps to test onboarding, quest proof, inline gate reviews, project creation and JSON export.
6. Test hosted storage persistence, real two-device peer negotiation and shell offline caching before distributing as a production-capable service.

## Upgrading an existing master

1. **Export the existing master local backup first.**
2. Replace the master root `index.html`, `service_worker.js`, `site.webmanifest`, documentation and public assets. Leave the five institutional edition directories untouched.
3. The service-worker cache is incremented to `sol-peace-master-shell-v2`, allowing the new shell to replace the prior cache on a secure hosted origin. Service-worker update propagation should be verified on each device.
4. Open the master; the existing `pra.sol_peace_master` v1 IndexedDB record is retained. New journey and optional motion preferences use localStorage only.
5. Use the HUD `Guided flow` and the five steps to test onboarding, quest proof, inline gate reviews, project creation and JSON export.
6. Test hosted storage persistence, real two-device peer negotiation and shell offline caching before distributing as a production-capable service.
