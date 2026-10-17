# Vorlagen: Shot-Map, Startbild, Video-Prompt

## 1. Shot-Map

Die Shot-Map ist der Bauplan. Ohne sie wird kein Prompt geschrieben.
Im Modus "nachbauen" wird sie am Vorbild GEMESSEN, im Modus "neu" wird sie bewusst ENTWORFEN.
Leg sie als `analyse/SHOTMAP.md` im Projektordner an.

```
# Shot-Map · <Projekt>

Quelle: <Datei/Idee> · <Länge> s · <Format> · Schnitte: <schnitt.py-Ergebnis>

## Kamera
Gemessen (kamera.py): <Kurzfassung pro Abschnitt>
Gegenprobe am Bogen: <festes Objekt> wandert von <Position> (<s>) nach <Position> (<s>)
  → Kamera schwenkt <LINKS/RECHTS> und kippt <HOCH/RUNTER>.
| Sekunde | Kamera | Was kommt von welchem Bildrand ins Bild |
|---|---|---|

## Set-Geografie (relativ zur Kamera)
Im ersten Bild: vorne ... / Mitte ... / hinten ... / links ... / rechts ...
Außerhalb des ersten Bildes: was liegt LINKS / RECHTS / UNTER / HINTER der Kamera,
und wie hängt es mit dem Sichtbaren zusammen (alles ist EIN zusammenhängendes Set).

## Ereignisse
| Sekunde | Was passiert | Wie groß / wie dramatisch |
|---|---|---|

## Ton (stimmen.py)
| Sekunde | Ruf wörtlich / Geräusch |
|---|---|
Lautheit: <LUFS>

## Look
Licht, Farben, Objektiv, Kameragefühl (Handkamera / Stativ / Kran)

## Warum es wirkt
Was passiert in Sekunde 1? Wo ist der Höhepunkt? Warum schaut man bis zum Ende?
```

## 2. Startbild-Prompt (Nano Banana Pro, nur Text)

Regeln:
- Nur aus Text. Das Vorbild wird nie als Referenz hochgeladen.
- Beschreib das ERSTE Bild der Shot-Map: oben, Hintergrund, Mitte, Vordergrund, jeweils mit Position im Bild.
- Was früh von einem Rand kommen soll, am Rand anlegen (eine Ecke reicht).
- Keine Wörter wie "smartphone" oder "phone". Am Ende immer:
  "Clean photographic frame: no on-screen text overlays, no camera interface, no REC sign, no timestamps, no borders."
- `--aspect_ratio 9:16` (oder das Format des Vorbilds). 2 Credits, also gern 2 Varianten und die bessere nehmen.

Beispiel (Miami-Nachbau, Bild "start_h", das mit dem Video funktioniert hat):
Auch hier: Struktur übernehmen, Inhalt aus deiner Shot-Map.

```
Behind-the-scenes photo, vertical 9:16, taken from a raised crew platform at the right edge of an enormous indoor wave tank, looking across the tank to the back left. Top of the frame: a dark steel ceiling truss with a few small round spotlights, two large bright square softbox lights hanging on the left side, and a long black telescopic camera crane arm entering from the upper right edge and reaching diagonally to the upper left, large white letters 'CUBE' on its end near the right edge, a remote camera head hanging from its tip at the upper left. Background: a vast royal-blue blue-screen wall with small orange plus-shaped tracking markers, a long blue curtain hanging on the left; at the back right a large grey corrugated hangar-style wave generator gate with a yellow-and-black hazard stripe band across its top; a few tiny crew members and monitors on the far side. Middle: the huge pool of calm, clear turquoise water fills most of the frame with bright reflections; small and far away on the left side of the water, a miniature amusement pier on stilts with a white Ferris wheel and little colourful booths. Foreground, lower right third, large and close: the grey concrete tank edge running diagonally from the bottom left toward the middle right with a dolly track; eight crew members in black t-shirts with EFFECTS CREW printed in white on the back, khaki shorts or trousers, headsets: one operates a big black cinema camera on a dolly in the lower left corner, a man in jeans stands behind a camera on a tripod, one raises a boom microphone with a furry windscreen, two kneel, others look at small monitors. Bright high-key studio light, natural colours, 24mm wide lens, everything sharp. Clean photographic frame: no on-screen text overlays, no camera interface, no REC sign, no timestamps, no borders.
```

## 3. Video-Prompt in vier Blöcken (Seedance 2.5, `omni_reference`, nur Startbild)

Gerüst:

```
One single continuous <handheld> shot. No cuts, no jumps, no zoom, no morphing.

SET LAYOUT (everything already exists from the first frame, only partly out of view):
The video starts exactly on the start image (image 1): <Startbild in 2-3 Sätzen>.
<Was außerhalb liegt, mit Richtung zur Kamera: "to the LEFT of and BELOW the camera ...",
 und wie es mit dem Sichtbaren verbunden ist.>

CAMERA MOVE (<wem folgt die Kamera>):
0 to <x> s: <...>
<x> to <y> s: the camera pans <LEFT/RIGHT> and tilts <UP/DOWN> to <...>. <Was von welchem Rand ins Bild kommt.>
...

NOTHING APPEARS OUT OF NOWHERE: no building, person or object materialises, grows, fades in
or transforms. Every element enters the frame only because the camera turns toward it,
exactly like a real camera on a real set. <Was die ganze Zeit an seinem Platz bleibt.>

ACTION AND SOUND:
0 s: <...> shouts "<Ruf wörtlich>".
<s>: <Ereignis, Größe an sichtbaren Objekten gemessen>.
...
<Ende>. Everything stays destroyed / nothing resets.

<Look in einem Satz>. Natural location sound only: <Geräusche>. No music.
```

