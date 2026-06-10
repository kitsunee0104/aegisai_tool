def analyze_ports(ports):

    findings = []

    port_map = {
        21: "FTP Service Detected",
        22: "SSH Service Detected",
        80: "HTTP Service Detected",
        443: "HTTPS Service Detected",
        445: "SMB Service Detected",
        631: "IPP/CUPS Printing Service Detected"
    }

    for port in ports:

        if port in port_map:
            findings.append(port_map[port])

        if port == 21:
            findings.append("Warning: FTP transmits data in plaintext")

        elif port == 445:
            findings.append("Warning: SMB is a common attack target")

        elif port == 22:
            findings.append("Info: Verify SSH hardening and key authentication")

    return findings
