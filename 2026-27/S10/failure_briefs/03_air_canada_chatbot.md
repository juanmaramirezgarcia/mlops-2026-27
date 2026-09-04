# Failure brief 3 · Air Canada's chatbot (2022–2024): "the chatbot is a separate legal entity"

*Read before Session 10 (Saturday 31 October). One page of facts; the diagnosis is your team's job in class and in Forum 5, Q3.*

**Kind of system:** generative AI · customer-service assistant on the airline's website · Canada

## What it was

Air Canada's website offered a chatbot to answer customers' questions. Like the HR assistant in Video 1 and Session 10, it produced written answers to free-text questions and could link to pages of the airline's website.

## What happened

- In **November 2022**, after his grandmother died, Jake Moffatt asked the chatbot about **bereavement fares** (reduced fares for people travelling because of a death in the family). The chatbot told him he could **book at the full price and apply for the bereavement discount within 90 days** of the ticket being issued.
- The chatbot's answer included a **link to Air Canada's bereavement policy page**, which said the opposite: the bereavement policy **does not apply to requests made after travel**.
- He booked and flew (about **CAD 1,640** for the round trip; the bereavement fare would have been about **CAD 760**), then applied for the partial refund. Air Canada refused, pointing to the policy page, and eventually offered a coupon.
- He took the case to the **British Columbia Civil Resolution Tribunal**. Air Canada argued that the chatbot was *"a separate legal entity that is responsible for its own actions"*, and that the customer should have checked the linked page.
- On **14 February 2024** the tribunal member, Christopher Rivers, called that argument *"a remarkable submission"*, found **negligent misrepresentation**, and ordered Air Canada to pay **CAD 650.88 in damages plus interest and fees (about CAD 812)**. Air Canada had not taken reasonable care to ensure its chatbot was accurate, and it made no difference that the information came from a chatbot rather than a static page. The chatbot was subsequently removed from the website.

## The numbers

| | |
|---|---|
| Fare paid vs bereavement fare | ≈ CAD 1,640 vs ≈ CAD 760 |
| Awarded | CAD 650.88 damages + interest and fees ≈ CAD 812 |
| Time from answer to ruling | ≈ 15 months |
| Decision | Moffatt v. Air Canada, 2024 BCCRT 149, 14 February 2024 |

## What we know, and what we do not

We know what the chatbot said, what the linked policy said, the airline's legal position and the tribunal's decision. We do not know how the chatbot was built (whether it retrieved the policy text or answered from a general model), whether its answers were ever evaluated against the policies, or who inside Air Canada owned it. Work with what is known; say explicitly where you are inferring.

## Your task

Fill the root-cause template (symptom · stage where it originated · missing control · accountable persona · corrective roadmap across the four modules), then one sentence: the single control that would most likely have prevented or contained it, and who should have owned it. Questions to help: the chatbot linked to the page that contradicted it; which guardrail from Session 10 checks an answer against its own sources? What should an assistant do with a policy question it is not sure about? Who is accountable for what an assistant writes, and does the small amount change the size of the precedent? Which of the six patterns (slide 21) apply?

## Sources

BC Civil Resolution Tribunal, *Moffatt v. Air Canada*, 2024 BCCRT 149 · American Bar Association, Business Law Today, February 2024, "BC Tribunal Confirms Companies Remain Liable for Information Provided by AI Chatbot" · CBC News, 15 February 2024 · AI Incident Database, incident 639.
