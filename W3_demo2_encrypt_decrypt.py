from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

print("=" * 60)
print("DEMO 2: RSA ENCRYPTION & DECRYPTION")
print("=" * 60)

# ==========================================================
# ALICE
# ==========================================================

print("\n[ALICE]")

message = b"Transfer Rp3.000.000 ke rekening Budi"

print("\nOriginal message:")
print(message.decode())

# Alice loads Bob's PUBLIC KEY
with open("public_key.pem", "rb") as f:
    bob_public_key = RSA.import_key(f.read())

# Create RSA-OAEP cipher using Bob's public key
cipher_encrypt = PKCS1_OAEP.new(bob_public_key)

# Encrypt the message
ciphertext = cipher_encrypt.encrypt(message)

# Base64 only makes ciphertext easier to display
ciphertext_b64 = base64.b64encode(ciphertext).decode()

print("\nEncrypting with Bob's PUBLIC KEY...")

print("\nCiphertext:")
print(ciphertext_b64)


# ==========================================================
# SEND CIPHERTEXT TO BOB
# ==========================================================

print("\n" + "=" * 60)
print("CIPHERTEXT SENT TO BOB")
print("=" * 60)


# ==========================================================
# BOB
# ==========================================================

print("\n[BOB]")

# Bob loads his PRIVATE KEY
with open("private_key.pem", "rb") as f:
    bob_private_key = RSA.import_key(f.read())

# Create RSA-OAEP cipher using Bob's private key
cipher_decrypt = PKCS1_OAEP.new(bob_private_key)

# Decrypt
plaintext = cipher_decrypt.decrypt(ciphertext)

print("\nDecrypting with Bob's PRIVATE KEY...")

print("\nRecovered message:")
print(plaintext.decode())

print("\n" + "=" * 60)
print("SUCCESS: Original message recovered!")
print("=" * 60)
