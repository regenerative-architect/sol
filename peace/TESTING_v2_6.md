# Testing — True Earth Intelligence icon v2.6

Date: 2026-10-15. Tests conducted in isolated Chromium with Playwright.

## Verified

- **45 new responsive interaction checks** at viewport widths 1440, 390 and 320 pixels. The globe button is exactly 50×50 pixels from initial render and after more than two seconds, *without any banner*. It resides outside the HUD layout, remains icon-sized after re-render, opens a bounded EIE floating panel, accepts local research queries and closes on Escape with keyboard focus restoration. No horizontal overflow or browser exceptions.
- **18 foundational**, **29 fluid-flow**, and **40 adaptive-guide** browser regression checks passed.
- Older public-edition import compatibility/security suite passed, including rejection of unsafe URLs and unsanitized user content.
- Unified structural checks passed, including 63 original institutional routes and new `shell-v9` service worker identifier.
- Node.js syntax check passed for master inline JavaScript.
- SHA-256 manifest entries were verified against every archived file; ZIP CRC checks passed.

## Still to test on a deployed HTTPS origin

Real cross-device Trystero WebRTC, hosted service-worker upgrade lifecycle, IndexedDB persistence after browser restart, mobile screen-reader usability, and a formal WCAG 2.2 AA audit.

## Run

```bash
python tests/eie_real_icon_browser.py
python tests/foundation_browser.py
python tests/flow_browser.py
python tests/adaptive_guides_browser.py
python tests/compatibility_browser.py
python tests/unified_structure.py
```

The v2.5 banner-based test is superseded by the v2.6 icon-only test.
