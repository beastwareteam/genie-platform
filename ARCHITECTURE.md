# Genie Platform Architektur (OOP, neutralisiert)

## Leitprinzipien
- Agent-Name: **Genie**
- Organisation: **BeastwareTeam**
- Strikte Layering-Regeln (kein direkter UI -> Infra Zugriff)
- Registry-Pattern für Commands/Tools/Tasks

## Mermaid

```mermaid
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
```

## Layer-Vertrag
1. `presentation` kennt nur `application` und `runtime/event_bus`
2. `application` kennt `domain` Ports + `runtime` Registries
3. `infrastructure` implementiert `domain` Ports
4. `shared` ist nur Utility/Config, ohne Business-Logik
