---
name: setup-idea-to-promise
description: Set up ignored local discovery storage without overwriting project conventions or creating specs.
license: Apache-2.0
metadata:
  version: "0.6.0"
---

Read [the discovery protocol](references/discovery-protocol.md) before acting.
Bundled templates are optional aids, not a mandatory artifact checklist.

# Set up a project for discovery

Read project instructions and determine the actual Git repository root. Inspect
existing .itp paths, Git tracking and ignore rules before writing. Do not reserve
specs/ or edit AGENTS.md, the P2P configuration, source documents or tracker settings.

Run the bundled `scripts/setup_project.py --root <project>` to preview. With user
authority for the described local setup run again with `--apply`. A direct request
to set up ITP covers only .itp/work/ creation and the shown ignore-rule addition.
Preserve existing ignore-file bytes. Stop on tracked discovery files, symlinks,
wrong-type paths, or uncertain project identity rather than deleting or moving them.

Run without concurrent filesystem edits. Reread the result; report any partial
local effects honestly. The helper is idempotent, uses Git but no network, and
never stages or commits. For a non-Git host, explain the storage/privacy limitation
and continue discovery inline instead of pretending the helper succeeded.

Explain `/discover <idea>` and the optional quick/normal/deep modes. Setup is not
required for an informal conversation and does not approve a promise or start P2P.
