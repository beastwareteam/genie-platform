---
icon: material/desktop-tower-monitor
---
# System
<!-- erzeugt: typenkatalog — nicht von Hand aendern -->


Wenn der Zustand des Rechners oder der Plattform beobachtet oder gesteuert wird.

23 Bausteine.

## agents_panel

Agenten-Übersicht: registrierte Agenten, Werkzeuge und Ausführungs-Status — Gene-Transfer des Agenten-Moduls (SP3 Welle 2).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## autostart_governor

Autostart-Governor: Read-only Übersicht plus Ausführen/Aktivieren/Deaktivieren/Entfernen je Autostart-Eintrag (Registry-Run-Keys + Startup-Ordner) — descriptor-getriebener Governor-Kern über den AutostartInfoPort + ResourceControlService (SYSGOV W3c).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## files_panel

Dateiverwaltung: Verzeichnisbaum, Suche und Datei-Operationen — Gene-Transfer des Datei-Moduls (SP3 Welle 3).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## firewall_governor

Firewall-Governor: alle Regeln der Betriebssystem-Firewall mit Zustand, Wirkung (zulassen/blockieren), Richtung, betroffenem Programm und Profil — plus Ein-/Ausschalten und Löschen über den descriptor-getriebenen Governor-Kern. Jede Regel wird über ihre eindeutige Kennung angesprochen, nicht über den mehrfach vergebenen Anzeigenamen; vor jedem Löschen wird die Richtlinie gesichert (SYSGOV W4/N3).

**Wann nehme ich es?** Wenn eine Regel der Windows-Firewall gesucht, geschaltet oder entfernt werden soll — etwa weil ein Programm nicht ins Netz kommt oder eine Block-Regel übrig blieb. Gemeint ist die Firewall des BETRIEBSSYSTEMS; Genies eigene Browser-Firewall (Seiten erlauben/sperren) liegt im Browser-Gene und hat mit diesem Typ nichts zu tun.

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## fritzbox_status

Zustand der Fritz!Box: erreichbar, gesendetes/empfangenes Volumen, Zahl der ihr bekannten Geräte, Weg in die Box-Oberfläche.

**Wann nehme ich es?** Wenn die Box selbst gemeint ist. Die Geräte des ganzen Netzes zeigt `network_devices` — dessen Zahl ist grösser, weil sie ARP-Funde einschliesst.

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## gene_browser_panel

Gen-Katalog: durchsuchen, verbessern, ableiten — Gene-Transfer des Gen-Browsers (SP3 Welle 3).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## learning_panel

Lern-Modul: Feedback, Wissensstand, Einbettungs-Vergleich und Gen-Lücken — Gene-Transfer des Lern-Moduls (SP3 Welle 3).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## library_panel

Gene-Bibliothek: gespeicherte Gene laden, verwalten, als Favorit merken — Gene-Transfer der Bibliothek (SP3 Welle 4).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## monitoring_panel

System-Monitoring: Metriken, Health-Status, Live-Events und LLM-Diagnostik — Gene-Transfer des Monitoring-Moduls (SP3 Welle 1).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## network_adapter_governor

Netzwerkadapter-Governor: Zustand, IP-Adresse, Herkunft, DNS, Gateway und Vorrang je Adapter — plus Aktivieren/Deaktivieren/Erneuern/Automatik/DNS-Wahl/Metrik über den descriptor-getriebenen Governor-Kern (SYSGOV W4).

**Wann nehme ich es?** Wenn ein Adapter eingestellt oder geschaltet werden soll — abschalten, auf automatisch stellen, DNS wechseln, Vorrang ändern. Nur zum Zusehen (Durchsatz, offene Verbindungen) ist `network_monitor` richtig; für die anderen Geräte im Netz `network_devices`.

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## network_devices

Geräte im eigenen Netz: ARP-Funde, Fritz!Box-Geräte und wiedererkannte Offline-Geräte — mit Icon/Name je Gerät und Doppelklick auf die Admin-Seite.

**Wann nehme ich es?** Wenn es um die anderen Geräte im Netz geht. Für den eigenen Rechner (Interfaces, offene Verbindungen, DNS) ist `network_monitor` richtig.

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Gibt weiter | device |
| Konfigurierbar | nein |

## network_diagnostics

Netzwerk-Diagnose: misst Gateway-Latenz und Paketverlust, jeden DNS-Server einzeln, den Weg nach draußen, die Pfad-MTU und die eigenen aus dem Netz erreichbaren Dienste — je Befund Messwert, Deutung und Vorschlag (SYSGOV W4).

**Wann nehme ich es?** Wenn etwas nicht stimmt und die Ursache gesucht wird — langsam, bricht ab, manchmal geht nichts. Für den laufenden Zustand ist `network_monitor` richtig, zum Einstellen `network_adapter_governor`.

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## network_monitor

Read-only Netz-Übersicht: Interfaces, aktive Verbindungen, DNS und Gateway — selbst-aktualisierend über den NetworkInfoPort (SYSCTL S2).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## plugins_panel

Plugin-Verwaltung: Registry, Hot-Reload und Beiträge — Gene-Transfer des Plugin-Moduls (SP3 Welle 3).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## process_governor

Prozess-Governor: Read-only Übersicht plus admin-gated Beenden/Hart beenden/Anhalten/Fortsetzen/Priorität je Prozess — descriptor-getriebener Governor-Kern über den ProcessInfoPort + ResourceControlService (SYSGOV W2).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## service_governor

Dienste-Governor: Read-only Übersicht plus admin-gated Start/Stop/Neu starten je Dienst — descriptor-getriebener Governor-Kern über den ServiceInfoPort + ResourceControlService (SYSGOV W1).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## service_monitor

Read-only Dienste-Übersicht: Name, Status, Starttyp und PID der OS-Dienste — selbst-aktualisierend über den ServiceInfoPort (SYSCTL S3).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## system_monitor

Read-only System-Übersicht: CPU, Arbeitsspeicher, Datenträger, Netzwerk und Top-Prozesse — selbst-aktualisierend über den SystemInfoPort (SYSCTL S1b).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## system_panel

Systempanel: alle System-Module (Monitoring, Agents, Workflows, …) in einem Panel — Navigation links, lazy Modul-Inhalt rechts. Ersetzt den Entwickler-Tabmodus.

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## task_governor

Aufgaben-Governor: Read-only Übersicht plus admin-gated Ausführen/Beenden/Aktivieren/Deaktivieren/Entfernen je geplanter Aufgabe — descriptor-getriebener Governor-Kern über den TaskInfoPort + ResourceControlService (SYSGOV W3a).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## user_buttons_panel

Aktions-Knöpfe verwalten: Palette, Reihenfolge und Eigenschaften — Gene-Transfer der Knopf-Verwaltung (SP3 Welle 3).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## workflows_panel

Workflow-Verwaltung: Definitionen, Läufe und Schritt-Status — Gene-Transfer des Workflow-Moduls (SP3 Welle 2).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |

## wse_panel

Workflow-Stage-Engine: Stufen, Läufe und Rückmeldungen — Gene-Transfer des WSE-Moduls (SP3 Welle 3).

| Merkmal | Wert |
| --- | --- |
| Bereich | Systempanel |
| Konfigurierbar | nein |
