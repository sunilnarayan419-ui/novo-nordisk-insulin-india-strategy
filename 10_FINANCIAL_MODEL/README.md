# Financial Model — Overview

## Purpose
Quantitative decision model estimating Novo Nordisk's addressable population, revenue, and gross margin in the India insulin market over a 5-year horizon, under three scenarios, with sensitivity analysis on the eight variables specified in `00_PROJECT_CHARTER/problem-statement.md`.

## Structure
- `raw-data/` — key public inputs used (ICMR-INDIAB prevalence figure, NPPA/DPCO price notifications) — see `../18_RESEARCH/source-library.md` for full citations
- `assumptions/` — see `../00_PROJECT_CHARTER/assumptions-register.md` and `../08_HEALTH_ECONOMICS/health-economic-assumptions.md` (assumptions are centralized there rather than duplicated)
- `calculations/` — model logic lives in `../15_ANALYTICS/python/insulin_india_model.py` (Python, no external dependencies beyond the standard library)
- `outputs/` — generated CSVs: `scenario_summary.csv`, `population_buildup.csv`, `sensitivity_analysis.csv`, and `model_readme.md`
- `scenarios/` — narrative scenario descriptions in this folder (`scenario-assumptions.md`)
- `sensitivity-analysis/` — narrative sensitivity discussion in this folder (`sensitivity-summary.md`)

## How to Reproduce
```
python3 15_ANALYTICS/python/insulin_india_model.py
```
This regenerates all files in `10_FINANCIAL_MODEL/outputs/` from the assumptions hard-coded at the top of the script. To test a different assumption, edit the relevant constant (e.g., `INSULIN_SHARE_OF_TREATED`, `NN_SHARE_OF_CHANNEL_Y0`) and re-run.

## Headline Results (Year 5)

| Scenario | NN Patients (Y5) | Revenue (₹ crore) | Revenue (US$M) | Blended Gross Margin % |
|---|---|---|---|---|
| Base | ~2.55M | ~2,083 | ~247 | ~63.1% |
| Upside | ~3.25M | ~2,806 | ~332 | ~64.3% |
| Downside | ~1.77M | ~1,275 | ~151 | ~58.6% |

*See `outputs/scenario_summary.csv` for full year-by-year detail and `../DISCLAIMER.md` for the evidentiary status of these figures — they are triangulated, publicly-sourced estimates for case-study purposes, not Novo Nordisk-disclosed or audited figures.*

## Key Insight from the Model
Even in the Downside Case — which assumes tighter price control extending to more analogue SKUs and continued biosimilar share erosion — **patient volume still grows** (from ~1.49M to ~1.77M), because underlying diabetes/insulin-treated population growth is structurally positive. What varies sharply across scenarios is **revenue and margin**, confirming this report's central strategic finding: the primary business risk is margin compression, not market disappearance, which argues for a portfolio and pricing strategy built for margin resilience rather than volume defense alone.
