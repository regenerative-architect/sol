# UN Peace Assurance OS — validation and known limitations

**Build/test date:** October 14, 2026. All content is unofficial and public-source-only. These results do not establish a field mandate, legal approval, or production security accreditation.

## Results achieved
- `node --check` on `assets/app.js` and `service_worker.js`: **PASS**.
- `python tests/verify_structure.py`: **PASS**, 15 individually addressable HTML pages, four structured datasets and public v1 handoff logic.
- Isolated Chromium suite `python tests/smoke_browser.py`: **20 PASS** checks. All 15 pages render; local note create/edit/search/export; public legacy handoff import and unsigned draft export; review checklist and theme; file hash unavailable/supported messaging; mobile drawer and Escape.
- Additional Chromium test: **PASS** import of existing Secret Service, FBI, Military and CIA public backups, HTML-safe text escaping, and HTTP URL rejection.
- Package SHA-256 manifest and ZIP file check: **PASS** at packaging time.

## Not certified in the test environment
- Direct `file://` browser navigation or full hosted-origin link transitions: the isolated browser used `set_content` and injected bundled CSS/JS because browser navigation may be blocked by administrative sandbox policy.
- IndexedDB persistence across real reloads and origin changes. Storage may fall back to memory-only; UI states this.
- Successful SHA-256 file calculation in an HTTPS/localhost secure context. Local test checked behavior when unavailable.
- Hosted service-worker install, stale-cache invalidation and reliable offline read-through after network drop.
- Full WCAG 2.2 AA independent audit, adversarial security testing, official source link revalidation after build, field verification or external institutional authorization.

## Acceptance test on your computer
1. Extract ZIP; open `index.html`, follow 3 module navigation links, then return to Overview. Check top search, mobile drawer, Escape and theme.
2. In Local evidence ledger, save a public note, refresh the page, confirm storage status, export, reset after confirmation, then reimport with preview and a collision choice.
3. Use a harmless test file on localhost/HTTPS in Evidence Lab, and independently compare SHA-256 output. `file://` may not expose Web Crypto.
4. On localhost or HTTPS, verify precached shell renders offline; linked UN pages and new source content **do not** work offline unless separately acquired.
5. Inspect Developer Tools: no remote scripts, analytics, POST traffic, government endpoints or automatic interagency transmissions.
6. Independently verify dated source claims before external decisions.
