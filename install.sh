#!/usr/bin/env bash
# Copies the kit's skills (and optionally an AGENTS.md template) into place for Codex.
# Local file copies only: no network access, no changes to Codex config.
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: bash install.sh [WORKSPACE] [--legacy | --repo] [--force]

  (default)  copy skills to ~/.agents/skills                (Codex user scope)
  --legacy   copy skills to ${CODEX_HOME:-~/.codex}/skills  (older Codex versions)
  --repo     copy skills to WORKSPACE/.agents/skills        (repo scope; ends up in WORKSPACE)
  WORKSPACE  also create WORKSPACE/AGENTS.md from templates/AGENTS.md if it does not exist
  --force    replace skill folders that already exist with the same name
EOF
}

KIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$KIT_DIR/.agents/skills"
MODE=user
WORKSPACE=""
FORCE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --legacy) MODE=legacy ;;
    --repo) MODE=repo ;;
    --force) FORCE=1 ;;
    -h|--help) usage; exit 0 ;;
    -*) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
    *) WORKSPACE="$1" ;;
  esac
  shift
done

case "$MODE" in
  user) DEST="$HOME/.agents/skills" ;;
  legacy) DEST="${CODEX_HOME:-$HOME/.codex}/skills" ;;
  repo)
    if [ -z "$WORKSPACE" ]; then
      echo "--repo needs a WORKSPACE argument" >&2
      exit 2
    fi
    DEST="$WORKSPACE/.agents/skills"
    ;;
esac

mkdir -p "$DEST"
count=0
for dir in "$SRC"/*/; do
  [ -f "$dir/SKILL.md" ] || continue
  dir="${dir%/}"
  name="$(basename "$dir")"
  if [ -e "$DEST/$name" ] && [ "$FORCE" -ne 1 ]; then
    echo "skip     $DEST/$name (exists; --force replaces it)"
    continue
  fi
  rm -rf "${DEST:?}/$name"
  cp -R "$dir" "$DEST/$name"
  echo "install  $DEST/$name"
  count=$((count + 1))
done
echo "$count skill(s) installed into $DEST"

if [ -n "$WORKSPACE" ]; then
  if [ -e "$WORKSPACE/AGENTS.md" ]; then
    echo "keep     $WORKSPACE/AGENTS.md (already exists; not modified)"
    echo "         merge useful parts by hand from $KIT_DIR/templates/AGENTS.md"
  else
    cp "$KIT_DIR/templates/AGENTS.md" "$WORKSPACE/AGENTS.md"
    echo "create   $WORKSPACE/AGENTS.md"
  fi
fi

cat <<EOF

Next: start Codex in the workspace and type /skills (or \$) to check the skills are listed.
Not listed? Restart Codex, or tell Codex: read $KIT_DIR/.agents/skills/kickoff/SKILL.md and follow it.
EOF
