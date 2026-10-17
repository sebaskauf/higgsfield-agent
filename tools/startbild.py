#!/usr/bin/env python3
"""Startbild-Treue: Startet das Video wirklich auf dem Startbild?

Vergleicht das erste Bild des Videos mit dem Startbild: weichgezeichnet, sehr klein,
kleine Verschiebungen ausgeglichen (die Kamera ist im ersten Frame oft schon minimal weiter).
Mittlere Abweichung pro Pixel (0-255).
Unter 20 = startet auf dem Startbild. 20-30 = prüfen. Über 30 = Startbild ignoriert.
(Gemessen an echten Seedance-Entwürfen: richtiges Startbild 3-13, falsches 33-55.)

  python3 startbild.py video/d1.mp4 bilder/start_a.png
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _video import frame_at  # noqa: E402


def abweichung(frame, bild, w=36):
    import numpy as np
    from PIL import ImageFilter, ImageOps
    h = int(round(w * frame.size[1] / frame.size[0]))
    a = np.asarray(frame.filter(ImageFilter.GaussianBlur(4)).resize((w, h)), np.float32)
    b = np.asarray(ImageOps.fit(bild, frame.size).filter(ImageFilter.GaussianBlur(4)).resize((w, h)), np.float32)
    best = 1e9
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            A = a[2 + dy:h - 2 + dy, 2 + dx:w - 2 + dx]
            best = min(best, float(np.mean(np.abs(A - b[2:h - 2, 2:w - 2]))))
    return best


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    from PIL import Image
    video, bild = sys.argv[1], sys.argv[2]
    f = frame_at(video, 0.0)
    if f is None:
        sys.exit("FEHLER: erstes Bild nicht lesbar")
    abw = abweichung(f, Image.open(bild).convert("RGB"))
    urteil = "startet auf dem Startbild" if abw < 20 else ("prüfen (Bogen ansehen)" if abw < 30 else "Startbild IGNORIERT")
    print(f"{os.path.basename(video)} vs {os.path.basename(bild)}: Abweichung {abw:.1f} -> {urteil}")
    sys.exit(0 if abw < 20 else 1)


if __name__ == "__main__":
    main()