Regeln:
- Zeiten in Sekunden, so genau wie die Shot-Map.
- Rufe wörtlich in Anführungszeichen, in der Sprache, in der sie gesprochen werden sollen.
- Größen an Objekten messen, die schon im Bild sind.
- Was abgesegnet ist, bleibt Wort für Wort stehen. Neue Version = alte Version + EINE Änderung.
- Jede Version mit Nummer in `PROMPTS.md` ablegen, mit einem Satz, was sich geändert hat und warum.

Beispiel (Miami-Nachbau v8.3: Kamera folgt der Welle nach links unten, Stadt kommt vom linken Rand).
**Das ist ein Beispiel für EIN bestimmtes Video. Übernimm die Struktur und die Art der Formulierung, nie den Inhalt.** Set, Richtungen, Zeiten und Rufe kommen immer aus deiner eigenen Shot-Map.

```
One single continuous handheld shot. No cuts, no jumps, no zoom, no morphing.

SET LAYOUT (everything already exists from the first frame, only partly out of view):
The video starts exactly on the start image (image 1): the camera stands on a raised crew platform at the near edge of a huge indoor wave tank. In front of the camera is the calm turquoise pool, the small miniature pier with the Ferris wheel is in the pool on the left, the grey wave gate is at the far back right, the black CUBE crane arm hangs at the top, and the crew stands on the platform in the foreground.
The small pier with the Ferris wheel is NOT an island and it is SHORT: a short wooden walkway connects the pier platform directly to the shore, and the shore begins just beyond the LEFT edge of the start image. Along the whole left side of the tank runs one LONG continuous miniature coastline, from the near-left corner below the camera all the way back to the far back wall of the studio: a wide sandy beach with hundreds of tiny people and colourful lifeguard towers, right behind the beach a beachfront road with tiny cars and a row of palm trees, and behind that road a long dense miniature Miami resort city, rows of pastel Art Deco hotels and many tall glass skyscrapers, stretching along the entire length of the coast toward the back. The land is long and very close to the left edge of the start frame; it is only just outside the frame at the start.

CAMERA MOVE (the operator follows the wave):
0 to 1.5 s: the camera holds the start view.
1 to 3 s: a gigantic wave pops up fast at the far back and rolls toward the pier. The camera pans to the LEFT and tilts DOWN to keep the wave in frame. Because the coast begins right beyond the left edge, already at about 2 s the beach, the beachfront road and the first hotels slide into view from the LEFT edge of the frame, directly connected to the short pier.
3 to 6 s: the camera keeps panning LEFT and tilting DOWN to follow the wave, and more and more of the long city slides in from the LEFT edge, the coastline stretching far toward the back of the studio. At 6 s the camera looks down the length of the shore: the long resort city fills the left half of the frame and recedes far into the back, the beach and the beachfront road run through the middle, and the pool with the incoming wave is on the right.
6 to 15 s: the camera stays on this view with small handheld movements. From about 10 s the long black CUBE crane arm with its overhead remote camera swings down into the top of the frame and flies forward over the flooded city, following the destruction.

NOTHING APPEARS OUT OF NOWHERE: no building, beach, palm tree, person or object materialises, grows, fades in or transforms. The pool never turns into a city. Every element enters the frame only because the camera turns toward it, exactly like a real camera in a real studio. The crew platform stays at the bottom of the frame the whole time.

ACTION AND SOUND:
0 s: a crew member loudly shouts "Action!" and a horn sounds.
1 s: the wave machine erupts and within about one second an even bigger, gigantic towering turquoise wave with a curling white crest and massive spray pops up across the whole tank, taller than the miniature skyscrapers, with a thundering rumble.
3.5 s: the wave explodes over the short pier and the shore right next to it, the Ferris wheel topples and breaks apart.
4 to 8 s: the wave rolls onto the land and floods the whole coastline from right to left: the beach, the beachfront road with its cars and palm trees, and the hotels behind it. It keeps travelling further to the LEFT and toward the BACK along the entire coast, destroying the resort city building by building; by 8 s whole hotels are already destroyed.
8 to 10 s: further back and further to the left the destruction continues: tall glass skyscrapers crack and topple one after another, debris and spray burst high into the air, the whole resort sinks under the water. At about 8.5 s the crew members standing at the far left end of the platform see the water coming, turn around and run toward the camera and past it.
10 s: a wall of water explodes over the edge of the set onto the crew platform in the foreground; a crew member yells "Oh no!" and scrambles back.
11 to 12.5 s: another crew member shouts "Camera three, stay on the tower!" while an operator keeps filming with a cinema camera on a tripod in the rushing water.
13 to 15 s: the whole city lies in ruins under churning white foam, water pours off the set. Everything stays destroyed.

Photorealistic miniature-scale water physics, very dramatic, bright high-key studio lighting, realistic handheld camera, nobody holds up a phone. Natural location sound only: crew voices, thundering rumble, explosive crash, roaring water. No music.
```

Aufruf (Entwurf):

```
python3 <tools>/job.py start --projekt <ordner> --out video/d1.mp4 seedance_2_5 \
  --mode omni_reference --start-image bilder/start_a.png --duration 15 \
  --aspect_ratio 9:16 --resolution 480p --draft=true --prompt "$(cat prompts/v1.txt)"
```
