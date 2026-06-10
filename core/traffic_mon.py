from scapy.all import sniff
import threading
import os

packet_count = 0
unique_ports = set()
latest_stats = None


# =========================
# CHECK ROOT ACCESS
# =========================
def is_root():
    return hasattr(os, "geteuid") and os.geteuid() == 0


# =========================
# PACKET PROCESSOR
# =========================
def process_packet(packet):
    global packet_count, unique_ports

    packet_count += 1

    if packet.haslayer("TCP"):
        try:
            unique_ports.add(packet["TCP"].dport)
        except Exception:
            pass


# =========================
# SNIFFING CORE WORKER
# =========================
def sniff_worker(duration):
    global packet_count, unique_ports, latest_stats

    # ❌ BLOCK IF NOT ROOT
    if not is_root():
        latest_stats = {
            "packet_count": 0,
            "connection_rate": 0,
            "unique_ports": 0,
            "error": "Root permission required for packet capture (run with sudo)"
        }
        return

    packet_count = 0
    unique_ports = set()

    try:
        sniff(
            prn=process_packet,
            store=False,
            timeout=duration
        )

        connection_rate = packet_count / duration if duration > 0 else 0

        latest_stats = {
            "packet_count": packet_count,
            "connection_rate": connection_rate,
            "unique_ports": len(unique_ports)
        }

    except Exception as e:
        latest_stats = {
            "packet_count": 0,
            "connection_rate": 0,
            "unique_ports": 0,
            "error": str(e)
        }


# =========================
# BLOCKING (CLI / API)
# =========================
def start_sniffing(duration=5):
    sniff_worker(duration)
    return latest_stats


# =========================
# NON-BLOCKING (DASHBOARD)
# =========================
def start_sniffing_async(duration=5):

    thread = threading.Thread(
        target=sniff_worker,
        args=(duration,),
        daemon=True
    )

    thread.start()

    return {
        "packet_count": 0,
        "connection_rate": 0,
        "unique_ports": 0,
        "status": "capturing"
    }


# =========================
# GET LATEST RESULTS
# =========================
def get_latest_stats():
    return latest_stats
