# Lab 09: Linux Incident Triage, Volatile RAM Capture & Forensic Preservation

> **Associated Module:** [Module 19: Incident Response](../docs/modules/module-19-incident-response-and-first-responder.md) & [Module 20: Computer Forensics](../docs/modules/module-20-computer-forensics-fundamentals.md)  
> **Difficulty Level:** Intermediate to Advanced  
> **Target Environment:** Linux VM (Ubuntu / Debian / RHEL) with sudo privileges  
> **Standard Reference:** RFC 3227 Guidelines for Evidence Collection and Archiving

---

## 🎯 Learning Objectives
By the end of this lab, you will be able to:
1. Apply the **RFC 3227 Order of Volatility** during a live cybersecurity incident.
2. Safely capture volatile artifacts (active network sockets, listening services, logged-in sessions, process trees) prior to powering down an endpoint.
3. Perform bit-stream forensic disk acquisitions using `dd` and verify evidence integrity with SHA-256 hashes.
4. Complete a standard legal Chain of Custody record.

---

## 📋 The RFC 3227 Order of Volatility

When responding to an active intrusion, preserve evidence starting from the most volatile (fragile) to least volatile:
1. **CPU Registers and Cache Memory**
2. **Routing Tables, ARP Cache, Process Table, Kernel Statistics, RAM**
3. **Temporary File Systems & Swap Partitions**
4. **Hard Disks and Persistent Storage Media**
5. **Remote Logging and Monitoring Systems**
6. **Physical Network Cabling and Topologies**
7. **Archival Backups and Cold Media**

---

## 🔬 Practical Scenario
At 02:45 AM, an endpoint alert indicates an unauthorized outbound SSH connection from an internal web server. You arrive on-site as the designated First Responder. You must collect volatile system telemetry before isolating the host from the network.

---

## 📋 Step-by-Step Triage Workflow

### Step 1: Prepare Forensics Mount Directory
Create an external collection directory (simulating an external forensic drive):
```bash
sudo mkdir -p /tmp/forensic_evidence/volatile
cd /tmp/forensic_evidence/volatile
```

---

### Step 2: Capture Live Network Sockets & Connections
Document open ports, listening daemons, and established external sockets:
```bash
# Network sockets and owning PID:
sudo ss -tulpn > network_listeners.txt

# All active connections with IP addresses:
sudo ss -anp > active_connections.txt

# Inspect ARP cache for gateway bindings:
ip neigh show > arp_cache.txt
```

---

### Step 3: Capture Running Processes & System Memory State
```bash
# Full process hierarchy with arguments:
ps auxfww > process_tree.txt

# List open files and network descriptors by process:
sudo lsof -n -P > open_file_descriptors.txt

# Currently logged in users:
who -a > logged_in_users.txt

# Recent login history:
last -F -n 20 > login_history.txt
```

---

### Step 4: Bit-Stream Forensic Disk Imaging with `dd`
Create a raw bit-for-bit forensic clone of a target drive or partition:

```bash
# Simulate creating a disk image:
sudo dd if=/dev/zero of=/tmp/forensic_evidence/test_disk.img bs=1M count=10 status=progress
```

Immediately calculate and freeze the SHA-256 hash of the forensic image:
```bash
sha256sum /tmp/forensic_evidence/test_disk.img | tee /tmp/forensic_evidence/evidence_hash.sha256
```

**Verification Principle:**
If the image hash matches the original drive hash, the evidence is legally admissible. Any subsequent analysis must be performed on a **copy** of the image, never the original.

---

## 📝 Chain of Custody Record Template

```text
========================================================================
                    CYBERSECURITY EVIDENCE CHAIN OF CUSTODY
========================================================================
Case Reference ID:    CCT-INC-2026-0891
Date & Time Acquired: 2026-11-11 15:45:00 UTC
Target Hostname:      srv-finance-web01.internal
Acquired By:          Senior Security Analyst (Adnan Al-Hmoud)
Item #  Description                 SHA-256 Verification Hash
------------------------------------------------------------------------
01      RAM/Volatile Triage Dump    9a12c8e... (Recorded in evidence log)
02      Bit-Stream Disk Image       f4b82c1... (Recorded in sha256 file)

Custody Log:
Transferred From: Analyst (A. Al-Hmoud) -> To: Evidence Vault Locker 4B
Reason: Safe Secure Storage for Investigation
Signatures: [Verified]
========================================================================
```

---

## 🧹 Environment Cleanup
```bash
sudo rm -rf /tmp/forensic_evidence
```
