from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len


def unpad(data):
    return data[:-data[-1]]


print("=" * 60)
print("DEMO 3: AES with Wrong Key")
print("=" * 60)

# User enters any plaintext
plaintext = input("\nEnter plaintext: ")

# Generate two different AES-128 keys
correct_key = get_random_bytes(16)
wrong_key = get_random_bytes(16)

# CBC Initialization Vector
iv = get_random_bytes(16)

# ============================================================
# ENCRYPT WITH CORRECT KEY
# ============================================================

cipher = AES.new(correct_key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext.encode()))

print("\nOriginal plaintext :", plaintext)

print("\nCorrect key :", correct_key.hex())
print("Wrong key   :", wrong_key.hex())

print("\nCiphertext:")
print(base64.b64encode(ciphertext).decode())


# ============================================================
# DECRYPT WITH CORRECT KEY
# ============================================================

correct_cipher = AES.new(correct_key, AES.MODE_CBC, iv)
correct_result = unpad(correct_cipher.decrypt(ciphertext)).decode()

print("\n" + "-" * 60)
print("DECRYPT WITH CORRECT KEY")
print("-" * 60)

print("Result:", correct_result)


# ============================================================
# DECRYPT WITH WRONG KEY
# ============================================================

wrong_cipher = AES.new(wrong_key, AES.MODE_CBC, iv)
wrong_result = wrong_cipher.decrypt(ciphertext)

print("\n" + "-" * 60)
print("DECRYPT WITH WRONG KEY")
print("-" * 60)

print("Result (hex):")
print(wrong_result.hex())

print("\nWrong key -> Original plaintext cannot be recovered.")
(.venv) 3568Q6L7_740108:aes-demo 740108$ clear

(.venv) 3568Q6L7_740108:aes-demo 740108$ more demo_wrong_key.py 
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len


def unpad(data):
    return data[:-data[-1]]


print("=" * 60)
print("DEMO 3: AES with Wrong Key")
print("=" * 60)

# User enters any plaintext
plaintext = input("\nEnter plaintext: ")

# Generate two different AES-128 keys
correct_key = get_random_bytes(16)
wrong_key = get_random_bytes(16)

# CBC Initialization Vector
iv = get_random_bytes(16)

# ============================================================
# ENCRYPT WITH CORRECT KEY
# ============================================================

cipher = AES.new(correct_key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext.encode()))

print("\nOriginal plaintext :", plaintext)

print("\nCorrect key :", correct_key.hex())
print("Wrong key   :", wrong_key.hex())

print("\nCiphertext:")
print(base64.b64encode(ciphertext).decode())


# ============================================================
# DECRYPT WITH CORRECT KEY
# ============================================================

correct_cipher = AES.new(correct_key, AES.MODE_CBC, iv)
correct_result = unpad(correct_cipher.decrypt(ciphertext)).decode()

print("\n" + "-" * 60)
print("DECRYPT WITH CORRECT KEY")
print("-" * 60)

print("Result:", correct_result)


# ============================================================
# DECRYPT WITH WRONG KEY
# ============================================================

wrong_cipher = AES.new(wrong_key, AES.MODE_CBC, iv)
wrong_result = wrong_cipher.decrypt(ciphertext)

print("\n" + "-" * 60)
print("DECRYPT WITH WRONG KEY")
print("-" * 60)

print("Result (hex):")
print(wrong_result.hex())

print("\nWrong key -> Original plaintext cannot be recovered.")
