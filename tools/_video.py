"""Gemeinsame Helfer: Videoinfos und einzelne Frames holen.

Grundregel: Nie ein ganzes Video roh in den Arbeitsspeicher laden.
Entweder einzelne Frames ziehen oder Frame für Frame aus einer Pipe streamen.
"""
import io
import json
import shutil
import subprocess
import sys


def need(binary):
    if shutil.which(binary) is None:
        sys.exit(f"FEHLER: '{binary}' fehlt. Installiere es zuerst (Setup im Agenten).")


def info(path):
    """Dauer (s), Breite, Höhe, fps eines Videos."""
    need("ffprobe")
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height,r_frame_rate:format=duration",
         "-of", "json", path],
        capture_output=True, text=True, check=True).stdout
    d = json.loads(out)
    s = d["streams"][0]
    num, den = s.get("r_frame_rate", "24/1").split("/")
    fps = float(num) / float(den or 1) if float(num) else 24.0
    return float(d["format"]["duration"]), int(s["width"]), int(s["height"]), fps


def frame_at(path, t, width=None):
    """Genau ein Frame bei Sekunde t als PIL-Bild (oder None, wenn t hinter dem Ende liegt)."""
    from PIL import Image
    vf = ["-vf", f"scale={width}:-2"] if width else []
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", path, "-frames:v", "1",
         *vf, "-f", "image2pipe", "-vcodec", "png", "-"],
        capture_output=True)
    if not r.stdout:
        return None
    return Image.open(io.BytesIO(r.stdout)).convert("RGB")


def stream_gray(path, w, h, fps=None):
    """Liefert Frames als (Zeit, numpy-Array h x w) nacheinander aus einer Pipe."""
    import numpy as np
    need("ffmpeg")
    vf = f"scale={w}:{h},format=gray"
    if fps:
        vf = f"fps={fps}," + vf
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", path, "-vf", vf,
                          "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
    size = w * h
    i = 0
    step = 1.0 / fps if fps else None
    try:
        while True:
            b = p.stdout.read(size)
            if len(b) < size:
                break
            yield (i * step if step else i), np.frombuffer(b, np.uint8).astype(np.float32).reshape(h, w)
            i += 1
    finally:
        p.stdout.close()
        p.wait()
