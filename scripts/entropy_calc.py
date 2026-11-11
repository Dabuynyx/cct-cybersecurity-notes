#!/usr/bin/env python3
"""
File Entropy Calculator (Shannon Entropy)
Used in malware analysis to detect packed, compressed, or encrypted payloads.
Range: 0.0 (uniform bytes) to 8.0 (completely random / encrypted bytes).
"""
import sys
import math
from collections import Counter

def calculate_entropy(filepath):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
    except Exception as e:
        print(f"Error opening file: {e}")
        return None

    if not data:
        return 0.0

    counter = Counter(data)
    total_bytes = len(data)
    entropy = -sum((count / total_bytes) * math.log2(count / total_bytes) for count in counter.values())
    return entropy

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 entropy_calc.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]
    entropy = calculate_entropy(filepath)
    if entropy is not None:
        print(f"File: {filepath}")
        print(f"Shannon Entropy: {entropy:.4f} / 8.0000")
        if entropy > 7.0:
            print("Assessment: VERY HIGH ENTROPY -> High probability of encryption, packing (UPX), or compression.")
        elif entropy > 6.0:
            print("Assessment: MODERATE TO HIGH ENTROPY -> Typical compiled native executable or mixed binary.")
        else:
            print("Assessment: LOW ENTROPY -> Plain text, scripts, or uncompressed structured data.")

if __name__ == '__main__':
    main()
