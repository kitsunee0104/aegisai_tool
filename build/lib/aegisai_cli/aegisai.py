from core.scanner import scan_target
from core.analyser import analyze_ports
from core.decision_engine import make_decision
from core.traffic_mon import start_sniffing

from utils.parser import extract_ports
from ai.model import predict

import numpy as np


def main():

    target = input("Enter target IP or Hostname: ").strip()

    if not target:
        print("Target cannot be empty.")
        return

    # =========================
    # Network Scan
    # =========================
    scan_output = scan_target(target)
    ports = extract_ports(scan_output)

    # =========================
    # Traffic Monitoring
    # =========================
    traffic_stats = start_sniffing(5)

    print("\nTraffic Statistics:")
    print(traffic_stats)

    # =========================
    # Port Analysis
    # =========================
    findings = analyze_ports(ports)

    # =========================
    # AI Feature Vector
    # =========================
    sample = [
        len(ports),
        traffic_stats["packet_count"],
        traffic_stats["connection_rate"],
        0,
        traffic_stats["unique_ports"]
    ]

    # =========================
    # AI Prediction
    # =========================
    ai_result = predict(sample)

    # =========================
    # Decision Engine
    # =========================
    decision = make_decision(findings, ai_result)

    # =========================
    # OUTPUT
    # =========================
    print("\n--- RESULTS ---")
    print("Target:", target)
    print("Ports:", ports)
    print("Findings:", findings)
    print("Traffic:", traffic_stats)

    print("AI Features:", sample)

    if ai_result == -1:
        print("AI Result: Anomaly Detected")
    else:
        print("AI Result: Normal")

    print("Decision:", decision)


if __name__ == "__main__":
    main()
