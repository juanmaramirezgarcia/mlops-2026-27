# Forum 1 · Recap posts (one per question)

*Ready to paste on the campus, one per thread.*

---

## Q1 recap · Why models never reach production

Thank you all: 27 of you answered, most with real cases from your own companies, and that made this thread a pleasure to read. Three things worth keeping:

**1. Give three different kinds of reason, not three versions of the same one.** The strongest answers took each reason from a different area. Marcos, for example, gave one legal reason (insurance compliance rules), one technical (the old policy system the model had to connect to) and one about people (how the agents actually sell). Camila G. and Anas did the same. Because the reasons were different, each one pointed to a different persona, and they said why *that* persona and not another. If the same persona appears in two of your three reasons, you have probably described one problem twice.

**2. A real obstacle is not the same as a to-do item** (Khem to Marcos). "Connect the model to the old system" is work that is usually planned and assigned: it delays a project but does not stop it. A reason a model *never* reaches production is something only one person can remove (legal approval, an owner after launch, a place in the business system for the model to plug into), and if that person does not act, the project quietly dies. A simple test: if nobody does anything special, will it happen anyway? If yes, it is a task, not a blocker.

**3. "Is the data secure?" and "are we allowed to use it?" are different questions** (Khem, Barbara). The first belongs to the Data Engineer; the second to Risk & Compliance.

The persona most often forgotten was the business owner of the decision the model feeds. A model nobody acts on never really reaches production.

Line of the week, from Khem: *"the platform can be 100% up while every order proposal is wrong."*

---

## Q2 recap · The responsibility map (RACI)

20 maps and no two alike, which is fine: the reasoning is what counts. Three lessons:

**1. Exactly one A per row.** That is the whole point of a RACI map: when a row has no A, nobody answers when that stage fails. A tip for next time: give validation its own row. When it sits inside "model development", the question of who signs off the model before it goes live disappears, and that is the most important decision in the map.

**2. Who signs off validation depends on the decision.** Some of you gave the A to the Product Owner ("good enough" is a business call); others gave it to Risk & Compliance ("the business should not mark its own homework"). Both can be right. Khem's rule of thumb: if the model affects someone's access to credit, a job or a price, the A moves to Risk.

**3. Responsible and Accountable are different questions.** The ML Engineer does the monitoring, but who answers when sales drop? (Barbara.)

Julio M. asked the best open question of the thread: when a model is retrained after drift, does it go back through validation? **Yes.** A retrained model is a new model, so it passes the same gates as any other. Otherwise the ML Engineer is approving a new model alone. Session 3 shows those gates (Dev → QA → Prod).

---

## Q3 recap · Training vs operationalising

Most of you defined the difference well, and the best definitions were short: *"a trained model is a result, an operational model is a service"* (Marcos); *"an experiment that ends vs a service that never ends"* (Armen).

What separated the strongest answers was the **consequence**: a mechanism and a cost.

- **Marcos:** claims history refreshed monthly instead of in real time, so renewals were underpriced for months.
- **Armen:** a pricing model with nowhere to plug it in, so zero revenue.
- **Ayushi:** a capability bought but never switched on, so cash sat on the shelves and aircraft stayed on the ground.

If your answer stopped at "the model will be wrong", ask yourself: wrong how, noticed by whom, and costing what?

One insight to keep: Ana Cristina noticed that if agents only call the leads the model ranks highest, the next training set contains only those leads, and the model learns from its own choices. Tanvi and Sigursteinn proposed a small random holdout, and Tanvi saw the catch: it costs calls today, so it is a business decision, not a technical one. We come back to these feedback loops in the monitoring sessions.

*A reminder for everyone: declare AI use (or no use) on every post, replies included.*
