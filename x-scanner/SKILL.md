---
name: x-scanner
description: >
  Scan X/Twitter for recent posts from a curated list of AI creators, tech builders,
  and news accounts using xAI's Grok API with the x_search tool. Use this skill whenever
  the user asks to: check what's happening on AI Twitter, scan X for news, pull recent
  tweets from creators, get an AI news digest, find trending topics, or generate content
  ideas from X. Also trigger on phrases like "what's trending on X", "scan Twitter",
  "AI news today". Requires XAI_API_KEY env var.
---

# X/Twitter Scanner

## What This Does

Uses xAI's Grok API with the built-in `x_search` tool to scan X/Twitter for recent posts.
Grok has native X data access — one API call handles search, filtering, and summarization.
No separate Twitter API credentials needed.

## Setup

Set `XAI_API_KEY` as environment variable (in `.zshrc` or `.env`).

Get an API key from https://x.ai/api

## How It Works

The script calls `https://api.x.ai/v1/responses` with the `x_search` tool enabled.
Grok searches X in real-time and returns a summarized digest.

## Accounts to Monitor

Edit the `DEFAULT_HANDLES` list in `scan_x.py` to customize.

**AI Labs / Products:**
- @AnthropicAI, @OpenAI, @GoogleAI, @cursor_ai

**AI Practitioners / Researchers:**
- @karpathy, @AndrewYNg, @sama, @OfficialLoganK, @mattshumer_

**Builders / Solopreneurs:**
- @gregisenberg, @levelsio, @itsolelehmann

**AI News / Commentary:**
- @TheRundownAI, @aakashg0, @WesRoth

**African Tech / Regulatory:**
- @TechCabal, @Aboroseh, @NDPCNigeria

## Flagging System

Posts marked `[FLAGGED]` when they hit:
- Breaking product launch or major feature drop
- Real revenue/growth numbers shared publicly
- Genuinely contrarian take on AI narratives
- Workflow that fits "1 person + AI > 10 people"
- High engagement: >500 likes or replies blowing up
- Relevant to: AI implementation, solopreneurship, African tech, regulatory compliance

## Usage

### Quick scan (last 12 hours)
```bash
python <skill-directory>/scripts/scan_x.py
```

### Custom time window
```bash
python <skill-directory>/scripts/scan_x.py --hours 6
```

### Specific accounts only
```bash
python <skill-directory>/scripts/scan_x.py --handles karpathy sama AnthropicAI
```

### Freeform X search
```bash
python <skill-directory>/scripts/scan_x.py --query "NDPA compliance 2026"
```

### Summary only
```bash
python <skill-directory>/scripts/scan_x.py --summary-only
```

## Default Workflow

1. Run `scan_x.py` to pull recent posts
2. If script fails (key expired, rate limited), fall back to WebSearch
3. Summarize top 5-8 stories (1-2 sentences each, with source link)
4. Present digest to user
5. **STOP.** Do NOT generate content ideas unless explicitly asked.
