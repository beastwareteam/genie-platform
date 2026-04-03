# Migrationsphasen zur Zielstruktur

Neue Priorisierung: Interface-First mit Domain-Freeze

## Phase 0 – Interface-Aufbau (JETZT / nächste 2 Sprints)
Neue Priorität: Schnitt 1 (Edge <--> Interfaces) stabilisieren, Domain bleibt frozen.

1. **Freeze-Regel in Commit-Checklist** – Domain-Änderungen manuell validieren
2. **Interfaces definieren** – ChatService, TaskService, SessionService als reine Protocols in application/interfaces/
3. **Facade aufbauen** – Implementierung in application/facade/ mit Orchestration
4. **ViewModel entkoppeln** – viewmodels konsumieren nur Interfaces, nie direkt QueryEngine
5. **Container-Wiring trennen** – separate DI-Profile für Core-Komposition und Edge-Komposition
6. **Server-Edge vorbereiten** – HTTP/WebSocket-Adapter gegen Facade-Interfaces
7. **Quality Gates aktivieren** – Interface-Contract-Tests, Linter-Regel für Edge->Interfaces
8. **Review** – Architektur-Review: Interface-Contract stabil?

## Phase A – Architektur-Härtung (nach Phase 0)
- Schichten und Regeln in Doku fixieren
- Leere Zielordner vollständig anlegen
- Basisklassen/Interfaces pro Schicht definieren

## Phase B – Kernlogik zuerst (nach Phase A)
- QueryEngine und TaskOrchestrator stabilisieren
- Use-Case-Schablonen einführen
- Domain-Policies und Value Objects ergänzen (Freeze aufgehoben)

## Phase C – Adapterisierung (nach Phase B)
- Infrastrukturzugriffe hinter Ports ziehen
- MCP/API/Persistenz-Adapter separieren
- Fehler- und Retry-Strategien zentralisieren

## Phase D – UI-Professionalisierung (nach Phase C)
- ViewModels vereinheitlichen
- UI nur an Interfaces + EventBus koppeln
- Konsistente Dialog-/Widget-Patterns

## Phase E – Stabilität (nach Phase D)
- Unit + Integration Tests schrittweise erhöhen
- Architekturverletzungen regelmäßig prüfen
- Performance/Profiling in Runtime-Hotpaths

## Priorität für nächsten Sprint
**Phase 0 Schritte 1-5** – Interface-Aufbau greift Schnitt 1 direkt auf
