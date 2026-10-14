# Financial Integrity Research OS — U.S. Secret Service-focused edition

**Status:** Unofficial public-interest, non-sensitive, offline-capable research prototype. **Snapshot date:** 2026-10-14. Created for Foster + Navi / Planetary Restoration Archive. No association, approval, accreditation or computer connection to the U.S. Secret Service or any other public agency. Not a law-enforcement or intelligence operational system.

## Purpose

Provide a verifiable public-source SITREP, a carefully scoped nonviolent suppression/disruption framework against **illegal procurement and financial fraud**, a local evidence-review register, a SHA-256 fingerprint utility, and an unsubmitted portable handoff JSON format for future separately governed reciprocal nodes.

Do not treat an allegation as a conviction. Do not assume that a component manufacturer's name found in a Russian weapon means the manufacturer knowingly supplied the Russian military. Do not treat income from ordinary commerce as proof of intent to prolong war. Do not include sensitive personal information, confidential SAR content, classified data, surveillance data or credentials.

## Launch

**Simple offline, `file://`:** Unzip the entire folder and open `index.html` in a modern desktop/mobile browser. Each module has a directly navigable `index.html`. No external files, remote fonts, APIs or build tools are required. Local IndexedDB behavior varies by browser and file-mode settings; if unavailable, the interface explicitly shows memory-only storage and allows backups. Live websites linked as primary sources do not work offline unless separately obtained.

**Hosted/PWA:** Serve the unzipped directory via HTTPS or localhost. `service_worker.js` can precache the seven HTML pages, JS, CSS and source registry. It cannot enable offline access to remote primary source websites or agency systems. PWA updates are versioned, activate safely after old clients close. Example local preview: `python3 -m http.server 8000 --directory usss_integrity_os` and open `http://localhost:8000/`.

**Mobile:** The side drawer supports Escape and focus cycling, the site supports screen readers, semantic links, keyboard controls, reduced-motion preferences, and light/dark display. Print from the browser; nonessential navigation is suppressed in print CSS.

## File tree

```
index.html                           Shared-shell entry point
modules/sitrep/index.html            Source-dated situation report
modules/review/index.html            Lead register/editor
modules/evidence/index.html          Evidentiary thresholds & local file hash
modules/framework/index.html         Lawful disruption sequence & checklist
modules/nodes/index.html             Draft reciprocal handoff contract
modules/governance/index.html        Privacy, logging and backup controls
assets/app.js                        Route registry, views, validation, IndexedDB
assets/styles.css                    Responsive, print, dark/light and reduced motion
assets/icon.svg                      Original geometric mark; not agency branding
service_worker.js                    Versioned optional local asset precache
site.webmanifest                     Hosted install metadata
data/sources.json                    Dated public primary-source index
data/handoff_schema.json             Non-sensitive interoperability sample
LICENSE                              MIT sample code license
```

## Documentation and boundaries

- **USSS scope:** U.S. Secret Service Cyber Fraud Task Forces address cyber-enabled financial crime and partner across public/private institutions. Export controls, customs smuggling, national-security investigations and prosecution have separate responsible agencies, such as BIS/OEE, HSI, FBI and DOJ. The USSS is not asserted to command these cases.
- **Cross-agency nodes:** The FBI, CIA, DoD, BIS and UN descriptors are only future schema concepts. No API, permissions, identity credentials, secure sharing or autonomous reporting are present. Any real connection needs a separately authorized/secured gateway, purpose limits, agreed jurisdiction, classification handling, encryption, provenance signatures, audit receipts and human oversight.
- **No central server:** IndexedDB stores non-sensitive lead notes and an ordinary local action log. localStorage saves theme/checklist. No automatic sync between devices, no data uplink. The action log is not a tamper-proof legal chain of custody.
- **Backup/export:** JSON schema version 2, validated imports from v1/v2, explicit conflict choices (keep, overwrite, copy), maximum 200 leads and 2 MiB imports. Duplicate IDs inside an import are rejected. The importer does not trust imported audit events. Exports require manual action.
- **Integrity:** SHA-256 fingerprints *bytes*, not authorship or truth. Browser crypto may require HTTPS or localhost. Files are not uploaded/stored. A future real evidence system would need verified custody, cryptographic signatures and access controls.
- **Feedback:** Correct inaccurate facts by editing local notes or the source-dated static briefing, preserving date and source URL. Verify published pages independently before operational reliance.
- **No covert action:** This public package cannot and should not initiate surveillance, hacking, asset freezes, import holds, interdiction or official tips. It only offers compliance-oriented thinking and human-reviewed referral preparation.

## Evidence standard

A. Physical artifact verified; B. manufacturer and production provenance; C. records of exporter and importer; D. actual military end-use traceability; E. evidence of **knowing unlawful facilitation**. Gate E requires an applicable prohibition plus proof of the actor's participation and knowledge. Public judicial admissions can be strong evidence; designations and media reports must be characterized correctly. No causal finding about desire to prolong war follows from commercial revenues alone.

## Sources (as reviewed for this edition)

- U.S. Secret Service, [Cyber Fraud Task Forces](https://www.secretservice.gov/contact/field-offices/)
- U.S. Commerce BIS, [Identify red flags](https://www.bis.gov/enforcement/identify-red-flags)
- DOJ, [Goltsev and Nasriddinov guilty pleas, 2024-07-09](https://www.justice.gov/usao-edny/pr/brooklyn-resident-and-canadian-national-plead-guilty-multi-million-dollar-export-control-0)
- DOJ, [Shevlyakov guilty plea, 2026-07-23](https://www.justice.gov/usao-edny/pr/estonian-national-pleads-guilty-exporting-electronics-benefit-russian-military)
- DOJ, [Yermolenko guilty plea, 2024-11-01](https://www.justice.gov/usao-edny/pr/us-and-russian-national-pleads-guilty-helping-russias-defense-sector-evade-us-export)
- DOJ, [Ilya Kahn guilty plea, 2024-11-07](https://www.justice.gov/usao-edny/pr/businessman-pleads-guilty-export-tax-charges-connection-shipments-other-sensitive)

Citations and sources in the OS point to official sources. These are historical cases and **not** proof that a network currently operates in October 2026.

## Future reciprocal node requirements

1. A human-approved, organization-owned identity and governance contract.
2. A public-only contract restricted to the receiving organization's authorized scope.
3. Secure transport, mutual authentication and role-based purpose limits for any live implementation.
4. Versions/migrations, revocation/correction procedures, privacy impact and legal review.
5. Authenticated acknowledgment and nonrepudiable event records, without covert transfers.
6. Ability to refuse, revise, or disconnect without corrupting local records.

## Attribution, licensing and reuse

Original modular application code is licensed under MIT (see `LICENSE`). The source material is cited through links and not represented as owned or endorsed by this project. Design the next editions as independently scoped nodes, not cosmetic relabelings of a common police/intelligence interface.
