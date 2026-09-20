from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def count_different_bits(data1, data2):
    return sum(
        (a ^ b).bit_count()
        for a, b in zip(data1, data2)
    )


print("=" * 60)
print("DEMO 2: AES Avalanche Effect")
print("=" * 60)

print("\nEnter TWO plaintexts.")
print("Each plaintext must be exactly 16 ASCII characters.")
print("Tip: change only ONE character between them.\n")

# Input plaintext
text1 = input("Plaintext 1: ")
text2 = input("Plaintext 2: ")

# Check length
if len(text1.encode()) != 16 or len(text2.encode()) != 16:
    print("\nERROR: Each plaintext must be exactly 16 bytes.")
    print("Plaintext 1:", len(text1.encode()), "bytes")
    print("Plaintext 2:", len(text2.encode()), "bytes")
    exit()

# Same AES-128 key
key = get_random_bytes(16)

print("\nSecret key :", key.hex())
print("Key length : 16 bytes = 128 bits")

# Encrypt exactly ONE block
# ECB is used ONLY here to observe the AES block directly.
cipher1 = AES.new(key, AES.MODE_ECB)
cipher2 = AES.new(key, AES.MODE_ECB)

ciphertext1 = cipher1.encrypt(text1.encode())
ciphertext2 = cipher2.encrypt(text2.encode())

print("\nPlaintext 1 :", text1)
print("Ciphertext 1:", ciphertext1.hex())

print("\nPlaintext 2 :", text2)
print("Ciphertext 2:", ciphertext2.hex())

# Count changed ciphertext bits
different_bits = count_different_bits(ciphertext1, ciphertext2)
total_bits = 128
percentage = different_bits / total_bits * 100

print("\n" + "-" * 60)
print("AVALANCHE EFFECT")
print("-" * 60)

print("Changed bits :", different_bits, "of", total_bits)
print("Percentage   : {:.1f}%".format(percentage))

print("\nA small change in plaintext")
print("causes many ciphertext bits to change.")
(.venv) 3568Q6L7_740108:aes-demo 740108$ clear

(.venv) 3568Q6L7_740108:aes-demo 740108$ more demo_avalanche.py 
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def count_different_bits(data1, data2):
    return sum(
        (a ^ b).bit_count()
        for a, b in zip(data1, data2)
    )


print("=" * 60)
print("DEMO 2: AES Avalanche Effect")
print("=" * 60)

print("\nEnter TWO plaintexts.")
print("Each plaintext must be exactly 16 ASCII characters.")
print("Tip: change only ONE character between them.\n")

# Input plaintext
text1 = input("Plaintext 1: ")
text2 = input("Plaintext 2: ")

# Check length
if len(text1.encode()) != 16 or len(text2.encode()) != 16:
    print("\nERROR: Each plaintext must be exactly 16 bytes.")
    print("Plaintext 1:", len(text1.encode()), "bytes")
    print("Plaintext 2:", len(text2.encode()), "bytes")
    exit()

# Same AES-128 key
key = get_random_bytes(16)

print("\nSecret key :", key.hex())
print("Key length : 16 bytes = 128 bits")

# Encrypt exactly ONE block
# ECB is used ONLY here to observe the AES block directly.
cipher1 = AES.new(key, AES.MODE_ECB)
cipher2 = AES.new(key, AES.MODE_ECB)

ciphertext1 = cipher1.encrypt(text1.encode())
ciphertext2 = cipher2.encrypt(text2.encode())

print("\nPlaintext 1 :", text1)
print("Ciphertext 1:", ciphertext1.hex())

print("\nPlaintext 2 :", text2)
print("Ciphertext 2:", ciphertext2.hex())

# Count changed ciphertext bits
different_bits = count_different_bits(ciphertext1, ciphertext2)
total_bits = 128
percentage = different_bits / total_bits * 100

print("\n" + "-" * 60)
print("AVALANCHE EFFECT")
print("-" * 60)

print("Changed bits :", different_bits, "of", total_bits)
print("Percentage   : {:.1f}%".format(percentage))

