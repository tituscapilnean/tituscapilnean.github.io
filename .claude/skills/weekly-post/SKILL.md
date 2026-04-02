---
name: weekly-post
description: Generate a weekly blog post from LinkedIn and X social media exports, matching the author's tone and blog conventions
argument-hint: "[linkedin-xlsx-path] [x-csv-path]"
effort: max
---

# Weekly Blog Post from Social Media Performance

Generate a publish-ready blog post for tituscapilnean.ro by analyzing the user's top-performing LinkedIn and X (Twitter) posts from the past week.

## Step 1: Gather inputs

The user will typically provide most inputs inline when invoking the skill. Parse what they give you and only ask for what's missing.

Required inputs:
1. **LinkedIn export file path** - an `.xlsx` file exported from LinkedIn Analytics (Content tab). If not provided via `$ARGUMENTS`, ask for it.
2. **X/Twitter export file path** - a `.csv` file exported from X Analytics. If not provided via `$ARGUMENTS`, ask for it.
3. **Drafts path** - usually `/Users/tituspml/Documents/Code/social-post-booster-bot/drafts/`. The user may provide this or you can default to it.

Optional inputs (use defaults if not specified):
4. **Angle or theme preference** - default: find the throughline from top-performing posts.
5. **What to exclude** - default: nothing excluded.
6. **Civic tie-in** - default: no mention.
7. **Title preference** - default: propose 3 options after analysis.

Do NOT ask for inputs the user already provided. Only ask for missing required inputs.

## Step 2: Read and analyze source data

Run all three data reads in parallel:

### LinkedIn (.xlsx)
- Use a Python venv at `/tmp/xlsx_venv` to install `openpyxl` if needed and parse the spreadsheet
- Extract the TOP POSTS sheet, which has two ranked lists: by engagements (left columns) and by impressions (right columns)
- Each row contains: Post URL, Post publish date, and the metric. No post text is included.
- Correlate post dates with drafts to get full text

### X/Twitter (.csv)
- Parse the CSV directly. It contains full post text in the "Post text" column
- Rank by impressions and engagements
- Filter to original posts (exclude replies starting with @)

### Existing drafts
- Read drafts from `/Users/tituspml/Documents/Code/social-post-booster-bot/drafts/` for dates matching the export range
- Files are named `YYYY-MM-DD.md` and contain full LinkedIn + X post text, sources, and evaluation scores
- These are the primary source of post content. Match draft dates to LinkedIn export dates to correlate metrics with full text

## Step 3: Analyze tone from recent blog posts

Read the 3 most recent English-language posts from `_posts/` to calibrate:
- Sentence structure and rhythm
- How sections are organized (H2 headers, short paragraphs)
- Opening style (direct, declarative, data-led)
- Closing style (punchy callback, forward-looking statement)
- Level of directness and opinion

## Step 4: Identify themes and propose structure

Present a ranked table of top posts showing LinkedIn and X metrics side by side, with the theme for each. Then:
- Identify the narrative throughline that connects them
- Propose 3 title options
- Propose a section outline (H2 headers)

Keep the proposal concise. **Wait for user approval of title and structure before writing.**

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
- **No em dashes**: Use periods, commas, or colons instead. Never use the — character.
- **No self-referential metrics**: Don't mention post impressions, engagement numbers, or "this was my top post" in the article itself. The data informs which themes to cover, but stays behind the scenes.
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
