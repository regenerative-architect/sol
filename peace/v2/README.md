# SOL Peace Commons — Convergence Worlds 2.0

**Build / source freeze:** 2026-10-14  
**Authors:** Foster + Navi / Planetary Restoration Archive  
**Status:** unofficial, independently developed, public-interest research and learning prototype. This is **not** a U.S. government, military, intelligence, law enforcement, NATO, ICRC or UN system.

## Start

Open `index.html` to launch the **single, continuous master interface**. It is a complete standalone HTML document (embedded styles, logic and evidence registry) and does not require a framework, account or network for core reading, RPG progression and local JSON export. Keep sibling folders for full editions. The master directly embeds casebooks, source registries, proposed interventions and review criteria from the supplied `peace.zip`; it does not silently fetch other sites.

### What's integrated

| Included source edition | Original entry | Original pages | Source records | Casebooks | Action plans | Review rules |
|---|---|---:|---:|---:|---:|---:|
| U.S. Military / USMC | `usmc/index.html` | 15 | 16 | 4 | 8 | 10 |
| U.S. Secret Service / USSS | `usss/index.html` | 7 | 7 | — | 6 | 7 |
| CIA | `cia/index.html` | 15 | 18 | 5 | 8 | 10 |
| FBI | `fbi/index.html` | 11 | 15 | 4 | 6 | 9 |
| UN | `un/index.html` | 15 | 20 | 6 | 9 | 11 |
| **TOTAL** | **Master + 5 preserved editions** | **63** | **76** | **19** | **37** | **47** |

The 63 pages shown here count each edition's original index and module pages. They remain separate for mandate-specific research and historical comparison. The master itself adds the continuous overview, native integrated Atlas and cross-domain Convergence Map, with existing quest/workshop/peer/vault modules preserved.

### Fluid learner experience

- **Convergence dashboard:** contextual mission, floating role and XP HUD, five pressable sector perspectives, small step flow, one-click switch that redraws only the selected panel.
- **Evidence Atlas:** offline-native full-text filtering by discipline, record type and keyword; expandable case limits and primary-source URLs; staged pagination.
- **Reciprocity laboratory:** compare proposed interventions and responsible mandates side by side, with a non-operational design clue for a civil-protection proposal.
- **Guided Constellation:** 8 classes, 16 evidence-grounded quests, 15 skills / 5 prerequisite-linked trees; traits measure *self-reported learning*, not qualifications.
- **Project workshop:** local draft with cited source, multiple disciplines and five review gates; private-by-default.
- **Peer rooms:** optional, consent-gated Trystero/WebRTC connection; public proposal sharing only after explicit confirmation, without identity or institutional verification.
- **Portable data:** IndexedDB where supported; graceful memory-only fallback plus manual JSON backup and interoperable `pra.reciprocal_public_handoff/v1` drafts.

## Privacy & data handling

No account, telemetry, hidden upload, covert surveillance, automated email or government connection. The native Atlas loads from data embedded in `index.html`. `data/integrated_public_records.json` is a separate audit copy and is not required for launching. User progress is separate from public registry content. Peer data enters an unverified review queue; no peer card can award XP or pass another user's review. Names of real agencies label **topic-specific research perspectives**, not permissions or participating entities.

### Online versus offline

- **Local file `file://`**: bundled content, master and original pages, navigation, class/quest/skill/project functions and JSON import/export work without a server. Browser restrictions may block IndexedDB or WebCrypto. If persistence fails, you must export a backup to retain work; the application reports memory-only mode.
- **HTTPS GitHub Pages**: enables hosted manifest/service worker and the browser security context. The master caches its own shell plus the five original edition entry points and shared scripts on service-worker installation. Other module pages cache on first successful visit when supported. **Unvisited pages and live source URLs do not work offline.**
- **Trystero**: entirely optional; requires live connectivity, signaling availability and WebRTC reachability. Two-device connectivity was **not tested** in this environment; manual public JSON handoff remains the dependable fallback.

## Installing into the original repository

Extract the ZIP: it contains a `peace/` directory. Publish the **contents of that directory** at `/sol/peace/` in the `regenerative-architect.github.io` repository. Keep the `usmc`, `usss`, `cia`, `fbi`, and `un` folders intact. See `DEPLOYMENT.md` for backup and validation steps. The app does not deploy anything by itself.

## Source and evidentiary limits

The embedded registry is a **dated snapshot from the supplied archive**, not a live claim that events, proposed agreements or sanctions are current beyond 2026-10-14. Archive authors' classifications are preserved, not independently re-adjudicated. Proposed actions are proposals, not authorized institutional operations. An original manufacturer appearing in a recovered weapon does not prove knowing sanctions evasion. Real interventions require human authorization, law, the consent of affected populations and independent verification.

**Zero-Harm / Anti-Inversion:** no offensive cyber, targeting, sabotage, covert persuasion, suspect identification through inference, forced transfer or private-person coercion. Proposal gates ask for source provenance, legal scope, civilian risks, strongest dissent and measurable results. Automated game scoring does not claim real-world civilian outcomes.

See `GUIDED_PLAYBOOK.md`, `ARCHITECTURE.md`, `DEPLOYMENT.md`, `TESTING.md` and `ATTRIBUTIONS_AND_LICENSES.md`.
