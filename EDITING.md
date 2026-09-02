# Editing the CHIRAL Bangladesh website

The lists that grow over time — people, programmes, partners — live in `.yml`
files next to the page they appear on. Edit one on github.com, click **Commit
changes**, and the site rebuilds and goes live on its own in about two minutes.

You do not need to install anything.

## The collections

| To change | Edit |
|---|---|
| Leadership team | `people/leadership.yml` |
| Research assistants | `people/assistants.yml` |
| Alumni roster | `people/alumni.yml` |
| Training programmes | `training/programmes.yml` |
| Partner institutions | `collaborators/partners.yml` |
| Publications | `publications/journal-articles.yml` |

Each file is a list. Every entry starts with `- path:` and the lines under it
are indented two spaces further.

## Adding someone to the team

Open `people/leadership.yml`, copy an existing entry, paste it at the end, and
change the details:

```yaml
- path:
  title: "Jane Doe"
  role: "Bioinformatic Analyst"
  image: "/img/research-staff/jane.jpg"
  linkedin: ""
  github: ""
```

- **No photo yet?** Delete the `image:` line — they get a placeholder tile.
- **No LinkedIn yet?** Leave the quotes empty. The icon still shows, dimmed and
  not clickable, and switches on as soon as you paste a URL between the quotes.
- **Photos** go in `img/research-staff/`. Upload with **Add file → Upload
  files** on github.com, then reference it as `/img/research-staff/your-file.jpg`.

To remove someone, delete their whole entry — from `- path:` down to the last
indented line.

## The one rule

**Indentation is the structure.** Copy an entry that already exists rather than
typing one from scratch, and never use tab characters.

If you get it wrong the site does not break: the build fails and the previous
version stays live. The **Actions** tab shows a red ✗ with the error.

## Everything else

Page wording, headings and one-off sections are written directly in each page's
`index.qmd` — `about/index.qmd`, `support/index.qmd`, and so on. Those change
rarely, and the text sits in plain HTML you can read and edit in place.

News posts are one folder each under `posts/`, containing an `index.qmd` with a
title, date and description at the top and the announcement below.

## Adding a publication

Open `publications/journal-articles.yml`, copy the entry that is there, and
change the fields:

```yaml
- path:
  title: "The paper's title"
  author: "Surname, A. B., Surname, C. D., & Surname, E. F."
  year: "2026"
  journal: "Journal name"
  doi: "https://doi.org/..."
  preprint: ""
  materials: ""
  categories:
    - Journal Article
```

Authors go in **APA style** — surname, then initials, with `&` before the last
one — in the order they were published. Keep a multi-word surname whole
("Al Mamun, A.", not "Mamun, A. A."); if you are unsure how a name splits,
the paper's Crossref record at `https://api.crossref.org/works/<doi>` gives the
family and given names the publisher registered.

Leave `doi`, `preprint` or `materials` as `""` when there isn't one — the tag
for it simply does not appear. The list sorts by year, newest first.

For preprints or conference work, make a second `.yml` file and add a second
listing block in `publications/index.qmd` — the people page splits its rosters
the same way.

## For developers

- Collections are native Quarto listings: `contents: <file>.yml` in the page's
  front matter, rendered by an EJS card template in `_templates/`.
- `_templates/person-card.ejs`, `programme-card.ejs`, `partner-card.ejs` emit
  the same classes the hand-written markup uses, so a collection and a static
  section look identical.
- `scripts/clean-urls.py` runs after render and strips `index.html` from the
  links Quarto generates, so the site serves directory URLs.
- `_quarto.yml` limits `render:` to this site's own pages — a reference
  checkout of another Quarto site sits untracked in the working tree, and
  without that limit Quarto walks into it and publishes its pages too.
