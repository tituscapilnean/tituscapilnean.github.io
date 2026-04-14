---
title: "Three Out of Four: Grading My 2020 Unicorn Calls"
date: 2026-04-14 12:00:00 +0000
categories: [English, Investing]
tags: [investing, venture, framework, unicorns, "2026"]
author: titus
---

In December 2020 I [published a framework](/posts/investing-criteria-1b-exit/) for asking one question: can this company produce a +$1B exit? I applied it to four companies. Two were tagged "high unicorn potential." Two were tagged "low." Five years later, the scorecard is in.

Three out of four. Here's what played out, and what the framework missed on the one it got wrong.

## Mux: called unicorn, got unicorn

**Score: ✅ High potential → hit unicorn**

Five months after that 2020 article, Coatue led a $105M Series D that valued Mux at $1B. Accel, a16z, and Dragoneer joined. Total raised: $177M across six rounds. Customers today include Paramount, Substack, Vimeo, Shopify, Dropbox, Fox, PBS, and Synthesia.

They haven't raised since 2021, and headcount dropped to 81 in 2024, down about 30% over two years. The post-ZIRP environment forced efficiency mode on API-first infrastructure companies like everyone else. No exit yet. But the hard prediction — "this clears $1B" — landed.

## PolicyGenius: right thesis, wrong macro

**Score: ⚠️ High potential → acquired below peak valuation**

This is the most interesting one, because every input to the framework said "unicorn" and the output still missed.

PolicyGenius raised $288M across six rounds, with a $125M Series E in March 2022. PitchBook last tagged them at $775M. A SPAC at $1.5B was on the table in 2021. Then the insurtech winter landed. June 2022: 25% layoffs. April 2023: acquired by Zinnia. The combined entity cleared $1B in enterprise value, and PolicyGenius contributed roughly a third of the combined revenue. But as a standalone, it exited below the $775M mark, let alone the $1.5B SPAC number. KKR and Eldridge rolled into Zinnia equity rather than cashing out.

Did the 2020 framework get this right? Technically the combined company crossed the line. Honestly, no. The thesis was that PolicyGenius was a $1B+ independent outcome, and it wasn't.

What I missed: unit economics sustainability in a rising-rate environment. Team, market, traction, investor signaling all looked correct. None of those filters asked the question "does the customer acquisition math still work if capital gets expensive?" For comparison marketplaces and consumer insurtech in particular, that question should have been load-bearing.

## CrowdAI: called low, went low

**Score: ✅ Low potential → defense acqui-hire**

CrowdAI eventually raised $18.3M across four rounds and was acquired by Saab in September 2023. The CEO joined Saab as Chief Digital and AI Officer. Defense acqui-hire, not a billion-dollar outcome.

The 2020 flags held: small team, low commercial traction, no marquee logos. The company pivoted hard into government and defense work (AFRL, Navy), which is exactly the niche-down move a company makes when commercial scale isn't working. Saab got AI/ML capability at a modest multiple on $18M raised.

## Chatdesk: called low, stayed low

**Score: ✅ Low potential → sustainable small business**

Chatdesk raised $9M across two rounds. As of December 2024: 17 employees. Still operating, still serving ecommerce brands, but never broke out of the niche. The 2020 flags held: late to market, crowded space, limited differentiation. A perfectly respectable services-heavy small business that was never going to produce a $1B outcome, and didn't.

## What the framework got right

The single strongest predictor across all four companies was **investor signaling and valuation velocity**. That filter alone would have sorted these four correctly at the time of writing. Coatue and Accel don't write Series D leads at $1B valuations on companies that aren't real. A Series A at $2-3M total raised from brand-name-absent investors is an equally loud signal in the opposite direction.

Team pedigree and market size mattered too, but they were noisy. PolicyGenius had the right team and market. Chatdesk had a decent team in an expanding market. The investors knew things about retention, expansion revenue, and unit economics that weren't visible from the outside, and their bets reflected that asymmetric information. The lesson: investor signaling isn't just about brand, it's a proxy for private data you don't have.

## What the framework missed

One filter needs to be added: **capital efficiency and path to profitability under stressed macro conditions.**

PolicyGenius is the cleanest example. The 2020 framework asked is the market big enough, is the team strong enough, is the traction real, are the right investors in. Yes, yes, yes, yes. What it didn't ask: does this business model compound even if ZIRP ends tomorrow?

For marketplaces, comparison platforms, and consumer financial services specifically, that question is binary. Either the per-customer economics survive a more expensive capital environment, or the company becomes an acquisition target at a down round the moment the music stops.

The fix is one additional filter, applied conditionally: for any company whose growth depends on paid acquisition or low-margin intermediation, require evidence that gross margins and payback periods improve — not just scale — with revenue.

## Updated framework

Original six filters from 2020:

1. Strong founding team
2. Team diversity and size
3. Traction and interest
4. Market size and size of pain
5. Investor signaling and valuation velocity
6. Timing

Refined for 2026:

1. Strong founding team (prior exits weighted heavily)
2. Team diversity and GTM muscle (not just engineering depth)
3. Traction and interest (retention and expansion matter more than logo slides)
4. Market size and size of pain (with an explicit expansion path required if the initial niche is sub-$5B)
5. Investor signaling and valuation velocity (the strongest single signal)
6. Timing
7. **Unit economics and capital resilience** (new — applied conditionally to any marketplace, intermediation, or paid-acquisition-dependent model)

Three out of four isn't a bad hit rate for a public bet published five years in advance. The one I missed, I missed for a reason the framework didn't capture. That filter's in now.

## Run the framework yourself

I packaged the updated framework as a [Claude Code skill](https://github.com/tituscapilnean/tituscapilnean.github.io/blob/main/.claude/skills/evaluate-company/SKILL.md) so it's runnable on any company without me in the loop. Point it at a company name or URL and it runs the seven filters, produces the scorecard, and names the most likely outcome explicitly.

To install it, grab [SKILL.md](https://raw.githubusercontent.com/tituscapilnean/tituscapilnean.github.io/main/.claude/skills/evaluate-company/SKILL.md) and drop it into `.claude/skills/evaluate-company/SKILL.md` in any project (or `~/.claude/skills/evaluate-company/SKILL.md` for a user-wide install). Invoke it with `/evaluate-company [company-name-or-url]`. Pass additional private context (unannounced rounds, internal metrics, pivot signals) as a second argument — the skill weights user-supplied private data over stale public databases.

It also supports multi-company side-by-side comparisons, which is how I now run most career and investment decisions when I'm choosing between two paths.
