import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Sample Training Dataset: [cmd_len, download, exec, recon, default_pass, privesc, persistence, dos, log_tamper]
X_train = np.array([
    [5, 0, 0, 1, 0, 0, 0, 0, 0],   # Reconnaissance (uname, whoami)
    [0, 0, 0, 0, 1, 0, 0, 0, 0],   # Brute Force (default pass)
    [45, 1, 1, 0, 0, 0, 0, 0, 0],  # RCE (wget + chmod)
    [60, 1, 1, 1, 0, 0, 0, 0, 0],  # Botnet (Mirai script)
    [10, 0, 0, 0, 0, 1, 0, 0, 0],  # Privilege Escalation (sudo su)
    [20, 0, 0, 0, 0, 0, 1, 0, 0],  # Persistence (crontab -e)
    [25, 0, 0, 0, 0, 0, 0, 1, 0],  # DoS (ping -f)
    [15, 0, 0, 0, 0, 0, 0, 0, 1],  # Log Tampering (rm -rf /var/log)
])

# Labels matching above categories
y_train = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, 'iot_attack_classifier.pkl')
print("AI Model Re-Trained Successfully with 8 Attack Categories!")

CLASSES = {
    0: "Reconnaissance", 
    1: "Brute Force", 
    2: "Remote Code Execution (RCE)", 
    3: "Botnet Activity",
    4: "Privilege Escalation",
    5: "Persistence",
    6: "Denial of Service (DoS)",
    7: "Log Tampering"
}

def predict_attack(feature_vector):
    loaded_model = joblib.load('iot_attack_classifier.pkl')
    prediction = loaded_model.predict([feature_vector])[0]
    probabilities = loaded_model.predict_proba([feature_vector])[0]
    confidence = round(max(probabilities) * 100, 2)
    return CLASSES[prediction], confidence

if __name__ == "__main__":
    test_feature = [10, 0, 0, 0, 0, 1, 0, 0, 0] # Test Privilege Escalation
    attack_type, conf = predict_attack(test_feature)
    print(f"Test Prediction: {attack_type} (Confidence: {conf}%)")
