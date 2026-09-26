from Crypto.PublicKey import ECC

print("\n" + "=" * 60)
print("DEMO: ECDH KEY EXCHANGE")
print("=" * 60)

# Generate key pair for Alice
alice_private = ECC.generate(curve="P-256")
alice_public = alice_private.public_key()

# Generate key pair for Bob
bob_private = ECC.generate(curve="P-256")
bob_public = bob_private.public_key()

print("\nSTEP 1 - GENERATE ECDH KEY PAIRS")
print("-" * 60)

print("Alice private key : SECRET")
print("Alice public key  :")
print(alice_public)

print("\nBob private key   : SECRET")
print("Bob public key    :")
print(bob_public)

print("\nPrivate keys stay SECRET.")
print("Public keys can be exchanged over the network.")
