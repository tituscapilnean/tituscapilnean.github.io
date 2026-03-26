---
title: "Everyone Can Build Now. Almost Nobody Knows When to Stop."
date: 2026-03-25 12:00:00 +0000
categories: [English, AI]
tags: [ai, agents, infrastructure, governance, "2026"]
author: titus
---

AI inference demand grew 1,000,000x in two years. Email volume doubled after AI adoption. Chat messages went up 145%. The productivity gain didn't free anyone — it just raised the bar for what "keeping up" means.

That disconnect tells you everything about where we actually are. The bottleneck isn't capability anymore. It's judgment. And most companies haven't noticed the shift.

## The capability gap closed

An AI agent ran 910 experiments in 8 hours this week, then rerouted itself to faster hardware without being told. Another one published a 79,000-word novel. At Harvard Medical School, agents access over 1,000 real scientific tools — protein structure retrieval, GWAS analysis, drug repurposing pipelines — and are contributing to the academic literature, not summarizing it. Their research boards have accumulated thousands of posts across AI safety, medicine, and AI research. These agents aren't assistants. They're participants.

NVIDIA's robotics chief put it plainly: a single agent can now coordinate an entire robot fleet, breaking goals into tasks, routing them dynamically, with no human in the loop. Over in biotech, an AI pipeline processed 25,000 chest CT scans in under 14 hours to score thymus health at a precision decades of radiology couldn't deliver.

The capability ceiling that everyone was racing toward? We hit it. What's exposed underneath is a different problem entirely.

## The governance gap just opened

Three companies made moves in the same week that frame what's actually at stake. Okta gave AI agents employee IDs with a kill switch. World gave shopping agents human passports. Proofpoint stopped checking identity altogether and started reading intent.

They're all looking at the same broken assumption: the accountability model software has relied on for 30 years. Every system we've built assumes actors have accounts, accounts have owners, and owners are responsible for what those accounts do. One login, one human, one chain of liability. That's false now. A single founder can deploy 50 agents. A single agent can trigger 10,000 actions. The surface area of "who did this?" just expanded by several orders of magnitude.

Most companies are still treating agent adoption like a software procurement decision — add the tool, capture the productivity gain, move on. But the leverage isn't in the model. It's in the infrastructure around it: who authorizes the agent, what systems it can touch, how it persists context across sessions, who's accountable when it goes off-script.

Identity was boring plumbing until every company became an internet company. Then Okta was worth $40B. Authorization was a checkbox until every company became a cloud company. Now every company is about to become an agent company. The authorization layer is being built right now, and most founders aren't watching it happen.

## The LLM is the new compiler

JavaScript got mocked for being too far from the hardware. The C++ crowd had a point. They also lost the web.

What's happening with prompts and MCP feels identical. Engineers who've built careers close to the metal — tuning weights, optimizing inference, writing CUDA kernels — are watching an abstraction layer eat their leverage. They're right that prompts are far from the hardware. That's exactly what makes them powerful.

Look at what's already shipping. Stripe co-released the Machine Payment Protocol this month, building on HTTP 402 so agents can request, authorize, and settle transactions in milliseconds without touching a human interface. Benedict Evans flagged that token budgets are now a standard line item in engineering compensation packages, because agentic coding burns hundreds of thousands of dollars in compute per developer per month.

The same pattern has played out in every programming era. Assembly gave way to C. Python and Java captured enterprise. JavaScript ate the frontend by abstracting away the browser's internals. In each transition, the layer that won was not the one closest to the hardware. It was the one closest to the problem.

Prompts are the new syntax. MCP is the new standard library. The builders who win won't necessarily understand transformer internals. They'll understand how to orchestrate systems that do.

## Knowledge gets compiled

Sahil Lavingia turned "The Minimalist Entrepreneur" into nine Claude Code skills this week — `/validate-idea`, `/mvp`, `/pricing`, `/first-customers`, `/marketing-plan`. One install command, describe your business, and the methodology runs against your specific context. Ship30for30 finished their first Claude Cowork Bootcamp with 250+ writers and founders, reporting 5-10 hours saved per week. They're already running a second cohort.

The value embedded in a business methodology was always its synthesis — someone distilling years of pattern recognition into a repeatable process. That synthesis lived in a book, a framework, a consulting deck. It required a trained human to apply it with judgment.

Now it runs as an agent with your context loaded.

