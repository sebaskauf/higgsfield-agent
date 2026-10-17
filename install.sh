#!/usr/bin/env bash
# Installiert den higgsfield-video-Agenten für Claude Code.
#   Agent-Datei    -> ~/.claude/agents/higgsfield-video.md
#   Werkzeuge      -> ~/.claude/higgsfield-video/ (tools/ + referenz/)
# Dein PROFIL.md dort bleibt bei Updates stehen. Bestehende Agenten werden nie
# ohne ausdrückliche Ansage überschrieben.
#
#   ./install.sh                  installiert, fragt bei Kollision nach
#   ./install.sh --force          überschreibt (sichert vorher mit Zeitstempel)
#   ./install.sh --name ki-video  installiert unter anderem Namen
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CFG="${CLAUDE_CONFIG_DIR:-${HOME}/.claude}"
NAME="higgsfield-video"
FORCE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --force) FORCE=1; shift ;;
    --name)  NAME="${2:-}"; [ -n "$NAME" ] || { echo "FEHLER: --name braucht einen Wert."; exit 1; }; shift 2 ;;
    -h|--help) sed -n '2,10p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "FEHLER: unbekannte Option '$1'."; exit 1 ;;
  esac
done

QUELLE="${REPO}/agent/higgsfield-video.md"
[ -f "$QUELLE" ] || { echo "FEHLER: $QUELLE fehlt."; exit 1; }

ZIEL_AGENTS="${CFG}/agents"
HEIM="${CFG}/${NAME}"
DATEI="${ZIEL_AGENTS}/${NAME}.md"
mkdir -p "$ZIEL_AGENTS"

if [ -f "$DATEI" ] && [ "$FORCE" -eq 0 ] && ! grep -q "higgsfield-video" "$DATEI"; then
  echo "Es liegt schon ein anderer Agent unter ${DATEI}:"
  echo
  sed -n '1,6p' "$DATEI" | sed 's/^/  /' | cut -c1-160
  echo
  echo "Der wird NICHT überschrieben. Du hast zwei Möglichkeiten:"
  echo "  ./install.sh --force           überschreiben (vorher wird gesichert)"
  echo "  ./install.sh --name ki-video   unter anderem Namen installieren"
  echo
  echo "Es wurde nichts verändert."
  exit 2
fi

if [ -f "$DATEI" ]; then
  BACKUP="${DATEI}.bak-$(date +%Y%m%d-%H%M%S)"
  cp "$DATEI" "$BACKUP"
  echo "Vorhandene Version gesichert: $BACKUP"
fi

# Werkzeuge + Referenzen (PROFIL.md im Heimordner bleibt unangetastet)
mkdir -p "${HEIM}/tools" "${HEIM}/referenz"
cp "${REPO}"/tools/*.py "${HEIM}/tools/"
cp "${REPO}"/referenz/*.md "${HEIM}/referenz/"
# Lernlog gehört dem Nutzer: nur anlegen, wenn er fehlt, nie überschreiben
[ -f "${HEIM}/LERNLOG.md" ] || cp "${REPO}/referenz/LERNLOG-START.md" "${HEIM}/LERNLOG.md"

# Agent-Datei mit echtem Pfad und ggf. neuem Namen
sed -e "s#__AGENT_HOME__#${HEIM}#g" "$QUELLE" > "$DATEI"
if [ "$NAME" != "higgsfield-video" ]; then
  perl -0pi -e "s/^name: higgsfield-video\$/name: ${NAME}/m" "$DATEI"
fi

echo "Installiert als '${NAME}':"
echo "  Agent:      ${DATEI}"
echo "  Werkzeuge:  ${HEIM}/tools"
echo "  Referenzen: ${HEIM}/referenz"
[ -f "${HEIM}/PROFIL.md" ] && echo "  Dein Profil ist geblieben: ${HEIM}/PROFIL.md"

command -v python3 >/dev/null || echo "HINWEIS: python3 fehlt noch. Das Setup im Agenten installiert es mit dir."
command -v ffmpeg  >/dev/null || echo "HINWEIS: ffmpeg fehlt noch. Das Setup im Agenten installiert es mit dir."
echo
echo "Wenn du gerade den Setup-Prompt abarbeitest, geht es direkt weiter."
echo "Rufst du den Agenten dagegen jetzt zum ersten Mal auf, starte Claude Code einmal neu."
