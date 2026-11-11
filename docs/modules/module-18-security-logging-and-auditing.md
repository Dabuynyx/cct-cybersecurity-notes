# Module 18: Security Logging and Auditing

> **Curriculum Track:** Certified Cybersecurity Technician (CCT) Knowledge Base  
> **Topic Domain:** Syslog Standard Architecture, Windows Event Auditing & Centralized SIEM Operations  
> **Status:** Original Study Synthesis & Technical Analysis

---

## 🧭 Theoretical Foundations & Conceptual Breakdown

### Personal Study Focus & Key Observations
- **Syslog Standard (RFC 5424)**: Facilities (auth, daemon, kern, user) and Severity levels (0 Emergency through 7 Debug).
- **Windows Security Event Auditing**:
  - Event ID 4624 (Successful logon) vs 4625 (Failed logon / brute-force indicator).
  - Event ID 4672 (Special privileges assigned / admin logon).
  - Event ID 4720 (User account created).
- **Log Integrity**: Remote write-once-read-many (WORM) log forwarding to prevent attacker log tampering.


---

## ⚙️ Technical Deconstruction & Operational Mechanics

Understanding the operational workflow and architectural implications of these concepts:
- **Adversary Perspective**: How threats identify misconfigurations or architectural weaknesses to establish footholds.
- **Defensive Engineering**: How technical, administrative, and physical controls operate synchronously to enforce defense-in-depth.
- **Verification & Telemetry**: How system logs, packet captures, and telemetry sensors capture anomalous indicators for security operations centers.

---

## 🛠️ Practical Hands-on Application

To solidify these theoretical models with terminal and packet-level experience, refer to the corresponding hands-on lab in [`labs/`](../../labs/):
- Review the step-by-step terminal instructions, command flags, and expected behavioral outputs.
- Execute exercises within an isolated lab VM environment to observe defensive mitigations in real time.

---

## 💡 Exam & Practical Takeaways

1. **Verify Terminology Precision**: Distinguish clearly between related terms (e.g., authentication vs authorization; vulnerability vs exploit; differential vs incremental backups).
2. **Remember Operational Sequences**: Memorize the NIST Incident Response steps, the RFC 3227 Order of Volatility, and the quantitative risk calculation formulas.
3. **Focus on Defensive Rationale**: Understand *why* specific controls are placed at specific layers of the enterprise architecture.

---
*Authored by [@Dabuynyx](https://github.com/Dabuynyx) for the cybersecurity community.*
