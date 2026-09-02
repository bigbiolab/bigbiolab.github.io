# Geospatial Health Research Group — Unit Overlay

This group is a unit of **CHIRAL, Bangladesh**. This overlay covers only what is **specific to
the Geospatial Health Research Group**. For everything else — code of conduct, ethics,
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

- **Languages:** Python (GeoPandas, rasterio, shapely) and/or R (sf, terra). Reproducible
  environments as in the center good practices.
- **GIS tools:** QGIS for interactive work; scripted analysis preferred over manual GIS edits
  (no untracked GUI edits — same rule as the center's "never edit via GUI").
- **Coordinate systems:** record the CRS/projection for every dataset; never assume.

## Spatial Data Privacy

- **Precise coordinates (household/point GPS) are identifiable data** — treat as **Sensitive**
  under the [Data Governance Policy](/shared/data-governance.md).
- Aggregate, jitter, or reduce precision before mapping or sharing publicly. Do not publish
  maps that can re-identify individuals or households.

## Data Repositories

- Deposit de-identified spatial datasets in an appropriate archive once consent and policy
  allow. Preserve acquisition/processing scripts under version control.

> Keep this overlay short. Anything that should apply to all of CHIRAL belongs in the shared
> documents, not here.
