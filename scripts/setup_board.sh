#!/usr/bin/env bash
set -euo pipefail

PROJECT_TITLE="Dayou Content Pipeline"
PIPELINE_FIELD="Pipeline Stage"
PIPELINE_OPTIONS="Idea,Script Draft,Review,Video,Published"
OWNER="${1:-@me}"

manual_setup() {
  cat <<EOF
Manual setup required.

1. Open GitHub Projects for ${OWNER}.
2. Create a new project named "${PROJECT_TITLE}".
3. Add a SINGLE_SELECT field named "${PIPELINE_FIELD}".
4. Add these options: Idea, Script Draft, Review, Video, Published.
5. Switch the layout to Board and group by "${PIPELINE_FIELD}".
6. Link the dayou-content repository so issues can be added to the board.
EOF
}

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    manual_setup
    exit 1
  fi
}

parse_project_number() {
  python3 -c '
import json, sys
payload = json.loads(sys.stdin.read() or "{}")
for key in ("number", "projectNumber"):
    if key in payload:
        print(payload[key])
        raise SystemExit(0)
print("")
'
}

require_command gh
require_command python3

if ! gh auth status >/dev/null 2>&1; then
  echo "gh CLI is not authenticated." >&2
  manual_setup
  exit 1
fi

echo "Creating GitHub Project: ${PROJECT_TITLE}"
if ! create_output="$(gh project create --owner "${OWNER}" --title "${PROJECT_TITLE}" --format json 2>/dev/null)"; then
  echo "Unable to create the project with gh. Check that your token has the 'project' scope." >&2
  manual_setup
  exit 1
fi

project_number="$(printf '%s' "${create_output}" | parse_project_number)"
if [[ -z "${project_number}" ]]; then
  echo "Project created, but the project number could not be parsed." >&2
  echo "Run 'gh project list --owner ${OWNER}' to find it, then add the field manually." >&2
  manual_setup
  exit 1
fi

echo "Creating field: ${PIPELINE_FIELD}"
if ! gh project field-create "${project_number}" \
  --owner "${OWNER}" \
  --name "${PIPELINE_FIELD}" \
  --data-type SINGLE_SELECT \
  --single-select-options "${PIPELINE_OPTIONS}" >/dev/null 2>&1; then
  echo "Project created, but the pipeline field could not be created automatically." >&2
  echo "Set it up manually in the project UI." >&2
  manual_setup
  exit 1
fi

cat <<EOF
Project created successfully.

Owner: ${OWNER}
Project: ${PROJECT_TITLE}
Project number: ${project_number}
Field: ${PIPELINE_FIELD}
Options: ${PIPELINE_OPTIONS}

Next manual steps in the GitHub UI:
- Switch the layout to Board.
- Group cards by "${PIPELINE_FIELD}".
- Link the dayou-content repository so content idea and weekly report issues can flow into the board.
EOF
