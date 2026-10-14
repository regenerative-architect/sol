# Deployment and rollback — Convergence Worlds 2.0

## Before replacing the previous master

1. Open the old master and **export a JSON backup** of local projects/quests. Prefer saving an additional copy offline.
2. Preserve your existing `/sol/peace/` files in a tagged repository commit or separate ZIP. The new bundle already contains copies from your supplied `peace.zip` but cannot guarantee it reflects independent edits made later in the GitHub repository.
3. Compare the five included edition folders (`usmc`, `usss`, `cia`, `fbi`, `un`) with your deployed site. Do not overwrite newer changes without merging them.

## Publish

Unzip `sol_peace_unified_bundle.zip`. It contains `peace/`. Copy the **contents** of `peace/` to `/sol/peace/` in the GitHub Pages repository (the path matching `https://regenerative-architect.github.io/sol/peace/`). Commit the files and wait for Pages to deploy. This package does not push to GitHub or send network communications on its own.

Check master `/sol/peace/`, native `#/atlas`, `#/campaign` and the five folder entries `/sol/peace/usmc/`, `/usss/`, `/cia/`, `/fbi/`, `/un/`. Verify data import/export, an inline quest submission, a skill unlock and a local page reload.

## Offline / PWA

Hosted HTTPS can install a versioned shell cache; the root SW precaches the master and the five edition **entry points and main assets**, plus a public JSON mirror. Other modules are cached **only after they are visited while online**. The latest source updates are not fetched in the background. Visit and refresh core sections online before assuming they will be available offline. `file://` cannot use service workers. Imported local data does not synchronize across devices automatically.

## Multiplayer validation

Test with **two consenting devices** and a securely communicated random room code. Join from both. Confirm room discovery, receiving a deliberately shared public project in the unverified inbox, disconnection, and JSON fallback. This step has not been performed in this build environment. Do not use confidential or personal records during tests.

## Rollback

Restore the prior Git commit or ZIP, then re-import a matching backup if needed. The master intentionally retains character backup schema version 1 and public handoff v1. Clear old cached resources only when necessary and after exporting progress. Avoid destructive reset during migration.
