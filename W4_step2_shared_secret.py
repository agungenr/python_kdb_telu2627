from Crypto.PublicKey import ECC
from Crypto.Protocol.DH import key_agreement

print("\n" + "=" * 60)
print("DEMO: ECDH SHARED SECRET")
print("=" * 60)

# Generate Alice's key pair
alice_private = ECC.generate(curve="P-256")
alice_public = alice_private.public_key()

# Generate Bob's key pair
bob_private = ECC.generate(curve="P-256")
bob_public = bob_private.public_key()

print("\nSTEP 1 - KEY PAIRS GENERATED")
print("Alice: Private A + Public A")
print("Bob  : Private B + Public B")


# Return raw ECDH shared secret
# (for demonstration purposes)
def show_shared_secret(shared_secret):
    return shared_secret


# Alice:
# Private A + Public B
alice_shared = key_agreement(
    static_priv=alice_private,
    static_pub=bob_public,
    kdf=show_shared_secret
)

# Bob:
# Private B + Public A
bob_shared = key_agreement(
    static_priv=bob_private,
    static_pub=alice_public,
    kdf=show_shared_secret
)

print("\nSTEP 2 - ECDH KEY AGREEMENT")
print("-" * 60)

print("Alice uses: Private A + Public B")
print("Bob uses  : Private B + Public A")

print("\nAlice shared secret:")
print(alice_shared.hex())

print("\nBob shared secret:")
print(bob_shared.hex())

print("\nSame shared secret? :", alice_shared == bob_shared)

print("\nIMPORTANT:")
print("The shared secret was NEVER transmitted over the network.")
