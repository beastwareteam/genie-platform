---
icon: material/cog
---
# Worauf die Plattform steht

Diese Seite beantwortet eine Frage, die man selten gestellt bekommt und immer haben will:
**womit ist das hier eigentlich gebaut?**

Zwei Dinge vorweg, weil sie den Rest lesbar machen:

- **Das Wichtigste läuft auf Ihrem Rechner.** Sprachmodelle, Sprachausgabe, Texterkennung,
  Datenbank — alles davon hat einen örtlichen Weg. Dienste im Netz sind eine Wahl, kein Zwang,
  und jeder von ihnen braucht einen Schlüssel, den Sie selbst eintragen.
- **Nicht jede Technologie hat hier ein Zeichen.** Wo es kein Herstellerlogo gibt oder wir
  keines zeigen dürfen, steht ein schlichtes Ersatzsymbol — und es ist als solches
  gekennzeichnet. Ein generisches Symbol, das wie ein Herstellerlogo aussieht, wäre eine
  Behauptung ohne Deckung.

<!-- erzeugt: technologien — nicht von Hand aendern -->

## Die Sprache selbst und was sie zum Laufen braucht

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/python.png"><img src="../../assets/icons/technologie/raster/python_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Python** | Die Sprache, in der die gesamte Plattform geschrieben ist. Mindestens 3.12, im Betrieb 3.13. |

## Fenster, Bausteine, Symbole, eingebettetes Web

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/pyside6.png"><img src="../../assets/icons/technologie/raster/pyside6_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **PySide6 (Qt for Python)** | Jedes Fenster, jeder Baustein, jede Animation — die gesamte Oberfläche steht darauf. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/qtwebengine.png"><img src="../../assets/icons/technologie/raster/qtwebengine_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **QtWebEngine (Chromium)** *(Ersatzsymbol)* | Der eingebettete Browser: Web-Ansichten, Browser-Bausteine, Wiedergabe geschützter Inhalte. |
| | *3 weitere Hilfsbibliotheken* | arbeiten hier mit, ohne ein eigenes Zeichen zu führen |

## Sprach- und Bildmodelle, örtlich wie entfernt

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/lm-studio.png"><img src="../../assets/icons/technologie/raster/lm-studio_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **LM Studio** *(Ersatzsymbol)* | Der örtliche Modellserver — Standardweg für jede Anfrage an ein Sprachmodell. Nichts verlässt den Rechner. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/ollama.png"><img src="../../assets/icons/technologie/raster/ollama_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Ollama** *(Ersatzsymbol)* | Zweiter örtlicher Modellserver, alternativ zu LM Studio. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/openai-api.png"><img src="../../assets/icons/technologie/raster/openai-api_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **OpenAI-API** *(Ersatzsymbol)* | Entfernter Modellweg — nur mit eigenem Schlüssel, nie ab Werk. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/stable-diffusion.png"><img src="../../assets/icons/technologie/raster/stable-diffusion_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Stable Diffusion** *(Ersatzsymbol)* | Bilderzeugung über eine örtlich laufende Instanz. |

## Vorlesen, Zuhören, Übersetzen

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/libretranslate.png"><img src="../../assets/icons/technologie/raster/libretranslate_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **LibreTranslate** *(Ersatzsymbol)* | Übersetzung im Chat-Fenster — der erste von drei Wegen. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/piper.png"><img src="../../assets/icons/technologie/raster/piper_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Piper** *(Ersatzsymbol)* | Örtliche Sprachausgabe: liest Antworten vor, ohne ins Netz zu gehen. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/whisper.png"><img src="../../assets/icons/technologie/raster/whisper_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Whisper** *(Ersatzsymbol)* | Spracherkennung für Diktat und Ton-Dateien. |
| | *4 weitere Hilfsbibliotheken* | arbeiten hier mit, ohne ein eigenes Zeichen zu führen |

## Absicht erkennen, Eingaben korrigieren

