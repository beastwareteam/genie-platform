---
icon: material/flask
---
# Advanced
<!-- erzeugt: typenkatalog — nicht von Hand aendern -->


Wenn kein deklarativer Typ passt — letzte Wahl, weil der Rumpf erzeugt statt deklariert wird.

2 Bausteine.

## custom

Exec-only: LLM-generierter PySide6-Code (class_body oder code)

**Wann nehme ich es?** **Letzte Wahl.** Nur wenn nachweislich kein deklarativer Typ passt: der Rumpf wird erzeugt statt deklariert und ist damit weder prüfbar noch im Editor bearbeitbar.

> **Führt Code aus.** Dieser Baustein kann hinterlegte Anweisungen ausführen. Das ist gewollt und wird vor jeder Ausführung bestätigt.

| Merkmal | Wert |
| --- | --- |
| Bereich | Erweitert |
| Konfigurierbar | nein |

## framework

Blueprint-Gene mit Varianten — wird zu konkretem Typ aufgelöst

**Wann nehme ich es?** Wenn eine Bauvorlage mit Varianten deklariert wird, deren konkreter Typ erst beim Auflösen feststeht — nicht für ein fertiges Interface.

| Merkmal | Wert |
| --- | --- |
| Bereich | Erweitert |
| Konfigurierbar | nein |
