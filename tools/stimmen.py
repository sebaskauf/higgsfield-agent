#!/usr/bin/env python3
"""Ton-Zeitachse: Wer ruft wann was, und wie laut ist das Video?

Transkribiert lokal mit Whisper (nichts geht ins Netz) und misst die Lautheit (LUFS).
Ohne Whisper wird nur die Lautheit gemessen.

  python3 stimmen.py original/vorbild.mp4
  python3 stimmen.py --sprache de --modell small video/d3.mp4
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile


def lufs(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "ebur128", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
    return float(m[-1]) if m else None


def transkript(wav, sprache, modell):
    try:
        import whisper  # Python-Paket openai-whisper
        res = whisper.load_model(modell).transcribe(wav, language=sprache, fp16=False)
        return res["segments"]
    except ImportError:
        pass
    if shutil.which("whisper"):
        d = tempfile.mkdtemp()
        subprocess.run(["whisper", wav, "--model", modell, "--language", sprache,
                        "--output_format", "json", "--output_dir", d, "--fp16", "False"],
                       capture_output=True)
        f = os.path.join(d, os.path.splitext(os.path.basename(wav))[0] + ".json")
        if os.path.exists(f):
            return json.load(open(f, encoding="utf-8"))["segments"]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--sprache", default="en")
    ap.add_argument("--modell", default="small")
    a = ap.parse_args()
    if not shutil.which("ffmpeg"):
        sys.exit("FEHLER: ffmpeg fehlt.")
    hat_ton = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                              "stream=index", "-of", "csv=p=0", a.video],
                             capture_output=True, text=True).stdout.strip()
    if not hat_ton:
        print(f"{os.path.basename(a.video)}: KEINE Tonspur")
        return
    print(f"{os.path.basename(a.video)}: Lautheit {lufs(a.video)} LUFS (Social-Standard ca. -14)")
    wav = os.path.join(tempfile.mkdtemp(), "ton.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.video, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    seg = transkript(wav, a.sprache, a.modell)
    if seg is None:
        print("Whisper fehlt, nur Lautheit gemessen. (pip install openai-whisper)")
        return
    if not seg:
        print("Keine Sprache erkannt.")
    for s in seg:
        print(f"{s['start']:5.1f}-{s['end']:5.1f} s: {s['text'].strip()}")


if __name__ == "__main__":
    main()
