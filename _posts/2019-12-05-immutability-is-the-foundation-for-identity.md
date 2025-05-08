---
title: Immutability is the foundation for identity
date: 2019-12-05 10:00:00 +0000
categories: [English, Blockchain]
tags: [identity, blockchain, immutability]
author: titus
---

When I was working actively in the blockchain space, one of the biggest debates for the “non-believers” was around immutability and why it matters, especially in the notorious double-spend problem. If you don’t recognize the problem, it’s hard to see a solution or an advantage.

**Chargebacks:** If chargebacks are not a problem, “immutability is not an advantage of blockchain, it is simply a feature of blockchain. But it is not solving anything, so why put it up as an advantage?”

**Government tax numbers:** “For instance, I can say that I have a product which makes sure that the government does not arbitrarily change your tax number. Okay. But is there a big problem of governments changing people’s tax numbers? Not in the slightest! So why mention it as an advantage? It is solving a non-existing problem.”

These challenges seem to be very different. But they are not.

Both the chargeback problem and the government tax problem described above are about identity. Let me explain how. Chargebacks are about who took my money for the wrong reasons and how I get it back, within a network. The government tax number is about how the government identifies its tax payers so you can be sure that it recognizes you have paid your dues. Both trust the central “oracle”, the governor of the network or the country administrators/tax collectors. Both are vulnerable to Sybil attacks and can only work with other networks/countries if there is trust and transparency across networks.

Let’s take a step back and talk about identity. There are three forms of identity as of today:

- **Non-digital identity** – think of your birth certificate, your driver’s license, your old passport and other paper/plastic/metal documents  
- **Digital identity** – your SSO service, your user management platform, Facebook account, your biometric data on a new passport, your email address, credit cards  
- **Decentralized identity** – similar to the digital identity category, but issued and/or stored outside a centralized database, on individual devices/mediums that the owner controls  

While the first two are easier to grasp, the third one is still nascent, with a few use cases emerging now in access management, cryptocurrency wallets, for example. You’d be tempted to say that immutability is only key for the decentralized identity category.

And you would be wrong.

Our world goes through great lengths to make sure that your non-digital and digital identity is unique and immutable, so that you can’t be one person today and another person the next day. This immutability and the identity consistency that it creates is the foundation of our society. You can create long term relationships only if the other person is who they say they are over time and that statement does not fundamentally change.

This immutability attribute is what makes identity possible, not just decentralized identity, all identity.

The difference is that you’re not relying on a 3rd party to keep records of who is who, like in the centralized examples. With decentralized identity, you are relying on immutable records of a person’s (or a bot’s, if you like) collection of credentials and their minimum viable verification proof (MVVP). There’s a lot of materials to read on the topic, especially from the W3C, a standardization body that makes the internet interoperable.

Since I brought up interoperability, immutability is a direct enabler of that as it becomes exponentially easier to operate across networks if you don’t have always verify all the actors all over again from scratch. The costs and time to verify drop significantly.

If you’re a blockchain non-believer, or nay-sayer, try thinking about a time you had to redo something all over again, like prove who you are, because there was no easy way to cross networks reliably. It might not be an obvious problem today, but in the future it will speed up and increase the security of travel, payments, building access, virtually any kind of transaction that occurs between two or more parties that need to be identified.
