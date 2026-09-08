# Project Roadmap — Novo Nordisk India Insulin Strategy (Independent Case)

## What changed from the original 12-week plan, and why

1. **Added parallel tracks.** The original plan was strict waterfall — market sizing fully finishes before competitive intelligence starts, which finishes before pricing starts. In practice, market sizing and competitive intelligence draw on overlapping sources and can run side by side; sequencing them serially just adds calendar time for no analytical benefit.
2. **Added two checkpoint gates** (end of Week 3, end of Week 6) where you explicitly revisit your hypotheses against what you've actually found, before sinking more weeks into a direction the evidence doesn't support.
3. **Added a buffer week (Week 8).** India-specific insulin pricing and procurement data is genuinely sparse in public sources — the original plan had zero slack, so any blocked data source would cascade through every remaining week.
4. **Added an explicit time budget** per phase, because "Week 3: Market Sizing" means something very different at 5 hrs/week vs. 25 hrs/week.
5. **Moved career-conversion work earlier and made it incremental** instead of a single end-loaded week — draft resume bullets and the interview story as each workstream finishes, not all at once when you're already fatigued and the details are fading.
6. **Collapsed 12 weeks to 10 phases**, matching the engagement-brief structure this roadmap should stay consistent with, rather than inventing a separate week count.

**Total estimated effort:** ~120–160 hours depending on data availability. At 10–12 hrs/week (realistic alongside a job or coursework), that's 10–12 weeks; at 20+ hrs/week, compress to 6–7.

---

## Phase 1 — Define (Week 1) · ~10–14 hrs

- [ ] Finalize problem statement and primary decision
- [ ] Identify the hypothetical decision-maker and decision
- [ ] Build the issue tree (MECE against the core decision, not just topic coverage)
- [ ] Draft hypotheses H1–H6 with required evidence for each
- [ ] Define scope boundaries (what this case explicitly does *not* cover)

**Output:** Project charter, issue tree, hypothesis register (all status: OPEN)

---

## Phase 2 — Foundation + Market Sizing *(run in parallel)* (Weeks 2–3) · ~24–30 hrs

**Track A — Science & Industry Foundation**
- [ ] Diabetes epidemiology and insulin biology basics
- [ ] Insulin classes, treatment pathways, patient journey
- [ ] India healthcare system structure (public/private split, procurement channels)

**Track B — Market Sizing**
- [ ] Bottom-up population cascade: total population → diabetes → diagnosed → treatment-eligible → insulin-relevant → addressable
- [ ] Top-down cross-check against published market-size estimates
- [ ] Triangulate; document the gap between top-down and bottom-up and why
- [ ] Patient segmentation (economically meaningful segments, not demographic trivia)

**✅ Checkpoint 1 (end of Week 3):** Do H1 and H2 hold up against what you've found so far? If your addressable population or segmentation looks nothing like assumed, revise the hypothesis register now — not in Week 8.

**Output:** Industry foundation doc, triangulated TAM/SAM/SOM, patient segmentation

---

## Phase 3 — Competitive Intelligence + Pricing/Access *(run in parallel)* (Weeks 4–5) · ~24–30 hrs

**Track A — Competitive Intelligence**
- [ ] Build the competitor database (product, class, pricing, distribution, positioning, patient support)
- [ ] Competitive matrix and price-value map
- [ ] Competitor response scenarios for each strategic option (build this now, reuse in Phase 6)

**Track B — Pricing & Market Access**
- [ ] Price benchmarking across insulin categories
- [ ] Patient affordability analysis
- [ ] Government programs, procurement channels, reimbursement pathway realism check

**Output:** Competitive intelligence database, pricing/access assessment

---

## Phase 4 — Health Economics (Week 6) · ~10–14 hrs

- [ ] Treatment cost model per patient segment
- [ ] Clinical value → economic value translation
- [ ] Budget-impact framing for payers/institutions

