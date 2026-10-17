#!/usr/bin/env python3
"""Einen fehlenden Ruf exakt an eine Sekunde ins Video mischen.

Hochpass 130 Hz (nimmt das Studio-Brummen der TTS-Stimme), leichter Hall, damit es
nach Raum klingt, danach das Ganze auf -14 LUFS. Bild wird nicht neu kodiert.
Danach immer mit stimmen.py gegenhören, ob der Ruf an der richtigen Stelle erkannt wird.

  python3 ruf.py video/d3.mp4 ton/ohno.mp3 10.0 video/d3_mit_ruf.mp4 [--db -3]
"""
import argparse
import subprocess


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("ruf")
    ap.add_argument("sekunde", type=float)
    ap.add_argument("out")
    ap.add_argument("--db", type=float, default=0.0, help="Lautstärke des Rufs anpassen")
    a = ap.parse_args()
    ms = int(round(a.sekunde * 1000))
    hat_ton = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                              "stream=index", "-of", "csv=p=0", a.video],
                             capture_output=True, text=True).stdout.strip()
    ruf = (f"[1:a]aformat=channel_layouts=stereo,highpass=f=130,aecho=0.8:0.5:40:0.25,"
           f"volume={a.db}dB,adelay={ms}|{ms}[r]")
    if hat_ton:
        fc = ruf + ";[0:a][r]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]"
    else:
        fc = ruf + ";[r]apad,loudnorm=I=-14:TP=-1.5:LRA=11[a]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.video, "-i", a.ruf, "-filter_complex", fc,
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", a.out], check=True)
    print(f"OK {a.out} (Ruf bei {a.sekunde:g} s)")


if __name__ == "__main__":
    main()
