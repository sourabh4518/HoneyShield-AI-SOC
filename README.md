# 🛡️ HoneyShield: Real-Time IoT AI SOC Threat Intelligence Dashboard

HoneyShield is an advanced AI-powered Security Operations Center (SOC) threat intelligence platform designed to transform raw honeypot logs into structured, actionable insights. Built around the **Cowrie Medium-Interaction Honeypot**, it combines Machine Learning threat classification, MITRE ATT&CK tactic mapping, and real-time visualization into a single unified dashboard.

---

## ✨ Key Features

* 🍯 **Medium-Interaction Honeypot:** Captures unauthorized SSH & Telnet brute-force probes and shell commands in an isolated environment.
* ⚡ **15-Second Automated Pipeline:** A background daemon (`auto_update.py`) continuously scans raw Cowrie logs and updates a structured SQLite database every 15 seconds.
* 🧠 **8-Category ML Threat Classifier:** Evaluates raw attacker shell commands using a trained machine learning model and calculates exact confidence percentage scores.
* 🎯 **MITRE ATT&CK Framework Mapping:** Automatically tags incoming malicious commands to official MITRE tactic and technique IDs (`mitre_mapper.py`).
* 📊 **Real-Time SOC Dashboard:** Built with Streamlit, featuring time-window filters (*1 Hr / 24 Hr / Historical*), live incident log tables, and 1-click PDF Threat Report export.

---

## 🛠️ Technology Stack

* **Operating System:** Kali Linux
* **Language:** Python 3
* **Honeypot Framework:** Cowrie SSH/Telnet
* **Database:** SQLite3 (`honeyshield.db`)
* **Machine Learning & Processing:** Scikit-Learn, Pandas, NumPy
* **Dashboard Frontend:** Streamlit
* **Reporting:** FPDF
