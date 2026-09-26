from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

print("=" * 60)
print("DEMO 3: RSA-OAEP — SAME MESSAGE, DIFFERENT CIPHERTEXT")
print("=" * 60)

# Same message
message = b"HELLO BOB"

# Load Bob's public key
with open("public_key.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

# Encrypt #1
cipher1 = PKCS1_OAEP.new(public_key)
ciphertext1 = cipher1.encrypt(message)

# Encrypt #2
cipher2 = PKCS1_OAEP.new(public_key)
ciphertext2 = cipher2.encrypt(message)

# Display as Base64
ct1 = base64.b64encode(ciphertext1).decode()
ct2 = base64.b64encode(ciphertext2).decode()

print("\nOriginal message:")
print(message.decode())

print("\nEncryption #1:")
print(ct1)

print("\nEncryption #2:")
print(ct2)

print("\nSame plaintext?  YES")
print("Same ciphertext? ", ciphertext1 == ciphertext2)

print("\nWhy?")
print("RSA-OAEP adds randomness before RSA encryption.")
