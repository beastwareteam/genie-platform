---
icon: material/view-dashboard
---
# Oberfläche

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/kopf/oberflaeche.png">
  <img src="../bilder/kopf/oberflaeche_hell.png" alt="Bannerbild: die Überschrift „Oberfläche“ neben vier gebauten Kacheln mit den Bereichen Technik, Vertrieb, Betrieb und Qualität.">
</picture>

Mit **62 Bausteinen** ist dies der größte Bereich der Plattform — alles, womit ein Mensch
unmittelbar umgeht: Eingeben, Auswählen, Auslösen, Anzeigen, Blättern, Zurückmelden.

Sie müssen keinen davon auswendig kennen. Sie beschreiben, was Sie brauchen, und die
Konstruktion wählt aus. Diese Seite erklärt, **wonach** sie wählt — damit Sie beeinflussen
können, was entsteht.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/bausteine/formular.png">
  <img src="../bilder/bausteine/formular_hell.png"
       alt="Ein Formular mit dem Titel „Zugang beantragen“: ein Pflichtfeld „Name“ mit
            Platzhalter, ein Auswahlfeld „Abteilung“, ein Datumsfeld „Gültig ab“ sowie die
            Schaltflächen „Absenden“ und „Zurücksetzen“.">
</picture>

*Ein Formular, wie es aus einer Beschreibung entsteht. Das Bild ist kein Entwurf: es wird
bei jeder Änderung neu aus einem echten Bau aufgenommen.*

## Die Bedienfläche selbst

Alles, was auf dieser Seite steht, entsteht **in** einer Fläche — und die wird selten
gezeigt. Hier ist sie, aufgenommen aus der laufenden Anwendung:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/oberflaeche/oberflaeche_gesamt.png">
  <img src="../bilder/oberflaeche/oberflaeche_gesamt_hell.png" alt="Die Bedienflaeche der Plattform: oben eine Reihe Aktionsknoepfe, darunter der Verlauf mit einer gebauten, durchsuchbaren Tabelle offener Vorgaenge, unten das Eingabefeld mit dem Senden-Knopf und eine Statuszeile.">
</picture>

*Ein Satz genügte: „eine Tabelle mit meinen offenen Vorgängen". Was daraus entstand, steht
im Verlauf — mit Suchfeld, Sortierung und CSV-Ausgabe, ohne dass davon etwas eigens
angefordert werden musste. Auch dieses Bild ist kein Entwurf: es wird aus dem echten
Programm aufgenommen, und wenn eine Bedienstelle daraus verschwindet, bricht die Aufnahme.*

### Wo finden Sie was

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/oberflaeche/oberflaeche_wegweiser.png">
  <img src="../bilder/oberflaeche/oberflaeche_wegweiser_hell.png" alt="Dieselbe Bedienflaeche mit nummerierten Markern an den Bedienstellen und einer Legende darunter: Aktionsleiste, Verlauf, Eingabe, Trenner und die Statuszeile mit dem Modell.">
</picture>

*Die Marker sitzen auf der echten Geometrie der Bedienelemente, nicht auf einer Zeichnung.*

**Oben die Aktionsleiste (1).** Je ein Knopf für einen Baustein, den Sie oft brauchen —
anpassbar über das Kontextmenü der Leiste, ein bis fünf Reihen hoch. **In der Mitte der
Verlauf (2).** Was gebaut wurde, steht dort **bedienbar**: Sie sortieren die Tabelle, Sie
tippen in das Suchfeld, Sie geben aus. **Unten die Eingabe (3).** Ein Satz genügt; Enter
sendet, `/` zeigt die Befehle, `↑`/`↓` blättert durch das Gesagte.

Zwischen den drei Bereichen liegen **Trenner**: daran ziehen Sie einen Bereich größer oder
klappen ihn ganz zu. Die Größen bleiben erhalten — das Fenster erinnert sich an sie.

In der Statuszeile stehen die Anzeigen zum Stand: **welches Modell antwortet (4)** und
**was die Selbstprüfung meldet (5)**.

### Dieselbe Fläche, zehn Gestaltungen

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/oberflaeche/oberflaeche_faecher.png">
  <img src="../bilder/oberflaeche/oberflaeche_faecher_hell.png" alt="Sieben Fassungen derselben Bedienflaeche gefaechert hintereinander, von dunkel ueber gedeckte Farbtoene bis hell und kontraststark — dieselbe Anordnung, unterschiedliche Gestaltung.">
</picture>

*Sieben der zehn Paletten, gefächert — vorn die dunkle Voreinstellung, hinten die helle und
die kontraststarke Fassung.*

Die Gestaltung liegt **nicht** im Programmcode, sondern in Paletten: Farben, Abstände,
Radien und Schriftgrößen stehen als benannte Werte da und werden zur Laufzeit gewechselt.
Deshalb sieht auf allen Bildern oben dieselbe Anordnung anders aus, ohne dass ein Baustein
etwas davon weiß — er fragt nach `accent.primary`, nicht nach einem Farbwert.

