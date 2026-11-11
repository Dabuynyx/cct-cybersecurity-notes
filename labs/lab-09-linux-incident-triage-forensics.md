# Lab 09: Linux Incident Triage, Volatile RAM & Artifact Capture

> **Associated Module:** [Module 19: Incident Response & Module 20: Computer Forensics](../docs/modules/)  
> **Environment:** Authorized Cybersecurity Lab / Sandbox  
> **Safety Notice:** All activities must be performed in isolated lab environments.

---

### Objective
Execute first-responder evidence acquisition on a suspected compromised Linux server adhering to RFC 3227 Order of Volatility.

### Prerequisites & Tools
- Linux Terminal (Root privileges)
- Tools: `dd`, `LiME` / memory dumper, `netstat`/`ss`, `lsof`, `sha256sum`

### Lab Walkthrough
1. **Step 1 - Volatile Memory & Network Connections (Highest Volatility)**:
   ```bash
   # Document active sockets and processes:
   ss -tulpn > /mnt/usb/volatile/net_connections.txt
   lsof -i -n -P > /mnt/usb/volatile/lsof_network.txt
   ```
2. **Step 2 - Running Process Tree & Logged in Users**:
   ```bash
   ps auxf > /mnt/usb/volatile/process_tree.txt
   who -a > /mnt/usb/volatile/active_users.txt
   last -F > /mnt/usb/volatile/last_logins.txt
   ```
3. **Step 3 - Forensic Bit-Stream Disk Imaging with Hash Verification**:
   ```bash
   dd if=/dev/sdb of=/mnt/usb/forensic_image.dd bs=4M conv=noerror,sync status=progress
   sha256sum /mnt/usb/forensic_image.dd > /mnt/usb/forensic_image.dd.sha256
   ```
4. **Step 4 - Chain of Custody Documentation**:
   Record evidence ID, acquiring officer, timestamp, physical location, and hash verification signatures.


---
*Created for the [CCT Cybersecurity Knowledge Base](https://github.com/Dabuynyx/cct-cybersecurity-notes) by [@Dabuynyx](https://github.com/Dabuynyx).*
