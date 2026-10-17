#!/usr/bin/env python3
"""Higgsfield-Katalog: zieht ALLE Modelle (Video, Bild, Ton) samt Parametern und Regeln
direkt aus der Higgsfield-CLI und schreibt eine kompakte Übersicht als Markdown.

Aufruf:  python3 katalog.py <ausgabe.md> [--json <cache.json>]
Kostet nichts (nur `higgsfield model list/get`). Dauer: ca. 2-4 Minuten.
"""
import json, subprocess, sys, datetime, re

OUT = sys.argv[1] if len(sys.argv) > 1 else "KATALOG.md"
CACHE = sys.argv[sys.argv.index("--json") + 1] if "--json" in sys.argv else None


def cli(args, timeout=45):
    try:
        r = subprocess.run(["higgsfield", *args, "--json"], capture_output=True, text=True, timeout=timeout)
        return json.loads(r.stdout) if r.stdout.strip() else None
    except Exception:
        return None


def caps(m):
    """Fähigkeiten aus Parametern und Regeln ableiten (nur was die CLI wirklich meldet)."""
    p = {x["name"]: x for x in m.get("params", [])}
    rules = " ".join(r.get("message", "") if isinstance(r, dict) else str(r) for r in (m.get("rules") or []))
    c = []
    if "duration" in p:
        d = p["duration"]
        c.append("Dauer " + ("/".join(d["enum"]) if d.get("enum") else f"frei (Std. {d.get('default')})") + " s")
    if "resolution" in p and p["resolution"].get("enum"):
        c.append("Auflösung " + "/".join(p["resolution"]["enum"]))
    for k, label in (("generate_audio", "Ton an/aus"), ("sound", "Ton an/aus"), ("audio_references", "Audio-Referenzen"),
                     ("start_image", "Startbild"), ("end_image", "Endbild"), ("image_references", "Bild-Referenzen"),
                     ("video_references", "Video-Referenzen"), ("multi_shots", "Multi-Shot"), ("draft", "Entwurf"),
                     ("dialogue", "Dialog-Eingabe"), ("voice_id", "Stimme")):
        if k in p:
            c.append(label)
    for k in ("mode", "variant", "quality", "preset", "style"):
        if k in p and p[k].get("enum"):
            c.append(f"{k}: " + "/".join(p[k]["enum"][:8]))
    m_img = re.search(r"at most (\d+) images", rules)
    if m_img:
        c.append(f"max {m_img.group(1)} Bilder")
    return "; ".join(c)


data = {}
lines = [f"# Higgsfield-Katalog (automatisch)", "",
         f"Erzeugt {datetime.date.today().strftime('%d.%m.%Y')} mit `tools/katalog.py` direkt aus der Higgsfield-CLI. "
         "Nur was die CLI meldet. Achtung: Manche Fähigkeiten stehen nicht als Parameter da (z. B. erzeugt Veo 3.1 Ton und Dialog "
         "nativ, ohne Schalter). Bei Zweifeln `higgsfield model get <job_type>` und die offizielle Seite prüfen.", ""]
for typ in ("video", "image", "audio"):
    lst = cli(["model", "list", f"--{typ}"]) or []
    lines += [f"## {typ.capitalize()} ({len(lst)} Modelle)", "", "| job_type | Name | Fähigkeiten laut CLI | Regeln |", "|---|---|---|---|"]
    for e in lst:
        jt = e.get("job_type")
        m = cli(["model", "get", jt]) or {}
        data[jt] = m
        rules = [r.get("message", "") if isinstance(r, dict) else str(r) for r in (m.get("rules") or [])]
        rtxt = " · ".join(rules)[:260].replace("|", "/")
        lines.append(f"| `{jt}` | {e.get('display_name','')} | {caps(m) or '-'} | {rtxt or '-'} |")
    lines.append("")

open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
if CACHE:
    json.dump(data, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"OK {OUT}: {len(data)} Modelle")
