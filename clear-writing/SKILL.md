---
name: clear-writing
description: Use when writing documentation, explanations, proposals, or any prose where the goal is transmitting ideas from your head into the reader's mind. Use when drafting feels unclear, when feedback says "I don't understand," or when writing for an audience with different expertise than yours.
---

# Clear Writing

## Overview

Clear writing is not about following grammar rules — it's about getting ideas out of your head and into someone else's. The words and the page are just tools to make that happen.

Inspired by Tom Albrighton's *How to Write Clearly*.

**Companion skills:** Use `writing-clearly-and-concisely` for grammar/composition mechanics (Strunk). Use `professional-communication` for email/meeting formats. This skill covers the *thinking* layer underneath both.

## When to Use

- Writing docs, READMEs, proposals, technical explanations
- Explaining a concept to someone with different expertise
- Drafting feels "right to you" but confusing to others
- Reviewing your own writing before publishing
- Translating complex technical decisions into plain language

## The Reader-First Principle

Content is what you say. **Context determines what the reader hears.**

Before writing anything, answer:

| Question | Why It Matters |
|----------|---------------|
| Who is reading this? | Vocabulary, depth, and tone depend on audience |
| What do they already know? | Start where they are, not where you are |
| What do they need to do after reading? | Shape the writing toward their next action |
| What objections will they have? | Address resistance before it forms |

**The Curse of Knowledge:** Once you understand something deeply, you forget what it was like not to know it. This is the #1 cause of unclear writing. You skip steps, use jargon, and assume shared context that doesn't exist.

**Fix:** Before writing, imagine explaining it to a smart colleague who just joined the team yesterday.

## Five Layers of Clear Writing

Work through these in order. Each layer builds on the previous one.

### 1. Think Before You Write

Don't start typing. Start by answering:
- What is the ONE thing I need the reader to understand?
- What's the simplest way to say it?
- What's the logical order?

**If you can't explain it in one sentence, you don't understand it well enough to write about it.**

### 2. Structure for Scanning

Readers don't read — they scan. Structure accordingly:

- **Lead with the conclusion.** Don't build up to it. State it, then support it.
- **One idea per paragraph.** If a paragraph covers two ideas, split it.
- **Topic sentences.** The first sentence of each paragraph states what the paragraph is about. The rest provides evidence, examples, or detail.
- **Short paragraphs.** 3-5 sentences max. White space is your friend.
- **Headers as a table of contents.** A reader should grasp your argument from headers alone.

### 3. Choose Words That Transmit

| Do This | Not This |
|---------|----------|
| Use concrete nouns and active verbs | Abstract nouns and passive constructions |
| "The server rejects the request" | "Request rejection is performed by the server" |
| Short, common words | Long, impressive-sounding words |
| "use" | "utilize" |
| "start" | "commence" |
| "help" | "facilitate" |
| One precise word | Three vague ones |
| "fast" | "in a quick and efficient manner" |

**Jargon rule:** Use jargon only when writing for people who share it. If in doubt, define it on first use.

### 4. Build Empathy Into the Text

- **Acknowledge what the reader is thinking.** "You might wonder why we don't just..." addresses resistance directly.
- **Use "you" and "we."** It creates conversation, not lecture.
- **Anticipate confusion.** If something could be misread, it will be. Rewrite it.
- **Provide context for decisions.** Don't just say what — say why. "We chose PostgreSQL over MongoDB because our data is highly relational" beats "We use PostgreSQL."

### 5. Edit Ruthlessly

First draft = getting ideas down. Editing = making them clear.

**Three editing passes:**

1. **Structure pass:** Is the order logical? Does each section earn its place? Cut anything that doesn't serve the reader's goal.
2. **Clarity pass:** Read each sentence. Can it be misunderstood? Is there a shorter way to say it? Kill filler words ("basically," "actually," "in order to," "it should be noted that").
3. **Voice pass:** Read it aloud. Does it sound like a human wrote it? Fix anything that sounds robotic or bureaucratic.

## Quick Diagnostic

Run this checklist on any piece of writing:

- [ ] Can a reader grasp the main point in the first two sentences?
- [ ] Does each paragraph start with a topic sentence?
- [ ] Are all paragraphs under 5 sentences?
- [ ] Is every technical term either shared jargon or defined?
- [ ] Does the structure work if the reader only reads headers?
- [ ] Have you said why, not just what?
- [ ] Read aloud: does it sound natural?

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Starting with background instead of the point | Lead with the conclusion, then context |
| Writing for yourself instead of the reader | Re-read as if you know nothing about the topic |
| Hedging everything ("it might be possible that...") | Commit to a statement. Qualify only when genuinely uncertain |
| Explaining how you arrived at the answer | Explain the answer. Save the journey for an appendix |
| Walls of text with no structure | Headers, bullets, short paragraphs |
| Using three words where one works | "in order to" → "to", "at this point in time" → "now" |