**✅ Checkpoint 2 (end of Week 6):** Re-test H3–H5 against the pricing, access, and economics evidence now in hand. Explicitly mark each hypothesis SUPPORTED / REJECTED / INCONCLUSIVE before moving into modeling — do not carry unresolved hypotheses into the financial model.

**Output:** Health economics model, updated hypothesis register

---

## Phase 5 — Buffer / Data Gap Resolution (Week 8) · flexible

Use this week for whichever of the following actually happened (at least one will):
- Chasing down a data source that turned out to be paywalled or unavailable, and documenting the assumption that bridges the gap
- Re-running any Phase 2–4 analysis that Checkpoint findings called into question
- Catching up if Weeks 2–6 ran long

If nothing needs fixing, use this week to start the financial model early rather than letting it sit idle.

---

## Phase 6 — Financial Model + Strategic Options *(run in parallel)* (Weeks 7–8, overlapping buffer) · ~24–30 hrs

**Track A — Financial Model**
- [ ] Revenue model: population × adoption × units/patient × net price
- [ ] Cost structure: COGS, distribution, access-program investment, commercial investment
- [ ] Base / Upside / Downside scenarios
- [ ] Sensitivity analysis (price, share, adoption, persistence, competitor pricing, cost, access spend)

**Track B — Strategic Options**
- [ ] Build out all four options using the model outputs from Track A
- [ ] Score against strategic attractiveness, patient impact, financial attractiveness, feasibility, defensibility
- [ ] Eliminate at least two options with stated evidence — this is the step most likely to get shortcut; don't let it
- [ ] Define kill criteria for the option you keep

**Output:** Auditable financial model, strategic option scorecard, eliminated-options rationale

---

## Phase 7 — Recommendation + Implementation (Week 9) · ~14–18 hrs

- [ ] Finalize the recommendation: what, who, where, how, when, how much, why, what-if
- [ ] Build the 0–12mo / Year 2 / Years 3–5 roadmap
- [ ] KPI framework (commercial, patient, market-access, operational, strategic)
- [ ] Risk register with mitigations

**Output:** Recommendation memo, implementation roadmap, KPI framework, risk register

---

## Phase 8 — Deliverables + Quality Control (Week 10) · ~14–18 hrs

- [ ] Build the executive deck (headline + evidence + implication per slide — no decorative charts)
- [ ] Write the executive memo
- [ ] Compile the source book (every material claim traceable)
- [ ] Run the five audits: fact-check, source-check, model-check, logic-check, executive-check
- [ ] Finalize GitHub repo structure and README

**Output:** Full consulting deliverable package, audited

---

## Ongoing (not a discrete week) — Career Conversion

Do this incrementally as each phase closes, not as a single Week 12 sprint:
- After Phase 2: draft the market-sizing resume bullet while the method is fresh
- After Phase 6: draft the financial-model and strategic-options bullets
- After Phase 8: assemble the portfolio summary and 2-minute pitch from what you already drafted, rather than writing it cold

Keep this material **outside** the analytical repo narrative — see `REPO_STRUCTURE.md` for where it belongs.

---

## Definition of Done

The project is complete only when every item below is true — not when the report is written:

- [ ] Business problem and decision-maker clearly defined
- [ ] Issue tree is MECE against the actual decision
- [ ] Every hypothesis has a final status (not left OPEN)
- [ ] Market size is triangulated (top-down + bottom-up reconciled)
- [ ] Competitors systematically analyzed, not just listed
- [ ] Patient segments are economically meaningful
- [ ] Financial model is auditable — every number traces to a source, assumption, or formula
- [ ] Scenarios and sensitivity analysis are complete
- [ ] At least two strategic options were eliminated with evidence, not just deprioritized
- [ ] Recommendation specifies segment, geography, product, price point, and investment amount
- [ ] Implementation roadmap and KPIs are realistic, not aspirational
- [ ] Five quality-control audits are complete
- [ ] You can defend the recommendation, unscripted, in under 10 minutes