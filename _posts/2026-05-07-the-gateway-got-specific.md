---
title: "The Gateway Got Specific"
date: 2026-05-07 12:00:00 +0000
categories: [English, AI]
tags: [ai, agents, gateway, infrastructure, personal-ai, pricing, mcp, "2026"]
author: titus
---

Last week I argued the margin moved out of the model and into the gateway: the layer that sits between an agent and everything outside its weights. The argument was abstract. The gateway was a thesis. A week of releases later, the gateway specified itself. Five forces pressed on the same surface and forced it into a shape you can actually build.

## Last week the model. This week the meter.

The first place a gateway has to do real work is at the price tag. Agents broke the math.

Cursor ran a 23 percent negative gross margin last quarter on a flat subscription, every dollar of revenue costing $1.23 in API spend. GitHub Copilot [moves to usage-based AI Credits](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) across Pro, Business, and Enterprise on June 1. Atlassian and HubSpot announced the same shift the week before. Ramp's data on AI SaaS spend put 74 percent of dollars on token-based pricing already. The application layer didn't choose this. The provider economics dragged it there.

Seat-based pricing assumed bounded user behavior. Agents do not have bounded behavior. They run loops, retry on failure, fan out across tools. The bill arrives whether or not the user knew what was happening, and it arrives at the SaaS vendor, not the user. The first thing the gateway has to do is meter outcomes per user, per tool, per task, with an auditable trail that supports both invoice disputes and product evals.

Outcome pricing punishes the vendor when models hallucinate. Pure usage punishes the user when an agent gets stuck in a loop. Capped pools with overage are where most products land first. The ones that make it to outcome pricing in 2027 are the ones whose evals are good enough to underwrite it, and the gateway is where those evals get computed.

The unit of value used to be the seat. The gateway is the meter now.

## The harness picks the architecture now.

If the gateway is the meter, the next question is what it bills against. Cross-provider routing is the easy version. Cross-architecture routing is the next.

TheSequence's series this week on the RNN comeback laid out the math. Attention is O(N²). The KV cache scales linearly with context length, layers, and batch size, then turns into the binding constraint on concurrency the moment the context gets long. NVIDIA Research published [KVTC](https://arxiv.org/abs/2511.01815), a transform-coding pipeline that compresses the KV cache 20 to 40 times for storage. Google Research published [TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/), claiming 6x memory and 8x speed gains on long-context inference with no accuracy loss. Both papers are admissions. The default architecture is hitting a physical ceiling, and the industry is patching around it.

New-generation RNNs are matching Transformer perplexity at scale with O(1) inference cost. Constant memory regardless of context length. The original RNN advantage, fixed hidden state, was exactly the property that makes long-running agentic inference economically viable.

Claude Mythos hit 93.9 percent on SWE-bench Verified by sustaining agentic loops. GLM-5.1 from Z.ai ran 8-hour sessions with 6,000+ tool calls at $1 per million tokens. Every one of those workloads is the worst case for an O(N²) attention bill. The bet for the next 18 months is the gateway abstracts this away. A step that needs full attention runs on a Transformer. A step that needs long working memory runs on a recurrent or hybrid architecture. The decision lives in the routing layer, alongside permissions, rollback, and per-tool budget.

Architecture is a billing decision now, made per call by the gateway.

## Connectors are table stakes. Precision is the moat.

Routing across architectures only matters if you can verify the work the agent does on top. The connector layer arrived this week. The verification did not.

