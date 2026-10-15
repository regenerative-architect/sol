# Testing — EIE Auto-Minimize 2.5

Date: 2026-10-15. Verified in an isolated Chromium/Playwright harness using direct page content.

## Verified

- 35 new targeted desktop, mobile and accessibility checks: brief banner display, auto-collapse to 44px globe, no additional auto-open, reliable click opening and closing, EIE evidence search retained, keyboard focus restoration, accessible name/tooltip, compact state across HUD rerenders, no horizontal overflow and no JavaScript page errors. Reduced-motion mode minimizes immediately. Both Enter and Space activate the icon.
- 18 inherited foundational EIE checks, 29 inherited fluid-flow checks and 40 inherited adaptive-guide checks passed.
- Inherited compatibility/security checks passed, including five previous institutional JSON formats and unsafe-HTML handling.
- Structural tests verify 63 prior edition pages and all five preserved original editions.
- Node.js JavaScript syntax check, full archive checksum and ZIP safety verified during packaging.

## Unperformed

- Live two-device WebRTC/Trystero handshake across real networks.
- Hosted service-worker update lifecycle, real offline reload, durable IndexedDB after browser restart.
- Formal WCAG 2.2 AA screen-reader audit. Browser tests are not equivalent to certification.

## Repeat

```bash
python tests/eie_compact_browser.py
python tests/foundation_browser.py
python tests/flow_browser.py
python tests/compatibility_browser.py
python tests/adaptive_guides_browser.py
python tests/unified_structure.py
python tests/verify_structure.py
```

Dependencies: Python Playwright and Chromium. No institutional system was accessed or changed.
