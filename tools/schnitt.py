#!/usr/bin/env python3
"""Sprung- und Schnitterkennung über die Frame-Differenz (gestreamt).

Faktor = größte Differenz zweier Nachbarframes geteilt durch den Median.
Über 6 = harter Schnitt oder Sprung. Eine echte durchgehende Einstellung liegt meist unter 4.

  python3 schnitt.py video/d1.mp4 video/d2.mp4
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _video import info, stream_gray  # noqa: E402

GRENZE = 6.0


def pruefe(path):
    import numpy as np
    _, _, _, fps = info(path)
    prev = None
    diffs = []
    for _, f in stream_gray(path, 64, 114):
        if prev is not None:
            diffs.append(float(np.mean(np.abs(f - prev))))
        prev = f
    d = np.array(diffs)
    med = float(np.median(d)) or 1e-6
    order = np.argsort(d)[::-1][:3]
    top = [(round((int(k) + 1) / fps, 2), round(float(d[k] / med), 1)) for k in order]
    faktor = top[0][1]
    urteil = "SCHNITT/SPRUNG" if faktor > GRENZE else "durchgehend"
    spitzen = ", ".join(f"{t}s x{f}" for t, f in top)
    print(f"{os.path.basename(path)}: max Faktor {faktor} bei {top[0][0]} s -> {urteil}   (Spitzen: {spitzen})")
    return faktor <= GRENZE


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ok = all([pruefe(p) for p in sys.argv[1:]])
    sys.exit(0 if ok else 1)
