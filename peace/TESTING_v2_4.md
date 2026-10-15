# Testing · Adaptive Pathways 2.4

Date: 2026-10-15. This is an independent public-interest research prototype. Source references are not live-fact subscriptions.

## Executed checks

- **40 interactive guide checks passed** (20 desktop + 20 mobile): inline HUD opening/closing, five-node lessons, class shortcut, simple/advanced switch, search, lesson progression, ten scenarios, suggested and all-five combinations, exported public-only draft, dedicated route, no JS exceptions, no viewport overflow.
- **18 inherited foundational checks passed** (EIE abstention, relevant citations, six inquiry prompts, mobile HUD).
- **29 inherited fluid-journey checks passed** (finding → reflection → project, backup, mobile drawer, navigation).
- **9 inherited cross-edition compatibility/security checks passed** (five predecessor imports, HTTPS source validation, HTML escaping, XP constraints).
- Five embedded subedition route registries and all **63 preserved HTML route pages** passed structure checks. JS syntax parsed under Node.js 22.
- Guide library structural assertions: **5 guides, 50 chapters, 10 scenarios, 31 unique node combinations, 310 pathway templates**.
- ZIP path safety, SHA-256 file manifest, JSON parse and package integrity verified below at packaging.

## Important unperformed tests

- Real two-device Trystero WebRTC handshake across live networks.
- Actual hosted GitHub Pages PWA precache, offline reload and IndexedDB persistence across browser restarts.
- Full WCAG 2.2 AA audit with screen readers and multiple physical devices.
- Any external government/UN service connection, authorization or real-world outcome.

## Reproduce

```bash
python tests/adaptive_guides_browser.py
python tests/foundation_browser.py
python tests/flow_browser.py
python tests/compatibility_browser.py
python tests/unified_structure.py
python tests/verify_structure.py
```

Requires Playwright/Chromium for browser tests. The browser harness loads page content directly, so it does not exercise `file://` routing, secure-origin service workers or real WebRTC.
