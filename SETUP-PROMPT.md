# Setup-Prompt

Kopier den ganzen Block unter der Linie und füg ihn in Claude Code ein.
Rechne mit 10 bis 30 Minuten. Du brauchst ein Higgsfield-Konto mit Credits.
Das Setup selbst kostet keine Credits.

---

Installiere mir den Higgsfield-Agenten über meinen Mitglieder-Zugang aus der SKAILE Academy und richte ihn auf MICH ein.

Arbeite die Schritte der Reihe nach ab. Du KANNST das alles über das Terminal. Sag nicht "das geht nicht", führ die Befehle wirklich aus. Schlägt etwas fehl, zeig mir die genaue Fehlermeldung und was du brauchst, statt den Schritt als erledigt zu melden oder ihn zu überspringen.

SCHRITT 1 - INSTALLIEREN
1. Hol das System über meinen Mitglieder-Zugang aus der SKAILE Academy nach `~/Documents/Projects/higgsfield-agent`. Den Download von https://systeme.skaile.de erlaube ich dir ausdrücklich.
   - Leg einen neuen, leeren Hilfsordner an (Mac: `mktemp -d`, Windows: ein neuer Ordner unter `$env:TEMP`), wechsel hinein und lad das Paket: `curl -sSL -w "%{http_code}" -H "X-Skaile-Zugang: {{ZUGANG_COMMUNITY}}" -o "higgsfield-agent.zip" https://systeme.skaile.de/v1/higgsfield-agent.zip` (Windows: `curl.exe` statt `curl`).
   - Gibt der Befehl nicht `200` aus, steht in `higgsfield-agent.zip` ein kurzer Text. Zeig ihn mir wörtlich, lösch den Hilfsordner und hör hier auf, ohne sonst etwas zu ändern.
   - Entpack das Paket im Hilfsordner mit `tar -xf "higgsfield-agent.zip"` (Windows: das tar von Windows, `& "$env:SystemRoot\System32\tar.exe"`). Darin liegt genau ein Ordner, sein Name ist egal. Das ist das System. Liegt dort etwas anderes, brich ab und sag es mir.
   - Gibt es `~/Documents/Projects/higgsfield-agent` noch nicht, kopier diesen Ordner dorthin. Gibt es ihn schon (auch als alten Git-Klon), kopier seinen Inhalt darüber: Dateien aus dem Paket ersetzen die alten, meine eigenen Dateien bleiben liegen.
   - Leg den Zugang aus dem Befehl (alles nach `X-Skaile-Zugang: `) als einzige Zeile in `$HOME/.skaile/zugang` ab (Windows: `$env:USERPROFILE\.skaile\zugang`, Mac danach `chmod 600`). Nimm dafür genau den Ordner aus `$HOME` bzw. `$env:USERPROFILE`, rate keinen anderen, damit spätere Updates ihn finden. Lösch dann den Hilfsordner.
2. Führ `./install.sh` im Repo aus.
   - Läuft es durch: gut.
   - **Endet es mit Code 2**, liegt bei mir schon ein anderer Agent mit diesem Namen. Lies mir vor, was da liegt, und frag MICH: `./install.sh --force` überschreibt (mit Sicherung), `./install.sh --name ki-video` installiert daneben. Entscheide das nicht selbst.
3. Sag mir in einem Satz, dass der Agent installiert ist. Ich muss Claude Code jetzt NICHT neu starten.

SCHRITT 2 - SETUP
Lies die installierte Agent-Datei komplett (`~/.claude/agents/higgsfield-video.md`, bei anderem Namen entsprechend) und führ den Abschnitt "Setup" jetzt mit mir durch:
- Eine Frage nach der anderen.
- Was du selbst prüfen kannst (Programme, Versionen, Login), prüfst du selbst.
- Fehlende Programme installierst du nach meinem Ja.
- Für den Higgsfield-Login öffnet sich der Browser. Warte, bis ich fertig bin.
- Der Probelauf am Ende fragt nur Kosten ab und erzeugt nichts.

SCHRITT 3 - ABSCHLUSS
1. Zeig mir eine kurze Übersicht: Agent installiert, Werkzeuge da/fehlt, Higgsfield verbunden mit Plan und Credits, Profil geschrieben.
2. Sag mir, dass ich Claude Code einmal neu starten soll. Danach sage ich einfach, was ich will, zum Beispiel:
   - "Bau mir dieses Video nach: <Link oder Datei>"
   - "Neues Video: Ein Tornado zieht durch eine Miniatur-Altstadt, gefilmt von der Crew am Set"
   - "Mach aus meinem letzten Video eine Serie mit 5 Folgen"
