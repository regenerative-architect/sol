# SOL Peace Commons 2.7 — Two-computer connection and troubleshooting

**Status:** Independent, unofficial public research prototype. **Scope:** Browser-to-browser peer collaboration for publicly reviewed proposals. No agency, military or United Nations systems are connected.

## What changed from 2.6

- Trystero signaling now attempts **both Nostr and MQTT** by default. Both computers must use the 2.7 release, the same invitation code and a compatible strategy; each app instance negotiates its own WebRTC channels. If Nostr fails to load, MQTT may still work.
- The indicator says **Searching · 0 connected** until `onPeerJoin` fires. Initializing a local room is **not** proof of a remote connection.
- The Peer Commons displays separate Nostr and MQTT statuses and connection errors reported by the proper Trystero `joinRoom(config, roomId, {onJoinError})` callback.
- **Test live peer data** sends only an explicit test ping and expects a round-trip pong. It does not broadcast projects, notes, profile information, or EIE queries.
- **Reconnect both networks**, **Copy safe diagnostic report**, and temporary **TURN** configuration are available. TURN credentials are tab/session memory only—not saved to local storage, logs, backups, or JSON handoffs.
- EIE remains a **50 × 50 px globe icon** from first render, opening the research panel independently of the top HUD.

## First test (same version on both computers)

1. Publish the **contents** of `peace/` into your `/sol/peace/` hosting directory. Verify `index.html` and `service_worker.js` are from the same 2.7 package.
2. On computer A and computer B, open **the same exact HTTPS master URL**, not different standalone editions. Perform a hard refresh; old cached versions may not interoperate with new versions.
3. Open **Peer Commons** on both. Confirm **Nostr + MQTT (recommended)** and the **same room code**. The default code is `sol-peace-public-commons-2026`. Keep both tabs open concurrently.
4. Look for **actual peer connection(s) ≥ 1**. **Searching** or a relay reporting **searching** means the peer connection has *not* been established.
5. On either computer, click **Test live peer data**. Successful output reports a measured response via Nostr or MQTT. A connected label without a successful data test is not conclusive end-to-end proof.
6. If the test fails, click **Reconnect both networks** and view the diagnostics. Test without extensions that block WebSockets, then try another browser. Try same-network devices as a comparator.

## Why two different networks might still fail

**Signaling:** Both browsers must be able to reach a common Nostr relay or MQTT broker. Some firewalls or browsers block WebSockets or module CDNs. This app uses version-pinned third-party JavaScript CDNs and public relays. Public relay availability is not guaranteed.

**WebRTC NAT traversal:** Even when signaling works, some carrier-grade NAT, symmetric NAT and enterprise firewall combinations block direct peer connections. **A reliable cross-network connection may require TURN**. Nostr/MQTT discovery do *not* replace TURN.

**TURN setup (optional, not built into public GitHub Pages hosting):** Obtain temporary TURN credentials from a provider you control or trust (e.g. Cloudflare TURN or a properly configured coturn deployment). On each computer, in Peer Commons > **Advanced: optional TURN relay**, enter the `turn:` or `turns:` server URI and separate temporary username and credential. Click **Apply TURN and reconnect**, then repeat the data test. Do not publish a static credential or embed one in the HTML. A production deployment should obtain short-lived credentials from a rate-limited, access-controlled backend; a static GitHub Pages site cannot securely mint these itself.

## Status meanings

| UI state | Means | Does not mean |
| --- | --- | --- |
| Loading peer discovery | The app is importing Trystero and opening relay discovery | Another peer exists |
| Searching · 0 connected | A local signaling room opened without a completed remote data channel | Cross-network connection succeeded |
| 1+ actual peer connection(s) | Trystero reported at least one WebRTC peer connection | Peer identity is verified or messages were reviewed |
| Peer data test passed | A test payload was acknowledged over a live peer action channel | Proposals were accepted or a person is trustworthy |
| Discovery error | A CDN/relay/handshake problem was observed | All networks and retry paths are definitively impossible |

## Data and safety

- Auto-connect is on by default **because the project owner requested it**. The controls expose a one-click opt-out; disabling auto-connect persists in this browser.
- A public lobby is open to strangers. Relays and connected peers may see network metadata including IP addresses. Do not transmit sensitive information or identify vulnerable individuals.
- Public proposals are transmitted **only after explicit confirmation**. Received proposals enter an **unverified local review queue**. Private evidence gates, journal entries, EIE queries, character data and exported backups are never sent automatically.
- The safe diagnostic report omits actual room invitation codes and TURN credentials. It may contain error messages; review before sharing.
- If live networking fails, use the **JSON handoff vault** for asynchronous collaboration. No automatic cross-device synchronization is implied.

## External technical references

- [Trystero connection troubleshooting and TURN](https://trystero.dev/docs/connections/)
- [Trystero signaling strategies](https://trystero.dev/docs/signaling-strategies/)
- [Trystero open-source repository / MIT license](https://github.com/dmotz/trystero)

**Attribution:** Foster + Navi / Planetary Restoration Archive. Original source files remain MIT-licensed where designated. The third-party Trystero library retains its license and attribution.
