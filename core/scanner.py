import subprocess


def scan_target(target):

    command = [
        "nmap",
        "-sV",
        target
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60
        )

        return result.stdout

    except Exception as e:
        return f"Scan Error: {e}"
