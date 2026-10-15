# SOL Peace Commons 2.7 — Reliable Peer Discovery

- Fixed the misleading room-ready state; status now reflects actual `onPeerJoin` events.
- Corrected the join-error callback to Trystero's documented `joinRoom` third-argument form.
- Updated the dynamic-import version pin to Trystero 0.26.0 and added an alternate CDN load path.
- Introduced dual Nostr + MQTT discovery, per-transport diagnostics, error isolation and manual reconnect.
- Added an explicit peer round-trip data test, with success / timeout outcomes.
- Added optional session-only TURN configuration for networks that require relaying; **no TURN service or secret is bundled**.
- Preserved the 50×50-pixel EIE floating icon, five original editions, JSON data formats, local-first storage and explicit public-only sharing.
- Bumped the service-worker cache identifier to avoid leaving obsolete `index.html` shell assets in active caches.

**Known limitation:** Two genuine browsers on different internet networks were not available for an end-to-end WebRTC test here. Public relays, CDNs, and restrictive NAT combinations cannot be guaranteed without operating appropriate TURN/signaling infrastructure.
