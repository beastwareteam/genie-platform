---
icon: material/tune
---
# Config
<!-- erzeugt: typenkatalog — nicht von Hand aendern -->


Wenn Einstellungen oder Profile der Plattform selbst bearbeitet werden.

5 Bausteine.

## benchmark_runner

Benchmark-Runner: führt die konfigurierten Vergleichsziele über die Compute-Ebene aus (config.benchmark.run) und zeigt den aggregierten Report (tok/J, Energie, Latenz) als Tabelle — Strang A3/V1.

| Merkmal | Wert |
| --- | --- |
| Bereich | Benchmark/Compute |
| Konfigurierbar | nein |

## config_panel

Profil-Verwaltung: 6 Profil-Typen, Tree-View, CRUD, Export/Import, Domain-Regeln.

| Merkmal | Wert |
| --- | --- |
| Bereich | Profil/Konfiguration |
| Konfigurierbar | nein |

## factory_settings_panel

Factory-Edge-Defaults: feste Token-Teilmenge (LLM/Konstruktion/Compute) mit Fabrik-Ereignis beim Schreiben — eigener Typ, damit weder Token-Filter noch emit_factory_event ins LLM-Spec-Schema wandern.

| Merkmal | Wert |
| --- | --- |
| Bereich | Profil/Konfiguration |
| Konfigurierbar | nein |

## settings_panel

AppSettings-Editor: alle 108 Felder kategorisiert, Inline-Validierung, Reset-Funktion.

| Merkmal | Wert |
| --- | --- |
| Bereich | Profil/Konfiguration |
| Konfigurierbar | nein |

## settings_quicklink

Deep-Link/Modal-Sprung zu einem Konfig-Modul (config.module.open) — in jeder Gene-Spec deklarierbar, kein eigener Editor (Strang A).

| Merkmal | Wert |
| --- | --- |
| Bereich | Profil/Konfiguration |
| Konfigurierbar | nein |
