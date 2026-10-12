---
name: video-performance-analyzer
description: >
  Analyze a short-form video (TikTok, Instagram Reel, YouTube Short, or any MP4) to extract
  its full transcript, understand why it performed, and generate concrete repurposing ideas.
  Use this skill whenever the user asks to: analyze a video, understand why something went
  viral, reverse-engineer a creator's content, extract a transcript from a video, figure out
  what makes a video perform, or get repurposing ideas from a video. Also trigger when the
  user says things like "why did this perform", "what's the hook here", "can I repurpose this",
  "analyze this TikTok/Reel", or drops a video file path or URL.
compatibility: "Requires GEMINI_API_KEY env var. Install: pip install google-genai"
---

# Video Performance Analyzer

## What This Skill Does

Takes a short-form video (MP4 file or YouTube URL) and returns:

1. **Full transcript** — every spoken word, on-screen text, audio cues, with timestamps
2. **Performance analysis** — why it works, mapped against proven growth frameworks
3. **Repurposing playbook** — concrete content ideas derived from the video

---

## Setup

**API Key:** Set `GEMINI_API_KEY` as environment variable (in `.zshrc` or `.env`)

**Install dependency (one-time):**
```bash
pip install google-genai
```

**Script location:** `<skill-directory>/scripts/analyze_video.py`

---

## Input Formats

| Format | How to pass it | Notes |
|--------|---------------|-------|
| Local MP4 file | File path as argument | Any size up to 2GB (free) / 20GB (paid) |
| YouTube URL | URL as argument | Public videos only |
| TikTok / Instagram | Download first with `yt-dlp`, then pass MP4 path | `yt-dlp -o video.mp4 <URL>` |

---

## Running the Analysis

### Quick run
```bash
python <skill-directory>/scripts/analyze_video.py /path/to/video.mp4
```

### YouTube URL
```bash
python <skill-directory>/scripts/analyze_video.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### With output saved to file
```bash
python <skill-directory>/scripts/analyze_video.py /path/to/video.mp4 --output /path/to/output.md
```

### Download + analyze Instagram Reel / TikTok (two-step)
```bash
yt-dlp -o /tmp/reel.mp4 "https://www.instagram.com/reel/XXXX/"
python <skill-directory>/scripts/analyze_video.py /tmp/reel.mp4 --output ~/Desktop/analysis.md
```

---

## Analysis Workflow

### Step 1: Run the script

The script will:
- Upload the video to Gemini Files API (or pass YouTube URL directly)
- Wait for processing (usually 10-30 seconds)
- Send the analysis prompt to Gemini
- Return structured Markdown output

### Step 2: Map against growth frameworks

After the script returns, interpret output through these dimensions:

**Hook — "The Hook Is a Contract"**
- Did the hook make the viewer feel implicated, called out, or urgently curious?
- 5 hook techniques: Contradiction, Specific number + unexpected context, Direct accusation, Stolen thought, Absurd reframe
- Framing trick: deliberate word choice that raises perceived stakes

**Structure — Progressive Intrigue**
- Map each timestamp beat and score whether stakes escalate beat-to-beat
- "therefore/but" chain — does each beat cause the next, or just follow it?
- Identify where information gaps open and close

**Credibility — Specificity Signal**
- Count concrete numbers, named people, specific dates, dollar amounts
- "Documentary proof" moments (showing receipts/sources visually)
- Generic claims = weak. Named + numbered claims = strong.

**Framing — Reader-First**
- Is the video about the creator's achievement, or the viewer's situation?
- Personal milestone framing = performs with existing audience, dies everywhere else

**Retention — Visual Pattern Interrupts**
- Visual change frequency: every 5-10s is the target
- Transitions, overlays, text cards, B-roll cuts that reset attention

**CTA — Loop-Closing vs. Loop-Opening**
- Best CTAs create a condition where following is the obvious next move
- Weak: "like and follow" / Strong: "we'll see what happens" (forward momentum)

### Step 3: Generate repurposing ideas

For each idea:
- Format (short-form video, LinkedIn post, X thread, newsletter)
- Hook/banner
- Content pillar mapping
- Funnel stage (TOFU / MOFU / BOFU)

**Sources to mine:**
- Strongest single claim → standalone hot take
- "Before/after" or "X vs. Y" implicit in narrative → comparison format
- Step-by-step workflow → listicle or tools video
- Emotional core (fear, surprise, outrage, relief) → personal angle script
- Stats/numbers → data-driven short-form
- Contrarian framing → X thread or newsletter hook

---

## Output Format

### 1. Full Transcript
Timestamped, verbatim. On-screen text overlays noted inline.

### 2. Visual & Audio Breakdown
- Format, background/set quality, music/audio tone, visual change frequency

### 3. Performance Scorecard

| Dimension | Score | Notes |
|-----------|-------|-------|
| Hook strength | | |
| Progressive intrigue | | |
| Specificity / credibility | | |
| Reader-first framing | | |
| Visual pattern interrupts | | |
| CTA quality | | |

### 4. Repurposing Playbook (4-8 ideas, at least 2 immediately scriptable)

### 5. What to Steal (3-5 specific, actionable techniques)

---

## Model Selection

- **Default:** `gemini-2.5-flash` — best balance of speed + video understanding
- **Premium:** `gemini-2.5-pro` — use for longer videos or deeper analysis (pass `--model gemini-2.5-pro`)
- **Free tier limits:** 8 hours of YouTube video/day. Short-form videos are well within limits.
