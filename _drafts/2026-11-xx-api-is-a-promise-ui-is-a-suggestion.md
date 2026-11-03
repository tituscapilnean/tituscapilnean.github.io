---
title: "An API Is a Promise. A UI Is a Suggestion."
date: 2026-11-16 12:00:00 +0000
categories: [English, AI]
tags: [ai, agents, mcp, api, ux, saas, outbound, "2026"]
author: titus
---

> **STUB.** Working notes for the `titus-blog-voice` skill. Delete everything above "Draft" before publishing.

## Status

- Outline: proposed, not yet approved
- Priority: 2 of 5 (most concrete moment; needs real numbers)
- Next step: get the UI vs API time numbers, approve the outline, then draft

## The moment (Titus's words)

> Instantly outbound campaign setup is 100x easier and faster via the API vs going into their UI that changes every 2 weeks.

## Outline

**Working title:** An API Is a Promise. A UI Is a Suggestion.
**Topic:** UI churn is a hidden tax on users. APIs and MCP servers are contracts, so agent-first access beats the dashboard for real work.

1. **The moment:** Setting up an outbound campaign in Instantly through the API vs. the UI, and finding the UI changed again since the last time.
2. **The situation:** More of your work runs through APIs and agents. Salesforce reportedly rebuilt its platform as headless and API-first in 2026. The SaaS selloff in early 2026 was framed as value moving from UI usability to how expressive and reliable a product's API is.
3. **The hidden system:** SaaS teams redesign UIs to show progress, ship features and move engagement metrics. Every redesign costs users time to relearn. An API has versions and deprecation notices. A UI just changes overnight.
4. **What people get wrong:** That UIs are dying. Sure, UIs still matter for approvals, review, exceptions and reporting. The UI moves from where you do the work to where you check it.
5. **The fix:**
   - **Build the MCP server first**, the UI second
   - **Version the API like a contract**, with deprecation windows
   - **Design the UI for review and approval**, not data entry
   - Price for outcomes or usage, because seats assume a human is logged in
6. **The close:** "The best product experience I had this month never showed me a screen."

**Framework:** An API is a promise. A UI is a suggestion.
**Personal angle:** Your own outbound stack, run from the terminal. At Civic, the question of who is clicking (a person or an agent acting for one) is the identity problem again.
**Section headers (draft):** Two weeks, new buttons / The UI tax / Where the UI still earns its place / Build the MCP server first

## Open questions

- [ ] Real numbers for the 100x: how long does a campaign setup take in the UI vs. via the API? ("2 hours vs. 2 minutes" is stronger than "100x".)
- [ ] OK to name Instantly? It's a fair, specific criticism, but it's your call.
- [ ] What do you drive the API with: Claude Code, a script, swamp?
- [ ] Any other tool where the same thing happened?

## Research and sources

- [Salesforce Headless 360 explained (DigitalAPI)](https://www.digitalapi.ai/blogs/salesforce-headless-360-explained): vendor-adjacent, verify against Salesforce's own announcement
- [The future of SaaS is APIs plus AI agents (Nordic APIs)](https://nordicapis.com/the-future-of-saas-is-apis-plus-ai-agents/): the skeptical case, UI still matters for oversight
- [API, MCP, CLI in the AI agent era (TIMEWELL)](https://timewell.jp/en/columns/api-mcp-cli-ai-agent-era): the February 2026 SaaS selloff framing
- [How autonomous agents and MCP are rewriting the SaaS playbook (XAIT)](https://www.xait.com/blog/beyond-the-browser-how-autonomous-ai-agents-and-mcp-are-rewriting-the-saas-playbook)

## Related posts (link, don't repeat)

- [The Gateway Got Specific](/posts/the-gateway-got-specific/): connectors as table stakes, precision as the moat
- [One Layer Deeper Than the Platform Can Swallow](/posts/one-layer-deeper-than-the-platform/)

## Draft

_Not started._
