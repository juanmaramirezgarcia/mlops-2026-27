# Failure brief 4 · The Dutch childcare-benefits algorithm (2013–2021): a risk score treated as proof

*Read before Session 10 (Saturday 31 October). One page of facts; the diagnosis is your team's job in class and in Forum 5, Q3.*

**Kind of system:** risk scoring (a self-learning model combined with rules) · fraud selection in public administration · the Netherlands. Known in Dutch as the *toeslagenaffaire*.

## What it was

The Dutch Tax and Customs Administration (Belastingdienst) pays childcare benefits to parents. To fight fraud, it used a **risk-classification system** to select claims for investigation. From around 2013 the system scored applications; high-risk claims were pulled for manual checks and, in practice, treated as fraud. **Nationality, including dual nationality, was among the risk indicators**, and the model was self-learning: officials could not explain why a particular family had been flagged.

## What happened

- Flagged parents were treated as fraudsters, often on the basis of **small administrative errors** (a missing signature, a late form), and ordered to **repay the full benefit received**, sometimes tens of thousands of euros, with no effective way to contest the decision. Families were bankrupted; some lost their homes and jobs; children were taken into care in a number of cases.
- Journalists at **RTL Nieuws and Trouw** brought the practice to light from **September 2018**. It emerged that families with a second nationality had been systematically singled out.
- A parliamentary inquiry published its report, **"Ongekend onrecht" (Unprecedented Injustice), on 17 December 2020**, describing a system in which fundamental principles of the rule of law had been violated.
- On **15 January 2021 the Rutte III cabinet resigned** collectively over the scandal.
- The **Dutch Data Protection Authority** found the processing of nationality *"unlawful, discriminatory and improper"* and fined the tax authority **EUR 2.75 million (December 2021)**, and a further **EUR 3.7 million (2022)** for an illegal blacklist (FSV) of suspected fraudsters.
- Compensation of **EUR 30,000 per wrongly accused parent** was announced in December 2020, with further schemes since; Amnesty International's 2021 report called the system *"Xenophobic Machines"*.

## The numbers

| | |
|---|---|
| Parents wrongly accused | ≈ 26,000 (figures up to 35,000 are cited) |
| Repayment demands | up to tens of thousands of euros per family |
| DPA fines | EUR 2.75 million (2021) + EUR 3.7 million (2022) |
| Initial compensation | EUR 30,000 per parent |
| Political outcome | resignation of the government, 15 January 2021 |

## What we know, and what we do not

We know the risk indicators included nationality, that scores triggered enforcement, that decisions could not be explained or effectively contested, and the institutional response. The full technical design of the model has never been published. Work with what is known; say explicitly where you are inferring.

## Your task

Fill the root-cause template (symptom · stage where it originated · missing control · accountable persona · corrective roadmap across the four modules), then one sentence: the single control that would most likely have prevented or contained it, and who should have owned it. Questions to help: which feature should never have been in the model, and which control would have caught it (Session 7's bias slide; Video 2's risk tiers)? What is the difference between a score that triggers an investigation and a score that triggers a penalty? Who could have said no, and at what level? Which of the six patterns (slide 21) apply?

## Sources

Dutch parliamentary inquiry committee, *Ongekend onrecht*, 17 December 2020 · Autoriteit Persoonsgegevens, decisions of December 2021 and April 2022 · Amnesty International, *Xenophobic Machines*, October 2021 · Al Jazeera / Reuters, "Dutch PM Rutte and his government quit over child welfare scandal", 15 January 2021.
