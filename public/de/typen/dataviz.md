---
icon: material/chart-bar
---
# Dataviz
<!-- erzeugt: typenkatalog — nicht von Hand aendern -->


Wenn Zahlen als Bild verständlicher sind als als Text — Verlauf, Anteil, Vergleich.

15 Bausteine.

## area_chart

Flächendiagramm aus Datenreihen (Skelett-gerendert)

> **Noch ein Gerüst.** Dieser Baustein ist bewusst unfertig — er lässt sich einsetzen, bringt aber noch keine ausgebaute Bedienung mit.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Konfigurierbar | nein |

## bar_chart

Balkendiagramm aus Datenreihen (Skelett-gerendert)

> **Noch ein Gerüst.** Dieser Baustein ist bewusst unfertig — er lässt sich einsetzen, bringt aber noch keine ausgebaute Bedienung mit.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Konfigurierbar | nein |

## card_grid

Raster-Layout aus Karten (responsive Spalten)

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Gibt weiter | selected_row |
| Konfigurierbar | nein |

## chart

Interaktiver Chart (Linien, Balken, Kreis, Radar)

**Wann nehme ich es?** Wenn eine eigene Datenreihe gezeichnet wird (Form über `chart_type`). Für Börsenkurse aus dem Netz: `live_chart`; für einen einzelnen Wert: `gauge`.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Nimmt entgegen | chart_series |
| Gibt weiter | series_data |
| Konfigurierbar | nein |

## dashboard

Dashboard-Layout mit Metriken, Charts und Tabellen

**Wann nehme ich es?** Wenn mehrere Kennzahlen und Diagramme **zusammen** einen Überblick geben. Für ein einzelnes Diagramm genügt `chart`.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Nimmt entgegen | metrics |
| Gibt weiter | metrics |
| Konfigurierbar | nein |

## donut_chart

Ring-/Donut-Diagramm aus Datenreihen (Skelett-gerendert)

> **Noch ein Gerüst.** Dieser Baustein ist bewusst unfertig — er lässt sich einsetzen, bringt aber noch keine ausgebaute Bedienung mit.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Konfigurierbar | nein |

## funnel_chart

Trichterdiagramm aus Datenreihen (Skelett-gerendert)

> **Noch ein Gerüst.** Dieser Baustein ist bewusst unfertig — er lässt sich einsetzen, bringt aber noch keine ausgebaute Bedienung mit.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Konfigurierbar | nein |

## gauge

Messuhr: ein Wert auf einer Skala (270°-Bogen mit Zeiger)

**Wann nehme ich es?** Wenn **ein** gespeister Wert gegen eine Skala gezeigt wird. Für den Verlauf mehrerer Werte ist `sparkline` gemeint, für Achsen und Legende `chart`.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Nimmt entgegen | value |
| Konfigurierbar | nein |

## heatmap

Konfigurierbare Wärmekarte (Matrix-Heatmap, Custom-paintEvent-Raster)

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Nimmt entgegen | matrix |
| Konfigurierbar | nein |

## line_chart

Liniendiagramm aus Datenreihen (Skelett-gerendert)

> **Noch ein Gerüst.** Dieser Baustein ist bewusst unfertig — er lässt sich einsetzen, bringt aber noch keine ausgebaute Bedienung mit.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Konfigurierbar | nein |

## live_chart

TradingView Advanced Chart — Live-Krypto/Börse via QWebEngineView

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Nimmt entgegen | chart_series |
| Gibt weiter | series_data |
| Konfigurierbar | nein |

## pie_chart

Kreisdiagramm aus Datenreihen (Skelett-gerendert)

> **Noch ein Gerüst.** Dieser Baustein ist bewusst unfertig — er lässt sich einsetzen, bringt aber noch keine ausgebaute Bedienung mit.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Konfigurierbar | nein |

## radar_chart

Netzdiagramm aus Datenreihen (Skelett-gerendert)

> **Noch ein Gerüst.** Dieser Baustein ist bewusst unfertig — er lässt sich einsetzen, bringt aber noch keine ausgebaute Bedienung mit.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Konfigurierbar | nein |

## scatter_chart

Streudiagramm aus Datenreihen (Skelett-gerendert)

> **Noch ein Gerüst.** Dieser Baustein ist bewusst unfertig — er lässt sich einsetzen, bringt aber noch keine ausgebaute Bedienung mit.

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Konfigurierbar | nein |

## sparkline

Kompakter Mini-Trend ohne Achsen (Linie mit Füllfläche)

| Merkmal | Wert |
| --- | --- |
| Bereich | Daten-Visualisierung |
| Nimmt entgegen | values |
| Konfigurierbar | nein |
