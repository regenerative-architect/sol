# Deploy /sol/peace/ Fluid Path v2.1

1. Export your existing master JSON backup before installing. Keep an independent copy.
2. Download `sol_peace_flow_bundle.zip`. Extract its top-level `peace/` directory and publish the **contents** into the existing `/sol/peace/` GitHub Pages path, preserving the five embedded subdirectories.
3. If the hosting repository root is `/sol/peace/`, `index.html` should resolve as `https://regenerative-architect.github.io/sol/peace/`. The subdirectories should remain `usmc/`, `usss/`, `cia/`, `fbi/`, `un/`.
4. Over HTTPS, the versioned service worker may cache the public shell following its successful install. It does not cache private data or guarantee that linked external sources work offline. Ordinary `file://` opening has no service worker.
5. After deployment, test the intro, topic switch, reflection skip/save, private project, JSON import/export, mobile drawer, source links and optional peer connection on two consenting devices.
6. If a previously installed PWA still displays v2.0, reload and check the browser's service worker/cache updates. Do not clear IndexedDB without exporting a backup.

The master uses no remote API and does not deploy or share data automatically. A signed, trusted peer exchange and real WebRTC handshake have **not** been verified by the included browser harness.
