#!/bin/bash
# ==============================================================================
# LinkedIn AI Bot - Automated Cron Job Runner
# ==============================================================================

# Directory where this script resides
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

# Environment settings for cron execution (GUI + Headless support)
export DISPLAY="${DISPLAY:-:0}"
export WAYLAND_DISPLAY="${WAYLAND_DISPLAY:-wayland-0}"
export XDG_RUNTIME_DIR="/run/user/$(id -u)"
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

echo "==============================================================================" >> "$LOG_FILE"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Cron job triggered: Starting LinkedIn AI Bot..." >> "$LOG_FILE"

# Execute bot once
"$PYTHON_BIN" cron_scheduler.py --once >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Bot execution completed with exit code: $EXIT_CODE" >> "$LOG_FILE"
echo "==============================================================================" >> "$LOG_FILE"

exit $EXIT_CODE
