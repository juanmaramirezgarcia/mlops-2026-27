# Failure brief 6 · Knight Capital (1 August 2012): 45 minutes, eight servers, one missed

*Read before Session 10 (Saturday 31 October). One page of facts; the diagnosis is your team's job in class and in Forum 5, Q3.*

**Kind of system:** not machine learning. An automated trading system and a software deployment. It is in this set because it is the cleanest illustration of why Module 2 (pipelines, CI/CD, rollout strategies, rollback) exists, and every one of its failure modes applies to a model deployment.

## What it was

Knight Capital was one of the largest market makers in US equities, executing a large share of all retail share trades. Its automated router, SMARS, split large "parent" orders into small "child" orders and sent them to exchanges. On **1 August 2012** the New York Stock Exchange launched its Retail Liquidity Program (RLP), and Knight had written new code for SMARS to take part.

## What happened

- In the week before launch, a Knight technician deployed the new RLP code to the **eight servers** that ran SMARS. **One of the eight was missed.** There was no second person checking, and no automated check that the servers matched.
- The new code **reused an old flag**. On the seven updated servers the flag now meant "RLP order". On the unpatched eighth server the same flag still triggered **"Power Peg"**, a function that had been **disabled in 2003 but never removed from the code**, and which, because of an earlier change, no longer knew when to stop sending child orders.
- Before the market opened, Knight's systems sent **97 automated emails** referencing "Power Peg disabled" to a group of staff. They were **not designed as alerts and nobody reviewed them**.
- At 09:30 the eighth server began sending millions of orders. Knight's staff had no documented procedure for the situation and **no kill switch**. In one attempt to fix it, they **uninstalled the new code from the seven correct servers**, which made things worse: now all eight ran the defective path.
- After about **45 minutes** the system was stopped. Knight had executed **4 million trades in 154 stocks**, more than **397 million shares**, and held about **$3.5 billion of unwanted long positions and $3.15 billion of short positions**. Unwinding them cost about **$460 million**, more than the company's cash. Knight was rescued by an emergency investment within days and merged with a competitor (Getco) within a year.
- In **October 2013** the SEC fined Knight **$12 million** for violating the Market Access Rule, citing the absence of adequate controls over the deployment and of procedures to respond.

## The numbers

| | |
|---|---|
| Duration | ≈ 45 minutes |
| Trades | 4 million executions · 154 stocks · 397 million shares |
| Positions | ≈ $3.5 billion long, $3.15 billion short |
| Loss | ≈ $460 million |
| Unread warnings | 97 emails before the open |
| SEC penalty | $12 million (16 October 2013) |

## What we know, and what we do not

This case is unusually well documented, because the SEC's order describes the sequence in detail. What we do not know is why the process had no second check and why the emails were not designed as alerts; treat those as the questions.

## Your task

Fill the root-cause template (symptom · stage where it originated · missing control · accountable persona · corrective roadmap across the four modules), then one sentence: the single control that would most likely have prevented or contained it, and who should have owned it. Questions to help: which rollout strategy from Session 5 would have limited the damage to one server's worth? What is the difference between an email and an alert (Session 7, Video 1 segment 6)? Why did the fix make it worse, and what does a rollback need in order to be safe? Which of the six patterns (slide 21) apply, and how would each translate to a model deployment?

## Sources

US Securities and Exchange Commission, *In the Matter of Knight Capital Americas LLC*, Order Instituting Administrative and Cease-and-Desist Proceedings, Release No. 34-70694, 16 October 2013 (the primary source; the timeline above follows it) · Henrico Dolfing, "Case Study 4: The $440 Million Software Error at Knight Capital".
