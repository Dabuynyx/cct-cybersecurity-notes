# 🛡️ CCT Exam Quick Reference & Formula Sheet

## Core Security Formulas & Triads
- **The Attack Formula:**  
  $$\text{Attack} = \text{Motive} + \text{Method} + \text{Vulnerability}$$
- **The CIA Triad (or CIV):**  
  Confidentiality, Integrity, Availability (Vulnerability/Non-Repudiation)
- **Quantitative Risk Analysis:**  
  - $\text{SLE} (\text{Single Loss Expectancy}) = \text{Asset Value (AV)} \times \text{Exposure Factor (EF)}$
  - $\text{ALE} (\text{Annualized Loss Expectancy}) = \text{SLE} \times \text{ARO (Annualized Rate of Occurrence)}$

## Standard Well-Known Ports & Protocols
| Port | Protocol | Layer / Service | Clear vs Encrypted Equivalent |
|---|---|---|---|
| **20/21** | FTP | File Transfer Protocol | Cleartext $\rightarrow$ SFTP (22) / FTPS (990) |
| **22** | SSH / SFTP | Secure Shell | Encrypted |
| **23** | Telnet | Unencrypted remote management | Cleartext $\rightarrow$ SSH (22) |
| **25** | SMTP | Simple Mail Transfer Protocol | Cleartext $\rightarrow$ SMTPS (465/587) |
| **53** | DNS | Domain Name System (UDP/TCP) | Cleartext $\rightarrow$ DoH / DoT (853) |
| **67/68**| DHCP | Dynamic Host Configuration | UDP Broadcast / Unicast |
| **69** | TFTP | Trivial FTP | UDP Cleartext (No auth) |
| **80** | HTTP | HyperText Transfer Protocol | Cleartext $\rightarrow$ HTTPS (443) |
| **88** | Kerberos | Network Authentication | Encrypted tickets (KDC/TGT) |
| **110**| POP3 | Post Office Protocol | Cleartext $\rightarrow$ POP3S (995) |
| **123**| NTP | Network Time Protocol | UDP Time sync |
| **143**| IMAP | Internet Message Access Protocol | Cleartext $\rightarrow$ IMAPS (993) |
| **161/162**| SNMP| Simple Network Management Protocol | SNMPv1/v2 (Clear community) $\rightarrow$ SNMPv3 (Auth/Priv) |
| **389**| LDAP | Lightweight Directory Access | Cleartext $\rightarrow$ LDAPS (636) |
| **443**| HTTPS | HTTP over TLS/SSL | Encrypted |
| **445**| SMB | Server Message Block | File sharing / lateral movement target |
| **1812/1813**| RADIUS | AAA Authentication & Accounting | UDP (Only password encrypted) |
| **3389**| RDP | Remote Desktop Protocol | Windows Remote Management |

## Order of Volatility (RFC 3227)
1. CPU Registers and Cache memory
2. Routing tables, ARP cache, process table, kernel statistics, RAM
3. Temporary file systems / swap space
4. Hard drives and non-volatile storage
5. Remote logging and monitoring data
6. Physical network topology and cabling
7. Archival media and backup tapes
