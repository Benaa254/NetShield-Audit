 NetShield-Audit: Enterprise Infrastructure & Threat Monitoring Engine

 📍 Deployment Environment: Kenya School of Government (ICT Division Simulation)

---

 📋 Project Overview
NetShield-Audit is an automated cybersecurity and system compliance tool designed to mirror enterprise network monitoring and defensive audits. Built natively in Python, the application actively audits system configurations for workstation fleets (ensuring OS verification and endpoint safety shield compliance) while running a network surveillance engine to track core networking protocols (`TCP/IP`, `DNS`, `HTTP`) and intercept potential localized broadcast loops.

This project demonstrates practical competence in infrastructure monitoring, automated log parsing, vulnerability assessment, and risk remediation mapping aligned with modern corporate governance standards.

---

 🛠️ System Architecture & Workflow

The engine operates across two distinct corporate security layers:
1. Asset Compliance Audit (Layer 3/7 System Check): Parses configuration data models to identify unverified, unlicensed operating systems or outdated endpoint defense applications.
2. Network Surveillance & Traffic Logging (Layer 3 Network Check): Sniffs live raw network traffic signatures to detect unencrypted text transmissions (such as HTTP Port 80 anomalies) or anomalous broadcast footprints (ARP bursts) capable of causing network friction or performance drops.
