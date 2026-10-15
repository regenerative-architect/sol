# U.S. Military Peace & Civilian Protection OS — Validation Report

**Build / fact freeze:** 2026-10-14. **Environment:** Linux container, Node.js syntax check, Python structural test, isolated Chromium browser test using a static document harness.

## Actually passed

- All **15 standalone HTML pages** exist and rendered application modules in isolated Chromium without uncaught JavaScript exceptions.
- JavaScript syntax check: `node --check assets/app.js`.
- Source/data files: `sources.json`, `actions.json`, `scope_matrix.json`, `handoff_schema_v1.json` parsed correctly; static structure check passed.
- Local public-note **create, edit, search and JSON backup export** were exercised.
- Import of a prior `pra.reciprocal_public_handoff/v1` public-only note and generation of an **unsigned, unsubmitted** v1 draft passed.
- Review checkboxes, dark theme, mobile drawer opening and Escape closing passed.
- File hash tool detects unavailable Web Crypto in an unsupported opaque document origin and gives an explicit message rather than fabricating a digest.
- Desktop and mobile interface screenshots generated in isolated Chromium.

## Tests not completed / limitations

- A real hosted/localhost page navigation was attempted; the browser environment returned `net::ERR_BLOCKED_BY_ADMINISTRATOR`, so **service-worker precaching, actually offline hosted reload, same-origin persistent IndexedDB across reloads, and successful Web Crypto SHA-256 path are NOT certified**.
- `file://` browser navigation was likewise not available for a complete origin-level test. No real government connectors exist to test.
- WCAG 2.2 AA conformance has not been audited with assistive technology; automated and manual accessibility assessment remains necessary.
- Source webpages are not cached and require an internet connection; fact freeze is not live.
- Handoff drafts have no digital signature, identity proof, verified receipt or authenticated transport.

## Recommended user smoke tests

1. Extract ZIP. Open `us_military_peace_os/index.html` by double-click; visit all module links, use search, theme, print and mobile drawer.
2. From a terminal in the parent folder run `python3 -m http.server 8000` and visit `http://localhost:8000/us_military_peace_os/`; verify service-worker `registered` status and reload after disconnecting from network.
3. Save a **public dummy note** in the Research Ledger, reload and verify persistence (storage browser permitting). Export JSON, delete the test note, re-import and choose conflict behavior.
4. In Evidence, hash a non-sensitive text file and compare the SHA-256 against a trusted local utility (`sha256sum` or Windows `certutil -hashfile file SHA256`).
5. In Nodes, generate the `PUBLIC_ONLY`, `submitted:false` draft; confirm no network request is made to any agency.
6. Test keyboard-only navigation, screen reader labels, reduced-motion preference, light/dark contrast, mobile scroll and print layout.
7. For deployment review caching update strategy, HTTPS origin and CSP/header configuration. Never input protected or operational data.

## Offline semantics

Extracted site reading pages are bundled locally. Hosted service workers (not usable under `file://`) precache the same-origin static site on successful installation. External sources and dynamic government information remain online-only. IndexedDB is origin-scoped and does not automatically move with files or between devices.
