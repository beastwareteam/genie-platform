# Engineering Checklist

## Vor der Implementierung
- [ ] Use-Case benannt und Scope klar abgegrenzt
- [ ] Betroffene Layer identifiziert
- [ ] ADR nötig? (Ja bei Architektur-/Schnittstellenentscheidungen)

## Während der Implementierung
- [ ] Keine Business-Logik in UI-Klassen
- [ ] Domain bleibt framework-unabhängig
- [ ] Infrastruktur nur über Ports angebunden
- [ ] Namensgebung neutral und projektspezifisch

## Vor PR
- [ ] Tests ergänzt/aktualisiert
- [ ] Dokumentation aktualisiert (README/ARCHITECTURE/ADR)
- [ ] Watchlist-Einfluss dokumentiert (falls genutzt)
- [ ] Selbstcheck auf Layer-Verletzungen durchgeführt
