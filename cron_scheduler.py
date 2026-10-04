import time
import subprocess
import os
import sys
from datetime import datetime, timedelta

# Always ensure working directory is the script's root directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

from config.settings import scheduler_interval_hours, run_scheduler

def run_bot() -> int:
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting LinkedIn AI Bot run...")
    try:
        # Using sys.executable to ensure we use the same python interpreter
        env = os.environ.copy()
        process = subprocess.Popen([sys.executable, "runAiBot.py"], env=env)
        exit_code = process.wait()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Bot run completed with exit code: {exit_code}")
        return exit_code
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error running bot: {e}")
        return 1

def main():
    # If invoked with --once or RUN_CRON=1, run single iteration (for Linux cron / CLI trigger)
    if "--once" in sys.argv or "-1" in sys.argv:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running single bot execution (--once)...")
        code = run_bot()
        sys.exit(code)

    if not run_scheduler:
        print("Scheduler is disabled in config/settings.py. Set run_scheduler = True to enable, or use '--once' to run once.")
        return

    print(f"LinkedIn AI Bot Scheduler started. Interval: {scheduler_interval_hours} hours.")
    
    try:
        while True:
            run_bot()
            
            next_run = datetime.now() + timedelta(hours=scheduler_interval_hours)
            print(f"Next run scheduled at: {next_run.strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Sleep in small increments to allow for keyboard interrupt
            sleep_time = int(scheduler_interval_hours * 3600)
            while sleep_time > 0:
                time.sleep(min(60, sleep_time))
                sleep_time -= 60
                
    except KeyboardInterrupt:
        print("\nScheduler stopped by user.")

if __name__ == "__main__":
    main()
