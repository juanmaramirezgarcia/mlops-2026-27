# Failure brief 1 · Zillow Offers (2018–2021): when a forecast becomes a purchase

*Read before Session 10 (Saturday 31 October). One page of facts; the diagnosis is your team's job in class and in Forum 5, Q3.*

**Kind of system:** classical machine learning · price forecasting · consumer real estate · United States

## What it was

Zillow is the largest real-estate website in the US, known for the "Zestimate", an automated estimate of any home's value. In 2018 it launched **Zillow Offers**: instead of only estimating prices, Zillow would buy homes directly from owners at a price set with the help of its forecasting models, renovate them lightly and resell them within months. The business depended on one prediction: what the home would sell for a few months later, minus the costs.

## What happened

- Zillow Offers scaled aggressively in 2021, when US home prices rose sharply and then cooled unevenly across cities. The number of homes Zillow held rose from 3,142 at the end of the second quarter of 2021 to 9,790 at the end of the third.
- On **18 October 2021** Zillow paused new purchases, saying it had a backlog of homes to renovate and sell.
- On **2 November 2021** Zillow announced it would **close Zillow Offers entirely**, write down the value of its inventory by more than **$500 million**, and lay off about **2,000 people, 25% of its workforce**.
- CEO Rich Barton: *"We've determined the unpredictability in forecasting home prices far exceeds what we anticipated."* Analysts reported that a large share of the homes Zillow held were listed for less than it had paid for them.

## The numbers

| | |
|---|---|
| Lifetime of the business | about three years (2018–2021) |
| Homes held, Q3 2021 | 9,790 (3,142 a quarter earlier) |
| Write-downs announced | more than $500 million |
| Layoffs | ≈ 2,000 people, 25% of the workforce |

## What we know, and what we do not

We know the forecasting model set purchase prices at scale, that the market changed direction during 2021, that Zillow kept buying while prices in several markets fell, and that the company's own explanation was forecast unpredictability. We do not know the model's internal metrics, its retraining cadence, or exactly which approval steps existed between a forecast and an offer. Work with what is known; say explicitly where you are inferring.

## Your task

Fill the root-cause template (symptom · stage where it originated · missing control · accountable persona · corrective roadmap across the four modules), then one sentence: the single control that would most likely have prevented or contained it, and who should have owned it. Questions to help: what is the difference between a forecast being wrong and a forecast becoming a purchase? When did Zillow learn whether each forecast was right (Video 1, segment 3)? Which of the six patterns (slide 21) apply?

## Sources

GeekWire, "Zillow to shutter home buying business and lay off 2,000 employees", 2 November 2021 · AI Incident Database, incident 149 · Zillow Q3 2021 shareholder letter and earnings call.
