#!/usr/bin/env bash
# Link these skills into ~/.claude/skills so Claude Code can find them.
#
#   ./install.sh                      link everything
#   ./install.sh --only a b c         link just those
#   ./install.sh --uninstall          remove links this script made
#   ./install.sh --dry-run            show what would happen
#
# Symlinks, not copies: `git pull` then updates every skill at once. Anything
# already in ~/.claude/skills that this script did not create is left alone.

set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${HOME}/.claude/skills"

MODE=link
DRY=false
ONLY=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --uninstall) MODE=uninstall; shift ;;
    --dry-run)   DRY=true; shift ;;
    --only)      shift; ONLY="$*"; break ;;
    -h|--help)   sed -n '2,12p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)           echo "Unknown option: $1 (try --help)" >&2; exit 1 ;;
  esac
done

mkdir -p "$DEST"

linked=0; skipped=0; removed=0

# A link is "ours" when it points inside this repo.
points_here() {
  local t; t="$(readlink "$1" 2>/dev/null)" || return 1
  case "$t" in "$SRC"/*) return 0 ;; *) return 1 ;; esac
}

if [[ "$MODE" == uninstall ]]; then
  for l in "$DEST"/*; do
    [[ -L "$l" ]] || continue
    if points_here "$l"; then
      $DRY && echo "  would remove $(basename "$l")" || { rm "$l"; removed=$((removed+1)); }
    fi
  done
  $DRY || echo "Removed $removed link(s). Anything not created by this script was left alone."
  exit 0
fi

# Which skills to link: the explicit list, or every directory holding a SKILL.md.
list_skills() {
  if [[ -n "$ONLY" ]]; then
    for n in $ONLY; do echo "$n"; done
  else
    for d in "$SRC"/*/; do
      [[ -f "${d}SKILL.md" ]] && basename "$d"
    done
  fi
}

while IFS= read -r name; do
  [[ -n "$name" ]] || continue
  src="${SRC}/${name}"
  dst="${DEST}/${name}"

  if [[ ! -f "${src}/SKILL.md" ]]; then
    echo "  no such skill: ${name}" >&2; continue
  fi

  if [[ -e "$dst" || -L "$dst" ]]; then
    if points_here "$dst"; then
      :                                  # already ours, nothing to do
    else
      echo "  skipped ${name} (something else is already there)"
      skipped=$((skipped+1))
    fi
    continue
  fi

  if $DRY; then echo "  would link ${name}"; else ln -s "$src" "$dst"; fi
  linked=$((linked+1))
done < <(list_skills)

if $DRY; then
  echo "Dry run: ${linked} to link, ${skipped} already occupied."
else
  echo "Linked ${linked} skill(s) into ${DEST}."
  [[ $skipped -gt 0 ]] && echo "Skipped ${skipped} where a file already existed."
  echo "Check with: ls ${DEST} | head"
fi
