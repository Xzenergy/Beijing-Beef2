import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


#Function to get an AES-128 key using PBKDF2
def get_key(password: str, salt: bytes, key_length: int = 16, iterations: int = 100000) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen=key_length)

#Function to encrypt using AES-128 CBC mode
def encrypt_data(plaintext: str, password: str) -> bytes:
    salt = os.urandom(16) #Generate random salt
    key = get_key(password, salt, key_length=16) #Give us the AES-128 key

    iv = os.urandom(16) #Generate random IV
    cipher = AES.new(key, AES.MODE_CBC, iv) #Create the AES cipher in CBC mode

    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size)) #Encrypt with padding
    return salt + iv + ciphertext #Gives us the combined salt, IV, and ciphertext

#User Input
password = 'sample_password' #Used for the encryption
plaintext = "Sensitive Data to Encrypt"

encrypted_data = encrypt_data(plaintext, password)
print("Encrypted Data (Hex): ", encrypted_data.hex())
