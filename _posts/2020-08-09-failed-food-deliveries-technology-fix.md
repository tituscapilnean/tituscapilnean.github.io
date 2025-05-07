---
title: Failed food deliveries – a technology fix
date: 2020-08-09 10:00:00 +0000
categories: [English, Blockchain, Food Delivery]
tags: [deliveries, tech, blockchain, identity, zero-knowledge]
author: titus
---

Today, a Caviar courier managed to not delivery my order. This is not the first time a courier fails to deliver my food, although it showed as confirmed in the app. I live on a little hilltop building, with an alley way entrance between two small lion statues. I’m aware it’s hard to find and I always add instructions on how to get to my apartment. It usually works, but sometimes I get to starve for another 30+ minutes until we figure out other alternatives to the meal we’d been waiting for.

In this day and age, with contactless deliveries, which are great, it’s hard for couriers to know that they have delivered to the right person. So we need a solution to enable them to verify the order destination without me being there.

Sounds like a job for zero-knowledge proofs, if you’re a crypto-geek, like me. Or it’s just a simple async identity verification problem.

There’s a problem with addresses. Your GPS might say you’re at one address, but you’re actually at another building. Some buildings have the numbers well-hidden, others don’t have any numbers altogether, so couriers have to guess.

Being in love with technology, and being an advisor for Tailpath, I propose this simple solution:

- As a customer, I want to give the courier enough information for them to be able to verify my identity, without being face to face with them, but not have to print / show identifiers each time. I also don’t want to reveal my personal information at the door.
- As a courier, I want an easy way to verify if I’m dropping off the order in the right location. But I don’t always know if that’s the right address. I can’t ask the customer due to COVID or because they are not home, so I need to rely on signage.
- As an app builder (i.e. Caviar, Uber Eats), I would like to have a reliable way for couriers and customers to make the transaction without physically meeting.

Customers could have their address on a QR code on their door, for couriers to scan with their Tailpath app, or a white-label version of it within Caviar or Uber Eats or similar. You’d only need to put the code up once, and reuse over and over again.

If the address matches with the address given in the app, the delivery is confirmed and the courier knows they dropped off the order correctly, and the customer is notified. The courier can also take a photo of the delivery at the correct door, for proof.

If the address doesn’t match, the courier can call the customer for further instructions.

This way, the courier proves they delivered in the right place, and the customer has no way of arguing that there was a mis-delivery if the courier scanned the code at their door and left a photo proof of the delivery.

I hope these apps get better, so less people have to go through the hassle of not having their food delivered correctly.
