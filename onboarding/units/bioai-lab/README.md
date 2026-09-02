# BioAI Lab — Unit Overlay

BioAI Lab is a unit of **CHIRAL, Bangladesh**. This overlay covers only what is **specific to
BioAI Lab** (machine learning and AI for the life sciences). For everything else — code of
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

Recruitment requires successful completion of the **No Code and Agentic AI for Life Sciences**
course at DeepBio Academy, followed by interview and selection — see the
[Recruitment Policy](/shared/recruitment-policy.md).

## Tech Stack

- **Languages:** Python primarily. Frameworks: PyTorch (default), plus the scientific ML stack
  (scikit-learn, etc.).
- **Environments:** pinned environments (`conda`/`uv` + lockfile) and, where used, GPU/CUDA
  versions recorded so training reproduces.
- **Compute:** GPU jobs that run on shared HPC follow the [BioHPC Lab](/units/biohpc-lab/README.md)
  scheduler and container rules.

## Reproducible ML

- **Set and record random seeds.** Version-control training/eval code and configs.
- **Track experiments** (e.g., runs, hyperparameters, metrics) and record the exact dataset
  split used. A result that cannot be reproduced from code + config + seed is not a result.
- **Version datasets and model artifacts** — do not commit large weights/data to Git; store in
  designated artifact storage and reference by version/hash.

## Responsible AI & Data

- Training data is governed by the [Data Governance Policy](/shared/data-governance.md); do not
  train on identifiable data without approval and consent coverage.
- Document model **intended use, limitations, and known biases** (a short model card) before any
  model informs decisions or is published.

> Keep this overlay short. Anything that should apply to all of CHIRAL belongs in the shared
> documents, not here.
