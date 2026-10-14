# FBI Integrity OS — actual validation record

**Snapshot:** 2026-10-14. This is an independently built public research prototype, not a deployed or audited government tool.

## Tests performed and passed

- Node.js JavaScript syntax checks on `assets/app.js` and `service_worker.js`.
- Standard-library offline structure verification (`tests/verify_structure.py`): 11 HTML documents, relative page links, application JS/CSS/manifest paths, data-source JSON, handoff version and same-origin precache list.
- Isolated Chromium Playwright DOM rendering for all 11 route views, using `page.set_content()` and injection of the local JS/CSS, because the test environment blocked both localhost and direct `file://` navigation.
- Isolated Chromium functional checks: local research record creation, editing, page search, manual JSON backup download, import preview and import of a USSS-compatible public-only handoff, manual export of an unsigned reciprocal handoff, nine-step review checkboxes, light/dark theme control, mobile drawer and Escape close.
- Confirmed graceful handling of unavailable Web Crypto in an opaque-origin (`about:blank`) browser test. The tool did **not** generate an invented digest.
- Visual inspection of desktop and mobile browser screenshots and mobile theme-control adjustment.

## Not tested / limits

- **Actual `file://` navigation**, per-origin IndexedDB persistence across pages and hosted PWA service-worker offline reload: browser navigation was blocked by administrator policy in the test runtime. These remain recommended manual acceptance tests on a normal local machine or HTTPS test server.
- **Actual file hashing:** in the isolated `about:blank` test origin Web Crypto was unavailable; the SHA-256 happy path remains unverified in this environment. Actual hashing is implemented using the browser's `crypto.subtle.digest` when available.
- Independent accessibility audit with screen-reader users, third-party penetration testing, legal review, or correctness of every external source over time was not conducted.
- No intelligence systems, official API, cloud sync, investigation case management, agency identity checks, live military data, or covert operations were tested or connected. They do not exist in this package.

## Recommended manual user acceptance tests

1. Extract the full ZIP. Open the root `index.html` with browser JavaScript enabled; navigate every module from the sidebar and direct bookmarks.
2. Test search, light/dark toggle and mobile menu with Escape and keyboard focus. Verify print preview.
3. Create an entirely synthetic public research note; reload and confirm local persistence **or** a visible memory-only warning. Export a backup before ending the session.
4. Import that backup, review collision options and verify record integrity. Import a USSS public-only handoff v1 JSON for interoperability.
5. Choose a non-sensitive file, calculate SHA-256, and compare the digest with another independent local hashing tool.
6. Optionally serve on localhost or HTTPS and verify that the core HTML shell loads offline after caching. External FBI/DOJ/BIS references should remain unavailable offline unless separately saved.
7. Confirm that downloading a handoff does not transmit information or imply an official case submission.

**Security reminder:** This local prototype is not suitable for classified, confidential, protected financial or personally sensitive evidence. IndexedDB is not encrypted by the application.
