"""
Novo Nordisk India Insulin Strategy — Quantitative Decision Model
==================================================================

Independent, publicly-sourced case-study model (see /DISCLAIMER.md).
All inputs are consulting assumptions / scenario assumptions grounded
in the public data cited in /18_RESEARCH/source-library.md and
/00_PROJECT_CHARTER/assumptions-register.md — this is NOT a
Novo Nordisk-disclosed or India-country-level-audited financial model.

Outputs (written to /10_FINANCIAL_MODEL/outputs/):
  - scenario_summary.csv         (Base / Upside / Downside, 5-year)
  - sensitivity_analysis.csv     (tornado-style, +/-10% on 8 variables)
  - population_buildup.csv       (TAM/SAM/SOM population walk)
  - model_readme.md              (how to reproduce)

Run: python3 insulin_india_model.py
"""

import csv
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "10_FINANCIAL_MODEL", "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

# -----------------------------------------------------------------
# 1. BASE POPULATION INPUTS (Year 0 / current)
# -----------------------------------------------------------------
DIAGNOSED_DIABETES_POP = 101_000_000      # ICMR-INDIAB 2023 (~10.1 crore)
TREATED_SHARE = 0.36                      # NNMS-cited treatment rate among diagnosed
INSULIN_SHARE_OF_TREATED = 0.27           # consulting assumption, mid-point (A1)

INSULIN_TREATED_POP_Y0 = int(DIAGNOSED_DIABETES_POP * TREATED_SHARE * INSULIN_SHARE_OF_TREATED)

# Channel mix (Y0), consulting assumption (patient-segmentation.md)
CHANNEL_MIX_Y0 = {
    "premium_private": 0.125,
    "mainstream_private": 0.375,
    "institutional_govt": 0.225,
    "rural_lowincome": 0.275,
}

# Blended annual value per patient by channel (INR), consulting assumption
ANNUAL_VALUE_PER_PATIENT_INR_Y0 = {
    "premium_private": 14_000,
    "mainstream_private": 6_500,
    "institutional_govt": 1_800,
    "rural_lowincome": 1_200,
}

# Novo Nordisk SAM-share of each channel, Y0 (consulting assumption)
NN_SHARE_OF_CHANNEL_Y0 = {
    "premium_private": 0.32,
    "mainstream_private": 0.18,
    "institutional_govt": 0.10,
    "rural_lowincome": 0.08,
}

# Gross margin by channel (consulting assumption, reflects price control + mix)
GROSS_MARGIN_BY_CHANNEL = {
    "premium_private": 0.78,
    "mainstream_private": 0.55,
    "institutional_govt": 0.22,
    "rural_lowincome": 0.28,
}

INR_PER_USD = 84.5  # illustrative, per assumptions-register A8

YEARS = 5


def run_scenario(name, pop_cagr, value_cagr_by_channel, nn_share_delta_by_channel_5yr,
                  margin_delta_by_channel_5yr):
    """
    Projects population, revenue, and gross margin for one scenario over 5 years.
    nn_share_delta / margin_delta are TOTAL change applied linearly over 5 years.
    """
    rows = []
    total_pop = INSULIN_TREATED_POP_Y0
    channel_pop = {c: total_pop * s for c, s in CHANNEL_MIX_Y0.items()}
    value_per_patient = dict(ANNUAL_VALUE_PER_PATIENT_INR_Y0)
    nn_share = dict(NN_SHARE_OF_CHANNEL_Y0)
    margin = dict(GROSS_MARGIN_BY_CHANNEL)

    for year in range(0, YEARS + 1):
        year_total_revenue_inr = 0.0
        year_total_gm_inr = 0.0
        year_total_nn_patients = 0

        for c in CHANNEL_MIX_Y0:
            pop_c = channel_pop[c] * ((1 + pop_cagr) ** year)
            vpp_c = value_per_patient[c] * ((1 + value_cagr_by_channel[c]) ** year)
            share_c = nn_share[c] + nn_share_delta_by_channel_5yr[c] * (year / YEARS)
            margin_c = margin[c] + margin_delta_by_channel_5yr[c] * (year / YEARS)

            nn_patients_c = pop_c * share_c
            revenue_c = nn_patients_c * vpp_c
            gm_c = revenue_c * margin_c

            year_total_revenue_inr += revenue_c
            year_total_gm_inr += gm_c
            year_total_nn_patients += nn_patients_c

        rows.append({
            "scenario": name,
            "year": year,
            "nn_patients": round(year_total_nn_patients),
            "revenue_inr_cr": round(year_total_revenue_inr / 1e7, 1),   # INR crore
            "revenue_usd_mn": round(year_total_revenue_inr / INR_PER_USD / 1e6, 1),
            "gross_margin_inr_cr": round(year_total_gm_inr / 1e7, 1),
            "blended_gross_margin_pct": round(100 * year_total_gm_inr / year_total_revenue_inr, 1),
        })
    return rows


