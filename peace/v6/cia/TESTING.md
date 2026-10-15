# Validation and known limits — CIA Peace Analysis OS

Date: 2026-10-14. Static checks and isolated browser tests are included with this delivery. A real hosted-origin test of IndexedDB persistence across reload, SHA-256 happy path and service worker offline installation is separate and may be restricted by the test environment.

Expected: 15 standalone pages; nav from route registry; local record CRUD; search; JSON import/export and previous-version public-only handoffs; manual unsigned drafts; mobile drawer; theme; hashes with honest unavailable state; no network submission.

## Tests performed (2026-10-14)

- `node --check` on `assets/app.js` and `service_worker.js`: passed.
- `python tests/verify_structure.py`: passed (15 routes and 4 machine-readable datasets).
- Isolated Playwright Chromium/browser-harness test: **20 checks passed**, including 15 complete dynamic route renders, public record add/edit/search/export, prior public handoff import/export, checklist and theme, mobile drawer/Escape behavior, and SHA-256 availability/error messaging.
- Additional browser-harness test: **passed** for legacy U.S. Military, FBI and Secret Service data imports, source-note HTML escaping, and rejection of insecure HTTP source references.
- `file://` direct navigation in the test environment: blocked with `ERR_BLOCKED_BY_ADMINISTRATOR`; **not** a product failure proof, but no real file-origin end-to-end certification is claimed.
- Hosted origin and service-worker offline install, IndexedDB persistence between real page reloads, and a *successful* Web Crypto SHA-256 calculation: **not certified** by these isolated browser tests.
- JSON generated and source references verified structurally. This is not agency-authenticated evidentiary chain of custody, intelligence analysis approval or security penetration testing.

## Suggested device checks

1. Extract bundle into local folder; open `index.html`, navigate through two module links and return home.
2. Test the mobile drawer, Escape, top search and theme. Enable scripts (degrades to static reading index otherwise).
3. Add a **public-source only** note, reload and verify storage state; export JSON; deliberately delete, import after preview and verify the restored record.
4. At a local-origin HTTPS/localhost host, inspect service-worker cache and reload offline. Confirm public external articles are **not** available offline automatically.
5. On a secure browser origin, hash a harmless local test file and independently compare its SHA-256 bytes to a trusted local hashing tool.
6. Check that no POST requests, trackers, remote scripts, messaging, agency transmissions, or automatic source fetches occur.
