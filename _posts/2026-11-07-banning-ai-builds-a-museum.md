---
title: "Ban AI at Work and You're Building a Museum"
date: 2026-11-07 12:00:00 +0000
categories: [English, AI]
tags: [ai, agents, future of work, open source, software factory, "2026"]
author: titus
---

I was at home on a weekend, surfing YouTube to catch up on AI news, and landed on the Swamp Club podcast. Somewhere in the episode, they mentioned that r/opensource had banned AI.

On October 24, the moderators [banned any project that uses AI, is made by it, or is meant for it](https://helpnetsecurity.com/2026/10/26/reddit-r-opensource-ai-ban), under a post titled "Your tokens aren't valuable: No more AI." They also banned projects and accounts younger than a year, and people who don't speak English, because they can't tell AI spam from a translated post anymore.

What does that rule actually protect? The solo developer who used Copilot to write their tests? The non-native speaker who ran a post through a translator? And who decides what counts as "made by AI," when the [Linux kernel already has AI-assisted code in it](https://www.linux-magazine.com/Online/News/r-opensource-Bans-AI-Assisted-and-AI-Related-Projects)?

I get the frustration, moderating a big community is thankless work and the slop is real. But if you need a filter, filter the spam: low-effort posts, fake accounts, nobody accountable for what they submit. Banning everything a model touched throws out the projects worth seeing, and it comes from a fear I also see at companies. People are so afraid of work that sounds like AI that they'd rather give up the thing that lets them move 100 times faster.

That fear is going to turn a lot of projects into museum pieces.

## Bans and mandates

r/opensource isn't alone. Gentoo [prohibits contributions made with LLM tools](https://www.tomshardware.com/software/linux/linux-distros-ban-tainted-ai-generated-code), NetBSD [treats that code as presumed tainted](https://linuxiac.com/netbsd-new-policy-prohibits-usage-of-ai-code/) unless the core team approves it in writing, and QEMU [declines contributions](https://www.gigazine.net/gsc_news/en/20250628-qemu-ai-code-generators-policy) it believes came from AI. Samsung [banned generative AI on company devices](https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak) in 2023, after engineers pasted internal source code into ChatGPT.

On the other side, Shopify's CEO wrote that ["reflexive AI usage is now a baseline expectation"](https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/), and teams have to show AI can't do a job before they ask for more headcount. Coinbase's CEO [fired engineers](https://techcrunch.com/2025/08/22/coinbase-ceo-explains-why-he-fired-engineers-who-didnt-try-ai-immediately) who hadn't tried the company's AI coding tools within a week and didn't have a good reason, an approach he admitted was heavy-handed.

Some of these bans have real reasons behind them, like leaked secrets or questions about where code came from, and I'll come back to those. Most companies sit somewhere between the two camps, and wherever you sit, there are two ways to die. Only one of them is obvious.

## Why we keep it manual

The people who insist on doing things by hand usually do it for one reason, and it's craft. A senior engineer has a very specific sense of what good code looks like, what the finished product should be, how the process should run and which standards matter, learned over years of shipping. A senior marketer has the same thing for a campaign: a taste element, a bar for what's good enough, what fits the brand and what will actually move the needle. It's how you guide an agency, a team, or your own work as a principal.

Experience makes it harder to let go. If you've done something the same way for 15 or 20 years, rebuilding your process from first principles, so an AI can follow it, is the hard part.

The taste is real, and it's usually the best thing about senior people. The problem is that it lives in their heads, and no agent can read it there.

## The obvious death

The first way to die is to stay manual, even when AI already does a good enough job.

Software engineering is the clearest example. **Any company that's still doing manual-only software engineering is already dead.** If your code reviews, checks and unit tests are still fully manual too, you're probably dead in the water already. The same goes for marketing: if you ship every campaign by hand, you're falling behind anyone who's using AI right now.

## The subtle death (it's me)

The second way to die is quieter. The company allows AI, but a human approves every step.

I'm the perfect example right now. I still micromanage a lot of the day-to-day work AI does for me, and everything goes through my review before it goes out, partly because the harnesses aren't there yet and partly because the bar for what goes out into the world is high. Mostly, though, it's a trust issue. After my agent [tagged the whole SDR team on a Thursday night](/posts/agent-tagged-the-whole-sdr-team/), I added an explicit approval step (yes, I made myself the bottleneck on purpose).

Even with me in the loop, it's a huge leap from how marketing used to work. I run marketing at a Series B startup with a team of three people in total, and we have dozens of live campaigns and contribute more than 35% of pipeline. Without AI, the same output would have needed two agencies, a designer, copywriters, paid ads managers and more. So I'm shipping about ten times faster than a manual-only marketer, and a marketer who goes fully agentic, with the right harnesses, will ship ten times faster than I do.

Right now, I'm the bottleneck in my own workflows. I don't plan to stay there. Once the trust framework is in place, I want to get out of the way of the agentic swarms and let them cook. Part of that is on me, building the harness and writing the instructions. The rest takes working at a company that's open to giving the AI worker that kind of freedom.

## Onboard the AI like a new hire

So how do you build that trust? You turn your taste into something the AI can follow, and you let it earn its autonomy one step at a time, the same way you would with a new hire. You don't have to stop reviewing tomorrow.

- **Humans own the brief.** The parameters, the definition of done, what good looks like. That part stays largely human, and you can use AI to sharpen it until the brief covers everything the factory needs to know.
- **Write tests and guidelines.** Our role as builders is to write the tests and the guidelines that prevent these errors from happening in the first place. Skipping the automation because we're scared it'll sound like AI doesn't fix anything.
- **Ban the actual failure.** Samsung's problem was secrets going into tools it didn't control, so that's the thing to block. curl got buried in AI slop bug reports and [ended its bug bounty](https://www.neowin.net/amp/beloved-tool-curl-is-shutting-down-its-bug-bounty-over-ai-slop-reports/), but it didn't ban AI. Its [contribution guide](https://github.com/curl/curl/blob/master/docs/CONTRIBUTE.md) accepts code written with the help of AI as long as it meets the normal standards, and bans people who submit made-up reports. My favorite line in it: "if someone can spot that the contribution was made with the help of AI, you have more work to do."
- **Onboard it like a team member.** At first you check its work and talk through what a great work product looks like. After 30, 60 and 90 days, a good hire gets to the point where you hand them a goal and the context, and they ship multiple campaigns to hit it.

So what would make me drop my review? The factory has to ship run after run without errors, the kind of run where I read it, understand it and say "yep, this is great work, keep going." The writing has to be high quality and match the brand voice, without sounding repetitive, mechanical or Claude-like, and it should feel familiar to the buyer, close to what they'll hear from a salesperson on the phone later in the funnel. And the visuals can't drift. From what I've seen in my work with AI over the past six months, it isn't quite there yet: the wording still gets awkward, and the visuals still drift.

I only just learned about the software factory approach, so I haven't shipped anything with it yet. My first try will be a nurture sequence, with my approval step still on. That's day one of onboarding.

Nudging the AI every step of the way is a 2023 way of thinking. Now we're talking about full autonomy in building, testing and shipping.

Keep your work human only, and you'll end up with a beautiful museum piece. People will stop by, say how nice it is, and go back to work with their agents.
