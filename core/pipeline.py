from core.scanner import scan_target
from core.analyser import analyze_ports
from core.traffic_mon import start_sniffing
from utils.parser import extract_ports
from ai.model import predict
import numpy as np


def run_pipeline(target):

    scan_output = scan_target(target)
    ports = extract_ports(scan_output)

    traffic_stats = start_sniffing(2)

    findings = analyze_ports(ports)

    sample = [
        len(ports),
        traffic_stats["packet_count"],
        traffic_stats["connection_rate"],
        0,
        traffic_stats["unique_ports"]
    ]

    ai_result = predict(sample)

    return {
        "ports": ports,
        "findings": findings,
        "traffic": traffic_stats,
        "ai_result": int(ai_result)
    }
