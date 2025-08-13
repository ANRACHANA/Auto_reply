import subprocess
import time
import sys

BOT_SCRIPT = "main.py"  # ឈ្មោះ script bot
RESTART_DELAY = 5  # វិនាទីចាំមុន restart

def run_bot():
    while True:
        print(f"[Watchdog] Starting {BOT_SCRIPT} ...")
        process = subprocess.Popen([sys.executable, BOT_SCRIPT])
        process.wait()
        print(f"[Watchdog] {BOT_SCRIPT} stopped. Restarting in {RESTART_DELAY} seconds...")
        time.sleep(RESTART_DELAY)

if __name__ == "__main__":
    run_bot()
