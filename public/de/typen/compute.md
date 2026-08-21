---
icon: material/calculator
---
# Compute
<!-- erzeugt: typenkatalog — nicht von Hand aendern -->


Wenn aus Eingaben ein Ergebnis gerechnet wird und die Rechenvorschrift zum Gen gehört.

2 Bausteine.

## calculator

Rechner: sichere Ausdruck-Auswertung (Mathematik/Funktionen, no-eval AST) plus Einheiten-Umrechnung (Länge/Masse/Zeit/Daten/Temperatur) — kein LLM.

| Merkmal | Wert |
| --- | --- |
| Bereich | Berechnung |
| Konfigurierbar | nein |

## compute

Berechnungs-Widget mit Eingabe-Parametern und Ergebnis-Anzeige

**Wann nehme ich es?** Wenn eine **eigene** Rechenvorschrift auf benannte Parameter angewandt wird (`function_body`). Für freies Rechnen genügt `calculator` ohne Vorschrift.

> **Führt Code aus.** Dieser Baustein kann hinterlegte Anweisungen ausführen. Das ist gewollt und wird vor jeder Ausführung bestätigt.

| Merkmal | Wert |
| --- | --- |
| Bereich | Berechnung |
| Nimmt entgegen | input |
| Gibt weiter | result |
| Konfigurierbar | nein |
