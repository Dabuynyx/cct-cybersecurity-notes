# Module 01: Information Security Threats & Vulnerabilities

> **Curriculum Track:** Certified Cybersecurity Technician (CCT) Knowledge Base  
> **Topic Domain:** Fundamental Threat Taxonomy, Threat Actors, Attack Vectors, Malware Mechanics & Vulnerability Scoring  
> **Status:** Original Study Synthesis & Technical Analysis

---

## 🧭 Theoretical Foundations & Conceptual Breakdown

### Personal Study Focus & Key Observations
- **Threat vs Vulnerability**: A vulnerability is a flaw or weakness in system architecture, design, or implementation; a threat is any actor or event that possesses the potential to exploit that flaw.
- **The Core Equation**: Risk emerges when a threat vector intersects with an unmitigated vulnerability against an asset of value.
- **Threat Actors Categorization**:
  - *Internal Insiders*: Possess legitimate physical and logical permissions; highest blast radius due to authenticated standing access.
  - *External Actors*: Script kiddies (automated tooling), organized cybercrime syndicates (financial extortion / ransomware), and advanced persistent threats (APT / state-sponsored espionage).
- **Malware Delivery Components**:
  - *Dropper / Downloader*: Small initial payload staging delivery to bypass static perimeter filters.
  - *Obfuscator / Packer*: Encoding routines designed to thwart static file signature and entropy-based AV analysis.
  - *Payload*: The active execution module (RAT, wiper, crypto-ransomware, keylogger).


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
