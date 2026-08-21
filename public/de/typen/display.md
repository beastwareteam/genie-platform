---
icon: material/monitor
---
# Display
<!-- erzeugt: typenkatalog — nicht von Hand aendern -->


Wenn Vorhandenes gezeigt werden soll, ohne dass der Nutzer es ändert.

7 Bausteine.

## definition_list

Begriff/Definition-Liste (Term + Erläuterung)

| Merkmal | Wert |
| --- | --- |
| Bereich | Anzeige |
| Konfigurierbar | nein |

## display

Anzeige-Widget für statische oder dynamische Inhalte

**Wann nehme ich es?** Wenn ein Text oder Wert nur gezeigt wird. Sobald es mehrere gleichartige Einträge sind: `list`; sobald sie Spalten haben: `table`.

| Merkmal | Wert |
| --- | --- |
| Bereich | Anzeige |
| Nimmt entgegen | text |
| Konfigurierbar | nein |

## key_value_list

Schlüssel-Wert-Liste (Label + Wert je Zeile)

| Merkmal | Wert |
| --- | --- |
| Bereich | Anzeige |
| Konfigurierbar | nein |

## list

Listenansicht mit optionalen Icons und Badges

**Wann nehme ich es?** Wenn gleichartige Einträge untereinander stehen und je Eintrag eine Zeile genügt — mit Spalten, Sortierung oder Filter ist `table` gemeint.

| Merkmal | Wert |
| --- | --- |
| Bereich | Anzeige |
| Nimmt entgegen | rows |
| Gibt weiter | selected_row |
| Konfigurierbar | nein |

## stat_tile

Kennzahl-Kachel mit Text (Skelett-gerendert)

> **Noch ein Gerüst.** Dieser Baustein ist bewusst unfertig — er lässt sich einsetzen, bringt aber noch keine ausgebaute Bedienung mit.

| Merkmal | Wert |
| --- | --- |
| Bereich | Anzeige |
| Konfigurierbar | nein |

## table

Tabellarische Datenansicht mit Sortierung und Filterung

**Wann nehme ich es?** Wenn Datensätze mit mehreren Spalten gezeigt, sortiert und gefiltert werden. Sollen sie auch angelegt und geändert werden, ist `management` der Typ.

| Merkmal | Wert |
| --- | --- |
| Bereich | Anzeige |
| Nimmt entgegen | rows |
| Gibt weiter | selected_row |
| Konfigurierbar | nein |

## weather

Wetter für eine Stadt (Open-Meteo, ohne Schlüssel)

| Merkmal | Wert |
| --- | --- |
| Bereich | Anzeige |
| Konfigurierbar | ja |
