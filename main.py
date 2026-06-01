import os
import sys

# This line forces Python to look in your current directory for the 'utils' folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.sniffer import start_sniffing
from utils.auditor import audit_fleet

def main():
    os.makedirs("data", exist_ok=True)
    
    print("====================================================")
    print("  NETSHIELD-AUDIT: KSG ICT DIVISION MONITORING ENGINE")
    print("====================================================\n")
    
    # 1. Run the Workstation Fleet Audit
    audit_fleet()
    print("\n----------------------------------------------------\n")
    
    # 2. Run Network Sniffer for 10 seconds
    start_sniffing(duration=10)
    
    print(f"\n[+] Execution complete. Review 'data/network_alerts.log'.")

if __name__ == "__main__":
    main()