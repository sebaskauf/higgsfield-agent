# Higgsfield-Stand

**Stand: 18.10.2026** (per `higgsfield model get` und `higgsfield generate cost`, CLI 1.1.24).
Älter als 7 Tage oder ein Modell fehlt hier: neu ziehen (Befehle unten) und das Datum oben ändern.
Preise sind Abfragen, keine Abbuchungen. Was wirklich abgebucht wurde: `higgsfield account transactions`.

## Neu ziehen

```
higgsfield model list --video ; higgsfield model list --image ; higgsfield model list --audio
higgsfield model get <job_type>          # Parameter, Grenzen, Pflichtfelder
higgsfield generate cost <job_type> ...  # Preis für genau diese Einstellung
```
Hängt ein Befehl, mit Timeout aufrufen (`perl -e 'alarm 60; exec @ARGV' higgsfield ...`).
Unklar, was eine Funktion macht: offizielle Seite per Websuche (higgsfield.ai/blog, Hersteller-Guides).

## Videomodelle, die der Agent wirklich nutzt

| job_type | Wofür | Wichtige Parameter und Grenzen | Preis (Abfrage) |
|---|---|---|---|
| `seedance_2_5` | One-Take, lange Shots, Referenzen, Verlängern | `--mode t2v / omni_reference / video_edit / video_extension`; Dauer bis 30 s; `--draft=true`; bis 30 Bilder (inkl. Start-/Endbild), bis 50 Referenzen gesamt; Start-/Endbild nur in `omni_reference`; `video_edit` genau 1 Video; `video_extension` braucht `--extension_mode forward/backward`; `--generate_audio` | Entwurf 5 s 15 · 10 s 30 · 15 s 45 · 30 s 90 · 720p 30 s 210 · 1080p 15 s 240 · 1080p 30 s 480 · Verlängerung Entwurf 10 s 30 |
| `kling_o3_image_reference` | Kling 3.0 Omni mit Referenzbildern, Multi-Shot | `--image` (Figuren), `--multi_shots=true --multi_prompt '[{"prompt":"...","duration":n},...]'`, Dauer bis 15 s, `--mode std/pro/4k`, `--sound on/off`. Ohne Multi-Shot `--multi_shots=false` explizit setzen, sonst Validierungsfehler | std 10 s 12,5 · pro 15 s Multi 30 (mit `--sound off` 22,5) · 4k 15 s Multi 90 |
| `kling_o3_flf` | Kling 3.0 Omni mit Start-/Endbild (Keyframe-Shot) | `--start-image`, `--end-image` (nur mit Start), Multi-Shot wie oben, bis 15 s | std 5 s 6,25 (mit `--sound off` 5) · pro 10 s 18 · pro 15 s Multi 27 · std 15 s Multi (6 Shots) 18,75 |
| `kling3_0` | Kling v3.0 klassisch | Start-/Endbild, std/pro/4k | std 5 s 10 · pro 10 s 25 |
| `hf_mult_motion_control` | Genjutsu: Bewegung aus eigenem Video auf Figur | genau 1 `--video`, mind. 1 `--image`, 480p/720p/1080p | 720p mit 15-s-Quelle 105 |
| `hf_mult_replace_object` | Genjutsu: Objekt in eigenem Video ersetzen | genau 1 `--video`, mind. 1 `--image` | vor Nutzung abfragen |
| `kling_video_edit` | Eigenes Video mit Kling umbauen | `--video` Pflicht, `--image` optional | vor Nutzung abfragen |
| `veo3_1` | Dialog/Sprechen nativ | Dauer 4/6/8 s, 16:9 oder 9:16, Startbild | vor Nutzung abfragen |
| `wan3_0` | Alternative, Audio-Referenzen | Dauer 2-30 s, `--audio-references`, Start-/Endbild nicht mit Referenzen kombinierbar | 720p 10 s 17,5 |
| `ad_multiplier_v2` | Ad Recreate: Werbe-Video mit eigenem Produkt neu bauen | genau 1 `--video` (eigenes Material), `--image`, `--mode recreate/sections`, `--section hook/cta/both` | 720p, 15-s-Video: 112 |
| `bytedance_video_upscale` | Hochrechnen | `--resolution 1080p --preset aigc` | Abfrage 1, abgebucht 3,01 |

Kling hat keinen Entwurfsmodus. Günstigste Teststufe: `--mode std --sound off`.

## Bildmodelle

| job_type | Wofür | Grenzen | Preis |
|---|---|---|---|
| `nano_banana_pro` | Startbilder, Keyframes, Figurenblatt | bis 14 Referenzbilder, 1k/2k/4k | 2k: 2 |
| `nano_banana_2_shots` | aus EINEM Bild mehrere Ansichten derselben Figur | genau 1 Referenz | 4 |
| `3d_jutsu_angles` | Figur/Objekt aus anderen Winkeln | bis 10 Referenzen | vor Nutzung abfragen |
| `soul_cinematic`, `text2image_soul_v2` | Higgsfield-eigener Look, eigene Soul-ID | höchstens 1 Referenz, `custom_reference_id` | vor Nutzung abfragen |
| `soul_location`, `soul_cast` | Orte / Figuren-Cast | siehe `model get` | vor Nutzung abfragen |

## Ton

| job_type | Wofür | Preis |
|---|---|---|
| `elevenlabs_v4` | Rufe, Stimmen, Dialog (`higgsfield voices list`) | kurzer Ruf 0,23 |
| `sonilo_music` | Musikbett, `--duration` in s | 30 s: 1,88 |
| `mirelo_text_to_audio`, `seed_audio` | Geräusche/SFX | vor Nutzung abfragen |

## Sonstiges

- `higgsfield preset list video-explainer`: 22 Erklär-/Stil-Presets (u. a. Editorial Motion Graphics, Stickman Cartoon, Claymotion, Paper Diorama, Whiteboard Doodle, 3D Papercraft, Pixel Art, Fluffy Toy). `preset resolve video-explainer <id>` gibt eine Media-ID, die als `--image <media-id>` Stil-Referenz angenommen wird (Seedance-Entwurf 5 s: 15, Nano Banana Pro: 2).
- `higgsfield preset list animation-action [--query walk]`: Bewegungsbibliothek (Meshy-Animationen, für 3D-Figuren).

- `brain_activity` (Virality Predictor): Video vor dem Posten bewerten lassen, `--video`.
- `higgsfield marketing-studio`: Werbung mit Avatar und Produkt (eigene Unterbefehle, `--help`).
- `higgsfield soul-id`: eigenes Gesicht trainieren (nur die eigene Person oder mit Einverständnis).
