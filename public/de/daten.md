---
icon: material/database
---
# Daten

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/kopf/daten.png">
  <img src="../bilder/kopf/daten_hell.png" alt="Bannerbild: die Überschrift „Daten“ neben einem gebauten Balkendiagramm „Vorgänge je Monat“ mit vier Säulen.">
</picture>

**31 Bausteine** für alles, was mit Datenbeständen zu tun hat: sie bedienbar machen, sie als
Bild verständlich machen, aus ihnen rechnen, sie verwalten und Zusammenhänge zeichnen.

## Die fünf Arten

| Art | Wofür | Beispiele |
| --- | --- | --- |
| **Bedienbare Bestände** | strukturierte Mengen, mit denen gearbeitet wird | Tabelle, Baum, Raster, Aufgabenbrett |
| **Bild statt Zahlenkolonne** | wenn ein Verlauf, ein Anteil oder ein Vergleich als Bild schneller verstanden wird | Linien-, Balken-, Flächen-, Kreisdiagramm |
| **Rechnen** | wenn aus Eingaben ein Ergebnis entsteht und die Rechenvorschrift dazugehört | Rechner, Rechenbaustein |
| **Verwalten** | wenn ein Bestand angelegt, gesucht, geändert und gelöscht wird | Verwaltungsfläche |
| **Zusammenhänge zeichnen** | wenn nicht Zahlen, sondern Beziehungen dargestellt werden | Ablauf-, Beziehungs-, Zeitdiagramm |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/bausteine/tabelle.png">
  <img src="../bilder/bausteine/tabelle_hell.png"
       alt="Eine Tabelle „Offene Vorgänge“ mit den Spalten Vorgang, Zuständig und Stand und
            drei Zeilen; darüber ein Suchfeld, die Angabe „3 Einträge“ und eine
            Schaltfläche zum CSV-Export.">
</picture>

*Ein bedienbarer Bestand: sortieren über die Spaltenköpfe, filtern über das Suchfeld,
ausgeben als CSV — ohne dass davon etwas eigens angefordert werden musste.*

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/bausteine/diagramm.png">
  <img src="../bilder/bausteine/diagramm_hell.png"
       alt="Ein Balkendiagramm „Vorgänge je Monat“ mit vier Balken für Mai bis August;
            darunter eine Leiste zum Umschalten auf Linie, Kreis, Streuung, Radar, Ringe
            oder Polar sowie eine Schaltfläche zum Speichern als PNG.">
</picture>

*Dieselben Zahlen als Bild. Die Darstellungsform lässt sich unten umschalten, ohne die
Fläche neu zu beschreiben.*

## Woher die Daten kommen

Ein Datenbaustein wird auf drei Wegen gefüllt, und es lohnt sich, den Unterschied zu kennen:

1. **Direkt hinterlegt** — die Werte gehören zur Fläche selbst. Gut für Feststehendes.
2. **Von einem anderen Baustein** — eine übernommene Datei füllt die Tabelle, eine Auswahl in
   der Tabelle füllt das Diagramm daneben. Das ist der Regelfall bei mehrteiligen Flächen.
3. **Aus einer Quelle** — Datei, Schnittstelle, Postfach.

Im [Baustein-Verzeichnis](typen/index.md) steht bei jedem Baustein, was er entgegennimmt und
was er weitergibt. Daraus ergibt sich, welche sich sinnvoll verketten lassen.

## Wo Ihre Daten bleiben

Was Sie in eine Fläche geben, bleibt auf Ihrem Rechner. Die Plattform bringt keinen Dienst
mit, an den Daten übertragen würden. Wo eine Fläche nach außen greift — eine Suche, eine
Schnittstelle, ein Übersetzungsdienst —, ist das die Aufgabe dieser Fläche und benannt.

## Rechnen mit hinterlegter Vorschrift

Rechenbausteine führen eine hinterlegte Vorschrift aus. Sie tun das in einer abgeschirmten
Umgebung mit begrenztem Sprachumfang — kein Zugriff auf Dateien, kein Nachladen beliebiger
Bestandteile. Näheres unter [Sicherheit](sicherheit.md).

## Was hier ehrlicherweise offen ist

- Diagramme sind für überschaubare Mengen ausgelegt. Bei sehr großen Beständen ist das
  Zeichnen spürbar, weil die Werte vollständig aufbereitet werden.
- Die Zeichnung von Zusammenhängen erzeugt feststehende Bilder — sie lassen sich ansehen, aber
  nicht durch Ziehen der Knoten umgestalten.
- Es gibt keine eigene Abfragesprache über mehrere Bausteine hinweg. Verknüpft wird über
  Weitergabe von einem Baustein zum nächsten, nicht über eine Abfrage.

---

Alle 31 Bausteine mit Beschreibung stehen im [Baustein-Verzeichnis](typen/index.md).