# -----------------------------------------------------------------
# 2. SCENARIO DEFINITIONS
# -----------------------------------------------------------------

# BASE CASE
base_rows = run_scenario(
    "Base",
    pop_cagr=0.07,
    value_cagr_by_channel={"premium_private": 0.03, "mainstream_private": 0.05,
                            "institutional_govt": 0.01, "rural_lowincome": 0.02},
    nn_share_delta_by_channel_5yr={"premium_private": 0.03, "mainstream_private": 0.05,
                                    "institutional_govt": 0.01, "rural_lowincome": 0.03},
    margin_delta_by_channel_5yr={"premium_private": -0.02, "mainstream_private": 0.00,
                                  "institutional_govt": 0.00, "rural_lowincome": 0.01},
)

# UPSIDE CASE
upside_rows = run_scenario(
    "Upside",
    pop_cagr=0.095,
    value_cagr_by_channel={"premium_private": 0.04, "mainstream_private": 0.07,
                            "institutional_govt": 0.02, "rural_lowincome": 0.035},
    nn_share_delta_by_channel_5yr={"premium_private": 0.05, "mainstream_private": 0.09,
                                    "institutional_govt": 0.02, "rural_lowincome": 0.05},
    margin_delta_by_channel_5yr={"premium_private": 0.00, "mainstream_private": 0.02,
                                  "institutional_govt": 0.01, "rural_lowincome": 0.02},
)

# DOWNSIDE CASE
downside_rows = run_scenario(
    "Downside",
    pop_cagr=0.045,
    value_cagr_by_channel={"premium_private": 0.00, "mainstream_private": 0.01,
                            "institutional_govt": -0.02, "rural_lowincome": 0.00},
    nn_share_delta_by_channel_5yr={"premium_private": -0.02, "mainstream_private": 0.00,
                                    "institutional_govt": -0.02, "rural_lowincome": 0.00},
    margin_delta_by_channel_5yr={"premium_private": -0.08, "mainstream_private": -0.05,
                                  "institutional_govt": -0.03, "rural_lowincome": -0.02},
)

all_rows = base_rows + upside_rows + downside_rows

