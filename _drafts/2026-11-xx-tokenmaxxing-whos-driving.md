---
title: "Who's Driving? The Stupidity of Tokenmaxxing"
date: 2026-12-07 12:00:00 +0000
categories: [English, AI]
tags: [ai, agents, productivity, tokenmaxxing, metrics, "2026"]
author: titus
---

> **STUB.** Working notes for the `titus-blog-voice` skill. Delete everything above "Draft" before publishing.

## Status

- Outline: proposed, not yet approved
- Priority: 5 of 5 (strong argument, but the moment needs one specific case)
- Next step: find one concrete scene, approve the outline, then draft

## The moment (Titus's words)

> I have seen people lose themselves at work in AI conversations that reinforced their own bad assumptions and created more slop than useful content or code, because they didn't clarify their intent or strategy. They relied on the AI driving both inputs and outputs, not to mention model choice for menial tasks.

## Outline

**Working title:** Who's Driving? The Stupidity of Tokenmaxxing
**Topic:** Token volume is a symptom. The real failure is handing the AI both the question and the judgment, then measuring how much it talked.

1. **The moment:** One specific person (anonymized) deep in an AI conversation, producing more and more output that confirmed what they already believed. **Needs a real case.**
2. **The situation:** Meta's internal leaderboard reportedly ranked 85,000+ employees by token use, with titles like "Token Legend". Uber reportedly ran one too, then moved away from it because costs rose without a clear productivity gain. Linear's COO compared ranking engineers by tokens to ranking marketers by spend.
3. **The hidden system:** Models tend to agree with whoever is typing. Leaderboards reward volume. Vendors benefit when customers celebrate consumption. Put them together and you pay to have your own assumptions confirmed, at scale.
4. **What people get wrong:** That more AI use means more output. Without intent going in, the AI drives both what goes in and what comes out. Tokens measure effort, not results.
5. **The fix:** Intent in, judgment out.
   - **Write the brief yourself** before you prompt: the goal, the audience, what done looks like
   - **Right-size the model:** the smallest model that does the job, frontier models for frontier problems
   - **Judge the output yourself**, against the brief, before it ships
   - **Measure cost per accepted output** (a merged PR, a published piece, a shortened cycle), not tokens
6. **The close:** A short line about who's driving.

**Framework:** Intent in, judgment out.
**Personal angle:** Your GTM background: marketing already made this mistake with vanity metrics (impressions, MQL counts). A short self-admission (a time you did it yourself) would fit how your old posts handled failure.
**Section headers (draft):** Lost in the conversation / The leaderboard problem / Agreeable machines / Intent in, judgment out

## Open questions

- [ ] One concrete case, even anonymized. For example: "a teammate spent two days with an AI on a positioning doc that started from a wrong ICP."
- [ ] An example of a big model used for a small task (like a frontier model reformatting a CSV)?
- [ ] Have you caught yourself doing it? What snapped you out of it?
- [ ] What would your "cost per accepted output" metric be for a GTM team?

## Research and sources

- [The Pulse: 'Tokenmaxxing' as a weird new trend (Pragmatic Engineer)](https://newsletter.pragmaticengineer.com/p/the-pulse-tokenmaxxing-as-a-weird-6b2)
- [Tokenmaxxing leaderboards debate (Business Insider, April 2026)](https://hn.jakechampion.name/reader/https://www.businessinsider.com/tokenmaxxing-ai-token-leaderboards-debate-2026-4)
- [Tokenmaxxing: why AI token consumption isn't engineering productivity (Faros AI)](https://www.faros.ai/blog/tokenmaxxing)
- [Meta created an internal leaderboard (Engineering Leadership)](https://newsletter.eng-leadership.com/p/meta-created-an-internal-leaderboard)
- Sources disagree on figures (85K employees, top 250, about 60 trillion tokens a month) and on whether Meta renamed or shut down the board. Verify against Business Insider or The Information before citing.

## Related posts (link, don't repeat)

- [Your AI Problem Is a Management Problem](/posts/your-ai-problem-is-a-management-problem/): the "briefing gap" section already argues for clear scoping. This post goes further: missing intent, agreeable models, model choice, and the wrong metric.
- [Everyone Can Build Now. Almost Nobody Knows When to Stop.](/posts/everyone-can-build-now/): judgment as the bottleneck
- [Triple-Ping Your Docs](/posts/triple-ping-your-docs/): your 2025 method for beating bland AI writing

## Draft

_Not started._
