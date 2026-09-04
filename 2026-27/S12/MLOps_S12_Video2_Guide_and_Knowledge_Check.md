# Video 2 · Session 12 · AI Governance & Regulatory Readiness

**Recording guide, segment plan and the knowledge check (with answer key)**
*Deck: `MLOps_S12_Video2_AI_Governance.pptx` (20 slides; the segment label sits top-right on every slide). The speaker notes of every slide contain the recording script, with minute marks. No demo; a document-and-diagram lesson.*

---

## 1. What this is

A self-paced 60-minute video lesson, released on Saturday 31 October together with Session 10 and Forum 5, open until Friday 6 November. It is the governance deep-dive the syllabus sets for Session 12: what governance is as an operational discipline, the EU AI Act (risk tiers, obligations, provider vs deployer, the timeline as currently in force, penalties), the NIST AI Risk Management Framework, the documentation artefacts, human oversight, generative-AI governance, and the mapping of every requirement to a pipeline control point. It ends with a ten-question knowledge check that counts towards continuous assessment (15% of the course, shared with Video 1's check and the module quizzes).

It closes Module 4 and the course. Session 10 is the live LLMOps-and-diagnostics class; this video is the governance half of the module, and its "requirement → control point" table is the course synthesis from the governance side.

## 2. Segment plan

Record in segments; each is a separate take and a separate chapter marker on the campus player.

| Segment | Slides | Minutes | Content | Running example |
|---|---|---|---|---|
| Opening | 1–2 | 0:00–3:00 | Title; the map of eight segments; the thread from Session 10; "this applies to… and it requires…" | — |
| 1 · Governance | 3–4 | 3:00–9:00 | Governance is controls, not documents; the test; intentionality and accountability | the six failures; the churn model |
| 2 · The landscape | 5 | 9:00–12:00 | EU / US / UK / China; the four recurring ideas (risk, transparency, oversight, documentation) | — |
| 3 · EU AI Act | 6–10 | 12:00–27:00 | The risk pyramid; seven high-risk obligations; provider vs deployer; limited-risk and GPAI transparency; the timeline (verified); penalties and the "tier then one control" skill | IberBank credit/fraud, Amazon, Epic, the HR assistant, the Dutch case |
| 4 · NIST AI RMF | 11–12 | 27:00–34:00 | Govern, Map, Measure, Manage; how it complements the Act; the GenAI Profile | the churn model |
| 5 · Documentation | 13–14 | 34:00–41:00 | Datasheet, model card, decision log: what, who, when; a filled churn model card | the churn model |
| 6 · Oversight & GenAI | 15–16 | 41:00–49:00 | RACI; human-in vs human-on-the-loop; what to add to govern the HR assistant | churn model; HR assistant |
| 7 · Control points | 17–18 | 49:00–57:00 | Requirement → step → artefact → monitor; the governance loop over the lifecycle | the whole course |
| 8 · Wrap-up | 19–20 | 57:00–60:00 | Three things; the knowledge check; the end of the course | — |

## 3. Recording notes

- **Read the notes, not the slides.** The script in the speaker notes is written to be spoken and says more than the slide shows; the slides are the anchor, the notes are the lesson.
- **Pace.** About 130 words a minute. Each slide's notes end with a `[Timing: from–to]` line; segment 3 (the AI Act) is the longest, so re-check the clock there.
- **The timeline slide (9) is the one to keep current.** The dates were verified the week of recording (see section 4). Before you record, or before each new cohort, re-check them: the high-risk deadline already moved once (the Digital Omnibus, in force 27 July 2026, pushed Annex III to 2 December 2027 and Annex I to 2 August 2028). If a date has changed again, update slide 9 and its notes and nothing else; the rest of the deck is date-independent by design. Say on camera that dates move and that students should check the current text.
- **Say "not legal advice" once** (it is in the opening notes) and mean it: this is what an operator needs to work with the lawyers, not a substitute for them.
- **Consistency with the course.** The examples are the ones students know: IberBank (S3, S5) as the high-risk credit/fraud case, the churn model (S1, S7, V1) for the model card and RACI, the HR assistant (S10, V1) for GenAI governance, and the six Session 10 failures, above all the Dutch childcare-benefits case, as the cautionary tale the high-risk rules exist for.
- **Pauses.** "Pause here to write your one-line note" at the end of slides 6 (the risk pyramid), 10 (tier then one control), 11 (the four NIST functions) and 17 (the requirement → control-point table). Those four carry the quiz answers.
- **After recording.** Upload with chapter markers at the segment starts; attach the deck as PDF; open the knowledge check with a one-week window (closes 6 November) and a single attempt (see section 5).

## 4. The regulatory facts, and where they were checked (September 2026)

The EU AI Act timeline as recorded, verified against the sources below:

| Date | Status | What applies |
|---|---|---|
| 1 Aug 2024 | In force | The Act enters into force |
| 2 Feb 2025 | Applies | Prohibitions on unacceptable-risk systems (Art. 5); AI-literacy duty (Art. 4) |
| 2 Aug 2025 | Applies | General-purpose AI model obligations (Art. 51–56); the EU AI Office operational |
| 2 Aug 2026 | Applies (now) | Transparency duties (Art. 50); enforcement machinery |
| **2 Dec 2027** | **Postponed to** | **High-risk standalone systems (Annex III)** — moved from the original 2 Aug 2026 |
| **2 Aug 2028** | **Postponed to** | **High-risk systems embedded in regulated products (Annex I)** |

The postponement is the **Digital Omnibus** amendment: provisionally agreed after a late-2025 Commission proposal, published in the Official Journal on **24 July 2026**, in force **27 July 2026** — six days before the original high-risk deadline. The prohibitions, the GPAI rules and the transparency duties were **not** postponed. Penalties (confirmed): up to €35M or 7% of worldwide turnover for prohibited practices; €15M or 3% for other breaches; €7.5M or 1% for misleading information.

NIST AI RMF 1.0 (2023): four functions — Govern, Map, Measure, Manage; voluntary. The **Generative AI Profile** (NIST-AI-600-1) was published in July 2024.

Sources checked: Gibson Dunn, "EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines" (2026); Software Improvement Group, "EU AI Act Summary [August 2026 update]"; Cloud Security Alliance research note on the omnibus deferral; the EU AI Act text (Regulation (EU) 2024/1689) and NIST AI RMF 1.0. **Re-verify before each recording or cohort**, because these dates have already moved once.

## 5. Knowledge check

**Settings for the campus:** 10 questions, multiple choice, one correct answer each; single attempt; 20-minute limit (target 12); randomise question order; show the score but not the answers until the window closes on 6 November; individual work, no AI tools (syllabus policy).

Each question describes an AI use case in two sentences and asks for its EU AI Act risk tier and one required control. Eight are tier-and-control; two ask which NIST function an activity belongs to. Distractors are plausible tiers or controls that do not fit.

### Questions

**Q1.** A bank uses an AI model to decide whether to approve personal-loan applications; a rejected applicant cannot easily find out why. Under the EU AI Act, what is this system's risk tier and one required control?

a) Minimal risk; no obligations
b) High-risk (access to essential services); human oversight and a right to an explanation of the decision
c) Limited risk; a label saying content is AI-generated
d) Prohibited; it must be switched off

