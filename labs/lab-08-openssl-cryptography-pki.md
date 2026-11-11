# Lab 08: OpenSSL Cryptography, Digital Certificates & Public Key Infrastructure (PKI)

> **Associated Module:** [Module 14: Cryptography Algorithms & PKI](../docs/modules/module-14-cryptography-algorithms-and-pki.md)  
> **Difficulty Level:** Intermediate  
> **Target Environment:** Any Linux / macOS / WSL terminal  
> **Prerequisites:** OpenSSL CLI (`openssl version`)

---

## 🎯 Learning Objectives
By the end of this lab, you will be able to:
1. Generate cryptographically strong asymmetric RSA private/public key pairs.
2. Build a Certificate Signing Request (CSR) and sign an X.509 digital certificate.
3. Perform authenticated symmetric file encryption using AES-256-CBC with PBKDF2 key derivation.
4. Generate and verify Hash-based Message Authentication Codes (HMAC) to ensure message integrity and authenticity.

---

## 📋 Step-by-Step Execution Guide

### Step 1: Symmetric Encryption with OpenSSL (AES-256-CBC)
Create a sample confidential file:
```bash
echo "CONFIDENTIAL: Customer payroll data 2026" > secret_data.txt
```

Encrypt the file symmetrically using AES-256 with PBKDF2 password derivation and a random salt:
```bash
openssl enc -aes-256-cbc -salt -pbkdf2 -iter 100000 -in secret_data.txt -out secret_data.enc
```
*(Enter a strong passphrase when prompted).*

Attempt to view the ciphertext:
```bash
cat secret_data.enc
```
*(Output is unintelligible binary data prefixed with `Salted__`).*

Decrypt the file:
```bash
openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -in secret_data.enc -out decrypted.txt
cat decrypted.txt
```

---

### Step 2: Asymmetric Cryptography — RSA Keypair Generation
Generate a 2048-bit RSA private key:
```bash
openssl genrsa -out private_key.pem 2048
```
Inspect the private key structure:
```bash
openssl rsa -in private_key.pem -text -noout | head -n 12
```

Extract the corresponding public key from the private key:
```bash
openssl rsa -in private_key.pem -pubout -out public_key.pem
```

---

### Step 3: Digital Certificate (X.509) Creation
Create a self-signed X.509 digital certificate valid for 365 days using our private key:
```bash
openssl req -new -x509 -key private_key.pem -out server_cert.crt -days 365     -subj "/C=US/ST=SecurityLab/L=Austin/O=CCTDefense/CN=internal.secure.local"
```

Verify certificate details and validity dates:
```bash
openssl x509 -in server_cert.crt -text -noout | grep -E 'Subject:|Issuer:|Not After'
```

**Expected Terminal Output:**
```text
        Issuer: C = US, ST = SecurityLab, L = Austin, O = CCTDefense, CN = internal.secure.local
            Not After : Nov 11 15:30:00 2027 GMT
        Subject: C = US, ST = SecurityLab, L = Austin, O = CCTDefense, CN = internal.secure.local
```
*Note:* In an enterprise PKI, the **Issuer** is a trusted Root Certificate Authority (CA), distinct from the server **Subject**.

---

### Step 4: HMAC Integrity & Authentication
Compute a Hash-based Message Authentication Code using SHA-256 and a pre-shared secret key:
```bash
openssl dgst -sha256 -hmac "EnterprisePreSharedKey#2026" secret_data.txt
```

**Expected Output:**
```text
HMAC-SHA256(secret_data.txt)= c8f92160538a16dbb679de87e59b2d6a54160a5df971b56952cf345220c388bc
```
If an adversary modifies a single character inside `secret_data.txt`, the HMAC recalculation will fail, warning the receiver that tampering occurred.

---

## 🧹 Environment Cleanup
```bash
rm -f secret_data.txt secret_data.enc decrypted.txt private_key.pem public_key.pem server_cert.crt
```
