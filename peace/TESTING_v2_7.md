# Verification — SOL Peace Commons v2.7

## Tests actually run

- Node.js parsed the embedded JavaScript without syntax errors.
- A Chromium-based isolated browser test mocked the Trystero module boundary: both Nostr and MQTT loaded; status stayed **searching** without a remote peer; a simulated remote join changed status to **connected**; a simulated probe received a matching acknowledgment; no profile or private content was auto-sent; disconnect left all mock transports; no uncaught page errors.
- Browser measured the floating EIE button at **50×50 px** on a 390 px mobile viewport.
- A separate mocked failure test rejected all Nostr CDN attempts, verified MQTT remained functional, simulated a peer join, and verified disconnect and no uncaught page errors.
- Inspected the five original research-site subdirectories, JSON data files and source tree for preservation.
- Rebuilt and verified the packaged ZIP and its SHA-256 manifest.

## Not verified here

- Successful negotiation between **two real machines on different networks**.
- Availability of external Nostr relays, MQTT brokers or CDN endpoints to either user's browser in the field.
- Actual use of a provider TURN relay; none is embedded or provisioned in the application.
- Hosted GitHub Pages service-worker update and IndexedDB survival across browser restarts.
- Full WCAG 2.2 AA certification.

These require deployment and user-side testing. An empty room or expired signaling route is not proof that all peer matching is broken; a live peer and the data-ping result are the critical tests.
