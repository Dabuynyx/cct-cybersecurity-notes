#!/usr/bin/env python3
"""
Application Security SQL Injection Demonstration & Prepared Statements Defense
Used in Lab 06 to illustrate the mechanics of dynamic query concatenation vs parameterized queries.
"""
import sqlite3

def run_demonstration():
    print("=" * 65)
    print("  OWASP Injection Defense: Parameterized Queries Demo")
    print("=" * 65)

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'admin', 'SuperSecretPass123', 'Administrator')")
    cursor.execute("INSERT INTO users VALUES (2, 'john_doe', 'Password456!', 'StandardUser')")
    conn.commit()

    payload = "admin' OR '1'='1"

    # Vulnerable implementation
    vulnerable_sql = f"SELECT id, username, role FROM users WHERE username = '{payload}' AND password = 'arbitrary_password'"
    print(f"\n[!] VULNERABLE SQL STRING:")
    print(f"    {vulnerable_sql}")
    cursor.execute(vulnerable_sql)
    vuln_user = cursor.fetchone()
    print(f"[*] Result: Logged in as -> {vuln_user[1]} (Role: {vuln_user[2]}) [EXPLOIT SUCCEEDED]")

    # Secure implementation
    secure_sql = "SELECT id, username, role FROM users WHERE username = ? AND password = ?"
    print(f"\n[+] SECURE PARAMETERIZED SQL:")
    print(f"    {secure_sql}  [Inputs bound as data parameters]")
    cursor.execute(secure_sql, (payload, 'arbitrary_password'))
    sec_user = cursor.fetchone()
    print(f"[*] Result: Query returned -> {sec_user} [ATTACK PREVENTED]")
    print("=" * 65)

if __name__ == '__main__':
    run_demonstration()
