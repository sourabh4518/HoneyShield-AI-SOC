# MITRE ATT&CK Mapper
# Sourabh ka Star Feature!

MITRE_MAP = {
    "whoami":        ("T1033", "System Owner Discovery"),
    "cat /etc/passwd": ("T1003", "OS Credential Dumping"),
    "ls":            ("T1083", "File & Directory Discovery"),
    "uname":         ("T1082", "System Info Discovery"),
    "wget":          ("T1105", "Ingress Tool Transfer"),
    "curl":          ("T1105", "Ingress Tool Transfer"),
    "netstat":       ("T1049", "Network Connections Discovery"),
    "ps":            ("T1057", "Process Discovery"),
    "chmod":         ("T1222", "File Permissions Modification"),
    "useradd":       ("T1136", "Create Account"),
    "passwd":        ("T1098", "Account Manipulation"),
    "ssh":           ("T1021", "Remote Services"),
    "nc":            ("T1059", "Command & Scripting"),
    "python":        ("T1059", "Command & Scripting"),
    "bash":          ("T1059", "Command & Scripting"),
}

import json

log_file = "var/log/cowrie/cowrie.json"

print("="*60)
print("  MITRE ATT&CK THREAT ANALYSIS REPORT")
print("  By: Sourabh | HoneyShield Project")
print("="*60)

found_techniques = []

with open(log_file, "r") as f:
    for line in f:
        try:
            data = json.loads(line)
            if "command" in data.get("eventid", ""):
                cmd = data.get("input", "")
                ip  = data.get("src_ip", "")
                ts  = data.get("timestamp", "")
                
                for keyword, (tid, tname) in MITRE_MAP.items():
                    if keyword in cmd:
                        print(f"\n⚔️  TECHNIQUE DETECTED!")
                        print(f"   Command   : {cmd}")
                        print(f"   MITRE ID  : {tid}")
                        print(f"   Technique : {tname}")
                        print(f"   Attacker  : {ip}")
                        print(f"   Time      : {ts}")
                        found_techniques.append(tid)
        except:
            pass

print("\n" + "="*60)
print("SUMMARY:")
print(f"Total Techniques Used: {len(set(found_techniques))}")
for t in set(found_techniques):
    print(f"  → {t}")
print("="*60)
