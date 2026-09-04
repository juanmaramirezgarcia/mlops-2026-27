# Session 7 · Live demo script: "what a drift report looks like" (Evidently + SHAP)

**Slot:** minutes 24–32 (slide 14 "What a drift report looks like", then slide 15 "What you just saw")
**Duration:** 8 minutes, browser and two images; everything pre-rendered, nothing computed live
**Assets:** `S07/demo/` — `drift_report.html`, `performance_by_segment.png`, `shap_waterfall.png`, `shap_summary.png` (built by `s7_demo_setup.py`); `lime_customer.html/.png`, `lime_text.html/.png` (built by `s7_lime_setup.py`)
**Second demo moment:** minutes 41–43 (slide 21 "A second opinion: LIME"), 2 minutes, optional browser

---

## 1. Setup (already done; what you need before the session)

The four files in `S07/demo/` are the demo. They were generated once from a churn model trained on "June" data and scored on "October" data in which two things changed: a new pricing plan moved monthly charges up (data drift) and a competitor launched fibre in the North, so long-tenure customers there started leaving (concept drift). Open them before class:

| Tab | File | What it shows |
|---|---|---|
| 1 | `drift_report.html` (double-click; opens in the browser) | Evidently data-drift report, June vs October, seven columns |
| 2 | `performance_by_segment.png` | Accuracy June vs October, overall and by segment, with the retrain trigger |
| 3 | `shap_waterfall.png` | Why one North, long-tenure customer scores 70% churn risk |
| (4) | `shap_summary.png` | Optional: which features drive risk across all customers |
| 5 | `lime_customer.html` | LIME on the same customer, interactive (used at minute 41, slide 21) |
| 6 | `lime_text.html` | LIME on a support message: the words that made it "about to cancel" |

Zoom the browser to 125%. The report is a single self-contained HTML file; it needs no server and no internet. If you want to regenerate the assets (not needed), install `evidently shap matplotlib` into the Session 3 venv and run the script from `S07/demo/`; the numbers are deterministic (fixed seeds), so they will match this document.

