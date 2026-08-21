# Herkunft der Technologie-Zeichen

> **Warum diese Datei Pflicht ist und nicht Beiwerk.** Devicon ist MIT-lizenziert — das gilt für
> die *Sammlung*. Die **Zeichen darin sind Marken ihrer Inhaber**, und eine Marke wird nicht
> mitlizenziert, nur weil die Datei, in der sie liegt, es ist. Wer das nicht festhält, kann später
> nicht belegen, unter welcher Erlaubnis ein Zeichen hier liegt.

Diese Datei nennt je Bestandteil: **Quelle**, **Lizenz der Datei**, **Inhaber des Zeichens**.

## Was hier liegt

| Datei | Quelle | Lizenz der Datei | Inhaber des Zeichens |
|---|---|---|---|
| `devicon_index.json` | [devicon.json](https://raw.githubusercontent.com/devicons/devicon/master/devicon.json), Stand 2026-08-20 | MIT (Devicon) | — (nur Namen, Farbwerte und Fassungsliste; **keine** Zeichen) |

Der Index enthält **keine Grafik**. Er ist die verkleinerte Namensliste, an der
`scripts/technologie_abdeckung.py` misst, ob es für eine Technologie überhaupt ein Zeichen gibt —
ohne Netzzugang, damit der Befund an zwei Tagen derselbe ist.

## Regeln für Ergänzungen

| Regel | Grund |
|---|---|
| Kein Zeichen ohne Zeile in dieser Tabelle | Sonst ist die Erlaubnis, unter der es hier liegt, nicht mehr rekonstruierbar |
| Kein Zeichen aus unklarer Quelle | „Irgendwo gefunden" ist keine Herkunft |
| Ersatzsymbole (Lucide) werden **als Ersatz** geführt | Ein generisches Symbol, das wie ein Herstellerlogo aussieht, ist eine Behauptung ohne Deckung |
| Farben, Formen, Seitenverhältnisse und Schriftzüge bleiben unangetastet | Viele Markenrichtlinien verbieten das Umfärben ausdrücklich; vereinheitlicht wird nur die Zeichenfläche |

## Verwandte Stellen

- `docs/technologie_icons.json` — die **gepflegte** Zuordnung Technologie → Zeichen, mit Grund je
  bewusster Auslassung
- `docs/runtime/technologie_abdeckung.json` — der **gemessene** Stand (maschinell, nicht von Hand
  ändern)
- `assets/icons/lucide/` — die Ersatzsymbole (ISC-Lizenz, liegen seit jeher im Baum)

## Die Zeichen

<!-- ZEICHEN-TABELLE: erzeugt von scripts/technologie_icons_bauen.py -->

| Datei | Technologie | Quelle | Lizenz der Datei | Inhaber des Zeichens |
|---|---|---|---|---|
| `duckduckgo.svg` | DuckDuckGo | Lucide `search` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `ffmpeg.svg` | FFmpeg | Lucide `video` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `git.svg` | Git | Devicon `git` (`original`) | MIT (Devicon) | Git |
| `git_einfarbig.svg` | Git | Devicon `git` (`plain`) | MIT (Devicon) | Git |
| `github.svg` | GitHub | Devicon `github` (`original`) | MIT (Devicon) | GitHub |
| `google-oauth.svg` | Google-Anmeldung (OAuth 2.0) | Devicon `google` (`original`) | MIT (Devicon) | Google-Anmeldung (OAuth 2.0) |
| `google-oauth_einfarbig.svg` | Google-Anmeldung (OAuth 2.0) | Devicon `google` (`plain`) | MIT (Devicon) | Google-Anmeldung (OAuth 2.0) |
| `imap.svg` | IMAP | Lucide `mail` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `json.svg` | JSON | Devicon `json` (`original`) | MIT (Devicon) | JSON |
| `json_einfarbig.svg` | JSON | Devicon `json` (`plain`) | MIT (Devicon) | JSON |
| `libretranslate.svg` | LibreTranslate | Lucide `languages` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `lm-studio.svg` | LM Studio | Lucide `server` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `markdown.svg` | Markdown | Devicon `markdown` (`original`) | MIT (Devicon) | Markdown |
| `mypy.svg` | mypy | Lucide `type-outline` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `nominatim.svg` | Nominatim (OpenStreetMap) | Lucide `globe` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `numpy.svg` | NumPy | Devicon `numpy` (`original`) | MIT (Devicon) | NumPy |
| `numpy_einfarbig.svg` | NumPy | Devicon `numpy` (`plain`) | MIT (Devicon) | NumPy |
| `ollama.svg` | Ollama | Lucide `bot` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `openai-api.svg` | OpenAI-API | Lucide `brain` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `opencv-python.svg` | OpenCV | Devicon `opencv` (`original`) | MIT (Devicon) | OpenCV |
| `opencv-python_einfarbig.svg` | OpenCV | Devicon `opencv` (`plain`) | MIT (Devicon) | OpenCV |
| `piper.svg` | Piper | Lucide `volume-2` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `pyside6.svg` | PySide6 (Qt for Python) | Devicon `qt` (`original`) | MIT (Devicon) | PySide6 (Qt for Python) |
| `pytest.svg` | pytest | Devicon `pytest` (`original`) | MIT (Devicon) | pytest |
| `pytest_einfarbig.svg` | pytest | Devicon `pytest` (`plain`) | MIT (Devicon) | pytest |
| `python.svg` | Python | Devicon `python` (`original`) | MIT (Devicon) | Python |
| `python_einfarbig.svg` | Python | Devicon `python` (`plain`) | MIT (Devicon) | Python |
| `pyyaml.svg` | PyYAML | Devicon `yaml` (`original`) | MIT (Devicon) | PyYAML |
| `pyyaml_einfarbig.svg` | PyYAML | Devicon `yaml` (`plain`) | MIT (Devicon) | PyYAML |
| `qtwebengine.svg` | QtWebEngine (Chromium) | Lucide `globe` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `ruff.svg` | Ruff | Lucide `gauge` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `sqlite.svg` | SQLite | Devicon `sqlite` (`original`) | MIT (Devicon) | SQLite |
| `sqlite_einfarbig.svg` | SQLite | Devicon `sqlite` (`plain`) | MIT (Devicon) | SQLite |
| `stable-diffusion.svg` | Stable Diffusion | Lucide `image` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `tesseract.svg` | Tesseract OCR | Lucide `scan-text` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `ultralytics.svg` | Ultralytics YOLO | Lucide `eye` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `vlc.svg` | VLC / libVLC | Lucide `film` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `whisper.svg` | Whisper | Lucide `mic` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `wikipedia.svg` | Wikipedia | Lucide `book` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |
| `windows-api.svg` | Windows | Devicon `windows11` (`original`) | MIT (Devicon) | Windows |
| `yt-dlp.svg` | yt-dlp | Lucide `download` — **Ersatz**, kein Herstellerzeichen | ISC (Lucide) | — (generisches Symbol) |

<!-- ENDE ZEICHEN-TABELLE -->
