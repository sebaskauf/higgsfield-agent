# Ursache und Wirkung (Seedance 2.5 über Higgsfield)

Gesammelt beim Nachbau eines viralen Behind-the-Scenes-Reels, Oktober 2026: über 20 Entwürfe,
rund 2.000 Credits, davon gut die Hälfte verbrannt, weil gewürfelt statt analysiert wurde.
Jede Zeile hier hat mindestens einen Entwurf gekostet. Lies sie, bevor du einen Prompt schreibst,
und schlag hier nach, bevor du eine Ursache rätst.

## Das Grundprinzip

**Ein KI-Video ist eine Kamerafahrt durch ein Set, kein Bild, das sich bewegt.**
Das Modell erfindet, was es nicht kennt. Sagt der Prompt nicht, WO etwas außerhalb des Bildes
liegt und WIE die Kamera dorthin kommt, erfindet das Modell es dort, wo die Kamera gerade
hinschaut. Dann "spawnen" Gebäude mitten im Wasser.

**Das Startbild gewinnt gegen den Prompt.** Was im ersten Bild nicht angelegt ist, kommt spät
oder gar nicht, egal was im Text steht. Soll etwas früh da sein, muss es im Startbild zumindest
am Rand angelegt sein. Aber: Zeigt das Startbild zu viel, ändert sich die ganze Geometrie.

## Symptom → Ursache → Fix

| Symptom im Entwurf | Ursache | Fix |
|---|---|---|
| Gebäude, Menschen, Objekte tauchen mitten im Bild aus dem Nichts auf | Kamerarichtung falsch oder Set-Geografie fehlt | Kamera am Vorbild messen (`kamera.py` + festes Objekt im Bogen), SET LAYOUT mit Richtungen ("to the LEFT of and BELOW the camera"), Block NOTHING APPEARS OUT OF NOWHERE |
| Zweite Hälfte friert ein oder läuft rückwärts aufs Endbild zu | Endbild mitgegeben | Kein Endbild. Nur Startbild |
| Szene setzt sich zurück (Stadt nach der Flut wieder trocken) | Referenzbild vom Zielzustand mitgegeben | Keine Referenzbilder vom Ziel. Zielzustand nur als Text mit Sekunde, plus "destruction is permanent, nothing resets" |
| REC-Symbol, Uhrzeit, Kamera-Interface im Bild | Wörter wie "smartphone", "phone video", "filmed on iPhone" | Weglassen. Stattdessen "realistic handheld camera, nobody holds up a phone". Im Bildprompt "no on-screen text overlays, no camera interface, no REC sign" |
| Hände mit Handy im Bild | "phone video" im Videoprompt | wie oben |
| Ein Objekt taucht viel zu früh auf | Größenvergleich mit noch unsichtbaren Objekten ("taller than the skyscrapers") | An Objekten messen, die schon im Bild sind ("three times as tall as the Ferris wheel") |
| Video beginnt nicht auf dem Startbild (`startbild.py` über 30) | Langer Prompt ohne Anker | Erster Satz im SET LAYOUT: "The video starts exactly on the start image (image 1): ..." und das Startbild kurz beschreiben |
| Etwas kommt erst ab Sekunde 5, obwohl der Prompt 2 sagt | Startbild zeigt an dieser Seite nichts davon | Im Startbild am Rand anlegen (eine Palme, eine Hausecke). Nicht gleich alles zeigen |
| Ganze Szene kippt (Welle trifft plötzlich von der Seite) | Mehrere Dinge auf einmal geändert (Startbild + Set + Ereignis) | Zurück zum letzten guten Stand, EINE Sache ändern |
| Harter Schnitt / Sprung mitten im Video | Modell schneidet bei überladenen Prompts gern | "One single continuous shot. No cuts, no jumps, no zoom, no morphing." ganz oben. Immer `schnitt.py` laufen lassen, auch wenn es auf dem Bogen gut aussieht |
| Ein Ruf fehlt oder kommt ~1 s zu spät | Modell lässt bei mehreren Rufen gern einen weg | Nicht neu würfeln. Ruf per ElevenLabs erzeugen (0,23 Credits) und mit `ruf.py` an die Sekunde mischen |
| Musik unter dem Video | nicht ausgeschlossen | "Natural location sound only ... No music." |
| Der 1080p-Lauf sieht anders aus als der abgesegnete Entwurf | 1080p ist ein neuer Wurf, kein schärferer Entwurf | Vorher sagen. Wer genau den Entwurf will: `video_edit`-Weg (siehe Agent, "Fertig machen") |

## Fremdes Material

Das Vorbild wird nie zu Higgsfield hochgeladen, auch nicht als Referenz. Video-Referenzen
(Seedance `--video`, Genjutsu, Ad Recreate, Kling Omni Edit) nur mit eigenem Material oder nach
ausdrücklicher Freigabe des Nutzers, mit Hinweis auf die Rechte. Details: `VIDEOTYPEN.md`.

## Was sich nicht bewährt hat

- **Würfeln in Runden von 2-4 Entwürfen** "mal sehen, was rauskommt". Der Kernfehler war in jeder
  Runde sichtbar und wurde als Zufall abgetan. Ein Entwurf pro Hypothese.
- **Direkt in 1080p testen.** 240 statt 45 Credits für einen Versuch, der schlechter war als der Entwurf.
- **Grob vergleichen.** Bilder nur alle 1,5 s angesehen, harten Schnitt übersehen, als fertig gemeldet.
- **"So nah wie möglich" sagen**, obwohl Kamera und Geografie noch nicht stimmen.
- **Einen Entwurf über die CLI fertig rendern** (`draft_job_id`): gab im Oktober 2026 einen Validierungsfehler.

## Kosten (gemessen 17.10.2026, vor jedem Job neu abfragen)

Alle anderen Modelle (Kling, Genjutsu, Ad Recreate, Musik): `HIGGSFIELD-STAND.md`.

Die Abfrage ist eine Schätzung. Was wirklich abgebucht wurde, zeigt
`higgsfield account transactions`. Läuft das Konto auch für andere Projekte,
zählen nur die eigenen Job-IDs im Ledger, nicht der Kontostand.

| Was | Credits |
|---|---|
| Startbild Nano Banana Pro | 2 |
| Seedance 2.5 Entwurf (draft, 480p) 15 s | 45 |
| Seedance 2.5 Entwurf 5 s | ca. 15 |
| Seedance 2.5 1080p 15 s | 240 |
| Seedance 2.5 `video_edit` 720p 15 s | 113 |
| Bytedance Video Upscale auf 1080p | Schätzung 1, berechnet wurden 3,01 |
| ElevenLabs v4, kurzer Ruf | 0,23 |