Numbers to have in your head: accuracy June 82% → October 80% overall; North with tenure over 36 months: 89% → 65%; the report flags 3 of 7 columns as drifted (monthly charges, promotions, the model's own predictions) but declares "dataset drift NOT detected" because its default rule needs half the columns to move.

---

## 2. The eight minutes, click by click

### Tab 1 · The drift report, the headline (≈ 1.5 min)

> "This is a drift report from Evidently, an open-source tool; the cloud platforms and IBM watsonx.governance produce the same thing in a dashboard. Left: the reference, the June data the model was trained on. Right: the current window, October's requests. For every column, two little histograms and a verdict."

Point at the headline: "Dataset drift is NOT detected." Then at the tiles: 7 columns, 3 drifted, share 0.429.

> "Read the small print: the threshold is 0.5. Three of seven columns moved, and the tool says 'no drift' because fewer than half moved. That is not a fact about the data; it is a default somebody did not change. Thresholds are decisions."

### Tab 1 · The table (≈ 2 min)

Scroll to the table. Point at `monthly_charges`: drifted, distance 0.71; the two histograms visibly shifted right.

> "Monthly charges: the new pricing plan. The whole distribution moved up. This is data drift, and the report sees it without a single label."

Point at `promo_weeks_last_quarter`: drifted. Then at `prediction`: drifted, distance 0.12.

> "And the model's own predictions moved: more customers scored as high risk. That is prediction drift, the earliest warning; the model is reacting to something."

Point at `tenure_months` and `region_north`: not detected, distances near zero.

> "Now the two that did not move: tenure and region. Remember them."

Click the arrow next to one drifted column to expand its distribution plot if time allows (10 seconds).

### Tab 2 · What the report cannot see (≈ 2 min)

> "October's labels have just arrived: who actually churned. Here is accuracy, June against October. Overall: 82 to 80. Two points; nobody would call a meeting. Now look at the second pair: North region, tenure over 36 months. 89 to 65."

Point at the dashed line: "This model's retrain trigger is 75%. Overall we never crossed it. The segment crossed it by ten points."

> "Tenure did not move. Region did not move. The drift report was right: the inputs are the same. What changed is what those customers do: a competitor arrived. Same inputs, different behaviour. That is concept drift, and no report on the inputs can see it. Only labels can, and only if you look by segment."

### Tab 3 · One explanation (≈ 1.5 min)

> "One of those customers. The model gave her 70% churn risk. Why? Start at the bottom: the average customer is 24%. Three support tickets pushed her up 26 points. High charges, 19 more. Long tenure pulled her down 8. Monthly contract, promotions, small pushes. And region: zero."

Pause on region_north = +0.

> "Zero. In June, region did not matter, so the model learned to ignore it. In October, region is the whole story in the North, and the model cannot know. An explanation that gives zero weight to the thing that changed is itself a monitoring signal: this is how a data scientist finds concept drift before the labels confirm it."

### Back to the slide (≈ 30 s)

> "Three things: a report that flagged three columns and said 'no drift', because thresholds are decisions; a two-point fall overall that was a seventeen-point fall in one segment; and an explanation that pointed at the missing piece. Data drift, concept drift, and why you need both the report and the labels."

Switch to slide 15, "What you just saw" (which carries the segment chart).

---

## 3. The LIME moment, in the explainability block (minute 41–43, slide 21)

Slide 21 carries both LIME images, so this can be done from the slide alone. With one extra minute, open **Tab 5** (`lime_customer.html`): LIME's own view, with the prediction probabilities on the left, the bars in the middle and the customer's actual values on the right.

> "Same customer, second method. LIME does not know anything about how the model was built; it asks the model thousands of 'what if' questions around this customer (what if she had two tickets instead of three? an annual contract?) and fits a simple rule to the answers. Read the bars: more than two tickets, a monthly contract and charges above €76 push towards churn; tenure pulls away; region and promotions do nothing. SHAP said the same by a completely different route. When two methods agree, trust the explanation more; when they disagree, you have learned that the explanation is fragile, which is also worth knowing."

Then **Tab 6** (`lime_text.html`): the support message with the highlighted words.

> "And this is what LIME does best. A message classified 'about to cancel', 89%. The highlighted words are the reason: switching, drops, unless, price, provider. 'Fixed' and 'week' pull the other way, because people who say 'fixed this week' sometimes stay. A support manager reads this in five seconds and knows what to do. Keep this picture: in Session 10 the model is a language model, and 'explain the output' becomes 'which part of the input drove it'."

Switch to slide 22, "Do not trust an explanation blindly", which follows naturally: LIME's simple model can be a poor fit.

## 4. Optional: the code behind the demo (if someone asks, ≈ 1 min)

**If someone asks "how much code is that?"** jump to appendix slides 39 (the Evidently lines: the report on the left, the same checks as PASS/FAIL tests on the right, which is what Video 1's monitoring job does) and 40 (the SHAP and LIME lines). Each is a dozen highlighted lines; the point to make is that the model is never touched: monitoring and explanation code sits beside the model. The full scripts are `s7_demo_setup.py` and `s7_lime_setup.py` in this folder if you prefer to open the real file.

## 5. Optional beeswarm (if ahead of time, ≈ 1 min)

Open `shap_summary.png`: the beeswarm of six features across 600 October customers. "This is the same explanation for everyone at once: which features push risk up in general. Support tickets and monthly contracts dominate; region is a thin line. If you produced this chart every month and stored it, the month region started to matter would be visible as a change in this picture. Explanations drift too."

---

## 6. If something goes wrong

| Problem | Do this |
|---|---|
| The HTML does not open or renders blank | Try another browser (the report uses JavaScript; any current browser works offline). Fallback: the screenshot `demo/screenshots/drift_report.png` if you took one; otherwise skip to Tab 2, which carries the lesson. |
| The LIME HTML shows a blank page | It needs JavaScript; any current browser works offline. The PNGs on slide 21 carry the same content. |
| A student asks what "Wasserstein distance" means | "How far you would have to move the bars of one histogram to make it the other. Bigger means more different. The formulas are in the appendix; not in the exam." |
| A student asks why the tool says no drift when three columns moved | That is the point; let them answer: the threshold is 0.5 by default; thresholds are decisions. |
| No time | Do Tab 1 headline (1 min) and Tab 2 (2 min). Skip the table detail and the waterfall; the waterfall is on slide 20 anyway. |

---

## 7. Checklist

- [ ] The six files open (report, segment chart, two SHAP images, two LIME pages); browser zoomed to 125%
- [ ] The three numbers memorised: 82 → 80; 89 → 65; 3 of 7, threshold 0.5
- [ ] Slides 15 (segment chart), 20 (waterfall) and 21 (LIME) ready as landing slides
- [ ] Optional screenshot of the report saved as fallback
