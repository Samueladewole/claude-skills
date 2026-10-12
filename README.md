# Claude Skills

348 skills for Claude Code. A skill is a folder holding a `SKILL.md`: a
description that says when it applies, and instructions for what to do when it
does. Claude loads one on its own when your work matches the description. You
never type a command.

Written by Samuel Adewole over several years of real project work. MIT
licensed, see `LICENSE`. A few are derived from other people's work and are
credited in `ATTRIBUTIONS.md`.

## Install

**1. Have Claude Code installed.**

```bash
npm install -g @anthropic-ai/claude-code
```

**2. Clone this repo somewhere permanent.** Not a temp folder; the install
links to it rather than copying, so it needs to stay put.

```bash
git clone https://github.com/Samueladewole/claude-skills.git ~/.agents/skills
```

**3. Run the installer.**

```bash
cd ~/.agents/skills
./install.sh
```

It symlinks each skill into `~/.claude/skills/`, where Claude Code looks for
them. Symlinks rather than copies, so `git pull` updates every skill at once.
Anything already in `~/.claude/skills` is left alone.

**4. Check it worked.**

```bash
ls ~/.claude/skills | head
claude
```

Then ask Claude something that should trigger one, for example "there's a bug
in this function and I can't work out why." It should reach for a debugging
skill without being told to.

## Install only some of them

348 skills is a lot, and most will not apply to your stack. To start with a
handful:

```bash
./install.sh --only writing-plans executing-plans reducing-entropy
```

This is the better first move. Install a few, notice which actually fire on
your work, add more when you miss something.

## Uninstall

```bash
./install.sh --uninstall
```

Removes only the symlinks this installer created. Your own skills stay.

## Writing your own

A skill is one folder and one file:

```
~/.claude/skills/reviewing-migrations/SKILL.md
```

```markdown
---
name: reviewing-migrations
description: Use when writing or reviewing a database migration, before it runs
  anywhere — checks reversibility, locking, and data loss.
---

# Reviewing Migrations

Before any migration is applied:

1. Can it be reversed? If not, say so explicitly and explain why.
2. Will it lock a large table? Name the table and estimate the row count.
3. Does it drop or narrow a column? That is data loss. Confirm it is intended.
```

**The `description` is the most important line.** It is not documentation, it
is the trigger. Write it as "Use when…" and name the situation concretely. A
vague description means the skill either never fires or fires constantly.

## What is not in here

Some skills on my machine are not in this repo, because they are not mine to
publish: Anthropic's bundled skills, a few third-party packs, and one that
encodes a client's house voice. `ATTRIBUTIONS.md` lists them. Nothing is
missing that you cannot get from its own source.

## Licence

MIT, see `LICENSE`. Read `ATTRIBUTIONS.md` before redistributing any part of
this collection.
