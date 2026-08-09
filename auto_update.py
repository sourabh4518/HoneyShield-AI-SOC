import time
import subprocess

print("🔄 Auto-updater started! Checking every 15 seconds...")

while True:
    subprocess.run(["python3", "database.py"])
    print("✅ Database updated:", time.strftime("%H:%M:%S"))
    time.sleep(15)
