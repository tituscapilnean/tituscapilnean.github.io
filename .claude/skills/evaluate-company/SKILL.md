---
name: evaluate-company
description: Evaluate a company's +$1B exit potential using Titus's 7-filter investing framework. Use when asked to analyze, grade, or score a company's unicorn potential, or to compare multiple companies as investment/career opportunities.
argument-hint: "[company-name-or-url] [optional: additional-context]"
effort: max
---

# Evaluate Company Unicorn Potential

Apply Titus's 7-filter framework to assess whether a company can produce a +$1B exit. Original framework at https://tituscapilnean.ro/posts/investing-criteria-1b-exit/. Retrospective and refinement at https://tituscapilnean.ro/posts/three-out-of-four-2020-unicorn-framework/.

## Step 1: Gather inputs

The user will typically provide a company name, URL, or both via `$ARGUMENTS`. Parse what they give you. Do NOT ask for inputs already provided.

Required:
1. **Company identifier** — name, domain, or URL. If missing, ask.

Optional (use defaults if not specified):
2. **Additional context** — anything the user already knows (funding rounds not yet public, pivot signals, internal metrics, customer calls). If provided, weight it heavily — private data beats public databases.
3. **Comparison companies** — if the user is comparing 2+ companies, evaluate each independently, then produce a side-by-side at the end.
4. **Decision context** — investment, career move, partnership, etc. This affects emphasis: investment decisions care more about exit probability and valuation, career decisions care more about trajectory and compounding.

## Step 2: Research in parallel

Run these lookups concurrently. Use WebSearch for each. Note the retrieval date alongside any figure — funding data goes stale fast.

1. **Funding history**: total raised, round sequence, lead investors, latest valuation. Query sources: Crunchbase, PitchBook, Tracxn. Cross-reference at least two.
2. **Team**: founder backgrounds (prior exits, relevant domain experience, accelerator affiliations). LinkedIn, Crunchbase founder pages.
3. **Headcount trajectory**: current size, year-over-year change. Tracxn and LinkedIn employee count are the cleanest signals. Flag any sustained decline.
4. **Customer traction**: named logos, case studies, public customer counts. Company site, press releases.
5. **Product direction and pivots**: has the company shifted core product in the last 2-3 years? Count pivots. Multiple pivots are a strong negative signal.
6. **Competitive landscape**: who are the incumbents and adjacent AI-native entrants? What's the moat narrative?
7. **Market size**: TAM estimates for the primary category. Be skeptical of top-line TAM numbers — weight addressable share higher.

If the user supplied private context (unannounced rounds, internal metrics, etc.), trust that over stale public data. Note explicitly when public sources contradict user-supplied information.

## Step 3: Apply the 7 filters

Score each filter as **Low / Medium / High** (with Medium-Low / Medium-High allowed when the signal is mixed). Briefly justify each score with the specific evidence from Step 2.

### 1. Strong founding team
Look for: prior exits (weighted heavily), deep domain experience, complementary co-founders, accelerator affiliations (YC, Techstars). First-time founders without domain expertise = Medium at best, regardless of pedigree.

### 2. Team diversity and GTM muscle
Look for: functional diversity (not just engineering), go-to-market leadership in place, reasonable headcount growth relative to stage. Engineering-heavy teams at Series A+ without GTM leadership is a flag.

### 3. Traction and interest
Look for: real customers (not just logos for slides), retention and expansion signals, product-market fit evidence. Count pivots — each pivot resets the traction clock. "2M verified users" means nothing if revenue doesn't compound.

### 4. Market size and pain
Look for: TAM large enough to support a $1B outcome, OR a credible expansion path from the initial niche. If the initial niche is sub-$5B, require an articulated horizontal expansion story with evidence the company is already executing it. "The TAM is $X billion" without addressable share analysis = discount by 80%.

### 5. Investor signaling and valuation velocity
The strongest single signal. Look for: tier-1 VCs (Sequoia, Benchmark, a16z, Accel, Bessemer, CRV, Coatue, Founders Fund, etc.) at appropriate stages, healthy round-over-round step-ups, repeat participation from existing investors in later rounds. Crowdfunded, ICO-funded, or angel-only funding at Series A+ = Low. No institutional round in 3+ years = Low.

### 6. Timing
Look for: competitive window open (slow incumbents, technology inflection, macro tailwind), AI-native advantage vs. legacy players, regulatory or demographic shifts favoring the model. "Too early" is a real failure mode — identify if the company has a pattern of being directionally right but 2-3 years ahead of monetization.

### 7. Unit economics and capital resilience (2026 addition)
Apply conditionally to any marketplace, comparison platform, intermediation business, or paid-acquisition-dependent model. Look for: gross margin trajectory (improving with scale, not flat), customer acquisition payback periods, evidence the business model works without ZIRP-era capital. This is the filter that would have caught PolicyGenius in 2020. For pure software/infrastructure businesses with high gross margins, this filter is less load-bearing.

## Step 4: Synthesize the verdict

Combine the seven scores into one of these verdicts:

- **High unicorn potential** — most filters High, investor signaling High, no major red flags
- **Medium unicorn potential** — mixed signals; plausible path to $1B but requires execution on specific expansion or efficiency thesis
- **Low-Medium unicorn potential** — one or two strong filters carry the story, but structural concerns (small team, serial pivots, weak investor signal) make $1B unlikely as standalone outcome
- **Low unicorn potential** — most likely outcomes are acqui-hire, small sustainable business, or quiet shutdown

State the most likely outcome explicitly (e.g., "$200-500M acquisition by a larger platform" or "sustainable $20M ARR services business"). A generic "probably won't hit $1B" isn't useful.

Flag anything speculative. Label private context separately from public data. Note any asymmetric information the user has (e.g., "you mentioned they just closed a $30M round — if confirmed, this moves filter 5 from Medium to Very High").

## Step 5: Present the output

Use this structure:

```
## [Company Name]: Applying the $1B Exit Framework

### Strong Founding Team
[Score] — [2-3 sentence justification with specific evidence]

### Team Diversity and GTM Muscle
[Score] — [justification]

### Traction and Interest
[Score] — [justification]

### Market Size and Pain
[Score] — [justification]

### Investor Signaling and Valuation Velocity
[Score] — [justification]

### Timing
[Score] — [justification]

### Unit Economics and Capital Resilience
[Score or N/A with reason] — [justification]

### Verdict: [High / Medium / Low-Medium / Low] Unicorn Potential
[2-3 paragraph synthesis. Name the most likely outcome explicitly. Flag speculation. Note private context separately.]
```

For multi-company comparisons, add a side-by-side table at the end with filter scores in rows and companies in columns.

## Voice and tone

Match Titus's blog voice:
- Direct, opinionated, specific. No hedging throat-clearing.
- Concrete numbers whenever available. "$288M across six rounds" beats "significant funding."
- Name the real risk, including the one the user might not want to hear.
- End with the most likely outcome, not a generic "time will tell."
- If the user is evaluating the company for a career move, include a final paragraph on trajectory implications (what does the next 3-5 years look like for someone joining now).

## What to avoid

- Don't copy marketing copy from the company site as evidence of traction.
- Don't let a single big-name investor override every other signal — Sequoia has written losing checks too.
- Don't treat TAM estimates from market research firms at face value. Always estimate addressable share.
- Don't score Medium across the board to avoid committing. Force High/Low calls where the evidence supports them.
- Don't forget to note the retrieval date on funding figures. Public databases lag 3-6 months behind reality.
