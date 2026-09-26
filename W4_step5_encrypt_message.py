from Crypto.PublicKey import ECC
from Crypto.Protocol.DH import key_agreement
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

print("\n" + "=" * 60)
print("DEMO: AES-GCM ENCRYPTION USING ECDH SESSION KEY")
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
# STEP 4 - Derive AES-256 session key using HKDF
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

print("\nSTEP 4 - SESSION KEYS")
print("-" * 60)

print("Same session key? :", alice_session_key == bob_session_key)


# --------------------------------------------------
# STEP 5 - Alice encrypts a message with AES-GCM
# --------------------------------------------------

message = b"Transfer Rp1.000.000 to Bob"

cipher_alice = AES.new(
    alice_session_key,
    AES.MODE_GCM
)

ciphertext, tag = cipher_alice.encrypt_and_digest(message)

nonce = cipher_alice.nonce

print("\nSTEP 5 - ALICE ENCRYPTS MESSAGE WITH AES-GCM")
print("-" * 60)

print("Plaintext:")
print(message.decode())

print("\nAES-256 Session Key:")
print(alice_session_key.hex())

print("\nNonce:")
print(nonce.hex())

print("\nCiphertext:")
print(ciphertext.hex())

print("\nAuthentication Tag:")
print(tag.hex())

print("\nAlice sends:")
print("Nonce + Ciphertext + Authentication Tag")
print("\nThe AES session key is NOT transmitted.")
