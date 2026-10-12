# Voiceprint

Edit a draft so it reads like a person wrote it — clearer, more direct, free of AI tells — without sanding off the writer's voice.

Most "de-slop" tools have one failure mode: they remove the machine patterns and leave behind clean, correct, forgettable prose. Correct-and-forgettable is its own tell. Voiceprint protects the fingerprint of the person who wrote the draft first, and edits around it second.

## What makes it different

- **The lightest edit that works.** Fix what's broken, leave what's working. A rough draft with a real voice still sounds like the same person afterward — only sharper.
- **Reads the register first.** A threat briefing, a landing page, and a Slack message want different things. If you have a register-specific skill installed, Voiceprint defers to it for structure and voice and applies tell-removal on top, rather than flattening everything into the same house polish.
- **Detect without guessing.** Ask "is this AI slop?" and it names each pattern with the exact line quoted and a short fix — evidence you can check yourself. It won't score your draft or claim to know a machine wrote it, because no honest tool can.
- **Checks its own work.** Every edit is graded against a built-in rubric (`eval.md`) before it comes back.

## What it catches

Manufactured contrast ("it's not X, it's Y"), throat-clearing openers, lone-expert setups, colon drama, pseudo-analysis `-ing` clauses, importance puffery, weasel attribution, hollow strong verbs, synonym rotation, negative stacking, fragment drama, machine rhythm, rhetorical bait, profound kickers, recap endings — plus cut-on-sight machine vocabulary, em-dash overuse, and formatting slop.

## Install

Drop the `voiceprint/` folder into your skills directory (for Claude Code: `~/.agents/skills/voiceprint/`, symlinked from `~/.claude/skills/voiceprint`). Then invoke it by name.

## Use

**Edit a draft.** Paste it and ask for a Voiceprint edit. You get the edited draft and a short **What changed** note — what was cut, what was deliberately kept, and whether it deferred to a register skill.

**Audit a draft.** Ask "is this AI slop?" or "audit this without rewriting." You get every tell it found, each with the quoted line and a short fix.

## Files

- `SKILL.md` — the editing stance, register routing, tell library, and workflow.
- `eval.md` — the pass/fail checks the skill runs on its own edits.

## License

MIT. See `LICENSE`.
