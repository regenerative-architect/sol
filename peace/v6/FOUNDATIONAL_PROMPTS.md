# Foundational prompts and sequential solution register

**SOL Peace Commons v2.3 — October 15, 2026**  
Mode: unofficial, public-interest, local-first research and learning prototype. No links to agency systems. These are design questions and demonstrable acceptance tests, not claims to have solved geopolitical bargaining or produced real-world peace outcomes.

## Cycle 1 — implemented and tested

| # | Foundational question to ask | Resolved implementation | Testable acceptance criterion | Status |
|---|---|---|---|---|
| 1 | What meaningful action can a first-time visitor take without choosing a class? | Keep the Fluid Path introduction and reveal one dated source without mandatory setup. | Open a source while preserving the same route; complete the flow with no sidebar. | Tested |
| 2 | Can the Earth Intelligence Engine say **I don't know**? | Remove all zero-term-match source and intervention suggestions; return `NO_ARCHIVE_MATCH`, zero citations, an explicit next research step. | Query nonsense unrelated to the corpus: zero citations and no intervention; query civilian protection: relevant dated links. | Tested |
| 3 | Can unknown peers collaborate without importing claims as authoritative? | Preserve Trystero's public-only, explicit-send protocol and the unverified review queue. No self/peer activity transfers permissions. | Mocked peer receives no alias/notes automatically; manual share strips private review gates. | Tested in mocked transport, not verified over live WebRTC |
| 4 | Does gamification reward learning rather than violence or institutional power? | Retain self-attested learning XP and skill prerequisites, clearly labeled non-certification. | XP/skills remain consistent on backup import; no approval inferred from completing a quest. | Tested in legacy suite |
| 5 | Does the user control connectivity and retain portable data? | Keep visible disconnect, persistent auto-join opt-out, manual JSON backups and memory-only warning. Separate auto-join from all private draft transmission. | Disconnect prevents rejoining; JSON roundtrip remains compatible. | Tested except real HTTPS persistence |
| 6 | What could make a well-intended proposal harmful? | Embed civilian impact, mandate, strongest dissent, independent metric and stop rules in proposal review. Add these as sequential EIE foundational questions. | Five independent review gates remain optional but reviewable; imported gates are not independently certified. | Tested in existing workflow |

## Additional engineering failures found and addressed

**False relevance:** In v2.2 a current research domain boosted unrelated sources, so a completely unrelated question could receive seemingly supportive links. In v2.3 a source must share an actual non-stopword token with the question. This is still keyword retrieval, *not* evidence validation. The status display distinguishes relevance from factual confidence; edition count is not treated as independent corroboration.

**Startup race:** In v2.2 automatic WebRTC setup could render a default profile before IndexedDB restoration finished. v2.3 initializes local storage first and then attempts peer discovery. It also listens for IndexedDB version changes and unexpected closure.

**Ambiguous online signal:** Opening a signaling room is not proof anyone else is connected. The HUD now displays “room open · seeking peers” until remote peers are actually observed, then counts unverified peers.

**Continuity:** Kept `pra.sol_peace_master` backup schema version 1 and `pra.reciprocal_public_handoff/v1` intact. Existing class IDs, XP calculations, five sub-editions, source registries and directory names have not changed.

## Cycle 2 — next unresolved questions, with leading implementation paths

| Proposed question | Why unresolved | Next concrete experiment / stop rule |
|---|---|---|
| 7. Can two independent browsers actually connect to Trystero on the hosted GitHub Pages site? | Test environment denies browser navigation to localhost, and a mock is not a signaling test. | Run on two consenting devices over HTTPS; verify genuine join, loss of connectivity, explicit send, received quarantine and disconnect. Stop claims of live collaboration if no handshake occurs. |
| 8. How can a source assertion reach independently verified status? | Keyword retrieval alone cannot test factual accuracy; source URLs may go stale. | Add human-reviewed claim cards with at least one primary source, date, original document, alternative explanation, revision history and signed adjudication, if trusted identity infrastructure exists. Do not automatically accept peer status. |
| 9. How should private rooms prove membership without making surveillance easier? | Random room codes are not identity authentication; WebRTC and discovery can expose metadata. | Evaluate short-lived invitations, consent disclosure, room-scoped membership verification and revocation; never require real identity for public reading. |
| 10. What is meaningful real-world progress? | XP measures activity, not humanitarian impact. | Distinguish activity telemetry from independently sourced outcome indicators (civilian casualties, access, verified truce violations). Never attribute macro-outcomes to an untested prototype. |
| 11. Is storage durable on ordinary devices? | Browser privacy modes, storage eviction, quota and service worker behavior vary. | Test Hosted HTTPS IndexedDB persistence, import/export after reload and offline precache in desktop/mobile browsers; display honest readiness indicators. |
| 12. How will an intervention change when the evidence turns against it? | Review criteria exist but implementation cannot enforce real-world stop rules. | Add proposal version history with disconfirming observations, a reviewer-controlled withdrawn/paused state and an exportable audit trail. No external action gateway without authority. |

## Future sequencing (not work already performed)

- **First:** live two-browser interoperability and failure-mode tests; keep no automatic content sharing.
- **Second:** provenance-grade claim ledger with corrections and dated source checks; allow explicit uncertainty.
- **Third:** secure, opt-in asynchronous handoffs, with validation and duplicate detection, never automatic trust.
- **Fourth:** independent civilian-outcome observables and stop rules, separated from gamified XP.
- **Fifth:** user-research validation of the simplified journey with reduced-motion and assistive-technology users.

## Principles and sources

- Trystero v0.25+ uses object-style `makeAction` and asynchronous peer join: https://trystero.dev/docs/getting-started/
- Public Nostr relays are discovery services, not guarantees of delivered messages: https://trystero.dev/docs/signaling-strategies/
- IndexedDB is same-origin local storage with possible quota and shutdown errors: https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB
- Untrusted objects must be schema-validated and protected from prototype pollution: https://cheatsheetseries.owasp.org/cheatsheets/JavaScript_and_TypeScript_Security_Cheat_Sheet.html
- Zero-Harm / Anti-Inversion: data received by peers remains untrusted; no covert outreach, surveillance, military targeting or automated institutional action. Any real-world use requires proper authority and specialist review.

**Attributions:** Original SOL Peace Commons implementation by Foster + Navi / Planetary Restoration Archive; source-attribution records and licenses remain in `ATTRIBUTIONS_AND_LICENSES.md`. SHA-256 supports integrity verification, not proof of authorship.
