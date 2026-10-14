# SOL Peace Commons — Fluid Path v2.1

**An accessible, offline-first public-interest peace research environment.** This version replaces the dense first-screen dashboard with one uninterrupted flow that gradually reveals only what the user needs. The uploaded five research editions remain packaged in full. This is an unofficial prototype with no government or UN connection.

## Simplified launch

1. Open `index.html` (or host this folder at `/sol/peace/` on GitHub Pages).
2. Press **Begin with a finding**; optionally choose another focus in an expandable section.
3. Read a public source; optionally save a learning observation and a private civilian-protection project.
4. Continue exploring or download a portable JSON backup. The complete advanced library stays available through the menu.

The entry experience does **not** request an account, class selection, peer connection, permission to share, or setup details. It uses gradual fades rather than dialog interruptions and respects reduced motion.

See [`FLOW_GUIDE.md`](FLOW_GUIDE.md) for the user guide and [`DEPLOYMENT.md`](DEPLOYMENT.md) for hosting notes.

## Preserved integrated modules

- Five separately preserved research editions: `usmc/`, `usss/`, `cia/`, `fbi/`, `un/` (63 route pages).
- Embedded dated research records: 76 public-source references, 19 casebook records, 37 proposed actions and 47 review criteria across the five editions.
- Full Evidence Atlas and convergence comparison, 8 learning roles, 16 self-attested quests, 15 sequential skills, five review gates per proposal.
- IndexedDB local state when available, JSON import/export and manual `pra.reciprocal_public_handoff/v1` drafts. Imported data remains unverified.
- Optional Trystero peer rooms using explicit consent, no auto-connect or institutional integrations.

## Technical notes

- Default entry: `index.html`, embedded CSS and vanilla JavaScript. Optional `service_worker.js`, `site.webmanifest`, `icon.svg` on HTTPS.
- The primary experience is a progressive DOM update of `#flowScene`, not route changes. Advanced modules use the existing hash router.
- Automatic storage uses the existing `pra.sol_peace_master` version 1 state contract. Prior exports remain compatible.
- No external accounts, telemetry or backend. Off-origin public sources do not work offline unless separately acquired through lawful means.
- Export a backup before replacing a deployed earlier version. Service worker cache name bumped for the v2.1 update.

## Trust boundaries

All imported and peer records are public-only, unverified and require independent review. XP measures local exercises only. This OS must not be used to claim official access, military command, intelligence collection capabilities or real peace outcomes.

**Attributions and licensing:** Foster + Navi / Planetary Restoration Archive; original code MIT. Third-party software and independently authored source material retain their licenses and attribution requirements. Read `ATTRIBUTIONS_AND_LICENSES.md`.
