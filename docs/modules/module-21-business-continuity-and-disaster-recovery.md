# Module 21: Business Continuity & Disaster Recovery (BC/DR)

> **Curriculum Track:** Certified Cybersecurity Technician (CCT) Knowledge Base  
> **Topic Domain:** Business Impact Analysis, Recovery Metrics (RTO, RPO, MTD) & Continuity Strategies  
> **Status:** Original Study Synthesis & Technical Analysis

---

## 🧭 Theoretical Foundations & Conceptual Breakdown

### Personal Study Focus & Key Observations
- **Key Recovery Metrics**:
  - *RTO (Recovery Time Objective)*: Maximum acceptable duration of system outage before operational failure.
  - *RPO (Recovery Point Objective)*: Maximum acceptable data loss measured in time.
  - *MTD (Maximum Tolerable Downtime)*: Total time the business can survive without the system ($MTD \ge RTO + WRT$).
- **Backup Methods**: Full vs Differential (changes since last full) vs Incremental (changes since last backup).
- **Recovery Sites**: Hot Site (fully synchronized) vs Warm Site (hardware ready, data restored on demand) vs Cold Site (empty facility).


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
