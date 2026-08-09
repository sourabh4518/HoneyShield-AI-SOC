import json

log_file = "var/log/cowrie/cowrie.json"

print("="*50)
print("HONEYPOT ATTACK LOGS")
print("="*50)

with open(log_file, "r") as f:
    for line in f:
        try:
            data = json.loads(line)
            event = data.get("eventid", "")
            
            if "login" in event:
                print(f"\n🔴 LOGIN ATTEMPT")
                print(f"   IP       : {data.get('src_ip')}")
                print(f"   Username : {data.get('username')}")
                print(f"   Password : {data.get('password')}")
                print(f"   Time     : {data.get('timestamp')}")
                
            elif "command" in event:
                print(f"\n⚡ COMMAND RAN")
                print(f"   IP      : {data.get('src_ip')}")
                print(f"   Command : {data.get('input')}")
                print(f"   Time    : {data.get('timestamp')}")
                
            elif "connect" in event:
                print(f"\n🟡 CONNECTION")
                print(f"   IP   : {data.get('src_ip')}")
                print(f"   Port : {data.get('src_port')}")
                print(f"   Time : {data.get('timestamp')}")
        except:pass
