# Genie Platform (BeastwareTeam)

Dieses Projekt ist ein neuer, neutralisierter PySide6-Startpunkt mit vollständig objektorientierter Struktur.

## Ziele
- neutrale Namensgebung (Agent: `Genie`)
- professionelle Layer-Architektur (Presentation/Application/Domain/Infrastructure/Runtime)
- klare Registries für Commands, Tools und Tasks

## Start
```bash
pip install -e .[dev]
python -m genie.main
```

## Struktur
- `src/genie/app`: Bootstrap, DI-Container, Lifecycle
- `src/genie/presentation`: PySide6 Views + ViewModels
- `src/genie/application`: Use-Cases, QueryEngine, Command-Logik
- `src/genie/domain`: fachliche Modelle + Port-Interfaces
- `src/genie/infrastructure`: Adapter (API, MCP, Persistenz, Plugins)
- `src/genie/runtime`: Tools, Tasks, Hooks, EventBus, FeatureFlags
- `src/genie/shared`: Config, Logging, Errors, Typing

## Namensneutralisierung
Legacy-/Fremdbezeichnungen wurden nicht übernommen. Der zentrale Agent-Name ist `Genie`.
