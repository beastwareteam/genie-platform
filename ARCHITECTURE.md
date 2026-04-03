# Genie Platform Architektur (OOP, neutralisiert)

## Leitprinzipien
- Agent-Name: **Genie**
- Organisation: **BeastwareTeam**
- Strikte Layering-Regeln (kein direkter UI -> Infra Zugriff)
- Registry-Pattern für Commands/Tools/Tasks
- **Interface-First:** Alle Konsumenten nutzen nur application/interfaces
- **Domain-Freeze:** Domain bleibt während Interface-Aufbau read-only

## Mermaid

\\\mermaid
graph TD
  A[main.py] --> B[app/bootstrap.py]
  B --> C[app/container.py]
  C --> D[presentation/viewmodels/MainViewModel]
  C --> E[application/query_engine/QueryEngine]
  C --> F[application/task_orchestrator/TaskOrchestrator]
  C --> G[runtime/tools/ToolRegistry]
  C --> H[runtime/tasks/TaskRegistry]
  C --> I[runtime/event_bus/EventBus]
  C --> J[runtime/feature_flags/FeatureFlags]
  C --> K[shared/config/AppSettings]

  L[presentation/views/MainWindow] --> D
  D --> E
  D --> I

  E --> G
  F --> H

  G --> P[domain/ports/ToolPort]
  H --> Q[domain/ports/TaskPort]
\\\

## Layer-Vertrag
1. \presentation\ kennt nur \pplication/interfaces\ und \untime/event_bus\ (Interface-First)
2. \pplication/interfaces\ definiert reine Protocols (keine Implementierung)
3. \pplication/facade\ implementiert Interfaces und orchestriert QueryEngine + TaskOrchestrator
4. \pplication\ kennt \domain\ Ports + \untime\ Registries (aber Domain ist READ-ONLY / Frozen)
5. \infrastructure\ implementiert \domain\ Ports und ist agnostisch gegenüber Presentation
6. \shared\ ist nur Utility/Config, ohne Business-Logik

## Interface-First Architektur (NEU)

**Zwei klare Schnitte:**
- **Schnitt 1:** Presentation/Edge <--> \pplication/interfaces/*\ (Service-Fassade)
- **Schnitt 2:** Orchestration <--> Domain (Domain bleibt READ-ONLY/Frozen)

**Neue Schichten:**
- \pplication/interfaces/\ — abstrakte Service-Contracts (ChatService, TaskService, SessionService)
- \pplication/facade/\ — konkrete Service-Implementierung und Orchestration-Zentrum
- \infrastructure/server/\ — Server-Edge als alternativer Adapter gegen Facade-Interfaces

**Domain-Freeze aktiv:**
- Domain-Logik, Entities, Policies werden nicht erweitert
- Nur lesender Zugriff gestattet
- Freeze läuft bis Interface-Contract 2 Sprints grün läuft
