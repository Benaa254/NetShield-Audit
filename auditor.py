import json
import os

LOG_FILE = os.path.join("data", "compliance_logs.json")
ALERT_LOG = os.path.join("data", "network_alerts.log")

def audit_fleet():
    print("[*] Commencing fleet configuration audit...")
    if not os.path.exists(LOG_FILE):
        print("[-] Error: Compliance database not found.")
        return

    with open(LOG_FILE, "r") as f:
        devices = json.load(f)

    non_compliant_count = 0
    for device in devices:
        issues = []
        if not device["os_verified"] or not device["licensed"]:
            issues.append("Unlicensed/Unverified OS")
        if not device["endpoint_security_updated"]:
            issues.append("Outdated Endpoint Safety Shields")

        if issues:
            non_compliant_count += 1
            alert_msg = f"[CRITICAL RISK] Workstation {device['workstation_id']} ({device['ip_address']}) non-compliant due to: {', '.join(issues)}."
            print(alert_msg)
            with open(ALERT_LOG, "a") as al:
                al.write(alert_msg + "\n")
                
    print(f"[+] Audit Finished. Found {non_compliant_count} exposure vectors.")