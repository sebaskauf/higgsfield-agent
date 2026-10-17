#!/usr/bin/env python3
"""Kontaktbogen / Vergleichsbogen.

Eine Zeile pro Video, eine Spalte pro Zeitpunkt (Standard alle 0,5 s).
Mit --ref steht die Referenz immer in der ersten Zeile, darunter die Entwürfe.
Lange Videos werden auf mehrere Bilder verteilt (bogen_1.jpg, bogen_2.jpg ...).

  python3 bogen.py --out analyse/original.jpg original/vorbild.mp4
  python3 bogen.py --ref original/vorbild.mp4 --out analyse/vergleich_d3.jpg video/d3.mp4
  python3 bogen.py --schritt 0.25 --von 4 --bis 8 --out analyse/detail.jpg video/d3.mp4
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _video import info, frame_at, need  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="Kontakt- und Vergleichsbogen")
    ap.add_argument("videos", nargs="+")
    ap.add_argument("--ref", help="Referenzvideo, steht in der ersten Zeile")
    ap.add_argument("--out", required=True, help="Zieldatei .jpg")
    ap.add_argument("--schritt", type=float, default=0.5)
    ap.add_argument("--von", type=float, default=0.0)
    ap.add_argument("--bis", type=float)
    ap.add_argument("--breite", type=int, default=150, help="Breite pro Bild in Pixeln")
    ap.add_argument("--spalten", type=int, default=12, help="Zeitpunkte pro Bogen")
    a = ap.parse_args()
    need("ffmpeg")
    from PIL import Image, ImageDraw

    rows = ([("REF", a.ref)] if a.ref else []) + [(os.path.basename(v), v) for v in a.videos]
    durs = {p: info(p)[0] for _, p in rows}
    end = a.bis if a.bis is not None else max(durs.values())
    times = []
    t = a.von
    while t <= end - 0.04:
        times.append(round(t, 3))
        t += a.schritt

    # Zellgröße aus dem ersten Frame
    probe = frame_at(rows[0][1], min(a.von, durs[rows[0][1]] - 0.1), a.breite)
    cw, ch = probe.size
    label_w, head_h, gap = 110, 18, 4
    base, ext = os.path.splitext(a.out)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    chunks = [times[i:i + a.spalten] for i in range(0, len(times), a.spalten)]
    written = []
    for n, chunk in enumerate(chunks, 1):
        W = label_w + len(chunk) * (cw + gap)
        H = head_h + len(rows) * (ch + gap)
        sheet = Image.new("RGB", (W, H), "white")
        d = ImageDraw.Draw(sheet)
        for ci, tt in enumerate(chunk):
            d.text((label_w + ci * (cw + gap), 2), f"{tt:g}s", fill="black")
        for ri, (name, path) in enumerate(rows):
            y = head_h + ri * (ch + gap)
            d.text((4, y + 4), name[:16], fill="black")
            for ci, tt in enumerate(chunk):
                x = label_w + ci * (cw + gap)
                im = frame_at(path, tt, a.breite) if tt < durs[path] - 0.02 else None
                if im is None:
                    d.rectangle([x, y, x + cw, y + ch], fill=(200, 200, 200))
                    continue
                if im.size != (cw, ch):
                    im = im.resize((cw, ch))
                sheet.paste(im, (x, y))
        out = a.out if len(chunks) == 1 else f"{base}_{n}{ext or '.jpg'}"
        sheet.save(out, quality=88)
        written.append(f"{out}  ({chunk[0]:g}-{chunk[-1]:g} s)")
    print("\n".join(written))


if __name__ == "__main__":
    main()
