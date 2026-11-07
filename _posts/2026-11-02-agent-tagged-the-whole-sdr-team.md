---
title: "My Agent Tagged the Whole SDR Team on a Thursday Night"
date: 2026-11-02 12:00:00 +0000
categories: [English, AI]
tags: [ai, agents, "2026"]
author: titus
---

_I've missed sharing stories on this blog. My last post here was back in May, and it's time to get back into it._

On a Thursday night, I handed one of my Claude Code workflows a spreadsheet. It was a list of people who had opened or clicked a third-party email blast, potential targets we wanted to follow up with. The job was one the workflow had done before: match those contacts against the accounts in our ICP database, map each account to the SDR who owns the follow-up, and let the team know in Slack.

It did all of that, and then it posted the message, tagging the whole SDR team, before I had a chance to check any of it.

## What went wrong

The earlier runs had been smaller batches, so the Slack message tagged fewer people and was easy to scan. This batch was hundreds of accounts. On top of that, the workflow skipped some of the guardrails on which accounts to tag, so non-ICP accounts went out right next to the ICP ones, all dumped into one long message.

The SDRs noticed and started asking why some of these accounts were on the list at all, since they clearly weren't ICP. I deleted the post and tagged the right SDRs again.

## How my workflows learn

Here's the part that makes this more interesting than a bad Slack message. My workflows aren't stateless. Each run leaves a record in an execution ledger, and after incidents or dry runs with errors, I ask the agent to formalize my feedback into rules. Over time those rules harden, and the workflow gets better without me repeating myself.

That's also how it learned the wrong lesson. Every previous run had ended with a Slack post and nobody had complained (the batches were small and the output looked fine), so posting at the end became part of how the job gets done. Nothing in its history said what to do with hundreds of accounts, and nothing said the ICP rule was non-negotiable.

**A workflow that learns from its own history will learn whatever that history teaches, including the shortcuts that only worked because the stakes were small.**

## What it cost

The cost wasn't technical. The SDRs got distracted by deals that were never ICP, and they lost a little confidence in the MQLs we were sending them.

In GTM, that confidence matters more than any single list. When reps start second-guessing the leads they get, they cherry-pick, follow up late, or quietly ignore the list. One noisy Slack message won't kill a pipeline, but a few of them will teach a team to stop trusting it.

## What I changed

I did what I do after every incident: I asked the workflow to turn my feedback into rules. Three of them came out of that Thursday night.

- **Explicit approval before posting.** The workflow now needs my explicit yes before it posts to the SDR team.
- **Strict ICP.** The ICP designation in Salesforce decides which accounts get tagged, instead of including everything the way it did on that run.
- **Summaries for big batches.** When an SDR has multiple leads, the workflow sends a short summary (you have X ICP accounts from this campaign) instead of dumping every account into Slack.

Sure, the approval step slows things down a little. I'll take that over another round of SDRs asking why a non-ICP account landed on their list.

If you're running agents in your GTM stack, look at every step that notifies a human, and ask what happens when the next batch is ten times bigger than anything the agent has seen. If the answer depends on habits it picked up from small, easy runs, add a checkpoint before you find out the way I did.

(I wrote about the bigger picture of agent access and control in [Capability Is the Floor. Control Is the Moat.](/posts/capability-is-the-floor-control-is-the-moat/) This one is the hands-on version.)

The next time that workflow tags the SDR team, it will be because I said yes.
