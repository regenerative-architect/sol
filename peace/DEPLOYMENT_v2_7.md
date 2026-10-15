# Deploy SOL Peace Commons v2.7 to GitHub Pages

1. Export your existing private JSON backup before any replacement.
2. Extract the ZIP. Publish the **contents of its `peace/` directory** to `https://regenerative-architect.github.io/sol/peace/`. Do not change the `/usmc/`, `/usss/`, `/cia/`, `/fbi/` or `/un/` hierarchy.
3. Use the **same release on both test devices**. Important modified files are the root `index.html` and `service_worker.js`; the complete ZIP includes the intact portal structure.
4. Allow GitHub Pages to deploy. Hard-refresh both computers (Ctrl+Shift+R or Cmd+Shift+R). If an old service worker remains active, use DevTools > Application > Service Workers > Update, then reload. Avoid deleting local IndexedDB data during service-worker inspection.
5. Open the master root URL on both computers and follow [PEER_CONNECTION_GUIDE_v2_7.md](PEER_CONNECTION_GUIDE_v2_7.md). Default signaling uses **both Nostr and MQTT** with a shared room code. View live count and test data exchange.
6. Where WebRTC direct connection remains impossible, provision a **legitimate TURN server** and supply ephemeral credentials separately on each client. A static HTML site cannot guarantee connectivity through restricted NATs without such infrastructure.
7. If needed, keep JSON handoff workflows as the graceful offline and no-peer fallback.

This is an independent educational prototype, not government or UN infrastructure. No other user's data is synchronized or imported without the user's explicit action.
