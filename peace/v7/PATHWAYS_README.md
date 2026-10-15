# Adaptive Pathways 2.4 · Implementation Guide

**Scope:** Five named institutional *research perspectives* (USSS, FBI, CIA, U.S. Military, UN), ten mission templates and all 31 nonempty combinations of the five lenses (310 scenario–combination templates are also available in `data/pathway_catalog.json`). Other named companies and private individuals in underlying casebooks are not automatically assigned mandates or culpability.

## Minimal path

1. Open `index.html` as usual. The original one-action introduction remains.
2. Open **🧭 Guides** from the persistent HUD, or the optional `#/guides` navigation route.
3. Select a lens and read one simple lesson. Only open advanced guidance, acceptance tests or pitfalls when necessary.
4. Switch to **Combined pathways**; choose a problem and 1–5 lenses. The site calculates the included roles, missing suggested reviewers, safety gates and a six-stage public research route.
5. Export a clearly marked `pra.sol_public_pathway_draft/v1` JSON file, or open the existing private proposal workshop. Nothing is transmitted automatically.

## Pathway semantics

There are `2^5−1=31` **nonempty combinations** of five perspectives, evaluated against ten scenario templates (310 potential selections). These are combinations of documentation and expert *views*, not a real collaboration network or a claim that every combination is appropriate. Suggested reviewers are included per scenario; missing expertise is disclosed. The UN cannot be ordered to deploy monitors; the CIA cannot enforce U.S. law; USSS cannot run export licensing; FBI cases require lawful authorities; and DoD defensive support cannot override civilian protection obligations.

## Data and offline support

The authoritative static guide dataset is `data/pathway_guides.json` and is also embedded in `index.html` for `file://` reading. `service_worker.js` caches the data file on HTTPS hosting. User guide preferences remain small localStorage keys; character and research state use the unchanged v1 IndexedDB schema. A new export (`pra.sol_public_pathway_draft/v1`) deliberately does not impersonate or modify the earlier `pra.reciprocal_public_handoff/v1` contract.

## Security and zero-harm

Guides are non-operational: no target selection, troop deployment, covert collection, private-person surveillance, offensive cyber, deceptive influence or sanctions evasion. Trystero is separate: entering a room transmits no guide selections or local notes. The online peer lobby discloses metadata exposure and remains manually disconnectable.

## Attributions

Foster + Navi / Planetary Restoration Archive. Original application remains under its accompanying MIT license; all inherited attributions remain intact. New guide text summarizes the official primary-source URLs displayed for each lens, not confidential or endorsed institutional material.
