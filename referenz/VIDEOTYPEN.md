# Videotypen: erkennen, Methode wählen, billig gegentesten

Jedes KI-Video wurde mit einer bestimmten Mechanik gebaut. Wer die falsche Mechanik nachbaut,
würfelt, egal wie gut der Prompt ist. Darum: **erst den Fingerabdruck messen, dann den Typ
bestimmen, dann mit einem billigen Gegentest bestätigen, erst dann das Budget einsetzen.**

Kennzeichnung der Quellen: **[CLI]** per `higgsfield model get` geprüft · **[Doku]** offizielle
Higgsfield-/Hersteller-Seite · **[Test]** selbst generiert und geprüft · **[Annahme]** plausibel,
aber noch nicht getestet. Annahmen im Projekt immer zuerst gegentesten.
Modelle, Parameter und Preise ändern sich: vorher `HIGGSFIELD-STAND.md` prüfen.

## 0. Analyse-Wege (Reihenfolge)

1. **Gemini-Videoanalyse (optional):** nur wenn `GEMINI_API_KEY` mit Guthaben da ist UND der Nutzer zustimmt, dass das Vorbild dafür an Google geht. Gemini sieht Bild und Ton nativ (Standard 1 Bild pro Sekunde, `video_metadata.fps` einstellbar, Zeitstempel nur sekundengenau, Datei inline unter 100 MB, YouTube-Links möglich) [Doku: ai.google.dev/gemini-api/docs/video-understanding, Modellname vor Nutzung dort prüfen]. Ergebnis als JSON nach `VORLAGEN.md` Abschnitt 4.1.
2. **Higgsfield-Videoanalyse (optional):** wenn der Higgsfield-Connector (MCP) verbunden ist, über dessen Videoanalyse (Struktur, Shots, Tempo). Nur mit Ja des Nutzers, weil das Vorbild dafür hochgeladen wird. Es dient nur der Analyse, nie als Referenz für eine Generierung.
3. **Immer verfügbar:** `shots.py`, `bogen.py`, `kamera.py`, `stimmen.py` lokal.

**Egal welcher Weg: Zeiten und Inhalte immer lokal gegenprüfen.** Schnittzeiten frame-genau mit `shots.py`, Inhalte am Bogen. KI-Analysen sind sekundengenau und erfinden gelegentlich Details.

## 1. Fingerabdruck messen (Pflicht, bevor du einen Typ nennst)

| Merkmal | Wie messen | Worauf es hinweist |
|---|---|---|
| Schnitte und Shot-Längen | `shots.py` (Liste aller Einstellungen) | 1 Einstellung = Kamerafahrt · viele Shots à 2-3 s = Montage |
| Kamera pro Shot | `kamera.py` + Bogen, pro Shot einzeln | bewegt sich durch ein Set oder steht fast still |
| Figuren über Shots | Bogen: gleiche Person, gleiches Outfit, gleiches Gesicht? | Figurenreferenzen nötig |
| Körperbewegung | Bogen in 0,25 s: natürlich, komplex (Tanz), exakt rhythmisch? | sehr menschliche komplexe Bewegung = Motion Control |
| Ton | `stimmen.py` + Anhören: Musikbett, Originalton mit Rufen, Dialog, Sprecher | Musik meist nachträglich drunter · Rufe/Dialog nativ generiert |
| Lippen | Bogen im Sprechmoment | synchron = Dialog im Modell oder Lipsync |
| Stil | Bogen | fotoreal, Knete/Clay, 3D-Animation, Anime, Papier |
| Text/Grafik | Bogen | saubere Schrift und Icons = Schnittprogramm/Motion Design, nicht das Videomodell |
| Länge, Format | `ffprobe` | über 15 s am Stück ohne Schnitt: nur Seedance 2.5 (bis 30 s) oder Verlängerung |
| Hinweise des Creators | Caption, Bio, Wasserzeichen, Interviews (Websuche) | Tool-Namen, aber oft nicht offengelegt |

Schreib das Ergebnis als Abschnitt `## Fingerabdruck` in die Shot-Map. Dann:
**Hypothese: Typ X, Methode Y, Sicherheit hoch/mittel/niedrig, weil ...** Bei mittel oder niedrig
zwei Methoden im Gegentest gegeneinander.

## 2. Die Typen

