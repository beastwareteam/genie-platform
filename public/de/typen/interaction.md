---
icon: material/gesture-tap
---
# Interaction
<!-- erzeugt: typenkatalog — nicht von Hand aendern -->


Wenn der Nutzer etwas auslösen soll — eine Aktion, keine Eingabe.

5 Bausteine.

## action_surface

Frei anordenbare Aktionsfläche (Raster/Ring/Bogen/Polygon/Wabe/Frei)

**Wann nehme ich es?** Wenn Knöpfe nicht in einer Reihe stehen sollen — Ring, Bogen, Wabe oder frei gesetzte Punkte. Für eine schlichte Knopfzeile bleibt `button_group` richtig.

| Merkmal | Wert |
| --- | --- |
| Bereich | Interaktion |
| Gibt weiter | action |
| Konfigurierbar | nein |

## button_group

Gruppe von Aktions-Buttons mit einheitlichem Styling

| Merkmal | Wert |
| --- | --- |
| Bereich | Interaktion |
| Gibt weiter | action |
| Konfigurierbar | nein |

## calendar

Kalender-Widget mit Ereignis-Verwaltung

| Merkmal | Wert |
| --- | --- |
| Bereich | Interaktion |
| Konfigurierbar | nein |

## command_console

Kommandozeile im Interface: Befehle (add/list/set/get/remove) auf das eigene Gene, mit Alias, Vervollständigung und Historie — tick-frei

| Merkmal | Wert |
| --- | --- |
| Bereich | Interaktion |
| Konfigurierbar | nein |

## edge_bar

Edge-Aktionsleiste (Undo/Export/Speichern/Laden) → Kommandos an die Tabelle (LUX-Stufe 4)

| Merkmal | Wert |
| --- | --- |
| Bereich | Interaktion |
| Gibt weiter | edge |
| Konfigurierbar | nein |
