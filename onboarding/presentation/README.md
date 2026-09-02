# CHIRAL Onboarding — Slide Deck

A [reveal.js](https://revealjs.com/) presentation covering the full CHIRAL onboarding, for lab
orientation across the DeepBio ecosystem.

## View it

- **Locally:** open `index.html` in a browser. (Uses reveal.js from a CDN, so you need internet
  the first time.)
- **Offline / no CDN:** serve the folder with any static server, e.g. `python -m http.server`
  then visit `http://localhost:8000/presentation/`.
- **GitHub Pages:** enable Pages for the repo; the deck is at `…/presentation/`.

## Controls

- `←` `→` / `Space` — navigate · `Esc` — slide overview · `S` — speaker notes · `F` — fullscreen.

## Branding

Built on the **DeepBio brand template** (`../brand-template/index.html`): Inter + Outfit fonts,
`#205E92` primary blue, dark section dividers, tag/card/stat components.

The joint logo is wired to `../logos/deepbio-chiral.png` (top-right, persistent). To swap it,
replace that file or edit the `.db-logo img src` in `index.html`. Fixed deck size is 1200×700.

## Export to PDF

Open the deck with `?print-pdf` appended to the URL, then Print → Save as PDF. Example:
`index.html?print-pdf`.

## Edit

Content is plain HTML `<section>` slides in `index.html`. Brand colors are CSS variables
(`--chiral`, `--deepbio`, `--accent`) at the top of the `<style>` block. The deck mirrors the
repo docs — when policy changes, update both.