## Die sechs Fragen, nach denen sortiert wird

| Wenn Sie… | dann greift |
| --- | --- |
| etwas eingeben oder auswählen wollen, das danach weiterverwendet wird | **Eingabe** — Formular, Auswahlfeld, Schieberegler, Datei-Übernahme |
| etwas auslösen wollen — eine Aktion, keine Eingabe | **Interaktion** — Schaltflächen, Schalter, Befehlsleisten |
| etwas nur zeigen wollen, ohne dass es geändert wird | **Anzeige** — Text, Wert, Liste, Tabelle, Abzeichen |
| Text als Inhalt setzen — Überschrift, Absatz, Quelltext | **Inhalt** |
| viel Inhalt abschnittsweise zeigen — eingeklappt, gestuft, geblättert | **Behälter** |
| jemandem etwas mitteilen, das er zur Kenntnis nimmt statt bedient | **Rückmeldung** — Hinweis, Fortschritt, Meldung |

Dazu kommen **Navigation** (zwischen Orten wechseln, ohne Daten zu ändern), **Zeitangaben**
(Zeitpunkt oder Zeitraum wählen), **Zustand** (Ampeln, Abzeichen), **Überlagerung** (Dialoge,
Einblendungen) und **Aufteilung** (wie der Platz auf der Fläche verteilt wird).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/bausteine/verlauf.png">
  <img src="../bilder/bausteine/verlauf_hell.png"
       alt="Ein senkrechter Verlauf mit drei Stationen: „Eingegangen — Antrag erfasst“,
            „Geprüft — Unterlagen vollständig“, „Freigegeben — Zugang erteilt“, verbunden
            durch eine Linie mit Ringen an jeder Station.">
</picture>

*Ein Zustand über die Zeit — dieselbe Sache, die als Tabelle nur eine Spalte „Stand“ wäre.*

## Warum die Unterscheidung zählt

Zwischen „ein Wert wird gezeigt" und „ein Wert wird eingegeben" liegt der ganze Unterschied
zwischen einer Anzeige und einem Formular. Beschreiben Sie also nicht nur **was**, sondern
**was damit geschehen soll** — daraus entsteht die Wahl.

Zwei Beispiele:

- *„Zeig mir die Auslastung"* führt zu einer Anzeige.
- *„Lass mich die Auslastungsgrenze einstellen"* führt zu einer Eingabe mit Wertebereich.

## Die Bausteine miteinander verbinden

Bausteine stehen nicht nebeneinander, sie können ineinandergreifen: Was der eine ausgibt, kann
der andere entgegennehmen — eine Auswahl in einer Liste füllt eine Anzeige daneben, eine
übernommene Datei füllt eine Tabelle. Im [Baustein-Verzeichnis](typen/index.md) steht bei
jedem Baustein, was er entgegennimmt und was er weitergibt.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/bausteine/kacheln.png">
  <img src="../bilder/bausteine/kacheln_hell.png"
       alt="Vier Kacheln nebeneinander mit den Überschriften Technik, Vertrieb, Betrieb und
            Qualität; jede trägt darunter eine Zahl offener Vorgänge und oben einen farbigen
            Streifen.">
</picture>

*Dieselben Angaben als Kacheln statt als Liste — die Wahl entsteht daraus, was Sie
beschreiben, nicht daraus, was Sie anklicken.*

## Größe und Aufteilung

Was Sie an einer Fläche ziehen, bleibt so. Spaltenbreiten, Trennerpositionen, die Reihenfolge
von Reitern — solche Handgriffe werden übernommen, sobald Sie sie machen.

Die **Größe des Fensters** verhält sich bewusst anders: sie wird nur im dafür eingeschalteten
Modus übernommen. Der Grund ist eine Alltagsbeobachtung — ein Fenster zieht man auch größer,
nur um Platz zu schaffen. Einen Spaltentrenner zieht dagegen niemand aus Versehen.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/bausteine/hinweis.png">
  <img src="../bilder/bausteine/hinweis_hell.png"
       alt="Ein grün umrandeter Hinweis mit Haken: „Änderung übernommen — Die Spaltenbreite
            wurde gespeichert und gilt beim nächsten Öffnen.“">
</picture>

*Übernommen heißt: beim nächsten Öffnen ist es noch so. Sie erfahren das, ohne danach
suchen zu müssen.*

## Was hier ehrlicherweise offen ist

- Einige Bausteine sind bewusst noch Gerüste: sie lassen sich einsetzen, bringen aber noch
  keine ausgebaute Bedienung mit. Sie sind im Verzeichnis als solche gekennzeichnet.
- Die Bedienbarkeit ohne Maus und mit Hilfsmitteln ist über alle Bausteine hinweg **nicht**
  durchgeprüft — siehe [Barrierefreiheit](barrierefreiheit.md).

---

Alle 62 Bausteine mit Beschreibung stehen im [Baustein-Verzeichnis](typen/index.md).
