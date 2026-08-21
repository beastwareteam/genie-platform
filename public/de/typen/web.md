---
icon: material/web
---
# Web
<!-- erzeugt: typenkatalog — nicht von Hand aendern -->


Wenn der Inhalt aus dem Netz kommt und eine Webseite oder Suche bleiben soll.

6 Bausteine.

## browser

Multi-Tab-Browser: kombinierte URL/Suche, Network Buddy Sidebar, SMB/Intranet-Unterstützung, Fritz!Box-Integration, Domain-Filter. Lazy QWebEngineView — kein separater Prozess.

**Wann nehme ich es?** Wenn im Gen **gesurft** wird: eigene Tabs, Adresszeile, Verlauf. Geht es nur um Suchergebnisse, ist `search_filter`/`search_browser` gemeint.

| Merkmal | Wert |
| --- | --- |
| Bereich | Netzwerk/Browser |
| Konfigurierbar | nein |

## contacts

Kontakte/Absenderlisten: lokale Kontaktverwaltung (anlegen/bearbeiten/löschen) plus Absender-Import aus dem Posteingang — Phase D.

| Merkmal | Wert |
| --- | --- |
| Bereich | Kommunikation |
| Konfigurierbar | nein |

## email_manager

E-Mail-Verwaltung: Posteingang, Lesen, Löschen, Verfassen/Senden über echten IMAP/SMTP-Dienst (EmailService via CredentialStore) — Cut E1.

| Merkmal | Wert |
| --- | --- |
| Bereich | Kommunikation |
| Konfigurierbar | nein |

## search_browser

Kombinierter Such-Gene + Browser im Split View: Links Suchergebnisse (Bing RSS), rechts QWebEngineView mit Bildern + JS.

| Merkmal | Wert |
| --- | --- |
| Bereich | Netzwerk/Browser |
| Konfigurierbar | nein |

## search_filter

Gefilterter Such-Gene: DDG/Brave, Domain-Filter, SafeWebFetcher-Inhalt, Profil-Dropdown.

**Wann nehme ich es?** Wenn gesucht wird und die **Trefferliste** das Ergebnis ist — mit Domain-Filter, ohne eingebettete Seitenansicht (die hat `search_browser`).

| Merkmal | Wert |
| --- | --- |
| Bereich | Netzwerk/Browser |
| Konfigurierbar | nein |

## web_research

Web-Recherchekarte: Suche + Lesemodus-Abruf mit vollständiger Quellenangabe; vom Betreiber ausgeschlossene Domains sind sichtbar und pro Domain übersteuerbar.

| Merkmal | Wert |
| --- | --- |
| Bereich | Recherche |
| Konfigurierbar | nein |
