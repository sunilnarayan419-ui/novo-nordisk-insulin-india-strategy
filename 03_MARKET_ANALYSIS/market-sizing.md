# Market Sizing

## Step 1 — Diagnosed Diabetes Population (FACT)
ICMR-INDIAB (2023): ~101 million (10.1 crore) people with diagnosed/detected diabetes in India; ~136 million with prediabetes (future conversion pool).

## Step 2 — Treated Population (DBI)
Public-health literature (NNMS survey data) indicates roughly 36% of people with diabetes are on any treatment, implying an actively-treated base of **~36 million**. This is the pool from which insulin-requiring patients are drawn (plus a smaller number of undiagnosed patients who present acutely and are insulin-initiated directly, e.g., via hospitalization).

## Step 3 — Insulin-Requiring Share (CA — Assumption A1)
Type 1 diabetes: assume ~3–4 million people in India are living with Type 1 diabetes (order-of-magnitude estimate consistent with India's ~90–95% Type 2 share of the ~101M diabetes population), all insulin-dependent.

Type 2 insulin-requiring share: clinical literature typically estimates that a meaningful minority of treated Type 2 patients — commonly cited ranges across LMIC contexts are roughly 20–30% of treated Type 2 patients — require insulin either as intensification or combination therapy. Applying a **25% mid-point** to the ~35 million treated Type 2 base yields **~8.5–9 million** Type 2 insulin-treated patients.

**Total current insulin-treated population estimate: ~12–13 million people** (Type 1 + Type 2 insulin-requiring), acknowledged as a triangulated order-of-magnitude estimate, not an official government statistic (no single public source publishes this figure directly for India).

## Step 4 — TAM / SAM / SOM
See `TAM-SAM-SOM.md` for the formal breakdown and the associated revenue sizing.

## Step 5 — Cross-Check
This estimate is broadly consistent with global market-share literature (IQVIA Institute) showing India as one of the largest LMIC insulin volume markets, and with the observation that India's insulin market, while large in patient count, skews toward lower average revenue per patient than high-income markets due to price control and human-insulin/biosimilar mix.

## Key Sensitivity
The single largest driver of uncertainty is the **insulin-initiation rate among treated Type 2 patients** — small changes in this assumption (20% vs. 30%) swing the addressable population by several million patients. This is explicitly tested in `10_FINANCIAL_MODEL/sensitivity-analysis/`.
