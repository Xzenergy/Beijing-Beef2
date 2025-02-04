import hashlib
from Crypto.Cipher import AES

# Generates the SHA1 authentication key
auth_password = "sample_password"
auth_key = hashlib.sha1(auth_password.encode()).hexdigest()[:16]
print("SHA1 Auth Key:", auth_key)

# Generates the AES128 privacy key (first 16 bytes of SHA1 hash, this can be changed for different types of AES, i.e 256)
privacy_password = "sample_password2"
aes_key = hashlib.sha1(privacy_password.encode()).digest()[:32]
print("AES128 Privacy Key:", aes_key.hex())