### A · One-Take-Kamerafahrt (z. B. Fake-Behind-the-Scenes, Miniatur-Katastrophe)
- **Fingerabdruck:** 1 Einstellung 10-15 s, Kamera folgt einem Ereignis durch ein Set, Ereignis eskaliert, Originalton mit Rufen.
- **Methode [Test]:** Startbild nur aus Text (Nano Banana Pro) → Seedance 2.5 `--mode omni_reference`, nur Startbild, Prompt in 4 Blöcken (VORLAGEN Abschnitt 3), Entwurf `--draft=true`.
- **Kosten [CLI]:** Startbild 2 · Entwurf 15 s 45 · Final 1080p 15 s 240.
- **Fallen:** alles in `REGELN.md`.

### B · Montage / Multi-Shot-Story mit gleichbleibenden Figuren (z. B. Cinematic-Paar, Fashion-Editorial)
- **Fingerabdruck:** viele Shots à ~1-4 s, dieselben Personen und Outfits in allen Shots, ein durchgehender Look (Licht, Farbe, Objektiv), Musikbett und oft **Dialog mit Lippenbewegung** (z. B. Telefonat). Ton immer mit `stimmen.py` prüfen, nie annehmen.
- **Was über solche Accounts bekannt ist:** Die Creatorin von @dreamfall.art legt ihre Tools nicht offen [Doku: alici.ai-Formel]. Eine Fallstudie zu einem ihrer Videos beschreibt: Keyframes zuerst als Bilder, dann je Shot animiert, 2-3 s pro Clip, ~15 s, subtile Bewegung [Fallstudie, nicht bestätigt]. Bekanntes Prinzip: „Welt festlegen, Shots darin variieren, jeder Shot in sich stabil“.
- **Häufigste Hypothese bei Dialog mit Lippen + Musik + bis 30 s (Fall dreamfall, 18.10.2026): Seedance 2.5 in EINEM Lauf** mit Figurenbildern als `--image-references` (kein Startbild), Storyboard-Notation, Dialog wörtlich mit Sprecher und Sekunde, `--generate_audio=true`. Reihenfolge: Storyboard mit kompletter Unterhaltung → Look-Profil → Figurenbilder im Stil des Vorbilds (Gate prüft der Agent selbst, Gesichter müssen nicht 1:1 sein) → 30-s-Entwurf (90 Credits) → vergleichen → eine Änderung. Kein Gesetz: Was gilt, entscheidet `HYPOTHESEN.md` anhand der Indizien.
- **Alternativen (je nach Indizien):**
  1. **Kling 3.0 Omni Multi-Shot [CLI]:** `kling_o3_image_reference --image <figur1> --image <figur2> --multi_shots=true --multi_prompt '[{"prompt":"...","duration":3},...]' --duration 15 --mode pro`. Bis 15 s pro Lauf (laut Hersteller-Guide bis 6 Shots [Doku]). Sehr günstig: pro 15 s 27-30 Credits, std 18,75 [CLI]. Längere Videos: zwei Läufe + Schnitt.
  2. **Einzelne Shots [CLI]:** pro Shot ein Keyframe (Nano Banana Pro mit Figurenreferenzen, bis 14 Referenzen, 2 Credits), dann Bild-zu-Video pro Shot (`kling_o3_flf --start-image <keyframe> --multi_shots=false`, std 5 s 6,25, pro 10 s 18; oder Seedance-Entwurf 5 s 15), zusammenschneiden per ffmpeg (VORLAGEN Abschnitt 4). Höchste Kontrolle über jeden Shot.
  3. **Seedance 2.5 bis 30 s mit Referenzen (= Standard oben) [CLI + Recherche]:** `--mode omni_reference`, bis 30 Bilder (Figuren, Orte), bis 30 s in einem Lauf (Entwurf 30 s 90, 720p 210, 1080p 480). Storyboard-Schreibweise im Prompt: „Shot 1: ... Then cut to ... Shot 2: ...“, Shots in Abschnitten von 2-3 s, pro Shot Reihenfolge Subjekt → Aktion → Kamera → Szene → Stil → Einschränkungen. Wie zuverlässig die Schnitte sitzen, erst mit 10 s testen.
