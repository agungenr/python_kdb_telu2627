from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pss

print()
print("=" * 60)
print("WEEK 5 - DEMO 1: RSA-PSS DIGITAL SIGNATURE")
print("=" * 60)

# STEP 1 - Generate RSA key pair
print("\nSTEP 1 - GENERATE RSA KEY PAIR")
print("-" * 60)

key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()

with open("alice_private.pem", "wb") as f:
    f.write(private_key)

with open("alice_public.pem", "wb") as f:
    f.write(public_key)

print("RSA key size : 2048 bits")
print("Private key  : alice_private.pem")
print("Public key   : alice_public.pem")
print("Key pair generated successfully!")

# STEP 2 - Create message and compute SHA-256 hash
print("\nSTEP 2 - HASH THE MESSAGE")
print("-" * 60)

message = b"Hello, KDB!"
message_hash = SHA256.new(message)

print("Original message :", message.decode())
print("Hash algorithm   : SHA-256")
print("SHA-256 digest   :", message_hash.hexdigest())

# STEP 3 - Sign using Alice's private key
print("\nSTEP 3 - CREATE DIGITAL SIGNATURE")
print("-" * 60)

signer = pss.new(key)
signature = signer.sign(message_hash)

with open("message.txt", "wb") as f:
    f.write(message)

with open("signature.bin", "wb") as f:
    f.write(signature)

print("Signature algorithm : RSA-PSS")
print("Signature size      :", len(signature), "bytes")
print("Signature (hex)     :", signature.hex())
print()
print("Files created:")
print("  1. alice_private.pem")
print("  2. alice_public.pem")
print("  3. message.txt")
print("  4. signature.bin")

print()
print("=" * 60)
print("DIGITAL SIGNATURE SUCCESSFULLY CREATED!")
print("=" * 60)
