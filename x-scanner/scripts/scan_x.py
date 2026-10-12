#!/usr/bin/env python3
"""
X/Twitter Scanner — uses xAI's Grok API with x_search tool to pull
recent posts from AI creators and news accounts.

Usage:
    python scan_x.py                         # default scan, all accounts
    python scan_x.py --hours 6               # last 6 hours
    python scan_x.py --handles karpathy sama # specific accounts only
    python scan_x.py --query "Claude update" # freeform X search

Output: JSON to stdout with Grok's summarized findings.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

DEFAULT_HANDLES = [
    # AI Labs / Products
    "AnthropicAI",
    "OpenAI",
    "GoogleAI",
    "cursor_ai",
    # AI Practitioners / Researchers
    "karpathy",
    "AndrewYNg",
    "sama",
    "OfficialLoganK",
    "mattshumer_",
    # Builders / Solopreneurs
    "gregisenberg",
    "levelsio",
    "itsolelehmann",
    # AI News / Commentary
    "TheRundownAI",
    "aakashg0",
    "WesRoth",
    # African Tech / Regulatory
    "TechCabal",
    "Aboroseh",
    "NDPCNigeria",
]

FLAG_CRITERIA = """
Mark a post as [FLAGGED] if it hits ANY of these:
- Breaking product launch or major feature drop (Claude, GPT, Gemini, Cursor, etc.)
- Real revenue/growth numbers shared publicly (MRR, ARR, user counts, conversion rates)
- Genuinely contrarian take that challenges mainstream AI narratives
- A workflow, system, or tool that fits "1 person + AI > 10 people"
- High engagement signal: viral post, >500 likes, or replies blowing up
- Anything relevant to: AI implementation, solopreneurship, African tech, regulatory compliance, GRC
"""

XAI_API_URL = "https://api.x.ai/v1/responses"
XAI_MODEL = "grok-3-fast"


def load_api_key() -> str:
    """Load xAI API key from environment."""
    key = os.environ.get("XAI_API_KEY", "")
    if not key:
        for env_path in [Path.cwd() / ".env", Path.home() / ".env"]:
            if env_path.exists():
                with open(env_path) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("XAI_API_KEY="):
                            return line.split("=", 1)[1].strip().strip('"').strip("'")
        print("ERROR: XAI_API_KEY not found in environment.", file=sys.stderr)
        print("Set it: export XAI_API_KEY=your_key", file=sys.stderr)
        sys.exit(1)
    return key


def call_grok_x_search(api_key: str, prompt: str, from_date: str | None = None, to_date: str | None = None):
    """Call the xAI Grok API with x_search tool enabled."""
    tool_config: dict = {"type": "x_search"}
    if from_date:
        tool_config["from_date"] = from_date
    if to_date:
        tool_config["to_date"] = to_date

    payload = {
        "model": XAI_MODEL,
        "input": [{"role": "user", "content": prompt}],
        "tools": [tool_config],
    }

    data = json.dumps(payload).encode("utf-8")
    req = Request(XAI_API_URL, data=data, method="POST")
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "curl/7.81.0")

    try:
        with urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        error_body = e.read().decode() if e.fp else ""
        print(f"API error {e.code}: {error_body}", file=sys.stderr)
        if e.code == 429:
            print("Rate limited. Try again later.", file=sys.stderr)
        return None
    except URLError as e:
        print(f"Network error: {e.reason}", file=sys.stderr)
        return None


def extract_text_from_response(response: dict | None) -> str:
    """Extract text content from the Grok API response."""
    if not response:
        return ""

    output = response.get("output", [])
    texts: list[str] = []
    for item in output:
        if item.get("type") == "message":
            content = item.get("content", [])
            for block in content:
                if block.get("type") == "output_text":
                    texts.append(block.get("text", ""))
        if "text" in item:
            texts.append(item["text"])

    if not texts:
        if "output_text" in response:
            texts.append(response["output_text"])
        choices = response.get("choices", [])
        for choice in choices:
            msg = choice.get("message", {})
            if "content" in msg:
                texts.append(msg["content"])

    return "\n".join(texts)


def scan_accounts(handles: list[str], api_key: str, hours: int) -> dict:
    """Scan accounts by asking Grok to search X for their recent posts."""
    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=hours)
    from_date = since.strftime("%Y-%m-%d")
    to_date = now.strftime("%Y-%m-%d")

    handles_str = ", ".join(f"@{h}" for h in handles)

    prompt = f"""Search X/Twitter for the most recent and noteworthy posts from these accounts in the last {hours} hours: {handles_str}

Return exactly 10 top posts (or as many as exist if fewer than 10). Rank by relevance to someone building AI-powered products, creating content about AI implementation, and running lean operations. Prioritize: AI product launches, real revenue/growth data, workflows, content creation tactics, African tech/regulatory news, and contrarian takes. Engagement is a secondary signal.

For each post, provide:
1. The account handle
2. A 1-2 sentence summary of the post
3. Engagement metrics if visible (likes, retweets, replies)
4. The post URL

{FLAG_CRITERIA}

Format:

[FLAGGED] @handle — summary of post (likes: X, retweets: Y) — url
@handle — summary of post (likes: X) — url

Put all [FLAGGED] posts at the top, then the rest below.

If fewer than 10 posts in this window, fill remaining with highest-engagement AI-related posts from the broader X feed. Label these [DISCOVERY].

Skip: retweets of old content, generic motivational posts, pure promo with no substance."""

    response = call_grok_x_search(api_key, prompt, from_date=from_date, to_date=to_date)
    summary = extract_text_from_response(response)

    return {
        "scan_time": now.isoformat(),
        "hours_back": hours,
        "accounts_queried": handles,
        "from_date": from_date,
        "to_date": to_date,
        "summary": summary,
    }


def search_topic(query: str, api_key: str, hours: int) -> dict:
    """Search X for a specific topic or query."""
    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=hours)
    from_date = since.strftime("%Y-%m-%d")
    to_date = now.strftime("%Y-%m-%d")

    prompt = f"""Search X/Twitter for the most recent and noteworthy posts about: {query}

Look at the last {hours} hours. Provide:
1. The most discussed angles and opinions
2. Key posts with author handles and URLs
3. Any breaking news or announcements
4. Engagement levels where visible

Focus on substantive posts with real information, not generic takes."""

    response = call_grok_x_search(api_key, prompt, from_date=from_date, to_date=to_date)
    summary = extract_text_from_response(response)

    return {
        "scan_time": now.isoformat(),
        "query": query,
        "hours_back": hours,
        "from_date": from_date,
        "to_date": to_date,
        "summary": summary,
    }


def main():
    parser = argparse.ArgumentParser(description="Scan X/Twitter via xAI Grok API")
    parser.add_argument("--hours", type=int, default=12, help="Hours to look back (default: 12)")
    parser.add_argument("--handles", nargs="+", default=None, help="Specific handles to scan")
    parser.add_argument("--query", type=str, default=None, help="Freeform search query")
    parser.add_argument("--summary-only", action="store_true", help="Print only summary text")
    args = parser.parse_args()

    api_key = load_api_key()
    handles = args.handles or DEFAULT_HANDLES

    if args.query:
        result = search_topic(args.query, api_key, args.hours)
    else:
        result = scan_accounts(handles, api_key, args.hours)

    if args.summary_only:
        print(result.get("summary", "No results."))
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
