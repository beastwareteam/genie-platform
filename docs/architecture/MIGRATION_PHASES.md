# Migrationsphasen zur Zielstruktur

## Phase A – Architektur-Härtung (jetzt)
- Schichten und Regeln in Doku fixieren.
- Leere Zielordner vollständig anlegen.
- Basisklassen/Interfaces pro Schicht definieren.

## Phase B – Kernlogik zuerst
- QueryEngine und TaskOrchestrator stabilisieren.
- Use-Case-Schablonen einführen.
- Domain-Policies und Value Objects ergänzen.

## Phase C – Adapterisierung
- Infrastrukturzugriffe hinter Ports ziehen.
- MCP/API/Persistenz-Adapter separieren.
- Fehler- und Retry-Strategien zentralisieren.

## Phase D – UI-Professionalisierung
- ViewModels vereinheitlichen.
- UI nur an Application + EventBus koppeln.
- Konsistente Dialog-/Widget-Patterns.

## Phase E – Stabilität
- Unit + Integration Tests schrittweise erhöhen.
- Architekturverletzungen regelmäßig prüfen.
- Performance/Profiling in Runtime-Hotpaths.

## Priorität für den nächsten Sprint
1. `application/use_cases` konkret füllen
2. `domain/policies` ergänzen
3. erster Infrastrukturadapter über Port anbinden
