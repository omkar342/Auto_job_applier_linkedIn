#!/bin/bash
# ==============================================================================
# LinkedIn AI Bot - Automated Cron Job Runner
# ==============================================================================

# Directory where this script resides
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

# Environment settings for cron execution (GUI + Headless support)
export PATH="/home/omkar/anaconda3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH"
export DISPLAY="${DISPLAY:-:0}"
export WAYLAND_DISPLAY="${WAYLAND_DISPLAY:-wayland-0}"
export XDG_RUNTIME_DIR="/run/user/$(id -u)"
export DBUS_SESSION_BUS_ADDRESS="unix:path=$XDG_RUNTIME_DIR/bus"

# Automatically find GNOME / Mutter / Wayland Xauthority if not already set
if [ -z "$XAUTHORITY" ]; then
    AUTH_FILE=$(ls -t "$XDG_RUNTIME_DIR"/.*auth* 2>/dev/null | head -n 1)
    if [ -n "$AUTH_FILE" ]; then
        export XAUTHORITY="$AUTH_FILE"
    elif [ -f "$HOME/.Xauthority" ]; then
        export XAUTHORITY="$HOME/.Xauthority"
    fi
fi

export RUN_CRON=1
export PYTHONUNBUFFERED=1

# Specify Python binary (Anaconda Python)
PYTHON_BIN="/home/omkar/anaconda3/bin/python3"
if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="$(which python3)"
fi

# Ensure log directory exists
LOG_DIR="$SCRIPT_DIR/logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/cron.log"

# Prevent concurrent overlapping runs
LOCK_FILE="/tmp/linkedin_ai_bot.lock"
if [ -f "$LOCK_FILE" ]; then
    OLD_PID=$(cat "$LOCK_FILE" 2>/dev/null)
    if [ -n "$OLD_PID" ] && kill -0 "$OLD_PID" 2>/dev/null; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Another instance of LinkedIn Bot is currently running (PID $OLD_PID). Skipping this run." >> "$LOG_FILE"
        exit 0
    else
        # Stale lock
        rm -f "$LOCK_FILE"
    fi
fi

# Write current PID to lock file
echo $$ > "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT

# Check operating hours (between 09:00 and 18:00 max)
CURRENT_HOUR=$(date +%-H)
CURRENT_MIN=$(date +%-M)
if [ "$CURRENT_HOUR" -gt 18 ] || ([ "$CURRENT_HOUR" -eq 18 ] && [ "$CURRENT_MIN" -gt 0 ]); then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Current time is past 6:00 PM ($CURRENT_HOUR:$CURRENT_MIN). Skipping cron execution." >> "$LOG_FILE"
    exit 0
fi

if [ "$CURRENT_HOUR" -lt 9 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Current time is before 9:00 AM ($CURRENT_HOUR:$CURRENT_MIN). Skipping cron execution." >> "$LOG_FILE"
    exit 0
fi

# Check daily auto-applied limit (max 50 jobs per day)
TODAY_COUNT=$("$PYTHON_BIN" -c "from modules.helpers import count_today_easy_applied_jobs; print(count_today_easy_applied_jobs())" 2>/dev/null || echo 0)
if [ "$TODAY_COUNT" -ge 50 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Daily auto-apply limit of 50 jobs reached today ($TODAY_COUNT applied). Skipping cron execution." >> "$LOG_FILE"
    exit 0
fi

echo "==============================================================================" >> "$LOG_FILE"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Cron job triggered (Applied today: $TODAY_COUNT/50): Starting LinkedIn AI Bot..." >> "$LOG_FILE"

# Execute bot once
"$PYTHON_BIN" cron_scheduler.py --once >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Bot execution completed with exit code: $EXIT_CODE" >> "$LOG_FILE"
echo "==============================================================================" >> "$LOG_FILE"

exit $EXIT_CODE
