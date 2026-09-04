# Failure brief 2 · Amazon's recruiting tool (2014–2017): a model that learned who used to be hired

*Read before Session 10 (Saturday 31 October). One page of facts; the diagnosis is your team's job in class and in Forum 5, Q3.*

**Kind of system:** classical machine learning · classification / ranking · HR and hiring · United States (reported by Reuters in October 2018)

## What it was

From 2014 a team in Amazon's Edinburgh engineering hub built an experimental tool to review job applicants' CVs and score them from one to five stars, the way shoppers rate products. The goal was to hand recruiters the top candidates automatically. About **500 models** were built, one per job function and location, recognising some **50,000 terms** that appeared in past CVs.

## What happened

- The models were trained on **ten years of CVs submitted to Amazon**, most of them from men, reflecting the gender imbalance of the technology industry. In effect the system learned what past successful applicants looked like.
- By 2015 the team realised the system was rating candidates for technical jobs in a gender-biased way. It **penalised CVs containing the word "women's"** (as in "women's chess club captain") and **downgraded graduates of two all-women's colleges**. It favoured verbs more common in male candidates' CVs, such as "executed" and "captured".
- Amazon edited the models to make them neutral to those particular terms, but could not guarantee they would not find other ways to sort candidates that proved discriminatory.
- The team was **disbanded by the start of 2017**; executives had lost hope for the project. A watered-down version was kept for basic tasks such as removing duplicate profiles.
- Amazon said recruiters looked at the tool's recommendations but **never relied solely on them**, and stated that the tool "was never used by Amazon recruiters to evaluate candidates".

## The numbers

| | |
|---|---|
| Models | ≈ 500, one per job function and location |
| Vocabulary learned | ≈ 50,000 terms |
| Training data | ten years of CVs, predominantly from men |
| Output | a 1–5 star rating per applicant |
| Lifetime | 2014 to early 2017; never the sole basis for a decision |

## What we know, and what we do not

We know the training data, the observed behaviour, the attempted fix and the outcome. We do not know what testing was done before recruiters saw any recommendation, whether outcomes were ever measured by gender, or who decided the use case was appropriate. Work with what is known; say explicitly where you are inferring.

## Your task

Fill the root-cause template (symptom · stage where it originated · missing control · accountable persona · corrective roadmap across the four modules), then one sentence: the single control that would most likely have prevented or contained it, and who should have owned it. Questions to help: where does a model learn "who is a good candidate" (Session 1, Session 7's three places bias enters)? Is removing the word "women's" a fix or a symptom removed? Was the failure caught by a control, or by people noticing? Which of the six patterns (slide 21) apply?

## Sources

Reuters (Jeffrey Dastin), "Amazon scraps secret AI recruiting tool that showed bias against women", 10 October 2018, as carried by CNBC and others.
