# AegisAI

**AegisAI** is an intelligent network security analysis tool that combines network reconnaissance, live traffic monitoring, machine learning-based anomaly detection, and automated risk assessment into a unified command-line interface. It is designed to assist security analysts, penetration testers, and defenders in rapidly identifying suspicious network activity and potential security risks.

---

## Key Features

### 🔍 Network Reconnaissance

AegisAI performs automated network scanning to identify exposed services and gather security-relevant information.

* Open port discovery
* Service identification
* Host profiling
* Rapid target enumeration

---

### 📡 Live Traffic Monitoring

Monitor network activity in real time to collect behavioral indicators and traffic statistics.

* Packet capture and analysis
* Connection rate monitoring
* Network activity profiling
* Unique port tracking

> Root privileges are required for packet capture functionality.

---

### 🤖 AI-Powered Anomaly Detection

AegisAI uses machine learning techniques to analyze collected telemetry and identify abnormal behavior.

* Isolation Forest-based anomaly detection
* Automated feature extraction
* Behavioral pattern analysis
* Real-time anomaly classification

---

### 🧠 Security Decision Engine

Correlates scan findings and behavioral indicators to generate actionable security assessments.

* Risk scoring
* Threat classification
* Automated decision making
* Security posture evaluation

---

### ⚡ Portable CLI Experience

Designed as a lightweight command-line security utility for Linux environments.

* pip-installable package
* Cross-distribution compatibility
* Minimal setup requirements
* Automated model initialization

---

## How It Works

AegisAI follows a multi-stage security analysis workflow:

1. **Target Intake** – Accept IP address or hostname.
2. **Network Scan** – Discover exposed ports and services.
3. **Traffic Monitoring** – Collect live network telemetry.
4. **Feature Extraction** – Build analysis vectors from collected data.
5. **AI Analysis** – Perform anomaly detection using machine learning.
6. **Decision Engine** – Generate final risk assessment.
7. **Reporting** – Present consolidated findings to the operator.

---

## Quick Start

### Prerequisites

* Python 3.10+
* Linux Operating System
* Nmap
* Scapy-compatible environment
* Root privileges (for packet monitoring)

---

### Installation (ToDo)

Clone the repository:

```bash
- git clone https://github.com/kitsunee0104/aegisai_tool.git
- cd aegisai_tool
```

Install the package:

```bash
- pip install -e .
```

Or install using pipx:

```bash
- pipx install .
```

---

## Usage

### Standard Scan

```bash
aegisai
```

Example:

```text
Enter target IP or Hostname: 127.0.0.1
```

---

### Traffic-Aware Scan (Recommended)

```bash
sudo env "PATH=$PATH" aegisai
```

This enables packet capture and live traffic monitoring.

---

## Example Output

```text
--- RESULTS ---

Target: 127.0.0.1

Ports:
[631, 5900]

Findings:
['IPP/CUPS Printing Service Detected']

Traffic:
{
    'packet_count': 373,
    'connection_rate': 74.6,
    'unique_ports': 3
}

AI Result:
Normal

Decision:
Medium Risk
```

---

## Core Components

| Component       | Purpose                                         |
| --------------- | ----------------------------------------------- |
| Scanner         | Network reconnaissance and port discovery       |
| Traffic Monitor | Live packet collection and telemetry generation |
| Analyzer        | Security-focused port and service analysis      |
| AI Engine       | Machine learning anomaly detection              |
| Decision Engine | Automated risk classification                   |

---

## Security Workflow

```text
Target
   │
   ▼
Network Scan
   │
   ▼
Traffic Monitoring
   │
   ▼
Feature Extraction
   │
   ▼
AI Analysis
   │
   ▼
Decision Engine
   │
   ▼
Risk Assessment
```

---

## License

MIT License

---

GitHub:
https://github.com/kitsunee0104
