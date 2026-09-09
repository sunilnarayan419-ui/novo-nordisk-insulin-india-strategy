# Assumption Audit

## Audit Scope
Cross-check of every assumption labeled CA (Consulting Assumption) or SA (Scenario Assumption) across the report against `00_PROJECT_CHARTER/assumptions-register.md` and `08_HEALTH_ECONOMICS/health-economic-assumptions.md`, to confirm internal consistency (i.e., the same assumption is not stated differently in two different sections).

## Findings
- Population/market-sizing assumptions (A1, insulin_share_of_treated = 27% midpoint of a 20–30% cited range) are used consistently across `03_MARKET_ANALYSIS/market-sizing.md`, `03_MARKET_ANALYSIS/TAM-SAM-SOM.md`, and the quantitative model (`15_ANALYTICS/python/insulin_india_model.py`).
- Growth-rate assumptions (6–8% base case) are used consistently across `03_MARKET_ANALYSIS/market-growth-scenarios.md` and the model's `pop_cagr=0.07` Base Case input.
- Currency assumption (A8, ~₹83–86/USD, model uses 84.5) is applied consistently wherever USD-equivalent figures are presented.

## No Material Inconsistencies Found
No instance was identified where two sections state materially conflicting versions of the same underlying assumption. Minor numeric rounding differences (e.g., "6–8%" in narrative text vs. "7%" point estimate in the model) are intentional — narrative sections present ranges, the model necessarily uses point estimates within those ranges.

## Recommendation
Any future update to a core assumption (e.g., a revised insulin-share-of-treated estimate) should be updated in `00_PROJECT_CHARTER/assumptions-register.md` first, then propagated to the model script and any narrative section referencing it, to maintain this consistency.
