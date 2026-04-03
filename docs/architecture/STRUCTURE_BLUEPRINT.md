# Struktur-Blueprint (konkret)

## Soll-Dateibaum

```text
src/genie/
  app/
    bootstrap.py
    container.py
    lifecycle.py
  presentation/
    views/
    viewmodels/
    widgets/
  application/
    use_cases/
    commands/
    query_engine/
    task_orchestrator/
  domain/
    entities/
    value_objects/
    services/
    ports/
    policies/
  infrastructure/
    api_clients/
    mcp/
    persistence/
    plugins/
    telemetry/
  runtime/
    tools/
    tasks/
    hooks/
    event_bus/
    feature_flags/
  shared/
    config/
    logging/
    errors/
    typing/
```

## Modul-Kontrakte
- use_cases: je Use-Case eine Klasse mit `execute()`.
- query_engine: turn-basierte Konversationsorchestrierung.
- task_orchestrator: Task-Lifecycle und Delegation.
- ports: reine Protocols/ABCs ohne Implementierungsdetails.
- infrastructure/*: Adapter, die Ports implementieren.

## Minimale Qualitätskriterien
- Jede neue Feature-Implementierung enthält:
  1) Use-Case
  2) Domain-Model/Policy (falls fachlich relevant)
  3) Adapter oder Stub-Adapter
  4) Unit-Tests

## Reihenfolge für Ausbau
1. domain + application vervollständigen
2. infrastructure adapterisieren
3. presentation über viewmodels stabil anbinden
4. runtime hooks und tool/task-pipeline ausbauen