with open(os.path.join(OUT_DIR, "scenario_summary.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
    writer.writeheader()
    writer.writerows(all_rows)

# -----------------------------------------------------------------
# 3. POPULATION BUILDUP TABLE (TAM/SAM/SOM walk, Year 0)
# -----------------------------------------------------------------
pop_rows = [
    {"layer": "Diagnosed diabetes population (ICMR-INDIAB 2023)", "population": DIAGNOSED_DIABETES_POP},
    {"layer": "Treated population (36% treatment rate)", "population": int(DIAGNOSED_DIABETES_POP * TREATED_SHARE)},
    {"layer": "Insulin-treated population / TAM (27% of treated)", "population": INSULIN_TREATED_POP_Y0},
    {"layer": "SAM (60% of TAM, NN-reachable channels)", "population": int(INSULIN_TREATED_POP_Y0 * 0.60)},
    {"layer": "SOM Year 0 (NN current patients, blended share)",
     "population": int(sum(INSULIN_TREATED_POP_Y0 * CHANNEL_MIX_Y0[c] * NN_SHARE_OF_CHANNEL_Y0[c] for c in CHANNEL_MIX_Y0))},
]
with open(os.path.join(OUT_DIR, "population_buildup.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["layer", "population"])
    writer.writeheader()
    writer.writerows(pop_rows)

# -----------------------------------------------------------------
# 4. SENSITIVITY ANALYSIS (tornado, +/-10% relative shift on Year 5 Base revenue)
# -----------------------------------------------------------------
base_y5 = [r for r in base_rows if r["year"] == YEARS][0]
base_y5_revenue = base_y5["revenue_inr_cr"]

sensitivity_variables = [
    "Insulin price (blended)",
    "Novo Nordisk market share",
    "Patient adoption / initiation rate",
    "Treatment persistence / adherence",
    "Competitor pricing (biosimilar discount depth)",
    "Distribution cost / cold-chain loss",
    "Access-program expenditure (opportunity cost)",
    "Overall market growth (population CAGR)",
]

# Illustrative sensitivity: approximate revenue elasticity per variable (consulting assumption)
# expressed as % change in Year-5 revenue per 10% adverse/favorable shift in the variable
elasticity_pct = {
    "Insulin price (blended)": 9.5,
    "Novo Nordisk market share": 10.0,
    "Patient adoption / initiation rate": 7.0,
    "Treatment persistence / adherence": 5.5,
    "Competitor pricing (biosimilar discount depth)": 6.0,
    "Distribution cost / cold-chain loss": 3.0,
    "Access-program expenditure (opportunity cost)": 2.0,
    "Overall market growth (population CAGR)": 7.0,
}

sens_rows = []
for var in sensitivity_variables:
    delta = elasticity_pct[var]
    low = round(base_y5_revenue * (1 - delta / 100), 1)
    high = round(base_y5_revenue * (1 + delta / 100), 1)
    sens_rows.append({
        "variable": var,
        "base_year5_revenue_inr_cr": base_y5_revenue,
        "low_case_inr_cr (-10% shift)": low,
        "high_case_inr_cr (+10% shift)": high,
        "revenue_swing_inr_cr": round(high - low, 1),
    })

# sort by swing descending for tornado order
sens_rows.sort(key=lambda r: r["revenue_swing_inr_cr"], reverse=True)

with open(os.path.join(OUT_DIR, "sensitivity_analysis.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(sens_rows[0].keys()))
    writer.writeheader()
    writer.writerows(sens_rows)

# -----------------------------------------------------------------
# 5. WRITE MODEL README
# -----------------------------------------------------------------
readme = f"""# Model Outputs — Reproducibility Note

Generated by `15_ANALYTICS/python/insulin_india_model.py`.

## Files
- `scenario_summary.csv` — Base/Upside/Downside projections, Year 0–5, covering NN India insulin
  patient count, revenue (INR crore and USD million), gross margin, and blended margin %.
- `population_buildup.csv` — TAM/SAM/SOM population walk from ICMR-INDIAB diagnosed population
  down to Novo Nordisk's current estimated served population.
- `sensitivity_analysis.csv` — Tornado-style sensitivity of Year-5 Base Case revenue to +/-10%
  shifts in each of the 8 variables specified in the problem statement.

## Headline Results (Year 5, INR crore)
- Base Case revenue: {[r for r in base_rows if r['year']==5][0]['revenue_inr_cr']} cr (~US$ {[r for r in base_rows if r['year']==5][0]['revenue_usd_mn']}M)
- Upside Case revenue: {[r for r in upside_rows if r['year']==5][0]['revenue_inr_cr']} cr (~US$ {[r for r in upside_rows if r['year']==5][0]['revenue_usd_mn']}M)
- Downside Case revenue: {[r for r in downside_rows if r['year']==5][0]['revenue_inr_cr']} cr (~US$ {[r for r in downside_rows if r['year']==5][0]['revenue_usd_mn']}M)

## Important Caveats
1. All inputs are consulting/scenario assumptions triangulated from public sources
   (see /00_PROJECT_CHARTER/assumptions-register.md and /18_RESEARCH/source-library.md).
   Novo Nordisk does not publicly disclose India-country-level insulin revenue, share, or
   margin at this granularity, so this model should be read as illustrative of *strategic
   direction and relative magnitude*, not as an audited or company-validated forecast.
2. Re-running the script with updated assumptions (e.g., a newer NPPA price notification,
   an updated ICMR-INDIAB figure) is the intended way to refresh this model — edit the
   constants at the top of the script rather than hand-editing the CSV outputs.
3. Currency conversion uses a fixed illustrative rate ({INR_PER_USD} INR/USD); no exchange-rate
   forecasting is attempted.
"""
with open(os.path.join(OUT_DIR, "model_readme.md"), "w") as f:
    f.write(readme)

print("Model run complete. Outputs written to:", OUT_DIR)
for r in base_rows:
    print(r)
