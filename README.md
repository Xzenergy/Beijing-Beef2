# AES-128 Encryption with SHA-256 Hashing

## Overview
This script securely encrypts data using **AES-128 in CBC mode** and also generates a **SHA-256 hash** of the original plaintext for integrity verification.

## Features
- **AES-128 Encryption (CBC Mode)**
  - Uses a securely derived **128-bit key** from a password via **PBKDF2 (SHA-256)**.
  - Generates a **random salt (16 bytes)** for each encryption to enhance security.
  - Uses a **random IV (16 bytes)** to ensure uniqueness of encrypted output.
  - Uses **PKCS7 padding** to handle variable-length input.

- **SHA-256 Hashing**
  - Computes a SHA-256 hash of the plaintext before encryption.
  - Helps verify data integrity after decryption (not included in this script).

## Installation
Ensure you have Python installed along with the required dependencies.

### Install Required Libraries:
```bash
pip install pycryptodome
```

## Usage
### Encrypting Data
Modify the `plaintext` and `password` values in the script as needed and run it:
```python
password = "sample_password2"  # Encryption password
plaintext = "Sensitive Data to Encrypt"

encrypted_data, plaintext_hash = encrypt_data(plaintext, password)
print("SHA-256 Hash of Plaintext:", plaintext_hash)
print("Encrypted Data (Hex):", encrypted_data.hex())
```

### Output
- **SHA-256 Hash of Plaintext**: A hash of the original plaintext message.
- **Encrypted Data (Hex)**: The encrypted data, including the salt and IV.

## Security Considerations
- The **salt** ensures that different encryptions of the same password generate unique keys.
- The **IV (Initialization Vector)** prevents patterns in encrypted messages.
- The **PBKDF2 function (100,000 iterations)** strengthens password-based key derivation.

## Future Enhancements
- Implement a secure **decryption function** (not included in this version).
- Add **HMAC authentication** to prevent tampering.

## License
This project is open-source and can be modified and used freely.

---

Let me know if you need any modifications or additional features! 🚀

