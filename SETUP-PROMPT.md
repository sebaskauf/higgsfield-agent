# Setup-Prompt

Kopier den ganzen Block unter der Linie und füg ihn in Claude Code ein.
Rechne mit 10 bis 15 Minuten. Du brauchst ein Higgsfield-Konto mit Credits.
Das Setup selbst kostet keine Credits.

---

Installiere mir den Higgsfield-Agenten aus diesem Repo und richte ihn auf MICH ein: https://github.com/sebaskauf/higgsfield-agent

Arbeite die Schritte der Reihe nach ab. Du KANNST das alles über das Terminal. Sag nicht "das geht nicht", führ die Befehle wirklich aus. Schlägt etwas fehl, zeig mir die genaue Fehlermeldung und was du brauchst, statt den Schritt als erledigt zu melden oder ihn zu überspringen.

SCHRITT 1 - INSTALLIEREN
1. `git clone https://github.com/sebaskauf/higgsfield-agent.git ~/Documents/Projects/higgsfield-agent` (existiert der Ordner schon: dort `git pull`).
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
