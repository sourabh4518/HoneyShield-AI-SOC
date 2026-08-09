import time
from twilio.rest import Client

# Twilio Credentials (Placeholders)
ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
TWILIO_NUMBER = 'YOUR_TWILIO_NUMBER'

# Target Phone Number
YOUR_PHONE_NUMBER = 'YOUR_PHONE_NUMBER'

last_call_time = 0
last_attack_time = 0
INACTIVITY_TIMEOUT = 1800  
COOLDOWN_PERIOD = 18000    

def trigger_classified_voice_alert(attack_source, ip_address, attack_detail):
    global last_call_time, last_attack_time
    current_time = time.time()
    
    time_since_last_call = current_time - last_call_time
    time_since_last_attack = current_time - last_attack_time

    is_new_session = (time_since_last_attack > INACTIVITY_TIMEOUT)
    is_cooldown_over = (time_since_last_call > COOLDOWN_PERIOD)

    if is_cooldown_over or (is_new_session and last_call_time != 0) or last_call_time == 0:
        try:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            
            twiml_message = f"""
            <Response>
                <Say voice="alice">
                    Security Warning! HoneyShield has detected an attack on your {attack_source}. 
                    Threat detail: {attack_detail}, originating from I.P. address {ip_address}. 
                    Please check your dashboard for further insights.
                </Say>
            </Response>
            """

            call = client.calls.create(
                twiml=twiml_message,
                to=YOUR_PHONE_NUMBER,
                from_=TWILIO_NUMBER
            )
            
            last_call_time = current_time
            last_attack_time = current_time
            print(f"[📞 CALL ALERT SENT] Source: {attack_source} | SID: {call.sid}")

        except Exception as e:
            print(f"[-] Twilio Call Failed: {e}")
    else:
        last_attack_time = current_time
        print(f"[i] Continuous attack on {attack_source} | Call suppressed by cooldown logic.")

if __name__ == "__main__":
    print("[+] Testing Voice Alert System...")
    trigger_classified_voice_alert("Web Application", "127.0.0.1", "SQL Injection Attempt")
