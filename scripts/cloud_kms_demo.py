#!/usr/bin/env python3
"""
AWS Cloud Security & KMS Envelope Encryption Demonstration
Illustrates Customer Master Key (CMK) and Data Encryption Key (DEK) lifecycle.
"""
import os
try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except ImportError:
    import sys
    print("Please install cryptography: pip install cryptography")
    sys.exit(1)

def run_envelope_demo():
    print("=" * 65)
    print("  AWS Cloud KMS Envelope Encryption Demonstration")
    print("=" * 65)

    # 1. Simulate the Hardware Security Module (HSM) hosting the Customer Master Key (CMK)
    hsm_master_key = AESGCM.generate_key(bit_length=256)
    kms_master_cipher = AESGCM(hsm_master_key)
    print("[1] Cloud KMS Customer Master Key (CMK) generated inside secure HSM.")

    # 2. Simulate KMS GenerateDataKey API Call
    # Returns (Plaintext DEK, Encrypted DEK Blob)
    data_encryption_key = AESGCM.generate_key(bit_length=256)
    dek_nonce = os.urandom(12)
    encrypted_dek_blob = kms_master_cipher.encrypt(dek_nonce, data_encryption_key, None)
    print("[2] KMS issued Plaintext DEK (256-bit) and Encrypted DEK blob.")

    # 3. Local Application Encrypts Large File Payload using Plaintext DEK
    sensitive_data = b"CONFIDENTIAL_PATIENT_MEDICAL_RECORDS_ICD10_DIAGNOSIS"
    local_data_cipher = AESGCM(data_encryption_key)
    file_nonce = os.urandom(12)
    ciphertext_file = local_data_cipher.encrypt(file_nonce, sensitive_data, None)
    print(f"[3] Local host encrypted payload ({len(sensitive_data)} bytes) with DEK.")

    # 4. Critical Security Rule: Securely zero/delete Plaintext DEK from RAM
    del data_encryption_key
    print("[4] PLAINTEXT DEK PURGED FROM APPLICATION MEMORY.")
    print("    Stored on Disk/S3: (file_nonce + ciphertext_file + dek_nonce + encrypted_dek_blob)")

    # 5. Decryption / Recovery Phase
    print("\n[5] Decryption Workflow Initiated:")
    print("    Sending encrypted DEK blob back to KMS HSM for decryption...")
    decrypted_dek = kms_master_cipher.decrypt(dek_nonce, encrypted_dek_blob, None)
    recovery_cipher = AESGCM(decrypted_dek)
    restored_plaintext = recovery_cipher.decrypt(file_nonce, ciphertext_file, None)
    print(f"    Recovered Payload: {restored_plaintext.decode()}")
    print("=" * 65)

if __name__ == '__main__':
    run_envelope_demo()
