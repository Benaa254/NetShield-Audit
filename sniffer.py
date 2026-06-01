import os
from scapy.all import sniff, ARP, IP

ALERT_LOG = os.path.join("data", "network_alerts.log")

def log_alert(message):
    print(f"[ALERT] {message}")
    with open(ALERT_LOG, "a") as f:
        f.write(message + "\n")

def packet_callback(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 1:
        if packet[ARP].dst == "ff:ff:ff:ff:ff:ff":
            log_alert(f"Broadcast Pattern Observed from MAC: {packet.src} -> Subnet Monitoring Triggered.")
    elif packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if packet.haslayer('TCP') and packet['TCP'].dport == 80:
            log_alert(f"Unencrypted HTTP Traffic detected from Host: {ip_src} to {ip_dst}")

def start_sniffing(interface=None, duration=10):
    print(f"[*] Initializing network surveillance engine...")
    sniff(iface=interface, prn=packet_callback, timeout=duration, store=0)