# Lab 07: AWS Cloud Security & KMS Envelope Encryption

> **Associated Module:** [Module 10: Virtualization and Cloud Computing Security](../docs/modules/)  
> **Environment:** Authorized Cybersecurity Lab / Sandbox  
> **Safety Notice:** All activities must be performed in isolated lab environments.

---

### Objective
Implement cloud envelope encryption using AWS KMS and secure Amazon S3 bucket policies.

### Prerequisites & Tools
- AWS CLI configured or LocalStack mock environment
- Python `boto3`

### Lab Walkthrough
1. **Enforce S3 Bucket Encryption & Block Public Access**:
   ```bash
   aws s3api put-public-access-block --bucket my-cct-secure-bucket        --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
   ```
2. **Envelope Encryption Workflow with Python `boto3`**:
   - Request Data Key from KMS Customer Managed Key (CMK):
     ```python
     import boto3
     kms = boto3.client('kms')
     response = kms.generate_data_key(KeyId='alias/cct-key', KeySpec='AES_256')
     plaintext_key = response['Plaintext']
     ciphertext_key = response['CiphertextBlob']
     ```
   - Encrypt file payload locally with `plaintext_key` (AES-256-GCM).
   - Destroy `plaintext_key` in memory.
   - Store encrypted payload alongside `ciphertext_key`.


---
*Created for the [CCT Cybersecurity Knowledge Base](https://github.com/Dabuynyx/cct-cybersecurity-notes) by [@Dabuynyx](https://github.com/Dabuynyx).*
