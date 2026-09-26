from Crypto.PublicKey import ECC
from Crypto.Protocol.DH import key_agreement
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

print("\n" + "=" * 60)
print("DEMO: BOB DECRYPTS THE MESSAGE")
print("=" * 60)

# --------------------------------------------------
# STEP 1 - Generate ECDH key pairs
# --------------------------------------------------

alice_private = ECC.generate(curve="P-256")
alice_public = alice_private.public_key()

bob_private = ECC.generate(curve="P-256")
bob_public = bob_private.public_key()


# --------------------------------------------------
# STEP 2 & 3 - Exchange public keys and
# compute ECDH shared secret
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


# --------------------------------------------------
# STEP 4 - Derive AES-256 session keys using HKDF
# --------------------------------------------------

alice_session_key = HKDF(
    alice_shared,
    32,
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


# --------------------------------------------------
# STEP 5 - Alice encrypts the message
# --------------------------------------------------

message = b"Transfer Rp1.000.000 to Bob"

cipher_alice = AES.new(
    alice_session_key,
    AES.MODE_GCM
)

ciphertext, tag = cipher_alice.encrypt_and_digest(message)
nonce = cipher_alice.nonce


# --------------------------------------------------
# STEP 6 - Bob decrypts the message
# --------------------------------------------------

cipher_bob = AES.new(
    bob_session_key,
    AES.MODE_GCM,
    nonce=nonce
)

decrypted = cipher_bob.decrypt_and_verify(
    ciphertext,
    tag
)

print("\nSTEP 6 - BOB DECRYPTS MESSAGE")
print("-" * 60)

print("Received Ciphertext:")
print(ciphertext.hex())

print("\nBob AES-256 Session Key:")
print(bob_session_key.hex())

print("\nDecrypted Message:")
print(decrypted.decode())

print("\nDecryption successful!")
