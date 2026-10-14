# Verification report — SOL Peace Commons Master v1.0.0

**Date:** 2026-10-14. **Platform:** Chromium headless with Playwright isolated HTML context, Node.js syntax check, Python structure/JSON inspection.

## Verified in the isolated browser harness

- **40 smoke checks passed**, covering boot, ten visible registry routes plus search, five portal links, eight classes, sixteen quests, fifteen progressive skills, class switching, alias settings, four cited quest completions, XP recalculation, earned skill unlocking, cross-domain project creation, one cited cooperative review gate, public-only unsigned handoff export (including review metadata), complete local JSON backup export, quarantined manual import from a prior edition, import of the new master handoff, explicit fork without inherited peer approvals, search deep link, theme switching, mobile drawer and Escape, and absence of uncaught JavaScript page exceptions.
- **9 additional compatibility and safety checks passed:** public research backup extraction from all five earlier edition app IDs, rejection of unsafe source URLs, HTTPS-only acceptance, refusal of unearned skill points in a backup, and HTML-escaping of malicious markup entered as a project title.
- **Static checks passed:** HTML structure, one-file core shell, Node syntax validation for extracted inline JS, JSON examples and manifest parsing, required files, app references and per-file size limits.

## Important limitations — do not report these as tested working

1. **Local navigation blocked:** automated Chromium refused `http://127.0.0.1` with `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Tests used `page.set_content(...)` and therefore *did not test* a normal local server or actual `file://` navigation.
2. **IndexedDB persistence after actual reload not verified:** isolated pages used explicit **memory-only** fallback. UI and code path for persistence are implemented, but genuine browser-origin IndexedDB reliability and upgrading need independent testing on a regular browser.
3. **Service-worker install and offline fetch caching not verified:** requires deployed HTTPS/localhost origin. Offline app shell strategy was inspected statically; off-origin research and external CDN modules are never promised offline.
4. **Real WebCrypto SHA-256 success path not verified:** insecure isolated browsing context lacked `crypto.subtle`; the graceful error path passed. Use real HTTPS for positive-path hashing.
5. **Trystero 0.25.3 live P2P exchange not end-to-end tested:** dynamic import, room join, signaling reachability, peer discovery, transmission and network failures must be tested on two actual browser clients. API shape cross-checked with the project's public documentation. The optional MQTT strategy is experimental and may require further dependency resolution.
6. **Five project GitHub Pages live contents/availability not verified:** links are used exactly as supplied, not fetched.
7. No independent WCAG audit, screen-reader field test, penetration test, cryptographic identity audit, or legal review was performed.

## How to retest locally

```bash
python3 tests/verify_structure.py
python3 tests/smoke_browser.py
python3 tests/compatibility_browser.py
# In a normal terminal from this folder:
python3 -m http.server 8000
# Open http://localhost:8000/index.html and test in two different browsers/devices.
```

**Acceptance criteria before claims of production use:** verified hosted PWA install/refresh/offline; IndexedDB round-trip after reload and after update; actual secure-origin file hashing; successful two-client peer connection, explicit proposal transfer and leave; explicit consent checks and readable error states under relay failures; security and accessibility review; no private data in handoff flows; independently checked project portal URLs.
