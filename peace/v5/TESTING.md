# SOL Peace Commons v2.2 — Test and limitation report

**Build date:** October 14, 2026. Independent public-interest research prototype, not certified for consequential institutional use.

## Checks executed in the isolated Chromium harness

- **29** original Fluid Path flow checks: introduction, continuous navigation, topic switch, quest reflection, XP, private project, backup export, mobile drawer and JavaScript error checks — passed.
- **9** legacy import/security checks: backups from all five prior editions, HTTPS-only URL requirements, HTML escaping, skill integrity — passed.
- **20** EIE HUD checks: immediate access, local question analysis, archive-linked citations, alternative hypotheses, note saving, JSON draft export, legacy backup integration, auto-join opt-out and mobile HUD — passed.
- **13** mocked-Trystero contract checks: public auto-join, same app namespace, no misleading password on public room, no automatic alias/data transfer, immediate disconnect/opt-out, manual reconnect, sanitized public sharing only after confirmation — passed. **These are mocked-transport checks, NOT a successful real peer handshake.**
- **1** archive structure suite: five original editions, 63 original route files, static service-worker references, and schema compatibility — passed.
- `node --check` on the extracted inline application JavaScript — passed. Service worker syntax, embedded research registry parse and web manifest JSON parse — checked.

**Total: 72 passing checks, counting the five suites above as 29 + 9 + 20 + 13 + 1.** The suite counts are local assertions, not third-party certifications.

## Verification limits

- Hosted Chromium navigation to `http://127.0.0.1` was attempted and returned `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Therefore actual service-worker installation, persistence across browser reloads and local secure-origin SHA-256 completion could not be exercised end-to-end here.
- The genuine CDN-imported Trystero module, Nostr signaling infrastructure, and a real two-device WebRTC handshake were **not** successfully tested. Only the correct application-level join/leave API contract was tested with an in-memory mock. Network connectivity can fail for browsers, relays, CDN policy, NAT and missing TURN services.
- Source registry records are a dated October 14, 2026 archive and are **not** re-verified by EIE automatically. Heuristic source matching is not intelligence validation or a live news feed.
- Browser storage may be unavailable in private modes, file origins or quota-limited environments; export JSON backups. PWA caching only covers listed same-origin public assets. No guarantee of uncached remote content offline.

## Suggested hosted acceptance tests

On the real deployed HTTPS URL: confirm visible default peer discovery; connect two consenting devices, manually send only a harmless public proposal, verify recipient quarantine and no automatic profiles/notes; disconnect and reload to verify auto-join remains off; reconnect explicitly. Save an EIE memo and reload to check IndexedDB, import/export it, test airgapped EIE retrieval and WebCrypto SHA-256, verify service-worker update to cache v5 and reduced-motion/mobile behavior.
