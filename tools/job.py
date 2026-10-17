#!/usr/bin/env python3
"""Higgsfield-Jobs mit Kostenbremse und Ledger.

  python3 job.py kosten <modell> [parameter...]
  python3 job.py stand  --projekt <ordner>
  python3 job.py start  --projekt <ordner> --out video/d1.mp4 <modell> [parameter...]
  python3 job.py holen  --projekt <ordner> --out video/d1.mp4 <job-id>

start fragt erst die Kosten ab und bricht ab, wenn der Deckel aus CREDITS.md überschritten
würde. Jeder gestartete Job steht sofort im Ledger (auch wenn das Warten später abbricht).
Dateien aus einem Ordner namens "original" werden nie hochgeladen.
"""
import json
import os
import re
import signal
import subprocess
import sys
import time
import urllib.request

CLI = "higgsfield"
KOPF = "| Datum | Modell | Credits | Job-ID | Datei |\n|---|---|---|---|---|\n"


def run(args, timeout):
    """CLI aufrufen, stdin zu (sonst hängt sie manchmal), bei Timeout ganze Prozessgruppe beenden."""
    p = subprocess.Popen([CLI, *args], stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, text=True, start_new_session=(os.name != "nt"))
    try:
        out, _ = p.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        if os.name != "nt":
            os.killpg(p.pid, signal.SIGKILL)
        else:
            p.kill()
        return None
    return out


def schutz_original(params):
    for x in params:
        if os.path.exists(x) and "original" in os.path.normpath(os.path.abspath(x)).split(os.sep):
            sys.exit(f"STOPP: {x} liegt im Ordner 'original'. Das Vorbild wird nie zu Higgsfield hochgeladen.")


def kosten(modell, params):
    schutz_original(params)
    for versuch in range(2):
        out = run(["generate", "cost", modell, *params], 90)
        if out:
            m = re.findall(r"([\d.]+)\s*credits", out)
            if m:
                return float(m[-1])
            sys.exit(f"FEHLER bei der Kostenabfrage:\n{out.strip()[:800]}")
    sys.exit("FEHLER: Kostenabfrage hängt (2x 90 s). Nichts gestartet. Später nochmal versuchen.")


def ledger(projekt):
    f = os.path.join(projekt, "CREDITS.md")
    if not os.path.exists(f):
        sys.exit(f"FEHLER: {f} fehlt. Leg sie an mit der Zeile 'Deckel: <Zahl> Credits'.")
    txt = open(f, encoding="utf-8").read()
    m = re.search(r"Deckel:\s*([\d.]+)", txt)
    if not m:
        sys.exit(f"FEHLER: In {f} fehlt die Zeile 'Deckel: <Zahl> Credits'.")
    verbraucht = 0.0
    for zeile in txt.splitlines():
        teile = [t.strip() for t in zeile.strip().strip("|").split("|")]
        if len(teile) >= 5 and re.match(r"^[\d.]+$", teile[2]):
            verbraucht += float(teile[2])
    return f, float(m.group(1)), verbraucht


def eintragen(f, modell, cr, jid, out):
    txt = open(f, encoding="utf-8").read()
    if "| Datum |" not in txt:
        txt = txt.rstrip("\n") + "\n\n" + KOPF
    txt = txt.rstrip("\n") + f"\n| {time.strftime('%d.%m. %H:%M')} | {modell} | {cr:g} | {jid} | {os.path.basename(out)} |\n"
    open(f, "w", encoding="utf-8").write(txt)


def finde_url(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "result_url" and isinstance(v, str) and v.startswith("http"):
                return v
            r = finde_url(v)
            if r:
                return r
    if isinstance(o, list):
        for x in o:
            r = finde_url(x)
            if r:
                return r
    return None


def holen(jid, out):
    res = run(["generate", "wait", jid, "--json"], 1500)
    if res is None:
        sys.exit(f"Warten abgebrochen (25 Min). Der Job läuft weiter. Später: job.py holen --out {out} {jid}")
    try:
        url = finde_url(json.loads(res))
    except json.JSONDecodeError:
        m = re.search(r"https://\S+", res)
        url = m.group(0) if m else None
    if not url:
        sys.exit(f"FEHLER: kein Ergebnis für {jid}:\n{res.strip()[:800]}")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    urllib.request.urlretrieve(url, out)
    print(f"OK {out}")


def opt(args, name):
    if name in args:
        i = args.index(name)
        val = args[i + 1]
        del args[i:i + 2]
        return val
    return None


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ("kosten", "stand", "start", "holen"):
        sys.exit(__doc__)
    cmd = a.pop(0)
    if cmd == "kosten":
        print(f"{kosten(a[0], a[1:]):g} Credits")
        return
    projekt = opt(a, "--projekt")
    if not projekt:
        sys.exit("FEHLER: --projekt <ordner> fehlt.")
    f, deckel, verbraucht = ledger(projekt)
    if cmd == "stand":
        print(f"Verbraucht {verbraucht:g} von {deckel:g} Credits, frei {deckel - verbraucht:g}")
        return
    out = opt(a, "--out")
    if not out:
        sys.exit("FEHLER: --out <datei> fehlt.")
    out = out if os.path.isabs(out) else os.path.join(projekt, out)
    if cmd == "holen":
        holen(a[0], out)
        return
    modell, params = a[0], a[1:]
    cr = kosten(modell, params)
    if verbraucht + cr > deckel:
        sys.exit(f"STOPP: Job kostet {cr:g}, verbraucht {verbraucht:g}, Deckel {deckel:g}. "
                 f"Nichts gestartet. Deckel nur mit Ja des Nutzers erhöhen.")
    res = run(["generate", "create", modell, *params, "--json"], 120)
    jid = None
    if res:
        try:
            j = json.loads(res)
            if isinstance(j, list) and j:
                jid = j[0] if isinstance(j[0], str) else j[0].get("id")
            elif isinstance(j, dict):
                jid = j.get("id") or j.get("job_id") or (j.get("jobs") or [{}])[0].get("id")
        except json.JSONDecodeError:
            m = re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", res)
            jid = m.group(0) if m else None
    if not jid:
        sys.exit(f"FEHLER beim Start, keine Job-ID (meist nicht berechnet). Prüf 'higgsfield generate list'.\n{(res or 'Timeout')[:800]}")
    eintragen(f, modell, cr, jid, out)
    print(f"JOB-ID {jid} gestartet ({cr:g} Credits, jetzt {verbraucht + cr:g} von {deckel:g})", flush=True)
    holen(jid, out)


if __name__ == "__main__":
    main()
