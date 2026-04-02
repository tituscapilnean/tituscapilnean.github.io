---
title: "Your AI Problem Is a Management Problem"
date: 2026-04-01 12:00:00 +0000
categories: [English, AI]
tags: [ai, agents, management, inference, observability, "2026"]
author: titus
---

The best AI agent operators don't look like engineers. They look like good managers. And the question that actually matters right now isn't "should I learn to code?" It's "do I know how to manage someone I can't see?"

## The management shift

Anthropic shipped auto mode for Claude Code this week, letting agents decide which actions are safe to execute without asking permission. OpenAI launched 20+ Codex plugins connecting its coding agent to Slack, Figma, and Google Drive. Linear announced that AI agents are now first-class users of its platform. OpenAI and Coinbase are onboarding agents the same way they onboard employees.

The pattern is obvious if you look at it from a management perspective. We blew past "can I build an agent?" and landed on "can I run a team of them?" The people doing it well are doing what good managers have always done: scoping work clearly, evaluating output honestly, building trust through iteration, knowing when to delegate versus when to step in.

Companies are still hiring for prompt engineering, the ability to talk to one AI really well. The game already shifted to agent orchestration. Managing multiple specialized systems that each do one thing. Coordinating handoffs. Teaching each one your standards over time. Someone put it well this week: teaching an AI your taste looks a lot like developing taste in the first place. The accumulation of many small moments, each one building like sediment on the last. That sounds more like mentoring a junior employee than writing a prompt.

## The briefing gap

Goldman Sachs published a number that should stop people mid-sentence: 76% of small businesses say they're using AI. Only 14% have actually integrated it into how they work.

That gap isn't about adoption. It's about direction. The pattern keeps showing up the same way. Someone points an agent at a task and expects it to figure things out from what it already knows. They don't send it to read the docs first. They don't feed it the current state of the integration, the changelog, the API reference. They just say "build this" and hope.

A model's training window is already months old. In a world where companies ship breaking changes weekly, months might as well be years. Every integration, every API call, every framework version your agent assumes is current is a potential miss.

A former Google product leader shared how he runs 40 AI agents for $500 a month. But what people skipped past was his method: he treats agents as strategic collaborators, not interns. He continuously iterates, replaces agents that drift, and feeds them current context. The $500 is the headline. The discipline behind it is the actual competitive advantage.

The bottleneck was never the technology. It was always the briefing.

## The math finally works

Three years ago, inference engineering belonged to a few hundred specialists at frontier labs. Today, open models like DeepSeek and Kimi closed the intelligence gap with closed models. Cursor built its latest product on an open model and used inference optimization to outperform API-based alternatives at 80% lower cost. One engineer at Baseten tried 77 different configurations before finding a setup that doubled tokens per second.

The techniques sound esoteric: quantization, speculative decoding, disaggregated serving. The economics are not. a16z just pointed at a $6 trillion IT services market built on 40,000+ managed service providers that mostly operate the way they did in 2005. Their argument: AI agents are now capable enough to handle the judgment calls that kept this industry manual. Ticket triage, compliance tracking, security enforcement. The human connective tissue holding fragmented systems together is becoming replaceable.

Every, the media company, is already running three AI agent employees alongside four humans, with their AI project manager operating on a dedicated machine 24/7. Open models made intelligence cheap. Inference engineering made running it cheap. Deploying agents into markets that couldn't justify the cost before now makes economic sense.

The companies that master inference, not model selection, eat that market.

## Speed without eyes

Here's the part nobody wants to talk about while celebrating faster inference. Mercury 2, a diffusion language model out of Stanford, generates multiple tokens simultaneously instead of one at a time. The result is inference speeds 5-10x faster than comparable frontier models. Jensen Huang put the shift plainly at GTC: "AI is finally able to do productive work, and therefore the inflection point of inference has arrived."

But Bessemer's new AI infrastructure roadmap names a failure pattern that should worry anyone deploying agents at scale. They call it the "confidence trap": the model gives a wrong answer with high confidence, the user accepts it, and no traditional monitoring catches it. No error signal, no thumbs down, no alert. The conversation looks fine in dashboards. The AI just quietly failed.

This pattern persists across 93% of cases even with more powerful models, because it stems from interaction dynamics, not capability gaps. Throwing a smarter model at it doesn't fix it. The roadmap argues the center of gravity in AI infrastructure has shifted from training to inference, and with it, the bottleneck has moved from "how smart is the model" to "how well can we harness it." Memory systems that maintain context across sessions. Evaluation platforms that catch semantic failures in real time. Continuous learning architectures that let models adapt after deployment.

Speed without observability is just failing faster.

## What this means

The compound advantage forming right now is contextual, not technical. The operators who started building that relationship with their agents six months ago, briefing them properly, evaluating their output, feeding them current context, already have something no one can shortcut. The ones starting today will have it over anyone who waits until next year.

This is the new literacy. Knowing how to use AI is table stakes. Knowing how to direct it, what context to load before it starts working, how to keep it current when the ground shifts weekly, how to detect failures that don't look like failures, that separates the 14% from the 76%.

The question worth asking isn't "should I learn to code?" It's "do I know how to manage someone I can't see?"
