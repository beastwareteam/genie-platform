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

## Server-Mode (lokal)
```bash
python -m genie.main --server --host 127.0.0.1 --port 8765
```
- Health: `GET /health`
- Prompt: `POST /prompt` mit JSON `{ "prompt": "..." }`

## Architektur-Check (One Command)
```bash
python -m genie.dev.architecture_check
```
Nach `pip install -e .[dev]` alternativ:
```bash
genie-architecture-check
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

## Architektur-Fokus (aktuelle Priorität)
- Zielarchitektur: `docs/architecture/TARGET_ARCHITECTURE.md`
- Struktur-Blueprint: `docs/architecture/STRUCTURE_BLUEPRINT.md`
- Migrationsphasen: `docs/architecture/MIGRATION_PHASES.md`

## Namensneutralisierung
Legacy-/Fremdbezeichnungen wurden nicht übernommen. Der zentrale Agent-Name ist `Genie`.
