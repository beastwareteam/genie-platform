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

## Arbeitsmodell
- Team-Arbeitsweise: `WORKING_MODEL.md`
- Engineering-Checkliste: `docs/ENGINEERING_CHECKLIST.md`
- Architekturentscheidungen: `docs/adr/`
- PR-Gates: `.github/PULL_REQUEST_TEMPLATE.md`

## Namensneutralisierung
Legacy-/Fremdbezeichnungen wurden nicht übernommen. Der zentrale Agent-Name ist `Genie`.
