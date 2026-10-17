#!/usr/bin/env python3
"""Shot-Liste: findet ALLE Schnitte eines Videos und schreibt die Einstellungen mit Länge auf.

Für Montage-Videos (mehrere Szenen) der erste Messschritt. Gestreamt, kein Video im Arbeitsspeicher.
Ein Schnitt = Frame-Differenz über GRENZE x Median und lokales Maximum (mind. 0,3 s Abstand).
Weiche Überblendungen erkennt das nicht sicher: im Bogen gegenprüfen.

  python3 shots.py original/vorbild.mp4
  python3 shots.py original/vorbild.mp4 --bilder analyse/shots --json analyse/shots.json

--bilder legt pro Einstellung ein Bild aus der Mitte ab (shot_01.jpg ...), plus shots_bogen.jpg.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _video import frame_at, info, stream_gray  # noqa: E402


def finde_schnitte(path, grenze, abstand):
    import numpy as np
    dauer, _, _, fps = info(path)
    prev, diffs = None, []
    for _, f in stream_gray(path, 64, 114):
        if prev is not None:
            diffs.append(float(np.mean(np.abs(f - prev))))
        prev = f
    d = np.array(diffs)
    med = float(np.median(d)) or 1e-6
    min_frames = max(1, int(round(abstand * fps)))
    schnitte = []
    for k in range(len(d)):
        faktor = d[k] / med
        if faktor <= grenze:
            continue
        lo, hi = max(0, k - min_frames), min(len(d), k + min_frames + 1)
        if d[k] < d[lo:hi].max():
            continue
        t = round((k + 1) / fps, 3)
        if schnitte and t - schnitte[-1][0] < abstand:
            continue
        schnitte.append((t, round(float(faktor), 1)))
    return dauer, fps, schnitte


def main():
    ap = argparse.ArgumentParser(description="Shot-Liste eines Videos")
    ap.add_argument("video")
    ap.add_argument("--grenze", type=float, default=6.0)
    ap.add_argument("--abstand", type=float, default=0.3, help="Mindestabstand zweier Schnitte in s")
    ap.add_argument("--bilder", help="Ordner für ein Bild pro Einstellung")
    ap.add_argument("--json", help="Shot-Liste zusätzlich als JSON speichern")
    a = ap.parse_args()

    dauer, fps, schnitte = finde_schnitte(a.video, a.grenze, a.abstand)
    grenzen = [0.0] + [t for t, _ in schnitte] + [round(dauer, 3)]
    shots = []
    for i in range(len(grenzen) - 1):
        von, bis = grenzen[i], grenzen[i + 1]
        shots.append({"nr": i + 1, "von": von, "bis": bis, "laenge": round(bis - von, 2),
                      "schnitt_faktor": schnitte[i - 1][1] if i else None})

    laengen = [s["laenge"] for s in shots]
    print(f"{os.path.basename(a.video)}: {dauer:.2f} s, {len(shots)} Einstellung{'' if len(shots) == 1 else 'en'}, "
          f"Schnitt im Schnitt alle {sum(laengen) / len(laengen):.2f} s "
          f"(kürzeste {min(laengen):.2f} s, längste {max(laengen):.2f} s)")
    print("| Shot | von | bis | Länge |")
    print("|---|---|---|---|")
    for s in shots:
        print(f"| {s['nr']} | {s['von']:.2f} | {s['bis']:.2f} | {s['laenge']:.2f} |")

    if a.bilder:
        from PIL import Image
        os.makedirs(a.bilder, exist_ok=True)
        thumbs = []
        for s in shots:
            mitte = (s["von"] + s["bis"]) / 2
            img = frame_at(a.video, mitte, width=360)
            if img is None:
                continue
            p = os.path.join(a.bilder, f"shot_{s['nr']:02d}.jpg")
            img.save(p, quality=88)
            s["bild"] = p
            thumbs.append(img.resize((180, int(180 * img.height / img.width))))
        if thumbs:
            cols = min(6, len(thumbs))
            rows = (len(thumbs) + cols - 1) // cols
            th = max(t.height for t in thumbs)
            bogen = Image.new("RGB", (cols * 180, rows * th), "white")
            for i, t in enumerate(thumbs):
                bogen.paste(t, ((i % cols) * 180, (i // cols) * th))
            bogen.save(os.path.join(a.bilder, "shots_bogen.jpg"), quality=85)
            print(f"Bilder: {a.bilder}/shot_XX.jpg + shots_bogen.jpg")

    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump({"video": a.video, "dauer": dauer, "fps": fps, "shots": shots}, f,
                      ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
