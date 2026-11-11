# 🔍 Nmap & Wireshark Quick Reference

## Essential Nmap Commands
```bash
# Host Discovery (Ping Sweep)
nmap -sn 192.168.1.0/24

# Fast SYN Stealth Scan (Top 1000 ports)
nmap -sS -T4 192.168.1.50

# Full TCP Scan with OS Detection, Version Fingerprinting & Traceroute
nmap -sS -sV -O --traceroute -p- -T4 192.168.1.50

# UDP Scan for DNS, SNMP, DHCP
nmap -sU -p 53,67,68,161,162 192.168.1.50

# Vulnerability Scanning via NSE Scripts
nmap --script vuln 192.168.1.50

# Output results in all formats (Normal, XML, Grepable)
nmap -sV -p 1-1024 192.168.1.50 -oA initial_recon
```

## Wireshark Display Filters for Incident Analysis
- `tcp.flags.syn == 1 and tcp.flags.ack == 0` : Detect SYN scan attempts
- `tcp.flags.reset == 1` : Detect connection resets (RST)
- `dns.flags.response == 0` : Monitor outbound DNS queries (tunneling/C2)
- `http.request.method == "POST"` : Inspect web form submissions / exfiltration
- `arp.duplicate-address-frame` : Detect potential ARP cache poisoning / IP conflicts
- `frame contains "password"` : Detect cleartext authentication strings
