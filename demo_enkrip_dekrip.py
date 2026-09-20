from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len


def unpad(data):
    return data[:-data[-1]]


print("=" * 60)
print("DEMO 1: AES Encrypt and Decrypt")
print("=" * 60)

# User enters any plaintext
plaintext = input("\nEnter plaintext: ")

# Generate AES-128 secret key
key = get_random_bytes(16)

# CBC requires a 16-byte IV
iv = get_random_bytes(16)

print("\nSecret key :", key.hex())
print("Key length :", len(key), "bytes =", len(key) * 8, "bits")

# Encrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext.encode()))

print("\nPlaintext  :", plaintext)
print("Ciphertext :", base64.b64encode(ciphertext).decode())

# Decrypt using the SAME secret key
cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
recovered = unpad(cipher_decrypt.decrypt(ciphertext)).decode()

print("\nDecrypting with the SAME secret key...")
print("Recovered  :", recovered)

print("\nSame secret key -> plaintext successfully recovered.")
