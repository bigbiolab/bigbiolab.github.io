# Population Health Studies Division — Unit Overlay

This division is a unit of **CHIRAL, Bangladesh**. This overlay covers only what is **specific
to the Population Health Studies Division**. For everything else — code of conduct, ethics,
communication, authorship, data governance, good practices — follow the center-wide documents:

- [Center Guidelines](/shared/center-guidelines.md)
- [Publication & Authorship Policy](/shared/publication-authorship-policy.md)
- [Data Governance Policy](/shared/data-governance.md)
- [Social Media Policy](/shared/social-media-policy.md)
- [Good Practices](/shared/good-practices.md)
- [GitHub Basics](/shared/github-basics.md)

Where this overlay is silent, the center documents apply. Where it conflicts, the center
documents win unless the director approves an exception.

---

## Entry Requirement

Recruitment requires successful completion of the **The Academic Research Workflow** course at
DeepBio Academy, followed by interview and selection — see the
[Recruitment Policy](/shared/recruitment-policy.md).

## Tech Stack

- **Languages:** R (tidyverse, survey, epitools) and/or Python (pandas, statsmodels, lifelines).
  Reproducible environments as in the center good practices.
- **Analysis:** all statistics done in scripts, not spreadsheets. Exporting to Prism/Jamovi is
  acceptable but not preferred; the script remains the source of truth.

## Study Data & Ethics

- Survey and clinical study data are typically **Sensitive / Identifiable** — handle per the
  [Data Governance Policy](/shared/data-governance.md).
- **Ethics/IRB approval and participant consent are prerequisites** for collection and analysis.
  Keep the approval reference and the study protocol with the project.
- Separate direct identifiers from the analysis dataset; keep the identifier key in restricted
  storage.

## Reporting

- Follow the relevant reporting guideline for the study design (e.g., STROBE for observational
  studies, CONSORT for trials) when writing up.

> Keep this overlay short. Anything that should apply to all of CHIRAL belongs in the shared
> documents, not here.
