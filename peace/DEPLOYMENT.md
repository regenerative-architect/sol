# Deploy SOL Peace Commons v2.2 — EIE + Trystero default

1. **Backup first**: open the currently deployed master and export your progress through the JSON backup button. Keep it separately before replacing files.
2. Download the new ZIP and extract the **contents of `peace/`** to `https://regenerative-architect.github.io/sol/peace/`. Preserve all five sibling editions: `/usmc/`, `/usss/`, `/cia/`, `/fbi/`, `/un/`.
3. This edition uses `index.html` with embedded CSS and JavaScript; GitHub Pages can serve it as a static file without installing a framework. Keep `service_worker.js`, `site.webmanifest`, `icon.svg`, and `data/` in place for the optional hosted PWA and traceability.
4. On online HTTPS, Trystero public-room discovery is **enabled on launch** unless disabled in localStorage. This can expose network metadata, including IP addresses, to signaling infrastructure and other peers. The status and **Disconnect** button remain visible in the HUD. No content should leave the browser unless the user explicitly confirms sharing a public proposal.
5. Test a real peer session with two authorized browsers: both open the same HTTPS URL and allow external CDN/Nostr traffic; inspect peer counts, share a harmless sample public proposal manually, verify it appears as unverified in the other person's inbox; disconnect and confirm no further messages. Never use real confidential, person-specific or operational case material.
6. Test EIE offline by disconnecting your network **after the app is loaded**; EIE must still retrieve from the embedded archive and export JSON. Its sources are historical and may not be accessible offline when opened externally.
7. For persistence and PWA, confirm IndexedDB survives reload, backups round-trip safely, and the service worker's `sol-peace-master-shell-v5` cache is active on HTTPS. Browser privacy modes/storage quotas and service-worker update behavior vary.
8. `file://` has no service worker or automatic public peer discovery. Local reading and JSON fallback remain usable, subject to browser storage rules.

**Rollback**: restore your earlier `index.html` and matching static PWA assets from backup; keep IndexedDB intact unless you intentionally choose to reset it. The master backup schema remains version 1, now accepting an optional `eieNotes` array. Previously saved progress should remain recognizable.

This package is a public-interest research prototype, not official software or an authorized institutional channel. No deployment, peer handshake, institutional outreach, or external EIE action was performed by the build process.

## Upgrade to v2.3

Retain the existing directory structure and sibling edition pages. Replace the static master assets from this ZIP, preserving `usmc/`, `usss/`, `cia/`, `fbi/` and `un/` folders. The local research schema is unchanged (`pra.sol_peace_master`, version 1). Export an old JSON backup before deployment and restore only after checking it. The service worker uses `sol-peace-master-shell-v6` to replace the prior v5 shell. A first online visit is needed for any newly introduced asset to become available offline. Trystero requires online signaling and is not cached by the service worker.


## 2.4 guide upgrade

Replace the master `index.html` and `service_worker.js` and add `data/pathway_guides.json` and `data/pathway_catalog.json`. Keep the existing five sibling editions. If using the full ZIP, deploy the contents of its `peace/` directory to `/sol/peace/`. Export previous progress first. Guides use separate localStorage preferences and preserve the master IndexedDB v1 format. Updated static cache namespace is `sol-peace-master-shell-v7`; old v6 caches are deleted on service-worker activation. `file://` has no service worker or live multiplayer guarantee.


## 2.4 guide upgrade

Replace the master `index.html` and `service_worker.js` and add `data/pathway_guides.json` and `data/pathway_catalog.json`. Keep the existing five sibling editions. If using the full ZIP, deploy the contents of its `peace/` directory to `/sol/peace/`. Export previous progress first. Guides use separate localStorage preferences and preserve the master IndexedDB v1 format. Updated static cache namespace is `sol-peace-master-shell-v7`; old v6 caches are deleted on service-worker activation. `file://` has no service worker or live multiplayer guarantee.

## 2.5 Earth Intelligence minimized-icon upgrade

Back up local progress, replace `index.html` and `service_worker.js` from this bundle, and retain `data/` and all five research subdirectories. The EIE control shrinks to a globe icon after 1.7 seconds; select the icon to expand the unchanged research panel. The hosted cache changes to `sol-peace-master-shell-v8`; reload after service-worker activation. All other data formats are unchanged.
