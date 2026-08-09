import sqlite3

def init_db():
    conn = sqlite3.connect("honeyshield.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            src_ip TEXT,
            username TEXT,
            password TEXT,
            command TEXT,
            mitre_id TEXT,
            ai_attack_type TEXT,
            ai_confidence REAL,
            UNIQUE(timestamp, src_ip, username, command)
        )
    ''')
    conn.commit()
    conn.close()
    print("Database ready with AI classification columns!")

if __name__ == "__main__":
    init_db()
