---
name: weekly-post
description: Generate a weekly blog post from LinkedIn and X social media exports, matching the author's tone and blog conventions
argument-hint: "[linkedin-xlsx-path] [x-csv-path]"
effort: max
---

# Weekly Blog Post from Social Media Performance

Generate a publish-ready blog post for tituscapilnean.ro by analyzing the user's top-performing LinkedIn and X (Twitter) posts from the past week.

## Step 1: Gather inputs (ASK BEFORE PROCEEDING)

Before doing any analysis or writing, ask the user for ALL of the following:

1. **LinkedIn export file path** — an `.xlsx` file exported from LinkedIn Analytics (Content tab). If not provided via `$ARGUMENTS`, ask for it.
2. **X/Twitter export file path** — a `.csv` file exported from X Analytics. If not provided via `$ARGUMENTS`, ask for it.
3. **Angle or theme preference** — ask: "Is there a specific angle, theme, or narrative you want to emphasize, or should I find the throughline from your top posts?"
4. **What to exclude** — ask: "Any topics or posts you want me to skip or downplay?"
5. **Civic tie-in** — ask: "How prominent should the Civic connection be? Options: no mention, subtle/implicit, or explicit."
6. **Title preference** — ask: "Do you have a working title in mind, or should I propose options after analysis?"

Do NOT proceed to Step 2 until the user has answered these questions.

## Step 2: Read and analyze source data

### LinkedIn (.xlsx)
- Use a Python venv at `/tmp/xlsx_venv` to install `openpyxl` if needed and parse the spreadsheet
- Extract the TOP POSTS sheet — identify posts ranked by impressions and engagements
- The spreadsheet contains URLs and metrics but NOT post text — you will need to ask the user to paste the text of their top posts, OR check if full post drafts exist in `/Users/tituspml/Documents/Code/social-post-booster-bot/drafts/` (files named `YYYY-MM-DD.md`)

### X/Twitter (.csv)
- Parse the CSV directly — it contains full post text in the "Post text" column
- Rank by impressions and engagements
- Filter to original posts (exclude replies starting with @)

### Existing drafts
- Check `/Users/tituspml/Documents/Code/social-post-booster-bot/drafts/` for full-length post drafts that match the date range
- These contain the complete text that was used for LinkedIn posts

## Step 3: Analyze tone from recent blog posts

Read the 3 most recent English-language posts from `_posts/` to calibrate:
- Sentence structure and rhythm
- How sections are organized (H2 headers, short paragraphs)
- Opening style (direct, declarative, data-led)
- Closing style (punchy callback, forward-looking statement)
- Level of directness and opinion

## Step 4: Identify themes and propose structure

From the top-performing posts across both platforms:
- Identify the 4-6 strongest themes by combined engagement
- Find the narrative throughline that connects them
- Propose 3 title options to the user
- Propose a section outline (H2 headers) to the user

**Wait for user approval of title and structure before writing.**

## Step 5: Write the article

### Frontmatter rules (from CLAUDE.md)
- `date:` must use UTC: `YYYY-MM-DD HH:MM:SS +0000`
- `tags:` — year numbers must be quoted strings (e.g., `"2026"` not `2026`)
- `author: titus` (defined in `_data/authors.yml`)
- `categories: [English, AI]` (adjust if content warrants different categories)

### Content rules
- **Tone**: Direct, opinionated, structured. No hedging. No filler. Lead with the point, not the reasoning.
- **Structure**: 5-7 sections with clear H2 headers. Short paragraphs (2-4 sentences). Punchy one-liners to close sections.
- **Data**: Include specific numbers, company names, and examples from the source posts. These are what made the posts perform.
- **Perspective**: First-person where it adds credibility ("Here's what I keep seeing..."), third-person analytical elsewhere.
- **No fluff**: No "in today's rapidly evolving landscape." No "let's dive in." No "without further ado."
- **Closing**: Callback to the title or opening. One sentence. Make it land.
- **Length**: 1,200-2,000 words. Long enough to develop ideas, short enough to hold attention.

### File naming
- Save to `_posts/YYYY-MM-DD-slug-from-title.md`
- Use today's date
- Slug should be 4-6 words max, lowercase, hyphenated

## Step 6: Review with user

After writing, ask:
- "Anything you want to cut, expand, or reframe?"
- "Happy with the title?"
- "Ready to commit, or want another pass?"
