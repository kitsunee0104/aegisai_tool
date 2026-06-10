import re


def extract_ports(scan_output):
    ports = []

    for line in scan_output.split("\n"):

        match = re.search(r"(\d+)/tcp\s+open", line)

        if match:
            ports.append(int(match.group(1)))

    return ports
