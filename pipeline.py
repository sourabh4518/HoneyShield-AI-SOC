import json
import time
import sqlite3
from feature_extractor import extract_features
from ai_classifier import predict_attack

LOG_FILE = "var/log/cowrie/cowrie.json"
DB_FILE = "honeyshield.db"

def process_live_logs():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                try:
                    data = json.loads(line)
                    event = data.get("eventid", "")
                    ip = data.get("src_ip", "")
                    ts = data.get("timestamp", "")

                    if "login" in event:
                        user = data.get("username", "")
                        pwd = data.get("password", "")
                        features = extract_features({"command": "", "password": pwd})
                        attack_type, confidence = predict_attack(features)
                        
                        cursor.execute('''
                            INSERT OR IGNORE INTO attacks 
                            (timestamp, src_ip, username, password, command, mitre_id, ai_attack_type, ai_confidence)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (ts, ip, user, pwd, "LOGIN ATTEMPT", "T1110", attack_type, confidence))

                    elif "command" in event:
                        cmd = data.get("input", "")
                        features = extract_features({"command": cmd, "password": ""})
                        attack_type, confidence = predict_attack(features)
                        
                        cursor.execute('''
                            INSERT OR IGNORE INTO attacks 
                            (timestamp, src_ip, username, password, command, mitre_id, ai_attack_type, ai_confidence)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (ts, ip, "", "", cmd, "T1059", attack_type, confidence))

                except Exception:
                    pass
    except FileNotFoundError:
        pass

    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Real-Time AI Processing Pipeline Running... (Press Ctrl+C to stop)")
    while True:
        process_live_logs()
        time.sleep(3)
