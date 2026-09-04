# Failure brief 5 · The Epic sepsis model (2021): good in the vendor's data, poor in the hospital's

*Read before Session 10 (Saturday 31 October). One page of facts; the diagnosis is your team's job in class and in Forum 5, Q3.*

**Kind of system:** classical machine learning · clinical prediction (early warning) · healthcare · United States

## What it was

Sepsis is a life-threatening reaction to infection; detecting it early saves lives. Epic Systems, the largest electronic-health-record vendor in the US, ships a **proprietary sepsis-prediction model** inside its software. Hospitals switch it on and it raises an alert in the patient record when a patient's risk score crosses a threshold. It was used by about **170 Epic customers, representing hundreds of hospitals**. Epic reported the model's discrimination (AUC, Video 1 segment 2) at **0.76–0.83**.

## What happened

- In **June 2021** researchers at **Michigan Medicine** (University of Michigan) published an **external validation** in *JAMA Internal Medicine*: they ran the model on their own patients, **38,455 hospitalisations** between December 2018 and October 2019, of which **2,552 (7%) developed sepsis**, and compared its alerts with what actually happened.
- They found an **AUC of 0.63**, far below the vendor's reported range. At the alert threshold Epic recommended, the model identified **33% of sepsis cases (sensitivity)** and **missed 67%**; its **positive predictive value was 12%** (one alert in eight was a real case); specificity was 83%.
- The model **generated alerts on 18% of all hospitalised patients**, creating what the authors described as substantial **alert fatigue**, and identified only **7% of the sepsis cases that clinicians had not already recognised** themselves.
- **Epic disputed** the findings, saying the threshold the researchers used was too low for clinical staff (more appropriate for a rapid-response team) and that the model's inputs and formula were available to hospital administrators. Epic later revised the model and its guidance; the episode became the standard reference for why models must be validated locally before use.

## The numbers

| | |
|---|---|
| Vendor-reported AUC | 0.76–0.83 |
| AUC in external validation | 0.63 |
| Sensitivity / specificity at the recommended threshold | 33% / 83% |
| Positive predictive value | 12% |
| Patients alerted | 18% of all hospitalisations |
| Sepsis cases missed | 67% |
| Deployment scale | ≈ 170 customers, hundreds of hospitals |

## What we know, and what we do not

We know the vendor's claim, the external results on one large hospital, the alert burden, and the vendor's response. We do not know how many hospitals had validated the model on their own patients before switching it on, or how thresholds were chosen at each site. Work with what is known; say explicitly where you are inferring.

## Your task

Fill the root-cause template (symptom · stage where it originated · missing control · accountable persona · corrective roadmap across the four modules), then one sentence: the single control that would most likely have prevented or contained it, and who should have owned it. Questions to help: what gate in Module 2 (Session 3 and 5: model validation, approval) was skipped when a hospital switched the model on? The truth (who developed sepsis) existed in every hospital's records: why was it not compared with the alerts until researchers did it (Video 1, segment 3)? Which monitoring metric would have shown the alert burden? Which of the six patterns (slide 21) apply?

## Sources

Wong A. et al., "External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients", *JAMA Internal Medicine*, 21 June 2021 · Fierce Healthcare, "Epic's widely used sepsis prediction model falls short among Michigan Medicine patients", 22 June 2021 · Habib et al., "The Epic Sepsis Model Falls Short—The Importance of External Validation", *JAMA Internal Medicine* editorial, 2021.
