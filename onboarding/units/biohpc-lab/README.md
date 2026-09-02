# BioHPC Lab — Unit Overlay

BioHPC Lab is a unit of **CHIRAL, Bangladesh**. This overlay covers only what is **specific to
BioHPC Lab** (high-performance computing for the life sciences). For everything else — code of
conduct, ethics, communication, authorship, data governance, good practices — follow the
center-wide documents:

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

- **Languages:** Python, R, and shell; C/C++ or compiled tools where performance demands it.
- **Job scheduling:** cluster jobs run through the scheduler (e.g., **SLURM**) — no long jobs
  on login/head nodes. Submit scripts are version-controlled with the analysis.
- **Containers:** use **Apptainer/Singularity** (or Docker where allowed) for portable,
  reproducible environments across nodes.
- **Workflows:** workflow managers (e.g., **Nextflow/Snakemake**) so multi-step pipelines
  regenerate end-to-end and scale across nodes.

## Compute Etiquette & Resources

- Request only the cores, memory, GPUs, and walltime a job needs. Document resource needs in
  the project README.
- Store large intermediate files in designated scratch/replicated locations, not in home or in
  Git. Clean up scratch per cluster policy.
- Record the exact environment (modules, container hash, package versions) so runs reproduce.

## Data

- Data on shared compute is still governed by the [Data Governance Policy](/shared/data-governance.md);
  sensitive data stays in approved, access-controlled storage even on the cluster.

> Keep this overlay short. Anything that should apply to all of CHIRAL belongs in the shared
> documents, not here.
