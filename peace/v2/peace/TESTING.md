# Validation — Convergence Worlds v2.0

Date: 2026-10-14. Test environment: isolated headless Chromium `/usr/bin/chromium`, Python/Node. The browser environment blocks navigation to `127.0.0.1` and `file://`, so tests render the standalone HTML with Chromium `set_content()` and invoke real browser event handlers. This verifies most UI logic but is **not a substitute for actual hosted-origin tests**.

## Completed

- **42 legacy master smoke checks passed:** 12 routes, 8 classes, 16 quests, 15 skills, sourced quest completion, XP, skill unlocking, project review gates, public handoff export, imported-unverified quarantine, safe fork, JSON backup, search, theme, mobile drawer, honest WebCrypto fallback and no JS runtime errors.
- **21 guided journey checks passed:** persistent HUD, five inline phases, contextual tips, class change without navigation, inline quest proof, XP, minimal project creation, local export, animation toggle and mobile journey.
- **33 new integration checks passed:** five embedded registry sets; native Convergence Map, instant node switching, inline cross-domain comparison, Atlas filter/pagination/search/case detail, 19 casebooks, 37 interventions, 76 source records, five packaged edition outlinks, original backup schema, mobile drawer and no runtime exceptions.
- **9 previous edition compatibility/security checks passed:** public-only handoff imports from USSS, FBI, U.S. Military, CIA and UN; HTTPS source gating, HTML escaping and validation against unearned skill points.
- **Static validation passed:** 63 original edition HTML route paths exist, all 5 original edition app.js files and the new master inline module pass `node --check`; all 76 native corpus source URLs are HTTPS; service-worker syntax and referenced core files are present; manifest and ZIP CRC were checked.

## Not verified here

1. Two-device Trystero signaling, NAT traversal and WebRTC proposal delivery. The code is opt-in and requires network connectivity.
2. Hosted-origin service-worker install/activate, offline navigation under GitHub Pages, cross-reload IndexedDB persistence and actual secure-origin SHA-256 success path. The browser policy blocks localhost and `file://` navigation.
3. Access to external public source websites or whether linked reports have changed since the source freeze.
4. Whether the currently deployed GitHub Pages five folders contain newer work than the uploaded ZIP; no GitHub deployment or account action occurred.
5. Security review of third-party browser libraries or a penetration test. Don't import confidential data or deploy for real institutional use without independent review.

## How to run

```bash
python tests/unified_structure.py
python tests/unified_integration_browser.py
python tests/guided_flow_browser.py
python tests/smoke_browser.py
python tests/compatibility_browser.py
python tests/verify_structure.py
```

Requires Python Playwright and installed Chromium; adapt `executable_path` as necessary. Tests may overwrite preview PNG screenshots.

## Manual post-deployment acceptance

Publish to a test HTTPS path. Load online, check service worker and Cache Storage, go offline and verify only previously cached content opens. Create a quest and project; reload twice; confirm persistence or see memory-only fallback. Export/import matching JSON. Then test two consenting peer browsers, an explicit public-only share, unverified inbox receipt, and deletion/revocation. Validate mobile focus order, print and reduced-motion settings. Do not imply any connected agency or UN authorization.
