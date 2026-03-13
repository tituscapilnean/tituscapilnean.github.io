---
title: "I've Been Running AI Agents for Months — Here's How I Can Set One Up for You"
date: 2026-03-13 09:00:00 -0800
categories: [English, AI]
tags: [ai agents, automation, civic, identity, tools]
author: titus
---

For the past several months I've been running AI agents in my own workflows — not experimenting in sandboxes, but actually deploying them against real tasks and seeing what breaks.

The stack I keep coming back to is **[OpenClaw](https://openclaw.ai)**: a self-hosted gateway that enables AI agents to get real tool access. You message it from your phone the way you'd message a person, and it acts: browsing, executing tasks, accessing your Gmail and Calendar, pulling documents, firing off webhooks, when connected to the right tools. It runs on your own infrastructure, which means your data doesn't touch someone else's servers.

## What "agent with tool access" actually means

The difference between a chatbot and an agent is that the agent can *do things*. OpenClaw agents can have access to Gmail, Google Calendar, Google Drive, Slack, databases, and dozens of other services — not by storing credentials on your machine, but by routing API calls through a gateway that handles authentication separately. If this is scary, then we should probably have a conversation about it.

Which brings me to the part that took time to get right.

## The security problem most agent setups ignore

Connecting an agent to your Gmail or Drive is a real authorization decision. Most hobbyist setups hand the agent an OAuth token with broad permissions and move on. That works for tinkering. It's not how you'd run it for anything business-critical.

This is exactly what I work on at **[Civic](https://civic.com)**. Civic is the security layer for AI agents, and **Civic** is what I use as the connector between OpenClaw and every cloud service and application it touches that has private information on it.

Here's how it works in practice:

- **OAuth flows happen off-host through Civic** — credentials never reach the machine OpenClaw is running on
- **Tokens never touch OpenClaw directly** — all API calls route through the MCP gateway
- **Read-only by Civic configuration** — Gmail can read, search, and draft but not send; Calendar can view events but not create or modify them; OpenClaw has to request elevation for write operations
- **Instant revocation** — terminate access to any service immediately without reconfiguring the agent
- **Built-in guardrails** — automatic PII detection (SSNs, credit cards, emails), prompt injection blocking (based on OWASP standards), and parameter presets that create hard limits the agent cannot override
- **30-day token expiration** — periodic re-authorization by design, not an afterthought
- **Full request/response logging** — 30 days of audit trail so you can see exactly what the agent did

One operational detail worth calling out: you never log into Civic on the same machine where OpenClaw is running. Configuration happens on a separate device. It's a simple rule, but it's the kind of thing that separates a secure deployment from one that looks secure.

## What I'm offering

I've spent years as a builder — shipping GTM systems, data pipelines, and growth tooling across early-stage and growth-stage companies. I know what it looks like when automation actually fits into a team's workflow versus when it creates one more thing to maintain.

If you want a working AI agent setup, I can build and deploy it with you. Here's what the engagement covers:

- A hosted OpenClaw deployment configured for your specific workflows
- Secure connections to Gmail, Google Calendar, Google Drive, Slack, or other tools you're actually using — via the Civic MCP Gateway
- Guardrails configured to your risk tolerance: read-only by default, write operations requiring explicit elevation, PII redaction, prompt injection protection
- A walkthrough of the shared responsibility model so you know exactly what Civic handles and what you're responsible for on your end

This is hands-on work, not a template. I'll work through the actual use case with you and build something that holds up in production.

## Who this is for

Founders and operators who've been meaning to move on AI but keep deprioritizing it because figuring out what to trust takes time they don't have. If your day is full of email, scheduling, documents, and context-switching between tools — and you want to hand the repeatable parts off to something that works *safely* — reach out.

DM me on [X](https://x.com/titus_k) or find me on [LinkedIn](https://linkedin.com/in/tituscapilnean).