3 weitere Hilfsbibliotheken arbeiten hier, ohne ein eigenes Zeichen zu führen.

## Bildschirm abgreifen, Text und Objekte erkennen

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/numpy.png"><img src="../../assets/icons/technologie/raster/numpy_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **NumPy** | Zahlenfelder für Bild- und Tonverarbeitung. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/opencv-python.png"><img src="../../assets/icons/technologie/raster/opencv-python_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **OpenCV** | Bildverarbeitung: Vorlagen auf dem Bildschirm finden, zuschneiden, für die Texterkennung vorbereiten. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/tesseract.png"><img src="../../assets/icons/technologie/raster/tesseract_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Tesseract OCR** *(Ersatzsymbol)* | Texterkennung im Bild — die zweite Stufe der Erkennungskette. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/ultralytics.png"><img src="../../assets/icons/technologie/raster/ultralytics_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Ultralytics YOLO** *(Ersatzsymbol)* | Objekterkennung auf dem Bildschirm, samt eigenem Training dafür. |
| | *8 weitere Hilfsbibliotheken* | arbeiten hier mit, ohne ein eigenes Zeichen zu führen |

## Dateien lesen, speichern, recherchieren

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/duckduckgo.png"><img src="../../assets/icons/technologie/raster/duckduckgo_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **DuckDuckGo** *(Ersatzsymbol)* | Web-Recherche ohne Schlüssel — der Standardweg der Suche. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/json.png"><img src="../../assets/icons/technologie/raster/json_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **JSON** | Konfiguration, Belege, Verzeichnisse, Sitzungszustand. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/markdown.png"><img src="../../assets/icons/technologie/raster/markdown_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Markdown** | Jede Dokumentation, jede öffentliche Seite, jeder Baustein-Steckbrief. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/nominatim.png"><img src="../../assets/icons/technologie/raster/nominatim_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Nominatim (OpenStreetMap)** *(Ersatzsymbol)* | Ortsnamen zu Koordinaten — für Wetter, Zeitzone und Karten. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/pyyaml.png"><img src="../../assets/icons/technologie/raster/pyyaml_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **PyYAML** | Liest die Baustein-Beschreibungen und die Konfiguration der Plattform. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/sqlite.png"><img src="../../assets/icons/technologie/raster/sqlite_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **SQLite** | Der örtliche Speicher: Bausteine, Versionen, Lernstand, Aufnahmen. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/wikipedia.png"><img src="../../assets/icons/technologie/raster/wikipedia_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Wikipedia** *(Ersatzsymbol)* | Nachschlagewerk für Sachfragen im Chat. |
| | *5 weitere Hilfsbibliotheken* | arbeiten hier mit, ohne ein eigenes Zeichen zu führen |

## Ton, Video, Streams

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/ffmpeg.png"><img src="../../assets/icons/technologie/raster/ffmpeg_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **FFmpeg** *(Ersatzsymbol)* | Spuren zusammenführen, umwandeln, Ton aus Video ziehen. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/vlc.png"><img src="../../assets/icons/technologie/raster/vlc_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **VLC / libVLC** *(Ersatzsymbol)* | Der Abspieler für Video und Ton, wo der eingebaute Weg nicht trägt. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/yt-dlp.png"><img src="../../assets/icons/technologie/raster/yt-dlp_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **yt-dlp** *(Ersatzsymbol)* | Findet die abspielbaren Fassungen eines Videos und lädt die passende. |
| | *2 weitere Hilfsbibliotheken* | arbeiten hier mit, ohne ein eigenes Zeichen zu führen |

## E-Mail, Anmeldung, fremde Konten

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/google-oauth.png"><img src="../../assets/icons/technologie/raster/google-oauth_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Google-Anmeldung (OAuth 2.0)** | „Mit Google anmelden“ für E-Mail und Kontakte. Die Schlüssel bleiben auf Ihrem Rechner. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/imap.png"><img src="../../assets/icons/technologie/raster/imap_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **IMAP** *(Ersatzsymbol)* | Postfächer lesen, Ordner verwalten, Nachrichten verschieben. |
| | *1 weitere Hilfsbibliothek* | arbeiten hier mit, ohne ein eigenes Zeichen zu führen |

