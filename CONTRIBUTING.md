# Contributing

This is an independent, single-author case-study project (see `DISCLAIMER.md`). It is not an open-collaboration repository, but the structure and methodology are intentionally documented so that:

1. The analytical approach can be **reviewed and critiqued** — every claim is labeled by evidentiary status (`00_PROJECT_CHARTER/problem-statement.md`), and a full quality-control audit trail is provided in `19_QUALITY_CONTROL/`.
2. The quantitative model can be **reproduced and extended** — `15_ANALYTICS/python/insulin_india_model.py` is a standard-library-only Python script; update the assumption constants at the top of the file and re-run to test alternative scenarios.
3. The structure can be **reused as a template** for similar life-sciences/biotech market-strategy case studies.

## If You Spot an Error
Given this is a static case-study repository, there is no formal issue tracker — but if you're reviewing this as part of an application/interview process, feedback is very welcome directly.

## Updating for Currency
The two most time-sensitive inputs are (a) NPPA/DPCO ceiling prices (revised annually via WPI indexation) and (b) ICMR-INDIAB / IDF prevalence figures (updated periodically). If reusing this repository's framework, re-verify both before drawing conclusions from the numbers.
