---
name: infographic-generator
description: >
  End-to-end workflow for creating infographic image assets. Research a topic,
  design a multi-section HTML layout, and export to PNG via Playwright. Bring
  your own brand book and/or reference images to match your style — or use the
  built-in default design system. Use this skill whenever the user asks to:
  create an infographic, turn a topic into a visual asset, build a carousel
  slide, design an explainer image, or export a layout as PNG. Also trigger on
  phrases like "make an infographic about X", "turn this into a visual",
  "build a 4-section layout", or "export this as a PNG". Works for any platform:
  LinkedIn, blog, newsletter, slides, or print.
compatibility: "Requires Node.js + Playwright. Install: cd /tmp && npm install playwright. No API key needed."
---

# Infographic Generator

End-to-end workflow: research -> layout -> HTML -> PNG. Bring your own brand book and inspiration images, or use the built-in default design system.

---

## Inputs

Collect before starting:

| Input | Required | Notes |
|-------|----------|-------|
| **Topic / title** | Yes | What the infographic is about |
| **Content points** | No | Key points per section. If not provided, run Step 0 first. |
| **Brand book** | No | Brand context — paste inline, drop a file, or describe it. Claude extracts colors, fonts, logo, tone. |
| **Inspiration image** | No | A reference infographic to match the layout structure |
| **Dimensions** | No | `portrait` (default) or `square` |
| **Output path** | No | Defaults to `./output/infographic-[topic].png` |

---

## Canvas Dimensions

| Format | Dimensions | Ratio | Best for |
|--------|-----------|-------|---------|
| **Portrait** (default) | 1080 x 1350px | 4:5 | Mobile-first, 4-section layouts |
| **Square** | 1200 x 1200px | 1:1 | Feed visibility, simpler 2-3 section layouts |

---

## Step 0 — Research (when content isn't provided)

If given a topic but not the specific points, research before building.

- Use WebSearch or WebFetch to gather current data
- For technical deep dives, search multiple sources
- Synthesize into **4 section angles** before writing any HTML

---

## Step 1 — Style Resolution

Determine the design approach before writing any code:

**Priority order:**
1. **Brand book provided** -> Extract: primary/accent colors, font family, logo/monogram, tone. Apply these instead of defaults.
2. **Inspiration image provided** -> Analyze: layout structure, column arrangement, visual hierarchy, section count, card patterns, header/footer treatment.
3. **Both provided** -> Brand book sets colors + fonts. Inspiration image sets layout.
4. **Neither provided** -> Use the built-in default design system (Step 2).

**When analyzing an inspiration image, extract:**
- Number of sections and how they're divided
- Column layout per section (1-col, 2-col, 3-col, grid)
- Header and footer treatment
- Card/box shapes (rounded, sharp, with icons, with tags)
- Typography hierarchy
- Visual accents (circles, arrows, flow diagrams, comparison tables)

---

## Step 2 — Build HTML (Built-in Default Design System)

### Canvas CSS

```css
/* Portrait */
width: 1080px; height: 1350px; background: #EFF4F0;

/* Square */
width: 1200px; height: 1200px; background: #EFF4F0;

display: flex; flex-direction: column; overflow: hidden;
```

### Structure (top to bottom)

| Element | CSS | Notes |
|---------|-----|-------|
| Header | `flex-shrink: 0; border-bottom: 2px solid rgba(26,39,68,0.1)` | Title + subtitle |
| Mechanism strip | `background: #1A2744; flex-shrink: 0` | Optional one-liner core mechanism |
| Sections 1-4 | `flex: 1; display: flex; flex-direction: column` | Equal height |
| Footer | `flex-shrink: 0; height: 58px; background: #1A2744` | Always present |

### Brand Colors

| Role | Hex |
|------|-----|
| Canvas bg | `#EFF4F0` |
| Dark navy | `#1A2744` |
| Light blue | `#6BA3D6` |
| Mid blue | `#4A7FB5` |
| Body text | `#4A4A5A` |
| Secondary text | `#7C7C8A` |
| Card — blue | `#D6E8F5` |
| Card — navy | `#D0D8E8` |
| Card — mint | `#D6EDE0` |
| Card — peach | `#F0E6D6` |
| Card — cream | `#F5F0EB` |
| Card — lilac | `#E4DCF0` |

