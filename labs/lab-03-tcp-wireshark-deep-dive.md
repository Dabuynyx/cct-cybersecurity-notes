# Lab 03: TCP 3-Way Handshake, Teardown & Anomaly Analysis

> **Associated Module:** [Module 03: Network Security Fundamentals & Module 17: Traffic Monitoring](../docs/modules/)  
> **Environment:** Authorized Cybersecurity Lab / Sandbox  
> **Safety Notice:** All activities must be performed in isolated lab environments.

---

### Objective
Inspect raw packet captures to understand the TCP state machine, detect SYN flooding anomalies, and identify anomalous TCP flag combinations (Xmas, NULL scans).

### Prerequisites & Tools
- Wireshark / TShark
- Python Scapy / Netcat

### Lab Walkthrough
1. **Capture Normal 3-Way Handshake**:
   - Filter: `tcp.flags.syn == 1 && tcp.flags.ack == 0` (SYN)
   - Filter: `tcp.flags.syn == 1 && tcp.flags.ack == 1` (SYN-ACK)
   - Filter: `tcp.flags.ack == 1 && tcp.flags.syn == 0` (ACK)
2. **Detect Abnormal Scans**:
   - **Xmas Scan**: `tcp.flags == 0x029` (FIN, PSH, URG enabled)
   - **NULL Scan**: `tcp.flags == 0x000` (No flags set)
   - **SYN Flood**: Massive ratio of SYN packets with no following ACK or completed handshake.


---
*Created for the [CCT Cybersecurity Knowledge Base](https://github.com/Dabuynyx/cct-cybersecurity-notes) by [@Dabuynyx](https://github.com/Dabuynyx).*