**Q2.** A government agency builds a system that scores citizens across many unrelated services to assign them a general "trustworthiness" rating used to grant or deny benefits. Tier and treatment?

a) High-risk; allowed with a conformity assessment
b) Limited risk; a transparency notice
c) Prohibited (unacceptable risk): general-purpose social scoring by public authorities is banned
d) Minimal risk; internal use only

**Q3.** An online shop adds a customer-service chatbot that answers questions about orders. It is not making decisions about anyone's rights. Tier and one required control?

a) High-risk; a fundamental-rights impact assessment
b) Limited risk; the chatbot must disclose that the user is interacting with an AI
c) Prohibited; chatbots are banned
d) Minimal risk; no obligation at all

**Q4.** A company buys a ready-made CV-screening model from a vendor and uses it, unchanged, to rank applicants for its own vacancies. Under the AI Act, what role does the company play, and what does that role require?

a) Provider; it must draft the model's technical documentation
b) Deployer; it must ensure human oversight, monitor the system in use, and (for this use) may need a fundamental-rights impact assessment
c) Neither; only the vendor has obligations
d) Provider; because using a model counts as building it

**Q5.** A hospital wants to switch on a vendor's sepsis-prediction model that flags at-risk patients. Recruitment, credit and this clinical use are all listed in Annex III. Tier and the control most relevant to the Epic case from Session 10?

