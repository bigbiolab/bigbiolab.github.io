# CHIRAL Data Governance Policy

CHIRAL works with health data. Some of it identifies real people. Mishandling it can harm
participants and end the center's ability to do research. This policy is **center-wide** and
binding on all units — Population Health Studies Division, Geospatial Health Research Group,
and Big Bioinformatics Lab. It complements the Data Management section of the
[Center Guidelines](/shared/center-guidelines.md).

This is a **living document**. Propose changes via pull request.

---

## 1. Data Classification

Classify every dataset before you touch it. The class sets the rules.

| Class | Examples | Handling |
|-------|----------|----------|
| **Public** | Published datasets, open reference data | No restriction. Version-control the download/processing scripts. |
| **Internal** | De-identified study data, intermediate files | CHIRAL members only. Stored in CHIRAL-controlled storage. |
| **Sensitive / Identifiable** | Names, addresses, phone, national ID, GPS of households, dates + location that re-identify, raw clinical/genomic data | Strictest rules below. Access by name, encrypted, never on personal devices unmanaged. |

When in doubt, treat data as **Sensitive**.

---

## 2. Ethics Approval & Consent

- **No data collection or analysis of identifiable human data without ethics/IRB approval.**
  Keep the approval reference with the project.
- Use data **only for the purpose covered by the participant's consent**. Secondary use needs
  a new approval or a documented waiver.
- Data-sharing with external collaborators requires a **data use / transfer agreement** and the
  director's sign-off.

---

## 3. Storage, Access & Backup

- **Sensitive data** lives only in CHIRAL-approved, access-controlled, **encrypted** storage —
  not on personal laptops, personal cloud drives, USB sticks, or personal inboxes
  (consistent with the [Social Media Policy](/shared/social-media-policy.md)).
- Keep at least one **backup in a separate location**. Source data is **read-only** to prevent
  accidental edits (see Center Guidelines → Data Integrity).
- Access is **least-privilege**: people get only the data their task needs. Maintain an access
  list per dataset. Remove access promptly when someone leaves (offboarding).
- Private repositories holding any non-public data must have a **minimum of two members** with
  access, so no dataset has a single point of failure.

---

## 4. De-identification

- Separate **direct identifiers** (name, ID, contact, exact address/GPS) from the analysis
  dataset. Keep the identifier key in separate, restricted storage with its own access list.
- For **geospatial** data, treat precise household/point coordinates as identifiable. Aggregate,
  jitter, or reduce precision before sharing or mapping publicly.
- Never commit identifiable data, identifier keys, or credentials to **Git**. Add them to
  `.gitignore`. If committed by mistake, treat as a breach (Section 6) — rotating/scrubbing,
  not just a new commit, since Git keeps history.

---

## 5. Sharing & Publication

- Deposit only **de-identified, consented** data in public repositories, and only when consent
  and approvals allow. Choose the repository appropriate to the unit (see your unit overlay).
- Every manuscript includes a **Data Availability statement** (see the
  [Publication & Authorship Policy](/shared/publication-authorship-policy.md)).
- Embargoes or sponsor restrictions are flagged to the director before any release.

---

## 6. Breaches

- A suspected breach (lost device, wrong-recipient email, leaked credentials, identifiable data
  pushed to a public repo) is reported to the director **immediately** — same day.
- Do not try to quietly fix and hide it. Honest, fast reporting is the rule; concealment is
  treated as misconduct.

---

## 7. Responsibilities

- **Every member**: knows the class of the data they handle and follows these rules.
- **Project lead**: maintains the access list, the ethics reference, and the identifier-key
  location for their project.
- **Director**: approves external sharing, exceptions, and handles breaches.
