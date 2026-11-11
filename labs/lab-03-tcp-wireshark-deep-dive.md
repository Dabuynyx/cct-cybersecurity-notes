# Lab 03: TCP 3-Way Handshake, Flag Manipulation & Teardown Analysis

> **Associated Module:** [Module 03: Network Security Fundamentals](../docs/modules/module-03-network-security-fundamentals.md) & [Module 17: Network Traffic Monitoring](../docs/modules/module-17-network-traffic-monitoring-and-analysis.md)  
> **Difficulty Level:** Beginner to Intermediate  
> **Target Environment:** Any Linux / macOS / Windows host with Wireshark or TShark  
> **Safety Warning:** Port scanning and packet injection should only be directed towards localhost (`127.0.0.1`) or designated lab targets.

---

## 🎯 Learning Objectives
By the end of this lab, you will be able to:
1. Deconstruct the TCP Finite State Machine and capture the exact 3-Way Handshake (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`) sequence.
2. Analyze graceful connection teardown (`FIN` / `ACK`) versus abrupt abortive resets (`RST`).
3. Identify anomalous TCP flag combinations used by reconnaissance tools (SYN Stealth, Xmas Scan, NULL Scan).
4. Build targeted Wireshark display filters to isolate connection state anomalies and potential Denial-of-Service attempts.

---

## 🛠️ Required Tools & Environment Setup
- **Packet Analyzer:** Wireshark (GUI) or `tshark` (CLI).
- **Network Probe:** `curl`, `netcat` (`nc`), or Python `scapy`.
- **Operating System:** Any modern Linux, macOS, or Windows workstation.

---

## 📋 Step-by-Step Execution Guide

### Step 1: Start Wireshark Packet Capture
1. Launch Wireshark.
2. Select your active network interface (e.g., `eth0`, `en0`, or `lo0` for loopback).
3. In the display filter bar, enter:
   ```text
   tcp.port == 80 || tcp.port == 443
   ```
4. Click the blue shark fin icon to start live capture.

---

### Step 2: Generate a Clean TCP Handshake & Teardown
In a terminal, issue a single HTTP request using `curl`:
```bash
curl -I http://example.com
```

Stop the packet capture and examine the first three packets.

**Detailed Packet Breakdown:**

| Frame | Direction | Flags Set | Sequence Number | Acknowledgment Number | Meaning |
|---|---|---|---|---|---|
| **#1** | Client $\rightarrow$ Server | `[SYN]` | Relative $Seq = 0$ | $Ack = 0$ | "Let's synchronize. My initial sequence number is $0$." |
| **#2** | Server $\rightarrow$ Client | `[SYN, ACK]` | Relative $Seq = 0$ | $Ack = 1$ | "I acknowledge your SYN ($0+1$). My sequence number is $0$." |
| **#3** | Client $\rightarrow$ Server | `[ACK]` | Relative $Seq = 1$ | $Ack = 1$ | "Handshake established. Connection is now ready for application data." |

---

### Step 3: Inspecting Connection Teardown (FIN vs RST)

#### Graceful Four-Way Teardown:
Locate the final frames of the conversation:
1. Client sends `[FIN, ACK]` ($Seq=120, Ack=340$).
2. Server responds with `[ACK]` ($Seq=340, Ack=121$).
3. Server closes its sending channel and sends `[FIN, ACK]` ($Seq=340, Ack=121$).
4. Client responds with final `[ACK]` ($Seq=121, Ack=341$).

#### Abrupt Reset (`RST`):
Trigger a reset by attempting to connect to a port that is closed:
```bash
nc -zv 127.0.0.1 65432
```
In Wireshark, observe:
```text
Client -> Server [SYN] Seq=0
Server -> Client [RST, ACK] Seq=0 Ack=1
```
*Firewall Rationale:* A closed TCP port natively replies with `[RST, ACK]`. A packet filtering firewall configured to silently drop packets will produce no reply at all (causing the client to time out), which informs port scanners that the port is "filtered".

---

### Step 4: Crafting & Detecting Abnormal Scan Patterns

Nmap leverages non-standard flag combinations to bypass legacy stateless firewalls and fingerprint OS behavior:

1. **Xmas Scan:** Sets the `FIN`, `PSH`, and `URG` flags ("lit up like a Christmas tree").
   - Wireshark Display Filter: `tcp.flags == 0x029`
2. **NULL Scan:** Clears all 6 standard control flags ($0x000$).
   - Wireshark Display Filter: `tcp.flags == 0x000`
3. **SYN Flood (DoS Detection):**
   - Wireshark Filter: `tcp.flags.syn == 1 && tcp.flags.ack == 0`
   - Go to **Statistics $\rightarrow$ Conversations $\rightarrow$ TCP**. If a single IP address initiates thousands of SYN frames without ever completing the 3-way handshake, a SYN flood attack is in progress.

---

## ❓ Analytical Questions
1. Why does the second packet of the 3-way handshake increment the acknowledgment number by 1 even though the SYN packet carried 0 bytes of payload data?
2. If an attacker sends a flood of SYN packets with forged source IP addresses, why does the server's memory become exhausted? What OS defense mechanism mitigates this (Hint: SYN Cookies)?

---

## 🛡️ Key Defensive Lessons
- **Enable TCP SYN Cookies:** When the TCP connection queue fills up, SYN cookies encode the connection state into the initial sequence number rather than allocating kernel memory blocks:
  ```bash
  sudo sysctl -w net.ipv4.tcp_syncookies=1
  ```
- **Stateful Firewalls:** Always enforce stateful connection tracking (`NEW`, `ESTABLISHED`, `RELATED`). Inbound packets that possess flags like `PSH` or `FIN` without an existing established session in the state table are immediately discarded.
