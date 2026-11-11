# Lab 06: OWASP Top 10 Web Exploits & Defenses (SQLi & XSS)

> **Associated Module:** [Module 09: Application Security Fundamentals](../docs/modules/)  
> **Environment:** Authorized Cybersecurity Lab / Sandbox  
> **Safety Notice:** All activities must be performed in isolated lab environments.

---

### Objective
Analyze SQL Injection and Stored/Reflected XSS attacks in a sandboxed application and implement defense code.

### Prerequisites & Tools
- DVWA (Damn Vulnerable Web Application) / OWASP Juice Shop
- Burp Suite Community Edition

### Lab Walkthrough
1. **Authentication Bypass via SQL Injection**:
   Payload: `' OR 1=1 -- -`
   Examine backend vulnerable query: `SELECT * FROM users WHERE user = '$input' AND pass = '$pass'`
2. **Defense Implementation (Parameterized Queries in Python)**:
   ```python
   # Vulnerable:
   # cursor.execute(f"SELECT * FROM users WHERE username = '{user}'")

   # Secure (Prepared Statement):
   cursor.execute("SELECT * FROM users WHERE username = %s", (user,))
   ```
3. **Cross-Site Scripting (XSS)**:
   Payload: `<script>alert(document.cookie)</script>`
   Mitigation: HTML Entity Encoding (`htmlspecialchars` / context-aware sanitization) + Content-Security-Policy (CSP) headers.


---
*Created for the [CCT Cybersecurity Knowledge Base](https://github.com/Dabuynyx/cct-cybersecurity-notes) by [@Dabuynyx](https://github.com/Dabuynyx).*
