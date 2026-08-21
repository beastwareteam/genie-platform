---
icon: material/calendar-clock
---
# Datetime
<!-- erzeugt: typenkatalog — nicht von Hand aendern -->


Wenn ein Zeitpunkt oder Zeitraum gewählt oder angezeigt werden soll.

4 Bausteine.

## clock

Selbst-tickende Uhr (Datum/Uhrzeit, konfigurierbar) — Timing-Familie C1

| Merkmal | Wert |
| --- | --- |
| Bereich | Datum/Zeit |
| Konfigurierbar | nein |

## date_picker

Datumsauswahl mit Kalender-Popup

| Merkmal | Wert |
| --- | --- |
| Bereich | Datum/Zeit |
| Gibt weiter | datum |
| Konfigurierbar | ja |

## date_range

Zeitraum-Auswahl (von/bis, Ordnung erzwungen)

| Merkmal | Wert |
| --- | --- |
| Bereich | Datum/Zeit |
| Gibt weiter | von |
| Konfigurierbar | ja |

## time_picker

Uhrzeitauswahl

| Merkmal | Wert |
| --- | --- |
| Bereich | Datum/Zeit |
| Gibt weiter | uhrzeit |
| Konfigurierbar | ja |
