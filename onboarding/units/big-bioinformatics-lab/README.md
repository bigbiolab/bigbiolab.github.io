# Big Bioinformatics Lab (BBL) — Unit Overlay

BBL is a unit of **CHIRAL, Bangladesh**. This overlay covers only what is **specific to BBL**.
For everything else — code of conduct, ethics, communication, authorship, data governance,
good practices — follow the center-wide documents:

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

Recruitment requires successful completion of the **Bioinformatics Mentorship** course at
DeepBio Academy, followed by interview and selection — see the
[Recruitment Policy](/shared/recruitment-policy.md).

## Tech Stack

- **Languages:** Python and R. All members are expected to be proficient in both.
- **Environments:** `renv` for R projects; a pinned Python environment (`conda`/`uv` +
  `environment.yml` or `requirements.txt`) for Python projects. Every analysis is reproducible
  from a clean environment.
- **Workflows:** Makefiles / shell scripts / workflow managers (e.g., Snakemake/Nextflow) so
  analyses regenerate end-to-end.

## Data Repositories

- Deposit generated data in the appropriate public archive once consent and policy allow —
  e.g., **GEO** for gene expression, **SRA** for raw sequencing. Preserve download/processing
  scripts under version control.
- Sequencing/clinical raw data is **Sensitive** — handle per the
  [Data Governance Policy](/shared/data-governance.md).

## Compute

- Document where each job runs (local / HPC / cloud) in the project README, including resource
  needs and where large intermediate files live.

> Keep this overlay short. Anything that should apply to all of CHIRAL belongs in the shared
> documents, not here.
