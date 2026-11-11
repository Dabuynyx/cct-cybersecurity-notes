# 🛡️ Certified Cybersecurity Technician (CCT) Knowledge Base & Practical Labs

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Certification](https://img.shields.io/badge/EC--Council-CCT-red.svg)](https://www.eccouncil.org/)
[![Status](https://img.shields.io/badge/Status-Complete%2022%20Modules-success.svg)]()
[![Hands-on Labs](https://img.shields.io/badge/Labs-9%20Practical%20Exercises-orange.svg)]()

> A comprehensive, technically rigorous, and hands-on knowledge base built from authentic study records, slide analyses, and practical labs for the **EC-Council Certified Cybersecurity Technician (CCT)** certification.

---

## 🧭 Repository Architecture & Navigation

This knowledge base connects theoretical cybersecurity principles directly to practical tools, network traffic analysis, system auditing, and incident response workflows.

```
cct-cybersecurity-notes/
├── docs/
│   └── modules/              # All 22 CCT In-Depth Study Modules (Theory & Slides)
├── labs/                     # Hands-on Cybersecurity Lab Guides (Terminal & Tools)
├── cheatsheets/              # High-Yield Exam Formulas, Port Tables & Command Sheets
├── scripts/                  # Automation scripts & verification tools
└── README.md                 # Complete Master Curriculum & Index
```

---

## 📚 Complete CCT Curriculum Modules (1 – 22)

| Module | Title | Key Subjects | Notes Link |
|---|---|---|---|
| **01** | Information Security Threats & Vulnerabilities | Threat Taxonomy, Actors, Attack Vectors, Malware Families, Droppers/Packers, CVSS | [Module 01](docs/modules/module-01-threats-and-vulnerabilities.md) |
| **02** | Information Security Attacks | Attack Formula, Social Engineering, ARP/DNS Spoofing, DoS/DDoS, Web Attacks | [Module 02](docs/modules/module-02-information-security-attacks.md) |
| **03** | Network Security Fundamentals | CIA Triad, Defense-in-Depth, OSI 7-Layer vs TCP/IP, Subnetting, IPv4/IPv6 | [Module 03](docs/modules/module-03-network-security-fundamentals.md) |
| **04** | Identification, Authentication & Authorization | Access Control Models (DAC, MAC, RBAC, ABAC), AAA Architecture, MFA, Password Security | [Module 04](docs/modules/module-04-identification-authentication-authorization.md) |
| **05** | Network Security Controls - Administrative | NIST CSF, ISO 27001, PCI-DSS, HIPAA, Security Policies, AUP, Personnel Security | [Module 05](docs/modules/module-05-administrative-network-security-controls.md) |
| **06** | Network Security Controls - Physical | Perimeters, Fences, Mantraps, Biometrics, HVAC, Fire Suppression, Anti-Tailgating | [Module 06](docs/modules/module-06-physical-network-security-controls.md) |
| **07** | Network Security Controls - Technical | Firewalls (Stateful/NGFW), IDS/IPS (Snort), Proxies, DMZ, VPNs (IPSec), RADIUS | [Module 07](docs/modules/module-07-technical-network-security-controls.md) |
| **08** | Network Security Assessment Tools & Techniques | Vulnerability Assessment vs Pentest, Threat Hunting, Nmap, Port Scanning, Nessus | [Module 08](docs/modules/module-08-network-security-assessment-tools.md) |
| **09** | Application Security Fundamentals | OWASP Top 10, SSDLC, SAST vs DAST, Parameterized Queries, CSP, WAF | [Module 09](docs/modules/module-09-application-security-fundamentals.md) |
| **10** | Virtualization & Cloud Computing Security | Hypervisors, IaaS/PaaS/SaaS, Shared Responsibility, AWS IAM, VPC, S3, KMS | [Module 10](docs/modules/module-10-virtualization-and-cloud-computing.md) |
| **11** | Wireless Network Security | 802.11 Standards, WEP vs WPA/WPA2/WPA3, Rogue APs, Evil Twin, Wi-Fi Analysis | [Module 11](docs/modules/module-11-wireless-network-security.md) |
| **12** | Mobile Device Security | BYOD/COPE/COBO, MDM/MAM/EMM, Jailbreaking/Rooting Risks, App Sandboxing | [Module 12](docs/modules/module-12-mobile-device-security.md) |
| **13** | IoT and OT Security | IoT Architecture, MQTT/CoAP/Zigbee, SCADA/ICS Purdue Model, Modbus, Cyber-Physical Attacks | [Module 13](docs/modules/module-13-iot-and-ot-security.md) |
| **14** | Cryptography Algorithms & PKI | Symmetric (AES) vs Asymmetric (RSA/ECC), Hashing (SHA-256), PKI, X.509, HMAC | [Module 14](docs/modules/module-14-cryptography-algorithms-and-pki.md) |
| **15** | Data Security & Protection | Data States (Transit, Rest, Use), Classification, DLP, Data Sanitization (NIST 800-88) | [Module 15](docs/modules/module-15-data-security-and-protection.md) |
| **16** | Network Troubleshooting & Diagnostics | 6-Step Troubleshooting Methodology, CLI Diagnostics (ping, traceroute, netstat, dig) | [Module 16](docs/modules/module-16-network-troubleshooting-and-diagnostics.md) |
| **17** | Network Traffic Monitoring & Analysis | TAPs vs SPAN Mirroring, NetFlow/IPFIX, Baseline Profiling, C2 Beaconing Detection | [Module 17](docs/modules/module-17-network-traffic-monitoring-and-analysis.md) |
| **18** | Security Logging and Auditing | Syslog RFC 5424 (Facilities/Severities), Windows Security Events, Centralized SIEM | [Module 18](docs/modules/module-18-security-logging-and-auditing.md) |
| **19** | Incident Response & First Responder | NIST SP 800-61 Lifecycle, CSIRT Roles, First Responder Evidence Preservation, Triage | [Module 19](docs/modules/module-19-incident-response-and-first-responder.md) |
| **20** | Computer Forensics Fundamentals | RFC 3227 Order of Volatility, Bit-Stream Forensics (dd), Chain of Custody, Artifacts | [Module 20](docs/modules/module-20-computer-forensics-fundamentals.md) |
| **21** | Business Continuity & Disaster Recovery (BC/DR) | BCP vs DRP, BIA, RTO, RPO, MTD, Backup Strategies (Differential/Incremental), Sites | [Module 21](docs/modules/module-21-business-continuity-and-disaster-recovery.md) |
| **22** | Risk Management Concepts & Frameworks | Risk Formula, Qualitative vs Quantitative Risk (SLE, ALE, ARO), NIST RMF, ISO 31000 | [Module 22](docs/modules/module-22-risk-management-concepts-and-frameworks.md) |

---

## 🛠️ Practical Hands-on Labs

Each lab provides concrete objectives, environment prerequisites, step-by-step terminal instructions, and defensive analysis:

1. [Lab 01: Malware Analysis & Static/Dynamic Inspection](labs/lab-01-malware-analysis-mechanics.md)
2. [Lab 02: Network Layer Attacks & ARP Poisoning Simulation](labs/lab-02-network-attacks-arp-poisoning.md)
3. [Lab 03: TCP 3-Way Handshake, Teardown & Anomaly Analysis](labs/lab-03-tcp-wireshark-deep-dive.md)
4. [Lab 04: Snort NIDS Deployment & Custom Signature Crafting](labs/lab-04-snort-nids-rule-crafting.md)
5. [Lab 05: Port Enumeration, Service Fingerprinting & NSE](labs/lab-05-nmap-recon-and-vulnerability-scan.md)
6. [Lab 06: OWASP Top 10 Web Exploits & Defenses (SQLi & XSS)](labs/lab-06-owasp-web-vulnerabilities.md)
7. [Lab 07: AWS Cloud Security & KMS Envelope Encryption](labs/lab-07-aws-cloud-kms-envelope-encryption.md)
8. [Lab 08: OpenSSL Cryptography, Digital Certificates & PKI](labs/lab-08-openssl-cryptography-pki.md)
9. [Lab 09: Linux Incident Triage, Volatile RAM & Artifact Capture](labs/lab-09-linux-incident-triage-forensics.md)

---

## ⚡ High-Yield Exam Cheatsheets

- [CCT Exam Quick Reference & Formula Sheet](cheatsheets/cct-exam-quick-reference.md): All formulas (ALE/SLE), standard port mappings, and Order of Volatility.
- [Nmap & Wireshark Quick Reference](cheatsheets/nmap-and-wireshark-commands.md): Essential scanning flags, timing templates, and display filters for packet analysis.

---

## ⚖️ License & Ethical Disclosure
This project is open-source under the [MIT License](LICENSE).  
All scripts and lab exercises are provided exclusively for educational research, certification study, and defensive evaluation in authorized lab environments.
