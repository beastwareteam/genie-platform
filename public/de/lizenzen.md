---
icon: material/scale-balance
---
# Lizenzen und Herkunft

Diese Seite sagt, unter welchen Erlaubnissen die Bestandteile dieser Plattform stehen — und
was für das Gesamtwerk gilt.

!!! warning "Für das Gesamtwerk ist noch keine Lizenz gesetzt"

    Es gibt bisher keine Lizenzdatei. Ohne eine solche Erklärung gilt das gesetzliche
    Urheberrecht: **alle Rechte vorbehalten**. Die Plattform ist einsehbar, aber nicht zur
    Weitergabe oder Weiterverwendung freigegeben.

    Das ist eine offene Entscheidung, keine Absicht. Die Aufstellung unten ist ihre
    Grundlage — die Wahl selbst trifft ein Mensch, und sie lässt sich schlecht
    zurücknehmen.

## Was hier an fremder Arbeit steckt

Die Angaben stammen aus den Paketen selbst und werden nachgezogen, wenn sich der Bestand
ändert.

<!-- erzeugt: lizenzen — nicht von Hand aendern -->

| Bestandteil | Fassung | Lizenz | Was das für die Weitergabe bedeutet |
| --- | --- | --- | --- |
| PySide6 | 6.11.0 | LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only | Weitergabe erlaubt, auch in einem geschlossenen Programm — solange der Nutzer die Bibliothek austauschen kann und der Lizenztext beiliegt. |
| PyYAML | 6.0.3 | MIT | Weitergabe und Änderung frei, solange Lizenztext und Urheberhinweis beiliegen. |
| tzdata | 2026.1 | Apache-2.0 | Weitergabe und Änderung frei, mit ausdrücklicher Patenterlaubnis; Änderungen sind zu kennzeichnen. |
| psutil | 7.2.2 | BSD-3-Clause | Weitergabe und Änderung frei, solange Urheberhinweis beiliegt und mit dem Namen der Urheber nicht geworben wird. |
| pywin32 | 312 | PSF | Weitergabe und Änderung frei, solange Lizenztext und Urheberhinweis beiliegen. |
| 19 Technologie-Zeichen | — | ISC (Lucide) | Weitergabe und Änderung frei, solange Lizenztext und Urheberhinweis beiliegen. |
| 22 Technologie-Zeichen | — | MIT (Devicon) | Weitergabe und Änderung frei, solange Lizenztext und Urheberhinweis beiliegen. |

<!-- ende: lizenzen -->

## Die eine Zeile, an der alles hängt

Von fünf mitgelieferten Bausteinen steht **einer** unter einer Copyleft-Lizenz: die
Qt-Anbindung. Das ist eine ungewöhnlich saubere Ausgangslage — aber es ist der tragende
Baustein, ohne den die Oberfläche nicht läuft.

Daraus folgt, in Kürze:

- Die freie Qt-Kette bietet **kein** MIT und **kein** BSD. Die mildeste Wahl ist LGPL.
- Unter LGPL darf eigener Programmcode eine andere Lizenz tragen — auch eine geschlossene —
  **solange der Nutzer die Qt-Bibliothek austauschen kann**. Bei den üblichen Bündelverfahren
  liegen die Qt-Bibliotheken als eigene Dateien neben dem Programm; diese Bedingung ist dann
  erfüllbar.
- **Fest verschmolzen** in eine einzige Programmdatei wird es zum Problem: dann greift die
  Austauschbarkeit nicht mehr, und es braucht entweder Zwischendateien zur Neubindung oder
  eine gekaufte Qt-Lizenz.
- Beizulegen sind in jedem Fall: der Lizenztext, ein Hinweis auf die Qt-Nutzung und ein
  Verweis auf dessen Quelltext.

## Zeichen sind nicht dasselbe wie Bilder

Die Technologie-Zeichen stammen aus zwei Sammlungen (Devicon, Lucide), und beide Sammlungen
sind frei lizenziert. **Die Marken darin gehören ihren Inhabern** — eine Marke wird nicht
mitlizenziert, nur weil die Datei, in der sie liegt, es ist. Deshalb werden Herstellerzeichen
hier nie umgefärbt oder verändert; wo es kein freigegebenes Zeichen gibt, steht ein
ausdrücklich als Ersatz gekennzeichnetes, allgemeines Symbol.

## Was hier ehrlicherweise offen ist

- **Die Lizenz des Gesamtwerks ist nicht gesetzt.** Bis dahin gilt das Urheberrecht in seiner
  Grundform.
- **Diese Seite ist keine Rechtsberatung.** Sie fasst zusammen, was die Pakete über sich
  selbst angeben. Für eine verbindliche Aussage gehört ein Anwalt gefragt.
- Aufgeführt sind die **mitgelieferten** Bestandteile. Was jemand zusätzlich in seiner eigenen
  Umgebung installiert, ist nicht Teil dieses Werks und steht hier nicht.
- Für die Zeichen ist die vollständige Herkunft — Quelle, Lizenz der Datei, Inhaber des
  Zeichens — je Datei im Quelltext-Verzeichnis hinterlegt.

---

Welche Technologien überhaupt verwendet werden, steht auf der Seite
[Technologie](technologie.md).
