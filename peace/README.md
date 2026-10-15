> **v2.7 connection update:** See [PEER_CONNECTION_GUIDE_v2_7.md](PEER_CONNECTION_GUIDE_v2_7.md) and [DEPLOYMENT_v2_7.md](DEPLOYMENT_v2_7.md) for the default Nostr + MQTT peer discovery, actual peer/data-test indicators and session-only TURN fallback. External public relays and cross-network WebRTC are not guaranteed.

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

## v2.3 Foundational improvement cycle

Begin in `index.html` with **Begin with a finding**. The optional Earth Intelligence HUD now contains an inline six-question **Foundational Compass** with a sequential Next action, a practical acceptance test for each question, and a source-research shortcut. An unrelated question returns an explicit evidence gap rather than unrelated citations. Public Trystero discovery remains the online default with visible disconnect and no automatic content sharing.

See `FOUNDATIONAL_PROMPTS.md`, `CHANGELOG_v2_3.md` and `TESTING_v2_3.md` for completed corrections, unresolved questions, measurable verification steps and safety constraints. Export a local JSON backup before replacing older versions.


## New in 2.4 — Progressive institutional guides

Open **Guides** in the HUD for 50 plain-language and advanced lessons covering USSS, FBI, CIA, U.S. Military and UN research perspectives. The **Combined pathways** tab supports 31 research-lens combinations across ten project scenarios, with visible legal boundaries and public-only export. See `PATHWAYS_README.md`, `MULTIDOMAIN_GUIDEBOOK.md`, and `data/pathway_catalog.json`. Opening a guide does not transmit information or confer institutional authorization.


## New in 2.4 — Progressive institutional guides

Open **Guides** in the HUD for 50 plain-language and advanced lessons covering USSS, FBI, CIA, U.S. Military and UN research perspectives. The **Combined pathways** tab supports 31 research-lens combinations across ten project scenarios, with visible legal boundaries and public-only export. See `PATHWAYS_README.md`, `MULTIDOMAIN_GUIDEBOOK.md`, and `data/pathway_catalog.json`. Opening a guide does not transmit information or confer institutional authorization.


## EIE HUD 2.5 — compact launcher

After the initial loading display, **Earth Intelligence** shrinks into an accessible 44px globe icon in the master HUD. Open it to use the unchanged offline research tools. The globe remains at the top even when collapsed, while the Trystero connection status/control is separate. For `prefers-reduced-motion`, the globe minimizes immediately. No private research data is shared automatically. See `CHANGELOG_v2_5.md` and `TESTING_v2_5.md`.


## EIE HUD 2.5 — compact launcher

After the initial loading display, **Earth Intelligence** shrinks into an accessible 44px globe icon in the master HUD. Open it to use the unchanged offline research tools. The globe remains at the top even when collapsed, while the Trystero connection status/control is separate. For `prefers-reduced-motion`, the globe minimizes immediately. No private research data is shared automatically. See `CHANGELOG_v2_5.md` and `TESTING_v2_5.md`.


## Current v2.6 correction: Earth Intelligence is *always* a real icon

The old v2.5 banner description above is superseded. From first paint, Earth Intelligence is an **exactly 50×50px floating globe** in the lower-right corner, outside the peer/character HUD flex row. There is no auto-minimize timer. Press 🌐 to open the bounded nonmodal panel; press × or Escape to close. The icon does not transmit any research. Run `tests/eie_real_icon_browser.py` to verify icon geometry at three viewport widths. See `CHANGELOG_v2_6.md`.
