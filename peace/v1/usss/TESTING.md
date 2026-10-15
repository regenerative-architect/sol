# Validation performed — 2026-10-14

The following checks **were actually performed**:

- Node v22 syntax parsing of `assets/app.js` and `service_worker.js` — passed.
- JavaScript VM smoke tests for each of the seven route view builders — rendered without runtime exceptions; all returned an H1 and nonempty content.
- JSON handoff contract smoke test — `PUBLIC_ONLY`, `submitted: false` confirmed.
- Input normalization smoke test — accepted valid public source URL, rejected a `javascript:` URL.
- BeautifulSoup file-link and HTML-shell static checks — seven `index.html` pages, no missing local assets referenced by the base HTML.
- Source index and sample handoff JSON parse checks — passed.
- Individual files verified below 2 MB.

**Not verified:** live end-to-end browser interactions, accessibility automation and hosted service-worker update behavior. Playwright/Chromium navigation of both localhost and `file://` was blocked by the execution environment with `ERR_BLOCKED_BY_ADMINISTRATOR`. The environment restriction is **not** evidence of an application defect or successful browser test. Manual testing on the target browser/device is still needed before operational reliance or external deployment.

**Recommended manual acceptance tests** (all using non-sensitive dummy records):

1. Open every page through nav and directly by its `index.html` path, including `file://` mode.
2. Create/edit/delete a local lead, navigate to another page and confirm it persists where IndexedDB is available.
3. Export backup JSON, import it with duplicate strategy `skip`, `overwrite`, and `copies`, then verify the intended outcomes.
4. Use `Evidence lab` to hash a small file with a known digest; verify browser reports when Web Crypto is unavailable.
5. Export a handoff and confirm `submitted: false`; no network request should occur.
6. Check dark/light, narrow mobile drawer + Escape, keyboard-only navigation, screen-reader semantics and print layout.
7. Test hosted HTTPS SW precache by reloading a previously opened page while offline, then verify remote source links are correctly unavailable if uncached.
8. Verify storage-denied/private mode fallback displays an explicit warning and does not claim persistence.
9. Attempt oversized/invalid JSON import and XSS text in a record; verify rejection/escaping.
10. Confirm that there are no telemetry calls or automatic transmissions in browser dev tools.
