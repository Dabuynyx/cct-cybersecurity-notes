# Lab 08: OpenSSL Cryptography, Digital Certificates & PKI

> **Associated Module:** [Module 14: Cryptography Algorithms & PKI](../docs/modules/)  
> **Environment:** Authorized Cybersecurity Lab / Sandbox  
> **Safety Notice:** All activities must be performed in isolated lab environments.

---

### Objective
Generate asymmetric RSA key pairs, create self-signed X.509 certificates, calculate SHA-256 HMACs, and encrypt data with AES-256-GCM.

### Prerequisites & Tools
- OpenSSL CLI (`openssl`)

### Lab Walkthrough
1. **Generate 2048-bit RSA Private Key & Public Key**:
   ```bash
   openssl genrsa -out private.key 2048
   openssl rsa -in private.key -pubout -out public.key
   ```
2. **Create Certificate Signing Request (CSR) & Self-Signed Cert**:
   ```bash
   openssl req -new -x509 -key private.key -out certificate.crt -days 365        -subj "/C=US/ST=Security/L=Lab/O=CCT/CN=lab.local"
   ```
3. **Symmetric File Encryption with AES-256-CBC / GCM**:
   ```bash
   openssl enc -aes-256-cbc -salt -pbkdf2 -in secret.txt -out secret.enc
   openssl enc -d -aes-256-cbc -pbkdf2 -in secret.enc -out secret_decrypted.txt
   ```
4. **HMAC Integrity Verification**:
   ```bash
   openssl dgst -sha256 -hmac "SharedSecretKey123" secret.txt
   ```


---
*Created for the [CCT Cybersecurity Knowledge Base](https://github.com/Dabuynyx/cct-cybersecurity-notes) by [@Dabuynyx](https://github.com/Dabuynyx).*
