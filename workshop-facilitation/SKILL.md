---
name: workshop-facilitation
description: Use when designing presentations, workshops, training sessions, onboarding programs, or any structured learning experience. Use when you need to take a group through complex ideas to a specific conclusion, or when preparing to teach, demo, or facilitate.
---

# Workshop Facilitation

## Overview

Running a brilliant workshop is not about charisma or showmanship — it's about following clear rules for structuring and arranging the session. Good design makes good facilitation nearly automatic.

Inspired by Rob Fitzpatrick & Devin Hunt's *The Workshop Survival Guide*.

**Companion skills:** Use `sticky-ideas` for making your content memorable. Use `clear-writing` for written materials. Use `professional-communication` for follow-up communications.

## When to Use

- Designing a workshop, training session, or bootcamp
- Preparing a technical demo or product walkthrough
- Building an onboarding program for new team members
- Creating a presentation that requires audience participation
- Planning a meeting where the group needs to reach a decision
- Structuring a complex explanation that unfolds over time
- Writing educational content (tutorials, courses, guides)

## The Workshop Skeleton

Design the skeleton BEFORE creating any slides or materials. This is your blueprint.

### Step 1: Define the Outcome

Answer one question: **What will participants be able to DO after this session that they couldn't do before?**

Not "understand" — *do.* Measurable, observable outcomes.

| Weak Outcome | Strong Outcome |
|-------------|----------------|
| "Understand our API" | "Integrate a payment endpoint and handle webhooks" |
| "Learn about testing" | "Write a failing test, make it pass, and refactor" |
| "Know our architecture" | "Trace a request from browser to database and back" |

### Step 2: Limit Your Outcomes

**Half-day = ~6 outcomes.** Allocate 30-45 minutes per outcome.
**Full day = ~10-12 outcomes.**

Depth beats breadth. A session that thoroughly covers 4 things beats one that skims 12.

### Step 3: Order by Dependency

Each outcome should build on the previous one. The audience should feel steady progression, not random jumps.

```
Outcome 1: Set up the dev environment
    ↓ (enables)
Outcome 2: Create a basic API route
    ↓ (enables)
Outcome 3: Add database queries with Drizzle
    ↓ (enables)
Outcome 4: Validate input with Zod
    ↓ (enables)
Outcome 5: Add auth middleware
    ↓ (enables)
Outcome 6: Deploy to Railway
```

## Five Teaching Formats

Alternate between these formats every 15-20 minutes to maintain energy and engagement. Never lecture for more than 20 minutes straight.

| Format | What It Is | When to Use | Duration |
|--------|-----------|-------------|----------|
| **Lecture** | You explain a concept | Introducing new ideas, extracting lessons | 10-20 min max |
| **Try It Now** | Hands-on practice | Building skills through doing | 10-30 min |
| **Small Group Discussion** | 2-4 people discuss a prompt | Wrestling with ambiguous questions | 5-15 min |
| **Q&A** | Audience asks, you answer | After each outcome or before breaks | 5-10 min |
| **Scenario Challenge** | Groups solve a realistic problem | Developing judgment and critical thinking | 20-45 min |

### Format Selection Guide

| Knowledge Type | Best Format |
|---------------|-------------|
| Facts and concepts | Lecture → Q&A |
| Practical skills | Lecture → Try It Now |
| Judgment and decision-making | Scenario Challenge |
| Exploring trade-offs | Small Group Discussion |
| Debugging/troubleshooting | Try It Now with intentional errors |

## The Value Nuggets Principle

Think of your session like a game. Each valuable insight = points earned. Boring stretches = points lost.

**The audience expects a constant flow of value.** Every 5-10 minutes should deliver an "aha" moment, a useful technique, or an engaging activity.

Signs you're losing them:
- Phones come out
- Eyes glaze over
- Questions stop
- Side conversations start

**Fix:** Switch format immediately. Call a 2-minute stretch break. Pose a provocative question.

## Schedule Springs

You WILL run behind. Plan for it.

**A schedule spring** is a section you can expand or compress without affecting learning outcomes:

- **Q&A sessions** — can be shortened from 10 to 3 minutes
- **Discussion rounds** — can be cut from 15 to 5 minutes
- **Bonus examples** — can be skipped entirely
- **Extended exercises** — can be shortened to just the core task

**Rule:** Place a spring after every 2-3 outcomes. Mark them in your notes so you can adjust in real-time.

**Structure each outcome block as:**

```
[Core content - NOT compressible]
[Exercise - can be shortened]
[Discussion/Q&A - SPRING, compressible]
[Transition to next outcome]
```

## Slide Strategy

Less is more. Only three slide types needed:

| Slide Type | Purpose | Example |
|-----------|---------|---------|
| **Outcome slide** | State what they'll learn next | "After this section: you can deploy to Railway in under 5 minutes" |
| **Exercise prompt** | Clear instructions for what to do | "1. Clone the repo 2. Run pnpm install 3. Create a .env file with..." |
| **Resource list** | Curated next-step materials | Links to docs, repos, articles |

**Don't create:** Slides full of text you plan to read aloud. Slides with complex diagrams you won't explain. Slides that exist to look impressive.

## Handling Difficult Moments

### Skeptical Audience

Don't ignore it — address it directly.

- "I know some of you are thinking [objection]. Let me address that."
- Acknowledge the concern is valid before explaining your perspective.
- Invite the skeptic to share more — often they become your strongest ally.

### Questions You Can't Answer

Say "I don't know" honestly. Then:
- "I'll find out and follow up after the session"
- "Does anyone here have experience with this?" (leverage the room)
- Write it on a "parking lot" board and return to it

### Running Behind

Compress your springs. Never skip core outcomes — skip the flexible padding around them. If seriously behind, acknowledge it: "We're running tight on time. I'm going to focus on [core thing] and share [skippable thing] as a resource afterward."

### Dead Room (No Engagement)

- Switch to a Try It Now exercise immediately
- Ask a specific person a direct (non-threatening) question
- Share a concrete failure story — vulnerability creates connection

## Designing for Written Content

These principles also apply to tutorials, guides, and documentation:

| Workshop Concept | Written Equivalent |
|-----------------|-------------------|
| Learning outcome | Section goal stated upfront |
| Try It Now | Code snippets the reader runs themselves |
| Discussion prompt | "Consider: why would you choose X over Y?" |
| Scenario challenge | "Exercise: build a [thing] using what you've learned" |
| Schedule spring | "Optional deep dive" or collapsible sections |
| Value nuggets | Tips, warnings, and insights between steps |

## Pre-Session Checklist

- [ ] Outcomes defined (measurable, verb-based "can DO" statements)
- [ ] 6 or fewer outcomes per half-day
- [ ] Outcomes ordered by dependency
- [ ] Format alternates every 15-20 minutes
- [ ] Schedule springs placed after every 2-3 outcomes
- [ ] Exercise prompts are clear and self-contained
- [ ] Materials tested on someone unfamiliar with the topic
- [ ] Backup plan for "what if we run 20 minutes behind?"

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Too many outcomes crammed in | Cut to 6 max. Depth > breadth |
| Lecturing for 40+ minutes | Switch format every 15-20 min |
| Exercises that are too hard | Break into smaller sub-tasks with hints |
| Exercises that are too easy | Add constraints or edge cases |
| No schedule flexibility | Add compressible springs between sections |
| Slides full of text | Use only outcome, exercise, and resource slides |
| Ignoring audience skepticism | Address objections directly and early |
| "Understand X" as an outcome | Use "Can DO X" — observable, measurable |
