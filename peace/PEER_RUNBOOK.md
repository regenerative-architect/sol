> **IMPORTANT 2.7 update:** For current dual-strategy discovery and TURN troubleshooting, follow [PEER_CONNECTION_GUIDE_v2_7.md](PEER_CONNECTION_GUIDE_v2_7.md). This older runbook describes the original network implementation.

# Trystero-default peer collaboration — operating runbook

## What “default” means

On an **online HTTP(S) page**, the app automatically attempts to import the pinned Trystero 0.25.3 Nostr strategy and join the **open** room `sol-peace-public-commons-2026`, unless this browser previously disabled automatic joining. This is the user's requested default. It is **not** a private/authenticated room, a persistent backend, or evidence that someone is connected. `0 peers` means no confirmed connected remote peers. Public Nostr relays are used to discover peers; the actual channel uses WebRTC. The public lobby does **not** set a misleading shared-secret password.

Peer software loads from `https://esm.sh/trystero@0.25.3` at runtime. Alternative MQTT discovery (manual only) uses `https://esm.sh/@trystero-p2p/mqtt@0.25.3`. Successful import requires an internet connection and CDN/relay availability. Browser/network conditions may prevent WebRTC; no TURN service is configured.

## Privacy disclosures

**The site will attempt peer discovery on visit when enabled.** The HUD visibly displays its status and disconnect button. Discovery exposes connection metadata to relays and can expose participant IP addresses to other peers. Do not assume room IDs, aliases or IP addresses identify real organizations. No personal account is required.

The application does **not** send any local notes, EIE questions, backups, quest results, institutional casebook records or profile names automatically. Public proposal sharing requires a deliberate click and confirmation; the shared payload strips private review-gate notes. Peers may send untrusted public proposals to the local review queue, capped at three per peer per minute. None is auto-verified.

## User controls

- **Disconnect** in the HUD stops peer participation and saves `sol_peer_autoconnect=off` for this browser, preventing automatic reconnection on the next visit.
- Peer Commons has **Enable automatic joining / Disable automatic joining**. Re-enabling reconnects to the default public lobby when possible.
- To use a more private invite-code room, disconnect, generate a long random invitation code (prefer a cryptographically random one), share it out-of-band, choose Nostr or MQTT and use manual Join. A password derived from that invite code is not a substitute for user verification.
- If offline, blocked, or CDN/relay discovery fails, read and work locally. Export a public proposal handoff JSON to share through a separately chosen channel. Peer rejoin does not synchronize past work automatically.

## What has NOT been verified

A real two-browser, two-device Internet WebRTC handshake was **not** successfully tested in this environment. The accompanying mocked transport tests verify the app's join/leave/control behavior only. No identity authentication, delivery receipt, or peer end-to-end security audit is claimed. Deployment testing on HTTPS with two consenting devices is required.

See Trystero's documentation at https://trystero.dev/docs/getting-started/ . MIT license: https://github.com/dmotz/trystero .
