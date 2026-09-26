from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

print("=" * 60)
print("DEMO 4: HYBRID ENCRYPTION — RSA + AES")
print("=" * 60)

message = b"Data mahasiswa Semester Ganjil 2026/2027"

# ==========================================================
# ALICE
# ==========================================================

print("\n[ALICE]")
print("Original message:")
print(message.decode())

# 1. Generate random AES session key
aes_key = get_random_bytes(32)   # AES-256

print("\n[1] Random AES session key generated.")

# 2. Encrypt DATA using AES
aes_cipher = AES.new(aes_key, AES.MODE_GCM)
ciphertext, tag = aes_cipher.encrypt_and_digest(message)

print("[2] Message encrypted using AES.")

# 3. Load Bob's public RSA key
with open("public_key.pem", "rb") as f:
    bob_public_key = RSA.import_key(f.read())

# Encrypt AES key using Bob's RSA public key
rsa_cipher = PKCS1_OAEP.new(bob_public_key)
encrypted_aes_key = rsa_cipher.encrypt(aes_key)

print("[3] AES key encrypted using Bob's RSA PUBLIC KEY.")

print("\n" + "=" * 60)
print("SEND TO BOB")
print("Encrypted AES Key + Encrypted Data")
print("=" * 60)


# ==========================================================
# BOB
# ==========================================================

print("\n[BOB]")

# 4. Load Bob's private RSA key
with open("private_key.pem", "rb") as f:
    bob_private_key = RSA.import_key(f.read())

# Recover AES key using RSA private key
rsa_cipher = PKCS1_OAEP.new(bob_private_key)
recovered_aes_key = rsa_cipher.decrypt(encrypted_aes_key)

print("[4] AES key recovered using Bob's RSA PRIVATE KEY.")

# 5. Decrypt DATA using recovered AES key
aes_cipher = AES.new(
    recovered_aes_key,
    AES.MODE_GCM,
    nonce=aes_cipher.nonce
)

recovered_message = aes_cipher.decrypt_and_verify(ciphertext, tag)

print("[5] Message decrypted using recovered AES key.")

print("\nRecovered message:")
print(recovered_message.decode())

print("\n" + "=" * 60)
print("SUCCESS!")
print("RSA protected the KEY.")
print("AES protected the DATA.")
print("=" * 60)
