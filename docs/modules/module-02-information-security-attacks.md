# Module 02: Information Security Attacks

> **Curriculum Track:** Certified Cybersecurity Technician (CCT) Knowledge Base  
> **Topic Domain:** Attack Formula, Social Engineering Vectors, Network-Layer Interception & Application Attacks  
> **Status:** Original Study Synthesis & Technical Analysis

---

## 🧭 Theoretical Foundations & Conceptual Breakdown

### Personal Study Focus & Key Observations
- **Attack Anatomy Formula**: $\text{Attack} = \text{Motive} + \text{Method} + \text{Vulnerability}$.
- **Social Engineering Mechanics**:
  - *Pretexting & Spear-Phishing*: Crafted scenarios exploiting authority, urgency, social proof, or scarcity.
  - *Watering Hole Attacks*: Compromising legitimate industry websites frequented by targeted organizational staff.
- **Network Layer Manipulation**:
  - *ARP Poisoning / Spoofing*: Exploits the stateless nature of IPv4 ARP resolution on Layer 2 switch fabrics.
  - *DNS Cache Poisoning*: Injecting forged zone mappings into local resolvers.
  - *Denial of Service (DoS/DDoS)*: Volumetric exhaustion (UDP/NTP/DNS amplification) vs state exhaustion (TCP SYN flood) vs application starvation (Slowloris HTTP).


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
