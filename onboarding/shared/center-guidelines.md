Table of Contents
---
- [Mission Statement](#mission-statement)
  - [Expectations](#expectations)
- [Appointment, Commitment & Affiliation](#appointment-commitment--affiliation)
  - [Nature of the Position](#nature-of-the-position)
  - [Roles & Reporting Structure](#roles--reporting-structure)
  - [Minimum Commitment](#minimum-commitment)
  - [Mandatory Affiliation & Promotion](#mandatory-affiliation--promotion)
  - [Exclusivity & Outside Commitments](#exclusivity--outside-commitments)
  - [Consequences of Non-Compliance](#consequences-of-non-compliance)
- [Communication](#communication)
  - [General](#general)
    - [Meetings](#meetings)
      - [Scrum](#scrum)
    - [Research Meeting](#research-meeting)
  - [Meeting Agenda](#meeting-agenda)
    - [Meeting Formats](#meeting-formats)
      - [Format 1: Braintrust](#format-1-braintrust)
      - [Format 2: Tech Talk/Discussion](#format-2-tech-talkdiscussion)
      - [Format 3: Post-Conference Presentations](#format-3-post-conference-presentations)
      - [Format 4: Big Ideas or Projects](#format-4-big-ideas-or-projects)
      - [Format 5: Journal Club](#format-5-journal-club)
      - [Format 6: Preprint Review](#format-6-preprint-review)
  - [Meeting Lead](#meeting-lead)
  - [Ad-Hoc Meetings](#ad-hoc-meetings)
- [Source Code, Data, and Reproducibility](#source-code-data-and-reproducibility)
  - [Pride](#pride)
  - [Programming Languages](#programming-languages)
  - [Licensing](#licensing)
  - [Version Control and GitHub Usage](#version-control-and-github-usage)
    - [Creating a CHIRAL Repository](#creating-a-chiral-repository)
    - [Code Review Process](#code-review-process)
    - [Handling Projects That Didn't Work](#handling-projects-that-didnt-work)
  - [Non-Code Versioning](#non-code-versioning)
  - [Data Management](#data-management)
  - [Reproducibility](#reproducibility)
  - [How to Modify this Document](#how-to-modify-this-document)

# Mission Statement

The **Center for Health Innovation, Research, Action, and Learning (CHIRAL), Bangladesh** is a research and training center that addresses critical public health challenges through data-driven science and capacity building.

These guidelines are **center-wide** and apply to every member of CHIRAL across all of its units:

- **Population Health Studies Division**
- **Geospatial Health Research Group**
- **Big Bioinformatics Lab (BBL)**
- **BioHPC Lab**
- **BioAI Lab**

Each unit maintains a short **overlay** document for matters specific to it (tech stack, data types, tools). Where an overlay conflicts with these center guidelines, the center guidelines take precedence unless an exception is approved by the director. Find your unit overlay under [`/units`](/units).

## Expectations
**Your role:** We expect that you will take primary responsibility for the success of your research project and career development. As a member of CHIRAL, you are expected to participate fully in the team. In general, members are expected to follow working hours that include 4 hours/day to facilitate discussion within the group. 

**Mentor Role:** Mentors role is to facilitate your success as well as that of your project. Within your project, mentors will serve as a sounding board for ideas, will help you plan your project, and will help to devise experiments to test your hypotheses. To facilitate your success, mentors will help you to plan your training, to devise a career plan that can take you to where you want to go, to advise you on your project-risk portfolio, and to provide guidance on other elements of career and project development as needed.

**Deadlines:** Our team is working hard to develop a reputation for high-quality science that is well presented. We all benefit from this reputation, but we must also work to maintain it. Abstracts for meetings must be shared with all co-authors, including mentors, at least one week prior to the deadline for submission. Failure to abide by this guideline will result in missing whatever the opportunity in question is.

Trainees in the CHIRAL will often receive opportunities to present their work at scientific conferences. These presentations reflect on the entire team. Oral presentations on projects must be presented to the research team during a braintrust meeting, and CHIRAL members are expected to address feedback that is provided. Once a project has been presented once and feedback incorporated, additional presentations are optional in advance of meetings. Poster presentations should be shared in the `#general` Zulip channel at least a week before printing.

**Code of Conduct:** At CHIRAL Bangladesh, we are committed to maintaining a safe, respectful, and harassment-free environment for all members and visitors. Discrimination or harassment based on gender, gender identity, age, disability, appearance, body size, race, religion, or any other personal characteristic will not be tolerated. This includes offensive comments, inappropriate images, intimidation, stalking, disruption, unwanted physical contact, and sexual advances. All members are expected to adhere to these guidelines, and any harassing behavior must cease immediately when asked. Please refer to the full Code of Conduct for more detailed information on our expectations. We prioritize cooperation to ensure a professional and inclusive atmosphere for everyone.

**Authorship:** Our team follows the [ICMJE's Uniform Requirements for Manuscripts Submitted to Biomedical Journals](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html) defintions of the roles of authors and contributors to our manuscripts.

**Ethics:** We expect CHIRAL members to be honest in scientific communications both within and outside the team. We expect that CHIRAL members will design experiments/study in a manner that minimizes both bias and self deception. We expect that CHIRAL members will keep agreements, be careful, and share their code and results openly with the scientific community. We expect that credit will be given where credit is due, including in scientific writing. Plagiarism is not tolerated. While a full enumeration of ethical considerations is outside of the scope of this document, CHIRAL provides a [document](https://github.com/CHIRAL/onboarding/blob/main/CHIRAL%20Code%20of%20Conduct.pdf) that we recommend.

In addition, please don't hesitate to raise any questions or concerns that you have at any point with the director.


# Appointment, Commitment & Affiliation

CHIRAL invests heavily in every member — mentorship, training, infrastructure, and the
opportunity to earn authorship on real research. In return, the center expects genuine
commitment and ownership. This section sets out the nature of the position and the
non-negotiable expectations that come with it. These rules are strict by design.

## Nature of the Position

- All positions at CHIRAL — including **Research Assistant** and **Group Leader** — are
  **voluntary and unpaid**. Membership is a research and training opportunity, **not
  employment**. No salary, stipend, or financial benefit is offered or implied.
- In exchange for your time, CHIRAL provides mentorship, training, access to infrastructure,
  co-authorship on work you contribute to (per the
  [Publication & Authorship Policy](/shared/publication-authorship-policy.md)), and — on
  satisfactory completion — a recommendation/experience letter.
- Because the position is unpaid, the center's accountability tools are limited to what it
  controls: **authorship, recommendation/experience letters, continued membership, and your
  CHIRAL affiliation.** These are earned, and they can be withheld or withdrawn.

## Roles & Reporting Structure

CHIRAL has a clear chain of responsibility. Every member knows whom they report to and what is
expected of their role.

```
Head of Organization (Director)
        │
   Group Leader        ← leads a unit/group; reports to the Director
        │
 Research Assistant    ← reports to their Group Leader
```

### Head of Organization (Director)
- Sets the center's overall direction, priorities, and standards.
- Final authority on disputes, exceptions, authorship escalations, external sharing, and removals.
- Approves outside-commitment requests and recommendation/experience letters.
- Group Leaders report to the Director.

### Group Leader
Reports to the **Director**. Leads a unit or research group.
- **Project leadership:** plans the group's projects, sets internal deadlines, and owns
  delivery and quality for the group's work.
- **Mentorship:** guides and supervises Research Assistants; supports their training and career
  development.
- **Code & research review:** ensures code review, reproducibility, and lab-book practices are
  followed in the group; reviews/approves pull requests.
- **Authorship & CRediT:** maintains the [CRediT table](/shared/publication-authorship-policy.md#5-contributor-roles-credit)
  for the group's papers and proposes author order with the Director.
- **Accountability:** logs participation lapses for their group and applies the
  [accountability ladder](/shared/publication-authorship-policy.md#11-accountability--penalty-ladder),
  escalating to the Director as needed.
- **Onboarding:** ensures new RAs complete onboarding, sign the agreement, and meet the
  affiliation/disclosure requirements.

### Research Assistant (RA)
Reports to their **Group Leader**.
- **Research:** carries out assigned analyses and project work to the standards in these
  guidelines and the [Good Practices](/shared/good-practices.md).
- **Reproducibility & records:** writes reproducible, reviewed code; keeps a lab book; manages
  data per the [Data Governance Policy](/shared/data-governance.md).
- **Participation:** attends lab meetings, communicates on time, and contributes to manuscript
  **revisions** per the [Publication & Authorship Policy](/shared/publication-authorship-policy.md).
- **Escalation:** raises blockers, concerns, and ideas with the Group Leader; may go to the
  Director if a concern involves the Group Leader.

> Reporting lines define accountability, not permission to bypass anyone — concerns about
> conduct or safety can always go directly to the Director.

## Minimum Commitment

- By accepting a position you commit to a **minimum active term of 18 months (1.5 years)**;
  the **standard expected commitment is 2 years**.
- "Active" means meaningfully contributing and meeting the participation and communication
  expectations in the [Publication & Authorship Policy](/shared/publication-authorship-policy.md)
  (attendance, timely communication, revision contribution).
- **Authorship is contingent on honoring this commitment.** A member who leaves, or goes
  inactive without the director's agreement, **before completing the committed term** forfeits
  authorship on any work that does not yet independently meet all four
  [ICMJE criteria](/shared/publication-authorship-policy.md#21-icmje-criteria) at the time of
  departure. Such contributions are moved to the Acknowledgments.
- Genuine, communicated reasons for early departure (illness, relocation, family, a paid job)
  are handled case by case with the director. Silent disappearance is not.

## Mandatory Affiliation & Promotion

Public ownership of your CHIRAL affiliation is **mandatory**, not optional:

- **List your affiliation** on your **LinkedIn** and **Facebook** profiles in the form
  *"[Position], [Unit], CHIRAL, Bangladesh."* A member who does not have one of these accounts
  must either create a professional profile or obtain a written exception from the director —
  not having an account is not an automatic exemption.
- **Follow and promote CHIRAL:** follow/like the center's official pages and **share the
  center's training and research activities** (events, posts, preprints, publications) on your
  profiles.
- Comply **within 2 weeks of joining** and keep it current for as long as you are a member.
- When an employer or collaborator requires it, add the personal-opinions disclaimer described
  in the [Social Media Policy](/shared/social-media-policy.md).

## Exclusivity & Outside Commitments

CHIRAL members are expected to devote their research effort to CHIRAL and to avoid divided
loyalty, conflicts of interest, and leakage of CHIRAL data or ideas to other groups.

- **No concurrent membership in another research organization, lab, or group** while a CHIRAL
  member, **except** with the **director's prior written approval**.
- **Disclosure is mandatory.** Every member must disclose, in writing, all outside affiliations
  and commitments — at onboarding, and within **7 days** of taking on any new one.
- **Academic thesis exemption.** Research conducted for your **own degree (thesis/dissertation)**
  at your university is **allowed and exempt** from the approval requirement — but it **must
  still be disclosed**, and CHIRAL data/work may not be used in it without agreement and proper
  attribution.
- **Within the ecosystem is fine.** Holding a role at DeepBio Limited or DeepBio Academy is not
  an "outside organization" — but disclose it so authorship and IP stay clear (see
  [ECOSYSTEM.md](/ECOSYSTEM.md)).
- **Failure to report an outside commitment is itself a punishable violation**, independent of
  whether the commitment would have been approved. Concealment is treated as a breach of the
  ethics expectations and, where CHIRAL data or work is involved, as misconduct under the
  [Publication & Authorship Policy](/shared/publication-authorship-policy.md#14-misconduct).

Because positions are unpaid, this is **not** a non-compete and does not bar a member from paid
employment needed to earn a living — it is a **disclosure-and-approval** rule to protect against
conflicts of interest and divided commitment. A member whose outside commitment is incompatible
with the CHIRAL minimum-commitment expectation may be asked to choose.

## Consequences of Non-Compliance

Failure to maintain the mandatory affiliation/promotion, or leaving before the committed term,
is treated as a participation lapse and follows the **accountability ladder** in the
[Publication & Authorship Policy](/shared/publication-authorship-policy.md#11-accountability--penalty-ladder).
Because the position is unpaid, consequences draw on the levers the center controls:

| Situation | Consequence |
|-----------|-------------|
| Affiliation/promotion not in place within 2 weeks, or removed while a member | Logged reminder → written warning → escalation per the accountability ladder. |
| Repeated or willful refusal | Authorship review; recommendation/experience letter withheld; removal from the organization. |
| Departure before the committed term without agreement | Forfeiture of authorship on work not yet meeting ICMJE criteria; no recommendation/experience letter; CHIRAL affiliation rights revoked; recorded as withdrawn. |
| Undisclosed outside organization / commitment, or joining another research group without approval | Written warning and required disclosure → escalation per the accountability ladder; if CHIRAL data or work was shared, treated as misconduct and may result in removal and revoked affiliation. |
| Claiming CHIRAL credit or work as one's own after leaving, or other ingratitude that misrepresents contribution | Treated as misconduct under the [Publication & Authorship Policy](/shared/publication-authorship-policy.md#14-misconduct). |

These terms are acknowledged in writing as part of onboarding (see the onboarding agreement).


# Communication
## General
**Zulip:** CHIRAL Bangladesh operates remotely and uses Zulip for internal communication. Members should prioritize Zulip messages over emails for faster response times. If an email is necessary, please ensure it is also acknowledged in Zulip. All members should join the following channels: `#general`, `#meeting`, and `#random`. 

**Social Media:** CHIRAL members are encouraged to share research and updates via public social media. If a member associates their profile with CHIRAL Bangladesh, they must adhere to the CHIRAL’s code of conduct. If required by an employer or collaborator, members should include a disclaimer stating that opinions are personal and do not represent CHIRAL Bangladesh. Please read [Social Media Policies for CHIRAL Bangladesh](/shared/social-media-policy.md). 

**IP/Openness:** Intellectual property and openness policies align with CHIRAL’s agreements with funding sponsors and institutional policies. Any concerns should be discussed with the director.

**Accounts:** CHIRAL members must create and maintain accounts for:
- GitHub (organization)
- Zulip (organization)

### Meetings
#### Scrum
Our team's scrum process involves three components:
1. A weekly kick-off meeting at `8:30 AM` `Friday` morning where individuals will lay out their goals for the week on Zoom.
2. A demo day meeting at `8:30 AM` `Saturday` afternoon where team members show off an accomplishment from the week in 3 minutes or fewer. This could be a new figure, section of a paper, some code that they are particularly happy with, or something that we learned from a paper, poster, or research presentation.
3. A daily virtual scrum update on Zulip.

We use Google Slides to share figures or paper sections for the demo day meeting; the link is pinned in the `#meeting `channel on Zulip and is not intended to be shared outside the lab. 

### Research Meeting 

Research meetings are scheduled for one hour on the third Friday of the month. All members of CHIRAL Bangladesh are expected to attend. Meetings are designed to provide a supportive environment for learning, constructive criticism, help, and scientific discussions.

## Meeting Agenda
The format of each meeting will be chosen by the meeting lead from the options below. The lead will rotate among members (see below) within the group. Guests with aligned research interests may join with a supermajority vote of lab members (>2/3) and are expected to attend and participate fully.

The lead will choose the format for each meeting. The different options for meeting formats are outlined below. Each member is expected to lead at least four Braintrust meetings per year (2 every 6 months).

### Meeting Formats
#### Format 1: Braintrust
The meeting lead presents their own research/project to the group. Presenters often focus on open questions or challenges in their work. Occasionally, they present a new talk or set of slides that they intend to deliver at a meeting, job talk, etc. This format helps the group become familiar with each other’s work and allows for feedback, advice, or help with research if needed.

#### Format 2: Tech Talk/Discussion
Talks on commonly used technology in the team, strategies for staying on top of the literature, organization, etc.

#### Format 3: Post-Conference Presentations
Journal club talk on a favorite poster/talk. Either from each person or from a selected set that the group votes on.

#### Format 4: Big Ideas or Projects
This format helps senior members practice for paper discussion sections/conclusions while helping newer members see where the boundaries of fields are.

#### Format 5: Journal Club
Presentation to be given by the meeting leader followed by group discussion. The meeting leader should aim to send the chosen paper one week before the scheduled meeting, and lab members are expected to be familiar with the content for discussion.

#### Format 6: Preprint Review
A preprint is discussed by the group. The discussion is led by the meeting leader, and all members are expected to be familiar with the content. The review is written collaboratively, but another member (not the meeting leader) formats, formalizes, and uploads it to the preprint server as a comment.

## Meeting Lead
Each member is expected to sign up as lead by the end of the previous academic semester (e.g., sign up by December for the Spring semester, sign up by June for the Fall semester.)

- Lab meeting sign-ups will happen twice a year (December and June) for the upcoming 6 months.
- Each member will sign up as lead for at least 2 lab meetings each semester (6 months).
- At least one of these meetings is expected to be a Braintrust meeting.

## Ad-Hoc Meetings
After meetings have been scheduled for the semester, any member can add an ad-hoc meeting as needed.

Ad-hoc meetings are intended to help CHIRAL members get advice and support on projects, prepare for talks, oral exams, etc.


# Source Code, Data, and Reproducibility

## Pride
We expect lab members to sign their code, ensuring that source code contributions are attributable to an individual's account on GitHub. To quote from *The Pragmatic Programmer*:

> Craftsmen of an earlier age were proud to sign their work. You should be, too… People should see your name on a piece of code and expect it to be solid, well-written, tested, and documented.

While some code may be proof-of-concept, it should always inspire confidence in its quality and reliability.

## Programming Languages
Analytical work across CHIRAL is done in **scripting languages** — primarily **Python** and **R** — never in spreadsheets. The specific language and tool stack depend on the unit (e.g., bioinformatics pipelines, geospatial/GIS, survey statistics); see your unit overlay under [`/units`](/units). Whatever the stack, all members are expected to write reproducible, reviewed code per the practices below.

## Licensing
We release as many research outputs as possible under **permissive open licenses** to maximize reproducibility and accessibility. The **BSD-2-Clause Plus Patent License** is the default license for software developed in the lab, as it is **OSI-approved**, simple, and highly compatible. However, certain funding agencies may require different licenses. If there are concerns about licensing, lab members should raise them in Zulip.

## Version Control and GitHub Usage
Our primary version control service is **GitHub**, and lab members should maintain their code in repositories under the **CHIRAL Bangladesh GitHub organization**. To facilitate code review and ensure best practices, the following workflow must be followed:

### Creating a CHIRAL Repository
1. Create a repository under the CHIRAL Bangladesh organization.
2. Immediately fork this repository into your user account.
3. Make commits to your personal repository first.
4. Follow the code review process before merging changes into the CHIRAL repository.

### Code Review Process
Code moves from personal repositories to CHIRAL repositories via **pull requests**. All changes must go through this review process:

1. Make changes and commit them to your **personal repository**.
2. Create a **pull request (PR)** into the corresponding CHIRAL repository.
3. Assign reviewers to the PR.
4. At least one lab member must approve the PR before merging.
5. PRs should focus on a **single functional area** to facilitate easier reviews.

Lab members are expected to participate in reviewing pull requests when assigned.

### Handling Projects That Didn't Work
Repositories may contain **failed projects** (e.g., proof-of-concepts that didn’t succeed). Keeping track of these failures helps us **avoid repeating mistakes** and fosters transparency in research.

## Non-Code Versioning
Non-code documents should be stored in a version-controlled environment. CHIRAL Bangladesh members should use **Google Drive or OneDrive** to maintain version history.

## Data Management
- **Publicly available data**: Scripts used to download and process these data should be preserved and version-controlled.
- **Generated data**: CHIRAL-generated data should be stored in a **replicated, backed-up location** and, once policy and consent allow, deposited in the relevant public repository as soon as possible. The appropriate repository is unit-specific (e.g., **GEO/SRA** for sequencing in BBL; spatial-data and survey-data archives for the other units — see your unit overlay). Handling of human/health data is governed by the [Data Governance Policy](/shared/data-governance.md).
- **Intermediate files**: Where feasible, reasonable-sized intermediate files should be stored to facilitate re-use, but workflows should always allow data to be regenerated.

## Reproducibility
All code should support **reproducible analyses**. This can be achieved through:

- **Makefiles**, **shell scripts**, or other automation approaches.
- Including scripts for generating figures in manuscripts.
- Ensuring all code is reviewed before the submission of a **preprint** or **manuscript**.

By adhering to these guidelines, CHIRAL Bangladesh ensures **transparent, high-quality, and reproducible** research practices.


## How to Modify this Document
This is a living document. The repository is at GitHub. To make changes, fork, edit the files you wish, and create a pull request. The pull request process is handled as described in the **Getting Code into CHIRAL Repositories** section.