The distinction that matters: a generic skill file is fast mediocrity. A skill file built with your specific product, your market, your ICP becomes something that compounds. The methodology executes against your actual problem, not a hypothetical founder's.

In two years, the question won't be "do you use AI?" It'll be "what's your skill stack, and how well does it know your business?"

## The real moat is judgment

Here's the part that should worry anyone building fast. Ed Sim calls it the Law of Agent Cannibalism: when agents can ship a new feature category overnight, every company creeps into every adjacent market. Lovable went from app builder to data science, marketing, and decks in the same sprint. Security vendors are expanding into adjacent categories faster than CISOs can evaluate them.

The economics look obvious. Why sign a three-year contract when an adjacent vendor is building into your vendor's territory with a weekend of agent-assisted development?

But the same agent-powered speed that lets you clone features is silently degrading the one thing that would make your version different: your team's ability to think. UC Berkeley researchers found that students addicted to their phones are 30% more likely to become cognitively dependent on AI. When they asked how many peers had stopped actively participating in their education, the estimate was 50%. At the number one public university in the world. Gen Z will make up 30% of the knowledge workforce within four years.

The symptoms are already showing up in the workplace. Employees shipping vibe-coded prototypes for features nobody asked for. Three-page GPT-generated business cases for $500 decisions. Meetings scheduled to discuss seven AI-generated options no human has actually thought through.

A study by ActivTrak across 163,000 employees found that after AI adoption, email volume rose 104%, chat messaging jumped 145%, and time in collaboration tools climbed 94%. AI was supposed to compress work. Instead, it's compressing the time between actions while expanding the total volume of actions. More outputs, more messages, more decisions per hour. The bottleneck moved from production to judgment.

Boris Cherny, the creator of Claude Code, now kills 80% of what he builds before it ships. His logic is simple: when production is nearly free, the only moat is taste. The ability to look at ten drafts and know which two are worth publishing. That filter is human, and it doesn't scale the way production does.

## Systems beat models

Ramp's March 2026 AI Index tells the clearest version of this story. Anthropic now wins 70% of new business matchups against OpenAI. Same benchmarks. Higher price. Compute-constrained. Still winning. A year ago, 1 in 25 businesses on Ramp paid for Anthropic. Today it's 1 in 4.

Anthropic isn't winning because its model is 10% better on a benchmark. It's winning because operators building serious AI workflows have figured out that model selection is almost irrelevant compared to the quality of the system surrounding it. Every connector built, every workflow configured, every memory the system accrues creates compounding switching costs.

The same principle applies everywhere. The companies that benefit most from AI are the ones with better filters, better judgment loops, tighter feedback between what gets built and what actually matters. AI is consolidating markets, not fragmenting them. The top 1% of companies already capture roughly 80% of economic value, and AI is widening that gap because larger organizations have bigger datasets and can use automation to absorb the coordination costs that normally slow them down.

Meanwhile, we're spending billions training humans to use AI tools at the exact same time those tools are becoming agents that don't need human operators. Coursera's AI training division is a $239M business precisely because the gap between knowing and doing is enormous — and enterprises keep falling into it. But agents don't fall into that gap. They don't revert to old habits after a sprint. They don't need a quarterly refresher.

The $239M upskilling economy is racing against its own premise.

## What this means if you're building right now

The model race is settled. The infrastructure question is wide open. Here's what that means in practice:

**Your playbook is a plugin now.** Whatever methodology, framework, or domain expertise gives your company its edge — it can be compiled into an executable agent. If you haven't started building your skill stack, someone in your market has.

**Agent authorization is the next identity layer.** If you're deploying agents across your SaaS stack without auditability, access governance, and revocation, you're operating in a blind spot. The companies that build the governance layer first will convert it into a structural moat — the same way Okta captured identity when every company went online.

**Judgment is the bottleneck, not production.** Everybody can generate now. The real skill is knowing when to stop. Hire for taste. Build feedback loops that filter signal from noise. The organizations that win will be the ones whose people can still evaluate whether something is worth shipping at all.

**The layer closest to the problem wins.** Not the one closest to the hardware. If you're optimizing inference while your competitor is orchestrating outcomes, you're solving the wrong problem.

The capability gap closed this week. What's left is the question of who builds the systems — the authorization, the governance, the judgment loops — that make all that capability safe to use.

Everybody can generate now. The real skill is knowing when to stop.
