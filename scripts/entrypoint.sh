#!/usr/bin/env bash
# safety switch, exit script if there's error. Full command of shortcut `set -e`
set -o errexit
# safety switch, uninitialized variables will stop script. Full command of shortcut `set -u`
set -o nounset
cmd="$*"

if [ "$FLASK_ENV" = "development" ]; then
  # flask db init
  flask db migrate -m "Update migration."
  flask db upgrade
else
  flask db migrate -m "Update migration."
  flask db upgrade
fi

# After running conditional migrations start gunicorn server
# Prepare log files and start outputting logs to stdout
touch ./logs/gunicorn-access.log
touch ./logs/gunicorn-error.log
tail -n 0 -f ./logs/gunicorn*.log &
gunicorn
    
exec "$cmd"
