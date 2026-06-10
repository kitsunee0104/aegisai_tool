import argparse

from core.scanner import scan_target
from core.analyser import analyze_ports
from core.traffic_mon import start_sniffing
from utils.parser import extract_ports
from ai.model import predict
from core.decision_engine import make_decision


def run(target):

    print(f"\n[+] AegisAI scanning: {target}\n")

    scan_output = scan_target(target)
    ports = extract_ports(scan_output)

    traffic_stats = start_sniffing(5)

    findings = analyze_ports(ports)

    sample = [
        len(ports),
        traffic_stats["packet_count"],
        traffic_stats["connection_rate"],
        0,
        traffic_stats["unique_ports"]
    ]

    ai_result = predict(sample)

    decision = make_decision(findings, ai_result)

    print("\n--- RESULTS ---")
    print("Target:", target)
    print("Ports:", ports)
    print("Findings:", findings)
    print("Traffic:", traffic_stats)
    print("AI Result:", "Anomaly" if ai_result == -1 else "Normal")
    print("Decision:", decision)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("target", nargs="?", default="127.0.0.1")
    args = parser.parse_args()

    run(args.target)


if __name__ == "__main__":
    main()
