# 🛡️ AegisAI — Autonomous SOC-Style AI Security Engine

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Security](https://img.shields.io/badge/SOC-Automation-red.svg)
![ML](https://img.shields.io/badge/ML-Isolation%20Forest-orange.svg)
![Status](https://img.shields.io/badge/Status-Production--Ready-success.svg)
![License](https://img.shields.io/badge/License-Educational-lightgrey.svg)
![Stars](https://img.shields.io/github/stars/kitsunee0104/aegisai_tool?style=social)

---
## 🚀 Project Overview

**AegisAI** is a lightweight SOC (Security Operations Center) simulation engine that integrates:

- Real-time network reconnaissance  
- Packet-level traffic monitoring  
- Machine Learning-based anomaly detection  
- Risk-driven decision intelligence  

---

⚙️ Installation
1. Clone Repository
git clone git@github.com:kitsunee0104/aegisai_tool.git
cd AegisAI

3. Install Dependencies
pip install -r requirements.txt

OR 

pip install -e .

🚀 CLI Usage
Basic Scan
**aegisai 127.0.0.1**

Remote Target Scan
**aegisai google.com**

🔐 Privileged Execution (Packet Capture)

Since AegisAI performs packet sniffing, root privileges may be required:

run this command:
**sudo env "PATH=$PATH" aegisai 127.0.0.1**

📊 Sample Output
[+] AegisAI scanning: 127.0.0.1

--- RESULTS ---
Target: 127.0.0.1
Ports: [631]
Findings: ['IPP/CUPS Printing Service Detected']
Traffic: {
    packet_count: 177,
    connection_rate: 35.4,
    unique_ports: 3
}
AI Result: Normal
Decision: Medium Risk

---

## 🧠 Key Capabilities

✔ Automated Nmap-based port discovery  
✔ Live traffic capture using Scapy  
✔ Feature extraction from network behavior  
✔ Isolation Forest-based anomaly detection  
✔ Rule + AI hybrid decision engine  
✔ CLI-based SOC workflow simulation  

---


🧱 Technology Stack
Python 3.10+
Scapy (Packet Analysis)
Nmap (Network Reconnaissance)
NumPy (Feature Engineering)
Scikit-learn (Machine Learning)
Isolation Forest Algorithm

⚠️ Disclaimer
This project is intended strictly for:
Educational purposes
Cybersecurity research
