---
icon: material/form-textbox
---
# Input
<!-- erzeugt: typenkatalog — nicht von Hand aendern -->


Wenn der Nutzer etwas eingeben oder auswählen soll und der Wert danach weiterverarbeitet wird.

8 Bausteine.

## autocomplete_field

Eingabe mit Autovervollständigung

| Merkmal | Wert |
| --- | --- |
| Bereich | Eingabe |
| Gibt weiter | suche |
| Konfigurierbar | ja |

## color_field

Farbauswahl-Eingabe (Farbwähler + Vorschau)

| Merkmal | Wert |
| --- | --- |
| Bereich | Eingabe |
| Gibt weiter | farbe |
| Konfigurierbar | ja |

## file_upload

Datei-Import (CSV/JSON) mit Laufzeit-Feldgruppen-Auswahl (LUX-3c)

**Wann nehme ich es?** Wenn Daten aus einer Datei ins Gen kommen — der Datensatz wird über `dataset` an gebundene Ziele (Tabelle/Chart) weitergereicht.

| Merkmal | Wert |
| --- | --- |
| Bereich | Eingabe |
| Gibt weiter | dataset |
| Konfigurierbar | ja |

## form

Formular mit konfigurierbaren Feldern und Validierung

**Wann nehme ich es?** Wenn mehrere zusammengehörige Werte in einem Rutsch erfasst werden — für einen einzelnen Schalter oder Import ist `toggle_group`/`file_upload` die kleinere Wahl.

| Merkmal | Wert |
| --- | --- |
| Bereich | Eingabe |
| Nimmt entgegen | prefill |
| Gibt weiter | output |
| Konfigurierbar | ja |

## rating

Bewertungs-Eingabe (klickbare Skala)

| Merkmal | Wert |
| --- | --- |
| Bereich | Eingabe |
| Gibt weiter | bewertung |
| Konfigurierbar | ja |

## slider_field

Schieberegler-Eingabe mit Live-Wertanzeige

| Merkmal | Wert |
| --- | --- |
| Bereich | Eingabe |
| Gibt weiter | wert |
| Konfigurierbar | ja |

## tag_field

Schlagwort-Eingabe (Chips mit Entfernen)

| Merkmal | Wert |
| --- | --- |
| Bereich | Eingabe |
| Gibt weiter | schlagwoerter |
| Konfigurierbar | ja |

## toggle_group

Gruppe von Schiebeschaltern (exklusiv bei Optionen) über Felder

| Merkmal | Wert |
| --- | --- |
| Bereich | Eingabe |
| Gibt weiter | output |
| Konfigurierbar | ja |
