# Sensitivity Analysis Summary

Full data: `../outputs/sensitivity_analysis.csv`. Each variable is shifted ±10% from its Base Case path and the resulting Year-5 revenue impact is measured (illustrative elasticities — consulting assumptions, see script comments in `../../15_ANALYTICS/python/insulin_india_model.py`).

## Ranked by Revenue Impact (Tornado Order)

| Rank | Variable | Revenue Swing (₹ crore) |
|---|---|---|
| 1 | Novo Nordisk market share | ~417 |
| 2 | Insulin price (blended) | ~396 |
| 3 | Patient adoption / initiation rate | ~292 |
| 3 (tie) | Overall market growth (population CAGR) | ~292 |
| 5 | Competitor pricing (biosimilar discount depth) | ~250 |
| 6 | Treatment persistence / adherence | ~229 |
| 7 | Distribution cost / cold-chain loss | ~125 |
| 8 | Access-program expenditure (opportunity cost) | ~83 |

## Interpretation
1. **Market share and price are the two highest-leverage variables** — this is intuitive but important to confirm quantitatively: it means competitive/commercial execution (share) and pricing architecture (price) matter more to the 5-year outcome than any single operational lever, reinforcing why this report's core recommendation is a portfolio/pricing strategy, not primarily an operational-efficiency program.
2. **Patient adoption and overall market growth carry equal, material weight** — both are largely outside Novo Nordisk's direct control (they depend on diagnosis rates, government screening programs, and macro health-system trends), meaning the company's own strategy execution (share, price) is the more controllable lever to focus resources on.
3. **Distribution/cold-chain and access-program spend have the smallest direct revenue sensitivity** in this model — this does NOT mean they are unimportant; rather, their primary value is in *protecting the market-share and adoption-rate assumptions* from eroding (i.e., they are enabling investments for variables 1 and 3 above, not independent revenue drivers in their own right). This nuance is important: cutting cold-chain investment to "protect margin" would likely show up as share and adoption erosion in a lagged, harder-to-attribute way, not as an immediate line-item saving worth its long-run cost.

## Use in Decision-Making
This tornado analysis supports prioritizing management attention and investment on **defensible market share (via differentiation, not just price) and disciplined, segment-aware pricing** as the two highest-leverage strategic levers, while treating supply-chain and access-program investment as necessary enablers rather than the primary source of upside.