- **Gegentest:** erst das Look-Gate (Figurenbilder neben Standbildern des Vorbilds), dann direkt der 30-s-Seedance-Entwurf. Am Vorbild vergleichen in dieser Reihenfolge: Look, Figuren, Dialog/Ton, Shot-Längen, Story.
- **Fallen [Annahme, im Projekt prüfen]:** Gesichter driften zwischen Shots (→ Figurenreferenzen in JEDEM Lauf, feste Namen und identische Beschreibung) · zu viele Shots in einem Lauf verschmelzen (→ max. 4-5 pro Kling-Lauf) · Ton: analysieren, was vorkommt (Dialog, Rufe, Soundeffekte, Atmo, Musik), genau das generieren, sonst nichts. Dialog wörtlich im Prompt, Musik nur als ähnliche Stimmung, nie den lizenzierten Song. Stummes Vorbild = stummer Nachbau.

### C · Figuren-Serie mit Dialog (z. B. Obst/Food mit Drama, sprechende Gegenstände)
- **Fingerabdruck:** stilisierte, wiederkehrende Figuren mit Gesicht, Dialog mit Stimmen, Mund bewegt sich, Soap-Story, mehrere Shots, oft gleiche Kulisse.
- **Methode:** Figurenblatt einmal bauen (Nano Banana Pro; mehrere Ansichten aus einem Bild mit `nano_banana_2_shots`, 4 Credits [CLI]), dann Shots wie Typ B. Dialog direkt im Videoprompt in Anführungszeichen mit Sprecher (Kling: `[Figur A, zittrige Stimme]: "..."` [Doku]; Seedance und Kling erzeugen Ton und Stimme mit [CLI: generate_audio/sound]). Alternative: Stimme separat mit `elevenlabs_v4` und als `--audio-references` an Seedance 2.5 oder Wan 3.0 geben, damit die Lippen passen [CLI-Parameter vorhanden, Lippenqualität Annahme].
- **Fallen:** Stimmen wechseln zwischen Shots (→ feste Stimmbeschreibung oder ElevenLabs-Stimme fix) · Figur verliert Gesicht (→ Figurenblatt in jedem Lauf).

### D · Clay / Stop-Motion / fester Stil-Look
- **Fingerabdruck:** Knete, Fingerabdrücke, sichtbare Textur, leicht abgehackte Bewegung (wie 12 Bilder pro Sekunde), Miniatur.
- **Methode:** Stil im Startbild/Keyframe festnageln („claymation, plasticine figures, visible fingerprints, handmade miniature set, stop-motion“), im Videoprompt dieselben Stilwörter plus ruhige Bewegung [Annahme]. Higgsfield hat dafür auch Stil-Presets: `higgsfield preset list video-explainer` (z. B. Claymotion, Paper Diorama, 3D Papercraft, Fluffy Toy), `higgsfield preset resolve video-explainer <id>` liefert eine Media-ID, die als `--image <media-id>` Stil-Referenz in Nano Banana Pro oder Seedance akzeptiert wird [CLI: Kostenabfrage gültig, Wirkung Annahme]. Das Stop-Motion-Ruckeln nicht vom Modell verlangen, sondern danach per ffmpeg erzeugen (`fps=12`, dann zurück auf 24).
- **Fallen [Annahme]:** Modell glättet zu weicher 3D-Animation (→ Stil im Bild verankern, nicht nur im Text).

### E · Motion Control: echte Bewegung auf eine KI-Figur (z. B. tanzende Statue, Figur macht exakt einen Trend nach)
- **Fingerabdruck:** sehr natürliche, komplexe, rhythmisch exakte Körperbewegung, die einem echten Clip folgt; die Figur selbst ist offensichtlich KI.
- **Methode [CLI]:** Genjutsu `hf_mult_motion_control --image <figur> --video <bewegungsquelle> --resolution 720p` (eine Quelle mit 15 s kostete 105 Credits in der Abfrage). Objekt in einem Video ersetzen: `hf_mult_replace_object`. Eigenes Video umbauen: `kling_video_edit` (Omni Edit).
- **WICHTIG:** Die Bewegungsquelle muss eigenes Material sein (selbst filmen). Das Vorbild wird nie hochgeladen.
- `higgsfield preset list animation-action` ist eine Bibliothek mit fertigen Bewegungen (Gehen, Kämpfen, Idle ...). Die Vorschauen stammen von Meshy, gedacht für 3D-Figuren (`3d_rigging`) [CLI]. Ob sie mit Genjutsu nutzbar sind: Annahme, erst prüfen.

