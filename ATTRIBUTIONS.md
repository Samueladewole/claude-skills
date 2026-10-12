# Attributions

This collection holds 414 skills. Most are original work by Samuel Adewole and
are covered by the MIT licence in `LICENSE`. The rest are not his to relicense,
and are listed here.

**Check this file before publishing any part of the collection.** A licence
header is an authorship claim, and a blanket one across the whole directory
would be wrong in the specific cases below.

---

## Derived from obra/superpowers (MIT)

Measured by text similarity against the upstream `SKILL.md` on 2026-10-12.
Anything at or above roughly 55% is a derivative work rather than an
independent one, however much it was later edited.

| Skill | Similarity |
|---|---|
| `receiving-code-review` | 97% |
| `systematic-debugging` | 96% |
| `verification-before-completion` | 92% |
| `writing-skills` | 88% |
| `dispatching-parallel-agents` | 85% |
| `test-driven-development` | 71% |
| `requesting-code-review` | 70% |

Upstream: https://github.com/obra/superpowers (MIT, Jesse Vincent).

MIT permits use, modification and redistribution, including commercially. The
one condition is that the copyright notice travels with the work. Each of the
seven now carries `source:` and `license:` in its frontmatter, so that notice
survives a copy-paste out of this directory.

### Same name, independent content

These share a filename with an upstream skill but the text is Samuel's own.
Measured similarity in brackets. No attribution owed; recorded so nobody
assumes otherwise later.

`executing-plans` (1%), `brainstorming` (4%), `finishing-a-development-branch`
(9%), `writing-plans` (12%), `subagent-driven-development` (13%),
`using-git-worktrees` (17%), `using-superpowers` (39%).

---

## Published third-party skills

Redistributed here under their own terms, with the licence recorded. Each
keeps whatever `LICENSE` file and frontmatter it came with.

### Apache 2.0 (12)

`algorithmic-art`, `brand-guidelines`, `canvas-design`, `frontend-design`, `impeccable-impeccable`, `internal-comms`, `mcp-builder`, `skill-creator`, `slack-gif-creator`, `theme-factory`, `web-artifacts-builder`, `webapp-testing`

Mostly Anthropic skills that ship with Claude Code. Apache 2.0 permits
redistribution provided the licence and notices are retained, which they are.

### MIT (19)

`agent-md-refactor`, `building-native-ui`, `database-schema-designer`, `dependency-updater`, `design-system-starter`, `expo-api-routes`, `expo-cicd-workflows`, `expo-deployment`, `expo-dev-client`, `expo-tailwind-setup`, `frontend-slides`, `native-data-fetching`, `react-native-best-practices`, `upgrading-expo`, `use-dom`, `vercel-composition-patterns`, `vercel-react-best-practices`, `vercel-react-native-skills`, `voiceprint`

Largely the Vercel and Expo skill packs. MIT permits redistribution provided
the copyright notice travels with the work. These declare MIT in frontmatter
rather than carrying a LICENSE file, so this entry is that notice.

---

## Not published

### Anthropic proprietary (4)

`docx`, `pdf`, `pptx`, `xlsx`

These carry Anthropic's proprietary licence, which forbids extracting,
copying, distributing or retaining them outside Anthropic's services, and
forbids derivative works. There is no non-commercial exception; the
restrictions do not depend on whether money changes hands.

Nothing is lost by leaving them out. They ship with Claude Code, so anyone
who installs it already has them.

### Third-party packs with no declared licence (30)

`baoyu-article-illustrator`, `baoyu-comic`, `baoyu-compress-image`, `baoyu-cover-image`, `baoyu-danger-gemini-web`, `baoyu-danger-x-to-markdown`, `baoyu-image-gen`, `baoyu-infographic`, `baoyu-post-to-wechat`, `baoyu-post-to-x`, `baoyu-slide-deck`, `baoyu-url-to-markdown`, `baoyu-xhs-images`, `impeccable-adapt`, `impeccable-animate`, `impeccable-audit`, `impeccable-bolder`, `impeccable-clarify`, `impeccable-colorize`, `impeccable-critique`, `impeccable-delight`, `impeccable-distill`, `impeccable-harden`, `impeccable-layout`, `impeccable-optimize`, `impeccable-overdrive`, `impeccable-polish`, `impeccable-quieter`, `impeccable-shape`, `impeccable-typeset`

Not refused on principle, simply unknown. Confirm terms upstream and they can
be published.

### Maintained upstream, install separately

`youtube-clipper` — https://github.com/op7418/Youtube-clipper-skill (MIT)

It ships as its own git repository. Nesting that inside this one made git
record a gitlink with no `.gitmodules`, so clones received an empty directory.
Rather than vendor a copy that would drift, get it from the source:

```bash
git clone https://github.com/op7418/Youtube-clipper-skill.git \
  ~/.agents/skills/youtube-clipper
~/.agents/skills/install.sh --only youtube-clipper
```

### Business asset

`intelligence-briefing-writing` encodes the DSI Advisory house voice. Held
back as a business asset rather than for any licence reason.

---

## Acknowledged influences

`clear-writing` credits Tom Albrighton's *How to Write Clearly*. An idea taken
from a book and rewritten is original expression, so no licence applies. The
credit stands because it is true.
