# Verification — foundational upgrade v2.3

**Environment:** isolated Chromium DOM harness; test date 2026-10-15. The hosted origin is NOT accessible to Chromium from this tool runtime; `Page.goto(http://127.0.0.1:8765/)` returned `net::ERR_BLOCKED_BY_ADMINISTRATOR` despite `curl` confirming the server responded.

## Passed

- **18** new foundational HUD / EIE tests (`tests/foundation_browser.py`): six-question progression, zero-match fail-safe, good-match retrieval, source coverage labeling, EIE drafts, desktop and mobile stability.
- **29** guided-flow browser checks (`tests/flow_browser.py`): journey, source reflection, private proposal, JSON backup, mobile accessibility.
- **20** EIE and HUD legacy checks (`tests/eie_peer_browser.py`): saved draft, archived source retrieval, explicit limits, mobile controls and existing JSON exports.
- **13** mocked peer API checks (`tests/peer_mock_browser.py`): auto-join namespace, public room configuration, no automatic transmission, disconnect, explicit share, private review-gate stripping.
- **9** schema/compatibility checks (`tests/compatibility_browser.py`): five prior edition imports, invalid URL rejection, legacy skill-point integrity and HTML escaping.
- **6** corpus/static structure checks (`tests/unified_structure.py`): five full editions plus shared route, archive, service worker and handoff compatibility.

**95 checks passed** across the above suites. These are internal assertions, not independently audited security or accessibility certifications.

`node --check` on the actual extracted main JavaScript passed. SHA-256 manifest and ZIP CRC checks are performed on the packaged files.

## Not certified

- Live two-device Nostr/Trystero discovery, NAT traversal and WebRTC connection reliability.
- Real origin IndexedDB persistence after browser reload or quota exhaustion.
- Hosted service-worker installation, offline behavior after deployment, or update delivery.
- Browser-by-browser screen-reader and keyboard audit at WCAG 2.2 AA.
- Completeness, currentness or legal accuracy of the archived Russia–Ukraine sources.

## Suggested acceptance run on GitHub Pages

1. Backup old master JSON; publish files from `peace/` without moving the five sub-editions.
2. On HTTPS, verify local source reading and EIE no-match state after a hard reload.
3. With two consenting browsers, confirm public room discovery, visible peer count, explicit sanitized share and unverified recipient queue; disconnect one browser and confirm no automatic rejoin.
4. Export and restore the old JSON backup. Verify EIE notes and review projects survive a new tab/reload.
5. Turn off network after first installation. Verify only precached content is available; Trystero and fresh external sources should fail gracefully.
6. Test screen readers, keyboard focus, touch input and reduced-motion mode before any consequential deployment.