### Typography

Load from Google Fonts: `Inter` (400/500/600/700/800) + `Playfair Display` (700 italic)

| Element | Spec |
|---------|------|
| Header title | Inter 800, 38-40px, `#1A2744`, letter-spacing -0.02em |
| Header subtitle | Inter 400, 14px, `#7C7C8A` |
| Section title | Inter 800, 16px, `#1A2744` |
| Card title | Inter 700, 12.5px, `#1A2744` |
| Card body | Inter 400, 11.5-12px, `#4A4A5A`, line-height 1.58 |
| Example box text | Inter 400 italic, 11px, `#7C7C8A` |
| Footer mark | Playfair Display italic 700, 15px, white |

### Section Numbered Circles

```css
.s1 { background: #6BA3D6; }  /* blue */
.s2 { background: #1A2744; }  /* navy */
.s3 { background: #4A7FB5; }  /* mid blue */
.s4 { background: #6BA3D6; }  /* blue */
```

Size: 28x28px, border-radius 50%, Inter 800 12px white.

### Section Content Patterns

| Section | Layout | Best for |
|---------|--------|----------|
| 1 | 2-col card grid | Two core concepts |
| 2 | 2-col or 3-col card grid | Feature breakdown, use cases |
| 3 | 1 card + flow diagram, OR 3-col | Process steps, loops |
| 4 | Before/After comparison table | Contrast, results |

**Card anatomy:**
- `card-icon` — 20x20px white square with box-shadow, emoji or symbol
- `card-title` — Inter 700 12.5px, with optional `.card-tag` pill
- `card-body` — descriptive text
- `card-example` (optional) — dashed border box, italic gray text

**Flow steps:** white boxes, centered, numbered blue circle, title, body. Connect with arrows.

**Comparison table:** 2-col grid. `bad` header vs `good` header with colored dots.

### Footer

```html
<div class="footer">
  <div class="logo-mark"><span>S</span></div>
  <div class="footer-name">Samuel Adewole</div>
</div>
```

Logo mark CSS: background `#6BA3D6`, 5px border-radius, Playfair Display italic white letter.

---

## Step 3 — Copy Rules

- **No filler words**: avoid "leveraging," "seamlessly," "powerful," "game-changing," "robust"
- **Titles**: sharp and specific — not generic guides
- **Example boxes**: write real, usable content — not placeholders
- **Tags** (DAILY / WEEKLY / ALWAYS): only use when accurate
- **Section count**: default 4. Use 3 if sparse; never above 4 in portrait.

---

## Step 4 — Export to PNG

**Save HTML to:** `./output/infographic-[topic].html` (relative to project root)

**Screenshot with Playwright:**

```bash
# Install Playwright if not already present (one-time)
cd /tmp && npm install playwright

# Set paths
HTML_FILE="$(pwd)/output/infographic-[topic].html"
PNG_FILE="$(pwd)/output/infographic-[topic].png"

# Create output dir
mkdir -p "$(pwd)/output"

# Export canvas to PNG
cd /tmp && node -e "
const { chromium } = require('playwright');
const htmlFile = process.argv[1];
const pngFile = process.argv[2];
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1200, height: 1500 });
  await page.goto('file://' + htmlFile);
  await page.waitForTimeout(1000);
  const canvas = await page.\$('.canvas');
  await canvas.screenshot({ path: pngFile, type: 'png' });
  await browser.close();
  console.log('Done: ' + pngFile);
})();
" -- "$HTML_FILE" "$PNG_FILE"
```

**Verify:** `ls -lh ./output/infographic-[topic].png` — expect 150K-300K.

> **Image pipeline: HTML -> Playwright -> PNG only. Do not use image generation APIs for infographics.**

---

## Customization Reference

| Thing to change | Where |
|---|---|
| Brand colors | Replace hex values in color table |
| Fonts | Swap Google Fonts import + font-family references |
| Footer name/initial | Edit the `logo-mark` span and `footer-name` div |
| Output directory | Change `./output/` to any path |
| Canvas size | Update canvas CSS + Playwright viewport |
| Section count | Add/remove section blocks; adjust flex distribution |
