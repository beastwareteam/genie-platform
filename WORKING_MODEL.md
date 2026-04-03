# Working Model für BeastwareTeam (Genie Platform)

## Ziel
Eigenständige Produktentwicklung mit professioneller OOP-Struktur, ohne Namens- und Konzeptkopie aus Fremdprojekten.

## Arbeitsweise (verbindlich)
1. Architekturänderungen laufen nur über ADR (ein Entscheid pro ADR).
2. Jede neue Funktion startet mit einem Use-Case in `application/use_cases`.
3. UI (`presentation`) darf keine Infrastruktur direkt aufrufen.
4. Externe Impulse aus der Watchlist sind nur Pattern-Inspiration, keine 1:1-Übernahme.
5. Architekturregeln aus `docs/architecture/TARGET_ARCHITECTURE.md` sind verbindlich.

## Sprint-Rhythmus
- Woche 1: Kernfunktion (Use-Case + Domain + Tests)
- Woche 2: UI-Integration + Infrastrukturadapter + Härtung
- Wöchentlich: 1 Watchlist-Review, max. 2 übernommene Ideen mit ADR-Bezug

## Definition of Done
- Unit-Tests für neue Domain-/Application-Logik
- Keine Layer-Verletzung
- Keine Legacy-/Fremdnamen in neuen Dateien
- ADR aktualisiert, wenn sich Architektur oder Schnittstellen verändern