a) Minimal risk; deploy and monitor informally
b) High-risk; accuracy and robustness validated on the hospital's own data before go-live
c) Limited risk; label the alerts as AI-generated
d) Prohibited; medical AI is not allowed

**Q6.** A social-media platform uses AI to generate a realistic video of a public figure saying something they never said, for a satirical campaign. Which AI Act duty applies most directly?

a) None; satire is exempt from all AI rules
b) The transparency duty: AI-generated or manipulated content (a deepfake) must be labelled as such
c) It is automatically prohibited
d) High-risk registration in the EU database

**Q7.** A firm adopts the NIST AI RMF. A team writes down, before building a hiring model, what the system is for, who could be affected, and what could go wrong. Which NIST function is this?

a) Govern
b) Map
c) Measure
d) Manage

**Q8.** In the same firm, a team runs quarterly tests of the deployed model's accuracy, its error rates by demographic group, and its robustness to bad inputs. Which NIST function is this?

a) Govern
b) Map
c) Measure
d) Manage

**Q9.** A retailer uses an AI model only to forecast how much stock to order for its warehouses; it makes no decision about any person. Tier and obligation under the AI Act?

a) High-risk; full conformity assessment
b) Limited risk; a disclosure that AI is used
c) Minimal risk; no specific AI Act obligations (though good practice still applies)
d) Prohibited; automated ordering is banned

**Q10.** An internal HR assistant answers employees' questions from company policy documents. It occasionally repeats an employee's name and salary that appeared in a document. Under governance and the AI Act's transparency regime, what is the right treatment?

a) Ignore it; the assistant is minimal risk
b) It is limited-risk for transparency (users must know it is AI), and the leak is a data-protection incident requiring a PII control on outputs, logging, and a human-escalation path
c) Prohibited; the assistant must be shut down permanently
d) High-risk; it needs a full conformity assessment before it can answer any question

### Answer key and rationale (professor only)

| Q | Answer | Why | Maps to |
|---|---|---|---|
| 1 | b | Credit/essential-services decisions about a person are Annex III high-risk; human oversight and explainability are required controls. | EU AI Act · high-risk |
| 2 | c | General-purpose social scoring by public authorities is an unacceptable-risk, prohibited practice (Art. 5). The Dutch case sits near this line. | EU AI Act · prohibited |
| 3 | b | An order-status chatbot is limited-risk; the duty is to disclose it is AI (Art. 50). | EU AI Act · limited risk |
| 4 | b | Using a bought model unchanged makes the company a deployer: oversight, monitoring in use, and a FRIA for some uses; the vendor is the provider. | EU AI Act · provider vs deployer |
| 5 | b | Clinical prediction is Annex III high-risk; accuracy/robustness validated locally before go-live is the control the Epic case lacked. | EU AI Act · high-risk · S10 |
| 6 | b | A deepfake triggers the Art. 50 transparency/labelling duty; satire is not exempt from labelling. | EU AI Act · limited risk |
| 7 | b | Understanding purpose, context and risks before building is the Map function. | NIST · Map |
| 8 | c | Assessing risks with numbers (accuracy, bias, robustness) is the Measure function. | NIST · Measure |
| 9 | c | Stock forecasting with no decision about a person is minimal risk; no specific AI Act obligation (good practice still applies). | EU AI Act · minimal risk |
| 10 | b | The assistant is limited-risk (disclose it is AI); repeating a name/salary is a data-protection incident needing a PII output control, logging and escalation — the S10 governance additions. | EU AI Act + governance · GenAI |

**Scoring:** 1 point each; pass at 6/10 for the continuous-assessment component. The two most-missed are usually Q2 (prohibited vs high-risk) and Q4 (provider vs deployer); spend two minutes on each at the exam review.

---

## 6. Checklist

- [ ] Deck reviewed; the timeline on slide 9 re-verified against the current AI Act text and any new omnibus changes
- [ ] Recorded in eight segments; total between 55 and 65 minutes
- [ ] Uploaded with chapter markers; deck attached as PDF
- [ ] Knowledge check created with the settings above; opens 31 October, closes 6 November 23:59
- [ ] Forum 5 opening post and the Session 10 closing slide point to the video and the deadline
- [ ] Exam-review session noted: Q2 and Q4 are the two to revisit
