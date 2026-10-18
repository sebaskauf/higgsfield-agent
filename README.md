# Higgsfield-Agent - KI-Videos nachbauen statt würfeln

Ein Claude-Code-Agent, der mit dir KI-Videos über Higgsfield (Seedance 2.5) baut.
Nicht "Prompt rein und hoffen", sondern so, wie ein Kameramann arbeitet: erst
verstehen, was im Video passiert, dann gezielt bauen, dann Bild für Bild vergleichen.

Aus dem Modul Faceless Content der [SKAILE Academy](https://www.skool.com/skaile-academy).

## Drei Modi

| Modus | Du gibst ihm | Er macht |
|---|---|---|
| **nachbauen** | ein virales KI-Video (Datei oder Link) | zerlegt es, misst Kamera und Zeitachse, baut die Mechanik nach |
| **neu** | eine Idee in einem Satz | entwirft den Bauplan und baut das Video daraus |
| **serie** | ein fertiges Video von dir | macht daraus weitere Folgen mit derselben Mechanik und eigener Geschichte |

## Welche Videos er kann

Bevor er baut, bestimmt er den **Videotyp** aus dem, was im Video messbar ist (Schnitte, Kamera,
Figuren, Ton, Stil), und wählt danach die Higgsfield-Funktion:

| Typ | Beispiel | Werkzeug |
|---|---|---|
| One-Take-Kamerafahrt | Miniatur-Katastrophe, Behind-the-Scenes | Seedance 2.5 |
| Montage mit gleichen Figuren | Cinematic-Paar, Fashion-Editorial | Kling 3.0 Multi-Shot oder Keyframes pro Shot |
| Figuren-Serie mit Dialog | Obst/Food-Drama, sprechende Gegenstände | Figurenblatt + Kling/Seedance mit Dialog |
| Stil-Look | Clay, Papier, Stop-Motion | Stil-Presets + Startbild |
| Motion Control | Figur tanzt deine Bewegung | Genjutsu (mit deinem eigenen Clip) |
| Werbung mit Produkt | UGC-Ad, Hook + CTA | Ad Recreate, Marketing Studio |
| Erklärvideo mit Text | Diagramme, UI | ehrlich: das ist Motion Design, kein KI-Video |

Was Higgsfield gerade kann (Modelle, Längen, Preise), zieht er sich vor jedem Projekt frisch über
die CLI. Erst ein billiger Gegentest, dann der volle Lauf. Nach jedem Projekt schreibt er ins
`LERNLOG.md`, was funktioniert hat.

## Warum das funktioniert

**Ein KI-Video ist eine Kamerafahrt durch ein Set, kein Bild, das sich bewegt.**
Wenn der Prompt nicht sagt, wo etwas außerhalb des Bildes liegt und wie die
Kamera dorthin kommt, erfindet das Modell es dort, wo die Kamera gerade hinschaut.
Dann tauchen Häuser mitten im Wasser auf. Das ist der häufigste Grund, warum
Nachbauten nicht aussehen wie das Original.

Darum misst der Agent zuerst: Wohin wandern feste Objekte im Bild, also wohin
schwenkt die Kamera? Was liegt links, rechts, hinter dem Bild? Was passiert in
welcher Sekunde, wer ruft wann was? Daraus schreibt er einen Prompt in vier
Blöcken und testet in günstigen Entwürfen.

Die Methode stammt aus einem echten Nachbau mit über 20 Entwürfen. Gut die Hälfte
der Credits ging dabei drauf, weil gewürfelt statt analysiert wurde. Jede Regel in
[`referenz/REGELN.md`](referenz/REGELN.md) hat mindestens einen Entwurf gekostet.

## Wie er mit deinen Credits umgeht

- Am Anfang jedes Projekts legst du einen **Credit-Deckel** fest, für den Anfang lieber niedrig (etwa 150 Credits). Darüber startet er nichts.
- **Vor jedem Job nennt er die Kosten** und wartet auf dein Ja.
- Getestet wird im **Entwurf** (480p, 45 Credits für 15 Sekunden), nicht in 1080p.
- **Pro Test ändert er genau eine Sache**, damit du weißt, was gewirkt hat.
- **Nach jedem Entwurf zeigt er dir das Ergebnis** (beim Nachbauen Original und Nachbau nebeneinander) und wartet auf dein Feedback, bevor der nächste Credit fließt.
- **Beim Start prüft er das Setup:** Login, Plan, Credits, Programme. Fehlt etwas, geht er den Teil mit dir durch.
- Jeder Job steht mit Kosten und Job-ID in `CREDITS.md` im Projektordner.

## Was er nicht macht

- Das Vorbild hochladen. Fremde Videos bleiben auf deinem Rechner und werden nur
  lokal zerlegt. Das Werkzeug blockt den Upload aus dem Ordner `original/`.
- Kopien posten. Ein 1:1-Nachbau ist eine Übung. Posten solltest du deine eigene
  Version mit eigenem Twist, als KI-Video gekennzeichnet.
- Ungefragt in 1080p rendern oder hochrechnen.

## Einrichten

Kopier den Inhalt von [SETUP-PROMPT.md](SETUP-PROMPT.md) in Claude Code. Der Agent
installiert sich, prüft deine Programme und verbindet sich mit Higgsfield.

Von Hand:

```
git clone https://github.com/sebaskauf/higgsfield-agent.git
cd higgsfield-agent
./install.sh
```

Du brauchst: Claude Code, ein Higgsfield-Konto mit Credits, ffmpeg, Python 3
(numpy, Pillow), Node.js für die Higgsfield-CLI. Whisper ist optional (für die
Ton-Zeitachse). Das Setup prüft alles und installiert, was fehlt.

**Getestet auf dem Mac.** Unter Windows ist der Agent nicht getestet.

## Benutzen

```
Bau mir dieses Video nach: https://www.instagram.com/reel/...
Neues Video: Ein Tornado zieht durch eine Miniatur-Altstadt, die Crew filmt am Set
Mach aus dem Video eine Serie mit fünf Folgen
```

## Was im Repo liegt

| Pfad | Inhalt |
|---|---|
| `agent/higgsfield-video.md` | der Agent |
| `referenz/REGELN.md` | Symptom, Ursache, Fix, Kosten |
| `referenz/VORLAGEN.md` | Shot-Map, Startbild-Prompt, Video-Prompt, mit echtem Beispiel |
| `tools/bogen.py` | Kontakt- und Vergleichsbogen |
| `tools/kamera.py` | misst die Kamerabewegung |
| `tools/schnitt.py` | findet Schnitte und Sprünge |
| `tools/startbild.py` | prüft, ob das Video auf dem Startbild beginnt |
| `tools/stimmen.py` | Rufe mit Zeit (Whisper) und Lautheit |
| `tools/ruf.py` | mischt einen fehlenden Ruf an die Sekunde genau ein |
| `tools/job.py` | Higgsfield-Jobs mit Kostenabfrage, Deckel und Ledger |
