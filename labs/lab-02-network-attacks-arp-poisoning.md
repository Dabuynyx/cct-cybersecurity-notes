# Lab 02: Network Layer Attacks & ARP Poisoning Simulation

> **Associated Module:** [Module 02: Information Security Attacks](../docs/modules/)  
> **Environment:** Authorized Cybersecurity Lab / Sandbox  
> **Safety Notice:** All activities must be performed in isolated lab environments.

---

### Objective
Demonstrate how ARP cache poisoning allows an attacker to intercept local network traffic (MITM) and implement defensive mitigations.

### Prerequisites & Tools
- Isolated Lab Network with 2 VMs (Victim, Gateway) and 1 Attacker VM (Kali)
- Tools: `arpspoof`, `dsniff`, `tcpdump`, `Wireshark`

### Lab Walkthrough
1. **Inspect Initial ARP Table on Victim**:
   ```bash
   arp -a
   # or ip neigh
   ```
2. **Execute ARP Poisoning (Educational Simulation)**:
   ```bash
   # Poison victim telling it we are gateway:
   arpspoof -i eth0 -t <VICTIM_IP> <GATEWAY_IP>
   ```
3. **Capture Packet Redirection**:
   Observe ARP replies flooding the switch broadcast domain and redirecting frames to the attacker MAC.
4. **Defensive Mitigations**:
   - Static ARP bindings: `arp -s <GATEWAY_IP> <GATEWAY_MAC>`
   - Dynamic ARP Inspection (DAI) on managed switches paired with DHCP snooping.


---
*Created for the [CCT Cybersecurity Knowledge Base](https://github.com/Dabuynyx/cct-cybersecurity-notes) by [@Dabuynyx](https://github.com/Dabuynyx).*
