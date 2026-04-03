# Watchlist (Parallelprojekte)

## 1) DonutShinobu/claude-code-fork
- URL: https://github.com/DonutShinobu/claude-code-fork
- Letzter bekannter Commit: `a99de1bb3c0c301b83b784abbcdb7a3674b2cd45` (2026-03-31)
- Scope-Hinweis: Snapshot-basierter Fork mit Fokus auf Analyse/Refactor

### Beobachtungspunkte (2-wöchentlich)
1. Architektur-Layering (Entrypoints, Orchestrator, Query-Kern)
2. Tool-/Task-Registry-Design
3. Plugin/MCP-Integrationsmuster
4. Stabilitäts-/Build-Strategien
5. Relevante Refactor-Patterns für Genie Platform

### Schnellprüfung
```bash
git ls-remote https://github.com/DonutShinobu/claude-code-fork.git HEAD
```

### Übernahme-Regel für BeastwareTeam
- Nur Patterns/Architekturideen übernehmen, keine 1:1-Namens- oder Strukturkopien.
- Jede Übernahme in eigenem ADR dokumentieren (`docs/adr/`).
