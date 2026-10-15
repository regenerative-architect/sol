# SOL Peace Commons — Earth Intelligence + Trystero v2.2

**One fluid, local-first peace-research workspace with Trystero as the default online collaboration layer and a read-only Earth Intelligence Engine (EIE) integrated into its HUD.** This is an independent public-interest prototype, not an official intelligence, policing, military, or UN system.

## Open the application

- **Hosted HTTPS** (recommended): publish the `peace/` contents at `https://regenerative-architect.github.io/sol/peace/`. On first online load, the application attempts to join the public Trystero research room (`sol-peace-public-commons-2026`) through Nostr discovery. The peer button remains visible in the HUD. **Anyone who discovers or knows this lobby code may join.** Signaling relays and peers may learn network metadata/IP addresses; use **Disconnect** or turn automatic joining off in Peer Commons. This feature is enabled by default at the user's request, not as a background or hidden integration.
- **Local `file://`**: reading, EIE research, public archives, local quests, notes and JSON import/export work without a server where the browser allows. Automatic online discovery is not attempted on `file://`; use the visible Connect control to try peer connection manually. Some browsers block its module import. There is no service worker under `file://`.
- **Offline**: EIE's deterministic retrieval uses sources embedded inside the HTML. No peer discovery, live news, external research, remote WebLLM downloads, or uncached webpages work offline. Manual JSON exchange remains possible.

## First run: three things, zero setup

1. The HUD shows **✦ Earth Intelligence** and **peer connection status**. The introduction stays a simple “Begin with a finding” flow.
2. Select **Earth Intelligence** to expand a slim analysis drawer inside the HUD. Ask a source-grounded question or select a suggested topic. It returns links to matching archived sources, a retrieved intervention concept, alternative hypotheses, limitations, and a next verification step. You can save the draft privately or export it as JSON.
3. Continue through **Explore → Reflect → Build** without visiting separate portals. You can explicitly send one sanitized, public proposal summary to connected peers; all incoming proposals remain unverified in your inbox.

**No AI model is secretly loaded.** EIE v2.2 is a functional, transparent local retrieval and hypothesis-scaffolding module, **not** an implementation of unrestricted AI autonomy or a gateway to external tools. No external operations are enabled. The network component only provides peer presence and explicitly initiated sharing.

## What is preserved

- All five complete agency/UN-themed editions: `usmc/`, `usss/`, `cia/`, `fbi/`, `un/` (63 original route files).
- 76 public source references, 19 casebook records, 37 intervention concepts, 47 review criteria, integrated Evidence Atlas, comparative convergence map.
- Eight educational classes, 16 self-reported quests, 15 sequential skills, five proposal review gates.
- Local IndexedDB when available and memory-only fallback, portable validated JSON backups, `pra.sol_peace_master` version 1 and `pra.reciprocal_public_handoff/v1` compatibility.
- Accessible navigation, mobile drawer, theme preference, optional motion, print-friendly content and versioned hosted PWA cache.

Read [`EIE_HUD_GUIDE.md`](EIE_HUD_GUIDE.md), [`PEER_RUNBOOK.md`](PEER_RUNBOOK.md), [`DEPLOYMENT.md`](DEPLOYMENT.md) and [`TESTING.md`](TESTING.md).

**Credit:** Foster + Navi / Planetary Restoration Archive. Original code MIT; third-party code and archived source content retain their own terms. See `ATTRIBUTIONS_AND_LICENSES.md`.
