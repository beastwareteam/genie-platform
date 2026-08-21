---
icon: material/home
---
<!-- quelle: de/index.md · stand: f43e042549af · fassung: von Hand -->

# Genie AI Platform

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/kopf/start.png">
  <img src="../bilder/kopf/start_hell.png" alt="Banner image: the headline “Beschreiben Sie es. Es entsteht.” next to a generated form with the fields Name, Abteilung and Gültig ab.">
</picture>

Genie AI Platform is a working environment that assembles itself while you use it. You say in one
sentence what you need — a table of your open invoices, a chart of monthly spending, a browser
window with two tabs side by side — and a usable surface appears. No picking from a toolbox, no
empty form waiting to be filled in.

**The important parts run on your own machine.** Language models, speech output, text
recognition, database — each of them has a local path. Networked services are a choice, not a
requirement.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/bausteine/tabelle.png">
  <img src="../bilder/bausteine/tabelle_hell.png"
       alt="A table titled „Offene Vorgänge“ with the columns Vorgang, Zuständig and Stand and
            three rows; above it a search field, the count „3 Einträge“ and a button to
            export as CSV.">
</picture>

*Built from a single sentence. Sorting by column headers, filtering through the search field,
exporting as CSV — none of it had to be asked for.*

## What that means in practice

| | |
| --- | --- |
| **You describe instead of building** | One sentence in everyday language is enough. What you leave out is filled in sensibly — and stays changeable afterwards. |
| **What you adjust, stays adjusted** | Column widths, splitters and tab order survive a rebuild of the surface. |
| **The appearance is a setting** | Colours, spacing and corner radii come from a theme and can be switched while running. |
| **Autonomous work has an emergency stop** | The platform can extend itself — **switched off by default**, and stoppable at any moment. |

## In numbers

These figures are checked against the platform itself; they cannot go stale without it showing.

| | |
| ---: | --- |
| **146 building blocks** | from a single input field to a system monitor |
| **23 families** | grouped by purpose, not by appearance |
| **3 permission tiers** | every action is classified before it runs |
| **2 languages** | German and English, more to follow |

## Take a look

<!-- kacheln: anfang -->
<div class="grid cards" markdown>

-   :material-map:{ .lg .middle } __Map of the building blocks__

    ---

    <picture><source media="(prefers-color-scheme: dark)" srcset="../bilder/kopf/landkarte.png"><img src="../bilder/kopf/landkarte_hell.png" alt="Bannerbild: die Überschrift „Landkarte der Bausteine“ neben einer gebauten Tabelle mit Bereichen und ihren Bausteinzahlen."></picture>

    What there is and where it belongs — 146 blocks in 23 families.

    [:octicons-arrow-right-24: Map of the building blocks](../de/landkarte.md)

-   :material-view-grid:{ .lg .middle } __Building block reference__

    ---

    <picture><source media="(prefers-color-scheme: dark)" srcset="../bilder/kopf/bausteine.png"><img src="../bilder/kopf/bausteine_hell.png" alt="Bannerbild: die Überschrift „Bausteine nachschlagen“ neben einem gebauten Verlauf mit drei Stationen."></picture>

    Every block described on its own — what it is, when to use it.

    [:octicons-arrow-right-24: Building block reference](../de/typen/index.md)

-   :material-view-dashboard:{ .lg .middle } __Interface__

    ---

    <picture><source media="(prefers-color-scheme: dark)" srcset="../bilder/kopf/oberflaeche.png"><img src="../bilder/kopf/oberflaeche_hell.png" alt="Bannerbild: die Überschrift „Oberfläche“ neben vier gebauten Kacheln mit den Bereichen Technik, Vertrieb, Betrieb und Qualität."></picture>

    Enter, choose, display, arrange — 62 blocks for the surface.

    [:octicons-arrow-right-24: Interface](../de/oberflaeche.md)

-   :material-database:{ .lg .middle } __Data__

    ---

    <picture><source media="(prefers-color-scheme: dark)" srcset="../bilder/kopf/daten.png"><img src="../bilder/kopf/daten_hell.png" alt="Bannerbild: die Überschrift „Daten“ neben einem gebauten Balkendiagramm „Vorgänge je Monat“ mit vier Säulen."></picture>

    Make data operable, understand it as a picture, calculate from it.

    [:octicons-arrow-right-24: Data](daten.md)

-   :material-play-box:{ .lg .middle } __Media and web__

    ---

    <picture><source media="(prefers-color-scheme: dark)" srcset="../bilder/kopf/medien_und_web.png"><img src="../bilder/kopf/medien_und_web_hell.png" alt="Bannerbild: die Überschrift „Medien und Web“ neben einer gebauten Liste „Was hier hineingeht“ mit vier Einträgen von Video bis PDF."></picture>

    Video and audio, the embedded browser, maps, PDF.

    [:octicons-arrow-right-24: Media and web](../de/medien_und_web.md)

-   :material-cart:{ .lg .middle } __Commerce__

    ---

    <picture><source media="(prefers-color-scheme: dark)" srcset="../bilder/kopf/handel.png"><img src="../bilder/kopf/handel_hell.png" alt="Bannerbild: die Überschrift „Handel“ neben einer gebauten Warenkorb-Übersicht mit Positionen und Endsumme."></picture>

    Price, product, cart, rating — when commerce data belongs on screen.

    [:octicons-arrow-right-24: Commerce](handel.md)

</div>
<!-- kacheln: ende -->

Also: [Videos](../de/videos.md) — from sentence to building block, a tour,
building your own; each one is also available in full as text (German).

## Getting started

!!! warning "The published source code is not yet at this state"

    These pages describe the platform as it is currently being developed. The source code is
    published separately and currently lags behind — what the commands below give you is an
    older state.

```bash
git clone https://github.com/beastwareteam/genie-platform.git
cd genie-platform
pip install -e .
python -m genie.main
```

After that, one sentence in the chat window is enough. If nothing appears, `/status` says what
is holding it up; `/wiki` explains the controls in detail.

## What is honestly still open

- **The platform is under development.** It runs, but it is not a finished product with
  guarantees.
- **No licence has been set for the work as a whole** — see [Licences and
  origin](../de/lizenzen.md) (German). Until then: all rights reserved.
- **Accessibility is intended, not verified.** What is missing is listed by name on the
  [Accessibility](../de/barrierefreiheit.md) page (German).
- **Most pages exist in German only.** This English version currently covers the entry point
  and a few explanatory pages; the reference pages are generated and are therefore still
  German-only.
- **The published source code lags behind.** These pages are current, the repository
  is not — the two are published separately.
- Testing happens on Windows. Other systems are intended but not verified.

---

What the platform is built on is described under [Technology](../de/technologie.md); which AI
functions exist and what they do under [AI transparency](../de/ki_transparenz.md) (both German).