Anthropic shipped [MCP connectors for nine creative tools](https://www.anthropic.com/news/claude-for-creative-work) in a single release: Adobe Creative Cloud, Autodesk Fusion, Affinity by Canva, Blender, Splice, Ableton, SketchUp, and Resolume. Adobe alone exposes more than 50 tools through one endpoint. Bilawal Sidhu's demo of a 2D image becoming a 3D Blender scene hit timelines the same day. The window you opened used to define the work. With MCP, the agent picks the window after you describe the outcome.

The interface assumption baked into every desktop app since the early 2000s collapsed in one release. Connectors are now table stakes. Anyone shipping into a domain in 2026 will expose an MCP server, and treating one as a moat is a category error.

The moat is precision. MCP gets complemented by traditional API access wherever batch matters, where you push 200 assets through the same transformation and need to audit the diff afterwards. The harness wraps both: model-driven prompts on the conversational path, deterministic API calls on the batch path, and an evaluation layer in between that checks derived outputs against ground truth before they ship.

Anti-hallucination at this layer is a controls discipline. Citation trails on every numeric claim. Schema validation on every tool output the agent passes downstream. Re-execution against deterministic baselines for anything an auditor will read. The teams that get precision out of that harness take the budget. The teams that ship a connector and call it integration ship a demo.

## Compute stopped being a purchase.

The gateway runs on someone else's compute, and this week we learned compute is no longer a thing you buy.

Anthropic announced a [10-year, $100B commitment to AWS](https://www.anthropic.com/news/anthropic-amazon-compute) for up to 5 GW of Trainium capacity. Days later, an additional [Google deal](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services) worth $10B now plus up to $30B more tied to performance milestones, on top of an existing TPU and Broadcom commitment. Amazon already holds 15 to 20 percent of Anthropic. Google holds 14 percent. The flow now: trade ownership and revenue share for capacity.

OpenAI committed $250B to Azure last fall. Microsoft is bond-financing its own data center buildout. CoreWeave loaded its balance sheet with debt secured against multi-year GPU contracts from the same labs. The labs commit future revenue to compute providers, the providers borrow against those commitments to build capacity, and the banks underwrite the loans on the strength of revenue that has not been earned yet.

A shadow loan economy is forming between AI companies, hyperscalers, and lenders, settling in committed-capacity contracts rather than cash. The collateral is forward demand for inference. For founders building on Claude, the substrate is no longer neutral. Mythos at $25 input and $125 output per million tokens is 5x Opus because the company cannot afford to let every prompt run on the most capable model. Your cost curve gets shaped by their capacity plan. The contract you signed last quarter is in a renegotiation queue.

Read those contracts. Route around them. All of it is generic infrastructure that everyone in the stack will eventually have.

## Your framework is the only thing left that's yours.

Everything above is generic infrastructure. Some of it ships in your gateway. Some of it ships in the platform's. The piece the platform cannot ship for you is the framework you encode into it.

The June 2026 SF ballot has 12 candidates running for a single congressional seat. Add the other statewide races and four local props and a voter has 40+ profiles to evaluate. Most people don't. They vote the slate card, follow the union endorsement, or skip the down-ballot races. The actual bottleneck on civic engagement is processing all that information consistently against your real values across 15 races you will never deeply research. There is more raw information available than any electorate in history, and that has not moved turnout.

So I built a Claude skill that does it. It encodes the framework I actually vote on: pro-housing supply, pro-public safety with accountability, skeptical of culture war on either side, execution over rhetoric. It applies that across every race on the ballot. It steel-mans candidates I would not vote for. It flags speculation explicitly. It distinguishes substantive alignment from pragmatic alignment from contrarian alignment, because those are different votes for different reasons.

The output was sharper than any voter guide I've read because the framework was specific to me.

This is where personal AI gets interesting. Generic copilots compress to the price of the underlying model, and the underlying model is the commodity now. A tool that encodes your specific decision framework and applies it to decisions you would otherwise outsource to gut feel or tribal cues compounds in a way the platform cannot replicate. Voting is the test case. The same pattern works for hiring, vendor selection, investment decisions, anywhere consistency matters more than novelty.

Your meter is yours. Your policies are yours. Your capacity contracts are yours. Your routing logic is yours. The framework wrapping all of it is the most yours of anything in the stack.

## The gateway got specific.

A month ago the gateway was a thesis. This week it specified itself. Meter what the agent does. Police the tools it touches. Read the compute contracts that price your inference. Pick the architecture that fits the step. Wrap all of it in a framework only you can write.

Generic capability is free. Generic infrastructure is in the platform. The only thing that compounds is what is specific to you.

The model is the commodity. The gateway is the company. This week the gateway got specific.
