from Crypto.PublicKey import ECC
from Crypto.Protocol.DH import key_agreement
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256

print("\n" + "=" * 60)
print("DEMO: ECDH -> HKDF -> SESSION KEY")
print("=" * 60)

# --------------------------------------------------
# STEP 1 - Generate key pairs
# --------------------------------------------------

alice_private = ECC.generate(curve="P-256")
alice_public = alice_private.public_key()

bob_private = ECC.generate(curve="P-256")
bob_public = bob_private.public_key()


# --------------------------------------------------
# STEP 2 - Compute raw ECDH shared secret
# --------------------------------------------------

def raw_secret(shared_secret):
    return shared_secret


alice_shared = key_agreement(
    static_priv=alice_private,
    static_pub=bob_public,
    kdf=raw_secret
)

bob_shared = key_agreement(
    static_priv=bob_private,
    static_pub=alice_public,
    kdf=raw_secret
)

print("\nSTEP 2 - ECDH SHARED SECRET")
print("-" * 60)

print("Alice shared secret:")
print(alice_shared.hex())

print("\nBob shared secret:")
print(bob_shared.hex())

print("\nSame shared secret? :", alice_shared == bob_shared)


# --------------------------------------------------
# STEP 4 - Derive AES session key using HKDF
# --------------------------------------------------

alice_session_key = HKDF(
    alice_shared,
    32,                 # 32 bytes = 256 bits
    b"",
    SHA256,
    context=b"KDB Week 4"
)

bob_session_key = HKDF(
    bob_shared,
    32,
    b"",
    SHA256,
    context=b"KDB Week 4"
)

print("\nSTEP 4 - DERIVE AES SESSION KEY WITH HKDF")
print("-" * 60)

print("Alice AES-256 session key:")
print(alice_session_key.hex())

print("\nBob AES-256 session key:")
print(bob_session_key.hex())

print("\nSame session key? :", alice_session_key == bob_session_key)
