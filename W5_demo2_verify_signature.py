from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pss

print()
print("=" * 60)
print("WEEK 5 - DEMO 2: RSA-PSS SIGNATURE VERIFICATION")
print("=" * 60)

# STEP 1 - Load Alice's public key
print("\nSTEP 1 - LOAD ALICE'S PUBLIC KEY")
print("-" * 60)

with open("alice_public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

print("Public key loaded successfully!")
print("RSA key size:", public_key.size_in_bits(), "bits")


# STEP 2 - Load original message and signature
print("\nSTEP 2 - LOAD MESSAGE AND SIGNATURE")
print("-" * 60)

with open("message.txt", "rb") as f:
    original_message = f.read()

with open("signature.bin", "rb") as f:
    signature = f.read()

print("Received message :", original_message.decode())
print("Signature size   :", len(signature), "bytes")


# STEP 3 - Verify original message
print("\nSTEP 3 - VERIFY ORIGINAL MESSAGE")
print("-" * 60)

original_hash = SHA256.new(original_message)

print("Message SHA-256:", original_hash.hexdigest())

verifier = pss.new(public_key)

try:
    verifier.verify(original_hash, signature)
    print("RESULT: SIGNATURE VALID")
    print("Message integrity verified!")
except (ValueError, TypeError):
    print("RESULT: SIGNATURE INVALID")


# STEP 4 - Modify the message
print("\nSTEP 4 - MODIFY THE MESSAGE")
print("-" * 60)

modified_message = b"Hello, KDB?"

print("Original message :", original_message.decode())
print("Modified message :", modified_message.decode())

modified_hash = SHA256.new(modified_message)

print("Modified SHA-256:", modified_hash.hexdigest())


# STEP 5 - Verify modified message
print("\nSTEP 5 - VERIFY MODIFIED MESSAGE")
print("-" * 60)

verifier = pss.new(public_key)

try:
    verifier.verify(modified_hash, signature)
    print("RESULT: SIGNATURE VALID")
except (ValueError, TypeError):
    print("RESULT: SIGNATURE INVALID")
    print("Message modification detected!")


print()
print("=" * 60)
print("DEMO 2 COMPLETED")
print("=" * 60)
