#!/usr/bin/env python3
"""Kamerabewegung messen: Wohin wandert der Bildinhalt, Sekunde für Sekunde?

Misst die globale Verschiebung zwischen Frames (Phasenkorrelation, gestreamt).
Wandert der Inhalt nach RECHTS, schwenkt die Kamera nach LINKS.
Wandert der Inhalt nach OBEN, kippt die Kamera nach UNTEN.

Das ist ein Messhelfer, kein Ersatz fürs Hinsehen: Bestätige die Richtung immer
am Kontaktbogen mit einem festen Objekt (Gebäude, Wand, Lampe), das im Bild wandert.
Große bewegte Dinge (Welle, Menschenmenge) können die Messung verfälschen.
Mit --bereich oben/unten/links/rechts misst du nur einen Bildteil (z. B. die feste Decke).

  python3 kamera.py original/vorbild.mp4
  python3 kamera.py --bereich oben original/vorbild.mp4
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _video import info, stream_gray  # noqa: E402

FPS = 6          # Messpunkte pro Sekunde
RUHIG = 0.4      # unter 0,4 % Bildbreite pro Sekunde gilt als ruhig


def verschiebung(a, b, win):
    """Um wie viele Pixel ist der Inhalt von a nach b gewandert? (dx>0 rechts, dy>0 unten)"""
    import numpy as np
    A = np.fft.fft2((a - a.mean()) * win)
    B = np.fft.fft2((b - b.mean()) * win)
    R = B * np.conj(A)
    R /= np.abs(R) + 1e-9
    r = np.fft.ifft2(R).real
    dy, dx = np.unravel_index(np.argmax(r), r.shape)
    h, w = r.shape
    if dy > h // 2:
        dy -= h
    if dx > w // 2:
        dx -= w
    return float(dx), float(dy), float(r.max())


def ausschnitt(f, bereich):
    h, w = f.shape
    return {"oben": f[: h // 2], "unten": f[h // 2:], "links": f[:, : w // 2],
            "rechts": f[:, w // 2:]}.get(bereich, f)


def richtung(px, py):
    teile = []
    if px > RUHIG:
        teile.append("Inhalt nach rechts = Kamera schwenkt LINKS")
    elif px < -RUHIG:
        teile.append("Inhalt nach links = Kamera schwenkt RECHTS")
    if py > RUHIG:
        teile.append("Inhalt nach unten = Kamera kippt HOCH")
    elif py < -RUHIG:
        teile.append("Inhalt nach oben = Kamera kippt RUNTER")
    return " · ".join(teile) or "ruhig"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--bereich", choices=["oben", "unten", "links", "rechts"])
    a = ap.parse_args()
    import numpy as np
    dur, W, H, _ = info(a.video)
    w = 180
    h = int(round(w * H / W / 2)) * 2
    prev = None
    sek = {}
    for t, f in stream_gray(a.video, w, h, FPS):
        f = ausschnitt(f, a.bereich)
        if prev is not None:
            win = np.outer(np.hanning(f.shape[0]), np.hanning(f.shape[1]))
            dx, dy, q = verschiebung(prev, f, win)
            s = int(t)
            sx, sy, n = sek.get(s, (0.0, 0.0, 0))
            sek[s] = (sx + dx, sy + dy, n + 1)
        prev = f
    print(f"{os.path.basename(a.video)} · {dur:.1f} s · Bereich: {a.bereich or 'ganzes Bild'}")
    print("Sekunde | Inhalt wandert (% Bildbreite / % Bildhöhe pro s) | Kamera")
    gx = gy = 0.0
    for s in sorted(sek):
        sx, sy, n = sek[s]
        fx = sx / n * FPS / w * 100
        fy = sy / n * FPS / h * 100
        gx += sx / w * 100
        gy += sy / h * 100
        print(f"{s:>3}-{s + 1:<3} | x {fx:+6.1f} %  y {fy:+6.1f} % | {richtung(fx, fy)}")
    print(f"Summe über das Video: Inhalt x {gx:+.0f} % der Bildbreite, y {gy:+.0f} % der Bildhöhe")
    print(f"Gesamt: {richtung(gx / max(dur, 1), gy / max(dur, 1))}")


if __name__ == "__main__":
    main()
