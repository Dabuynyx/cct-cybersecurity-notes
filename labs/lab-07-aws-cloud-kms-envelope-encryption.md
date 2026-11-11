# Lab 07: Cloud Security & AWS KMS Envelope Encryption Architecture

> **Associated Module:** [Module 10: Virtualization and Cloud Computing Security](../docs/modules/module-10-virtualization-and-cloud-computing.md)  
> **Difficulty Level:** Intermediate to Advanced  
> **Target Environment:** AWS Free Tier / LocalStack Mock Cloud / Python SDK  
> **Prerequisites:** Python 3, `pip install cryptography`

---

## 🎯 Learning Objectives
By the end of this lab, you will be able to:
1. Explain the **Envelope Encryption** paradigm used by major cloud providers (AWS, Google Cloud, Azure).
2. Differentiate between a **Customer Master Key (CMK / KMS Key)** and a **Data Encryption Key (DEK)**.
3. Understand why encrypting large datasets directly inside KMS HSMs is computationally inefficient and how envelope encryption solves this bottleneck.
4. Implement and verify a complete cryptographic envelope workflow locally using Python.

---

## 📐 Architecture Diagram: Envelope Encryption

```text
+-------------------------------------------------------------+
|                     AWS KMS (Hardware HSM)                   |
|  [ Customer Master Key (CMK) ]                              |
|           |                                                 |
|           |-- GenerateDataKey()                             |
|           |                                                 |
|           v                                                 |
|  (Plaintext DEK) <---------> (Encrypted DEK / Ciphertext)   |
+-----------|-------------------------------|-----------------+
            |                               |
            v                               |
 [ Local Application Memory ]               |
            |                               |
   Encrypts Large File Payload              |
            |                               |
            v                               v
   (Encrypted Data) +++++++++++++++ (Encrypted DEK)
                     Stored on S3
```

---

## 📋 Step-by-Step Python Verification Lab

We provide a self-contained demonstration script `scripts/cloud_kms_demo.py` that executes the exact mathematical flow of envelope encryption using AES-256-GCM.

```python
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Step 1: Simulate the KMS Customer Master Key (CMK) living in the HSM
hsm_cmk = AESGCM.generate_key(bit_length=256)
kms_hsm = AESGCM(hsm_cmk)
print("[+] Cloud KMS CMK initialized inside simulated HSM.")

# Step 2: Request KMS to Generate a Data Encryption Key (DEK)
# KMS returns: (1) Plaintext DEK for immediate local use, (2) Encrypted DEK for storage
raw_dek = AESGCM.generate_key(bit_length=256)
dek_nonce = os.urandom(12)
encrypted_dek = kms_hsm.encrypt(dek_nonce, raw_dek, None)
print(f"[+] KMS issued Plaintext DEK ({len(raw_dek)*8}-bit) and Encrypted DEK Blob.")

# Step 3: Local Application Encrypts Large Sensitive File using Plaintext DEK
sensitive_payload = b"CRITICAL_FINANCIAL_DATABASE_RECORD_SSN_987-65-4321"
local_cipher = AESGCM(raw_dek)
file_nonce = os.urandom(12)
ciphertext_payload = local_cipher.encrypt(file_nonce, sensitive_payload, None)
print("[+] Payload encrypted locally with Plaintext DEK.")

# Step 4: ZERO OUT PLAINTEXT DEK FROM MEMORY (Critical Best Practice)
del raw_dek
print("[+] Plaintext DEK wiped from local memory. Storing Ciphertext + Encrypted DEK.")

# --- DECRYPTION / RECOVERY WORKFLOW ---
print("\n[*] Recovering data: Sending Encrypted DEK back to KMS for decryption...")
recovered_dek = kms_hsm.decrypt(dek_nonce, encrypted_dek, None)
decryptor = AESGCM(recovered_dek)
decrypted_plaintext = decryptor.decrypt(file_nonce, ciphertext_payload, None)

print(f"[SUCCESS] Recovered Secret: {decrypted_plaintext.decode()}")
```

Run the demonstration:
```bash
python3 scripts/cloud_kms_demo.py
```

**Expected Terminal Output:**
```text
[+] Cloud KMS CMK initialized inside simulated HSM.
[+] KMS issued Plaintext DEK (256-bit) and Encrypted DEK Blob.
[+] Payload encrypted locally with Plaintext DEK.
[+] Plaintext DEK wiped from local memory. Storing Ciphertext + Encrypted DEK.

[*] Recovering data: Sending Encrypted DEK back to KMS for decryption...
[SUCCESS] Recovered Secret: CRITICAL_FINANCIAL_DATABASE_RECORD_SSN_987-65-4321
```

---

## 🛡️ S3 Cloud Bucket Security Best Practices
When storing encrypted assets in AWS S3:
1. **Enforce S3 Default Encryption:** Mandate AWS-KMS encryption on all bucket objects:
   ```bash
   aws s3api put-bucket-encryption --bucket secure-cct-bucket        --server-side-encryption-configuration '{
           "Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "aws:kms"}}]
       }'
   ```
2. **Block Public Access:**
   ```bash
   aws s3api put-public-access-block --bucket secure-cct-bucket        --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
   ```