## Prozesse, Dienste, Geräte, Eingabe-Automation

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/windows-api.png"><img src="../../assets/icons/technologie/raster/windows-api_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Windows** | Das Betriebssystem, auf dem die Plattform entwickelt und betrieben wird — Dienste, Registrierung, Aufgabenplanung. |
| | *4 weitere Hilfsbibliotheken* | arbeiten hier mit, ohne ein eigenes Zeichen zu führen |

## Tests, Typen, Stilprüfung

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/mypy.png"><img src="../../assets/icons/technologie/raster/mypy_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **mypy** *(Ersatzsymbol)* | Prüft die Typen im Quelltext, bevor ein Fehler im Betrieb auftreten kann. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/pytest.png"><img src="../../assets/icons/technologie/raster/pytest_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **pytest** | Der automatische Prüfstand: rund 9400 Prüfungen über alle Bereiche der Plattform. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/ruff.png"><img src="../../assets/icons/technologie/raster/ruff_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Ruff** *(Ersatzsymbol)* | Prüft den Quelltext auf Stil und Fallstricke — 14 Regelfamilien, bei jeder Änderung. |
| | *8 weitere Hilfsbibliotheken* | arbeiten hier mit, ohne ein eigenes Zeichen zu führen |

## Verpacken, Ausliefern, Werkzeuge am Baum

| | Technologie | Wofür |
| --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/git.png"><img src="../../assets/icons/technologie/raster/git_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **Git** | Versionsverwaltung: jede Änderung ist nachvollziehbar und umkehrbar. |
| <picture><source media="(prefers-color-scheme: dark)" srcset="../../assets/icons/technologie/raster/github.png"><img src="../../assets/icons/technologie/raster/github_hell.png" alt="" role="presentation" width="28" height="28"></picture> | **GitHub** | Der öffentliche Ort des Quelltexts — und ein Zugang für Entwickler-Bausteine. |
| | *3 weitere Hilfsbibliotheken* | arbeiten hier mit, ohne ein eigenes Zeichen zu führen |

<!-- ende: technologien -->

## Warum manche Zeilen kein Zeichen tragen

Rund vierzig Hilfsbibliotheken arbeiten hier mit, ohne in der Tabelle aufzutauchen: Zeichensätze
erkennen, Tabellen lesen, Ton entschlüsseln, Zeitzonen kennen. Sie bekommen keine eigene Zeile,
weil eine Reihe aus dreißig gleich aussehenden Platzhaltern nichts erklärt — die Zahl am Ende
jedes Bereichs sagt, wie viele es sind.

Vollständig aufgeführt sind sie trotzdem: die Plattform führt über jede verwendete Technologie
Buch, samt Herkunft, Lizenz und Markeninhaber jedes gezeigten Zeichens.

## Ein Wort zu den Zeichen

Die Herstellerzeichen stammen aus einer frei lizenzierten Sammlung. Das gilt für die
**Sammlung** — die Zeichen darin sind Marken ihrer Inhaber. Wir zeigen sie unverändert:

| Angepasst wurde | Unberührt blieb |
| --- | --- |
| die Zeichenfläche — alle gleich groß | Farben |
| der Abstand zum Rand — überall derselbe | Formen |
| die Strichstärke der **Ersatzsymbole** | Seitenverhältnisse und Schriftzüge |

Ein Markenzeichen wird auch dann nicht umgefärbt, wenn es farblich nicht zum gewählten Thema
passt. Das ist keine Nachlässigkeit, sondern die Regel: viele Markenrichtlinien verbieten genau
das.

---

Die Tabelle oben wird aus dem Technologie-Verzeichnis der Plattform **erzeugt**
(`scripts/technologie_abdeckung.py --seite`). Sie kann deshalb nicht veralten, ohne dass es
auffällt.