### F · Sprechende Person / Avatar / UGC-Werbung
- **Fingerabdruck:** eine Person spricht in die Kamera, Lippen synchron, wenig Schnitt, oft Untertitel.
- **Methode:** Marketing Studio der Higgsfield-CLI (`higgsfield marketing-studio`) für Werbung mit Avatar und Produkt; Veo 3.1 erzeugt Dialog nativ (4/6/8 s) [CLI]; Seedance 2.5 mit Dialog im Prompt. Eigenes Gesicht: Soul ID trainieren (eigener Higgsfield-Ablauf). [Lippenqualität je Modell: Annahme, gegentesten]
- **Bekannte Personen:** möglich, wenn der Nutzer das will (z. B. als Twist: eine bekannte Person in einem unerwarteten Szenario). Erinnere einmal daran, das Video als KI-generiert zu kennzeichnen, und lass ihn selbst entscheiden. Blockt Higgsfields Moderation einen Job (Status `ip_detected` oder `nsfw`, die Credits kommen zurück), sag ihm das offen.

### G · Erklärvideo / Motion Graphics (Text, Icons, Diagramme, Bildschirm)
- **Fingerabdruck:** flache Grafiken, Typo-Animation, exakte Texte, Bildschirmaufnahmen.
- **Unterscheiden:** Geht es um exakte Schrift, UI, Zahlen oder Diagramme, dann **kein Higgsfield-Video**: Videomodelle verfälschen Schrift. Das baut man mit Motion Design (z. B. Claude mit HyperFrames oder Remotion). Sag das ehrlich und verbrenn keine Credits.
- Ist es ein illustrierter Erklär-Stil (Strichmännchen, Whiteboard, Papier-Diorama, Aquarell, Pixel Art) mit wenig Text: Higgsfields Erklär-Presets (`preset list video-explainer`, 22 Stile) als Stil-Referenz [CLI], Text danach im Schnitt drüberlegen.

### I · Werbe-Format mit eigenem Produkt (z. B. UGC-Ad, Hook + CTA)
- **Fingerabdruck:** Produkt im Mittelpunkt, Hook in den ersten Sekunden, Call-to-Action am Ende, oft Person mit Produkt.
- **Methode [CLI]:** `ad_multiplier_v2` („Ad Multiplier Recreate“): genau 1 `--video` + `--image` (dein Produkt/Motiv), `--mode recreate` (ganzes Video) oder `--mode sections --section hook|cta|both`. 720p mit 15-s-Video ca. 112 Credits (Abfrage). Alternative: Marketing Studio.
- **Regel:** Das `--video` muss eigenes Material sein oder vom Nutzer ausdrücklich freigegeben (siehe unten).

### H · Länger als 30 s ohne Schnitt
- **Methode [CLI + Doku]:** Seedance 2.5 `--mode video_extension --extension_mode forward|backward --video <clip>` verlängert einen Clip (Entwurf 10 s 30 Credits [CLI]); laut Higgsfield sind Ketten bis etwa 90 s möglich [Doku].

## Video-Referenzen und fremdes Material

Standard bleibt: **Das Vorbild wird nie zu Higgsfield hochgeladen**, auch nicht als Referenz. Funktionen,
die ein Video als Referenz nehmen (Seedance `--video`, Kamera/Bewegung aus Video, Genjutsu,
Ad Recreate, Kling Omni Edit), bekommen nur **eigenes Material** des Nutzers. Fremdes Material nur,
wenn der Nutzer es ausdrücklich freigibt, und dann mit dem Hinweis, dass er die Rechte daran braucht
und eine so entstandene Kopie nicht veröffentlichen sollte.

## 3. Der billige Gegentest (Pflicht vor dem vollen Lauf)

- Ein repräsentativer Ausschnitt, nicht das ganze Video: ein Shot oder 5 s.
- Günstigste Stufe: Seedance-Entwurf 5 s (15) oder Kling std 5 s (6,25).
- Am Vorbild vergleichen (Bogen nebeneinander): Stimmt der Typ? Figuren, Look, Bewegung?
- Erst wenn der Gegentest den Typ bestätigt, den vollen Lauf mit Kosten vorschlagen.
- Widerspricht der Gegentest der Hypothese: Typ neu bestimmen, nicht am Prompt drehen.
