# Earth Intelligence Engine HUD — user and engineering guide

## Quick guide

Tap **✦ Earth Intelligence** in the fixed character HUD, then choose **Civilian protection**, **Supply-chain evidence**, **Ceasefire assurance**, **Recovery**, or type a question. The engine retrieves relevant archived source records from the five bundled editions, displays the five most relevant independent URLs it can find, and selects one matching public intervention concept. The response includes three counter-hypotheses, source/date cautions and an independent verification gate. It does not claim the selected intervention has worked.

**Save analysis privately** adds a short memo to the same local backup used by the master. **Export cited draft JSON** creates a separate `pra.earth_intelligence_draft/v1` JSON file, clearly marked `PRIVATE_REVIEW_DRAFT` and `autonomy: OFF`. Nothing is automatically shared with peers.

## Processing pipeline

`Question → tokenize locally → match archived source titles & discipline descriptions → deduplicate URLs → heuristic relevance sort → retrieve archived public intervention → display dissent & verification gate → optional save/export`.

There is **no large language model in this version**. The analysis is deterministic retrieval and transparent rule-based scaffolding. Relevance ranks are not probabilities, legal findings or confidence measures. It does not make a fresh internet search or validate an archival citation's present availability.

## Safety and rights model

- Sources and interventions are public archive snapshots from October 14, 2026; users must check current versions before making assertions.
- **No tools are connected to EIE** for outbound action. Research and drafts are local-only. No autonomous emails, publication, negotiation, sanctions, surveillance, military targeting, cyber intrusion, remote access, or self-modification.
- Peer WebRTC never receives EIE questions or notes automatically. Share a separate public-only proposal only after user confirmation.
- The EIE is advisory, not institutional; no record imported from a peer gains verified status or grants permissions.
- This is a first HUD runtime slice of the larger Earth Intelligence Engine. A future optional local WebLLM could assist drafting only after model, privacy, security, capability and independent-review checks, with deterministic fallback retained.

## Reuse and extension

Main HTML functions: `eieTokens`, `eieSourceCandidates`, `eieAnalyze`, `renderEiePanel`. Main state: `st.eieNotes`, validated as at most 60 short notes during import. Source archives remain `ARCHIVE`, supported node IDs in `NODES`. For a larger EIE, keep the same local-first data flow and implement any new capability behind a separately reviewed gateway with explicit permissions. Maintain auditable input/output, provenance and stop rules.

## v2.3: Evidence fail-safe and foundational compass

The HUD now presents six sequential systems-design questions, each with a proposed solution and an observable acceptance test. They progress locally and do not gate use of the application. Archive matching requires actual keyword overlap; unrelated queries return `NO_ARCHIVE_MATCH` and no source or intervention suggestions. The count of archival editions represented does not establish independent corroboration. See `FOUNDATIONAL_PROMPTS.md` for the remaining unsolved questions and their proposed tests.
