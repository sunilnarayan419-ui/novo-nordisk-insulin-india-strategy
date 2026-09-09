# Data Dictionary

## Core Population Variables
| Variable | Definition | Source | Value (Y0) |
|---|---|---|---|
| `diagnosed_diabetes_population` | People in India with diagnosed/detected diabetes | ICMR-INDIAB (2023), PIB | ~101,000,000 |
| `treated_share` | Share of diagnosed diabetics on any treatment | NNMS survey data (cited in peer-reviewed literature) | 0.36 |
| `insulin_share_of_treated` | Share of treated diabetics requiring insulin | Consulting assumption (A1) | 0.27 |
| `insulin_treated_population` | Derived: diagnosed × treated_share × insulin_share_of_treated | Model calculation | ~9,817,200 |

## Channel Variables
| Variable | Definition |
|---|---|
| `channel_mix` | Share of insulin-treated population by payer channel (premium private, mainstream private, institutional/govt, rural/low-income) |
| `annual_value_per_patient_inr` | Blended annual insulin spend per patient, by channel, in INR |
| `nn_share_of_channel` | Novo Nordisk's estimated share of insulin-treated patients within each channel |
| `gross_margin_by_channel` | Estimated gross margin %, by channel |

## Pricing Variables
| Variable | Definition | Source |
|---|---|---|
| `nppa_ceiling_human_insulin` | NPPA ceiling price, human insulin (40 IU/ml) | NPPA public notification | ₹15.09/ml |
| `nppa_ceiling_glargine_vial` | NPPA ceiling price, insulin glargine (100 IU/ml), vial/cartridge | NPPA public notification (NLEM 2022, WPI-adjusted 2023) | ₹244.13/ml |

## Model Output Variables
See `../15_ANALYTICS/python/insulin_india_model.py` docstring and `../10_FINANCIAL_MODEL/outputs/model_readme.md` for the full list of computed output fields (`nn_patients`, `revenue_inr_cr`, `revenue_usd_mn`, `gross_margin_inr_cr`, `blended_gross_margin_pct`).

## Data Lineage Note
All variables are either (a) directly sourced from a cited public document, or (b) a labeled consulting/scenario assumption. No variable in this dictionary represents Novo Nordisk-disclosed confidential data (see `../DISCLAIMER.md`).
