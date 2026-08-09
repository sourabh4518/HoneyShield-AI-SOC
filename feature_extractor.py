import re

def extract_features(event_data):
    """
    Extracts 9 numerical features from honeypot events for AI model.
    """
    command = event_data.get("command", "")
    pwd = event_data.get("password", "")
    
    cmd_len = len(command)
    
    # 1. Malware Download
    has_download = 1 if re.search(r'(wget|curl|tftp|ftpget)', command, re.IGNORECASE) else 0
    
    # 2. Execution / Permissions
    has_exec = 1 if re.search(r'(chmod|sh|busybox|killall|\.sh)', command, re.IGNORECASE) else 0
    
    # 3. Reconnaissance / System Info
    has_recon = 1 if re.search(r'(uname|proc|ifconfig|route|ps|whoami|id)', command, re.IGNORECASE) else 0
    
    # 4. Default IoT Password Match
    has_default_pass = 1 if pwd in ['admin', '123456', 'root', 'support', 'xc3511', 'vizpon'] else 0

    # 5. Privilege Escalation (NEW)
    has_privesc = 1 if re.search(r'(sudo|su|chown|chmod\s\+s|setuid)', command, re.IGNORECASE) else 0

    # 6. Persistence (NEW)
    has_persistence = 1 if re.search(r'(crontab|systemctl|init\.d|rc\.local|service)', command, re.IGNORECASE) else 0

    # 7. Denial of Service / Flood (NEW)
    has_dos = 1 if re.search(r'(ping\s+-f|hping|flood|slowloris|ddos)', command, re.IGNORECASE) else 0

    # 8. Log Tampering / Clearing Tracks (NEW)
    has_log_tamper = 1 if re.search(r'(rm\s+-rf|clear|unset|history\s+-c|/dev/null)', command, re.IGNORECASE) else 0

    return [cmd_len, has_download, has_exec, has_recon, has_default_pass, has_privesc, has_persistence, has_dos, has_log_tamper]
