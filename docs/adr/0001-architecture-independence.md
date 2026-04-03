# ADR 0001: Architekturelle Eigenständigkeit

## Status
Accepted

## Kontext
Das Projekt startet mit einer strukturellen Nähe zu bekannten Agent-Architekturen. Ohne klare Regeln steigt das Risiko für semantische Kopien, technische Fremdabhängigkeit und inkonsistente Entscheidungen.

## Entscheidung
Wir erzwingen architekturelle Eigenständigkeit über folgende Regeln:
1. Layer-Verträge sind strikt (Presentation -> Application -> Domain/Ports; Infrastructure implementiert Ports).
2. Namensraum und Begriffe sind projektspezifisch (`Genie`, `BeastwareTeam`, eigene Begriffe).
3. Externe Repos dienen nur als Benchmark; Übernahmen erfolgen ausschließlich als abstrahierte Patterns mit ADR-Verweis.
4. Jede größere Designentscheidung erhält ein ADR.

## Konsequenzen
- Höherer Initialaufwand, dafür bessere Wartbarkeit und IP-Klarheit.
- Reviews werden strikter, aber objektiver.
- Team kann schneller skalieren, weil Entscheidungslogik dokumentiert ist.
