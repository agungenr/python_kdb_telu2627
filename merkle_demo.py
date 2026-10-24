
import hashlib


# STEP 1: SHA-256 function
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()


# STEP 2: Calculate Merkle Root
def calculate_merkle_root(transactions):

    # Hash each transaction
    hashes = [sha256(tx) for tx in transactions]

    print("\nTransaction Hashes:")
    for i, h in enumerate(hashes):
        print(f"H{i+1}: {h[:16]}...")

    level = 1

    # Combine hashes until one root remains
    while len(hashes) > 1:
        next_level = []

        for i in range(0, len(hashes), 2):
            left = hashes[i]

            # Duplicate last hash if number is odd
            right = (
                hashes[i + 1]
                if i + 1 < len(hashes)
                else left
            )

            combined_hash = sha256(left + right)
            next_level.append(combined_hash)

        print(f"\nMerkle Tree Level {level}:")
        for h in next_level:
            print(h[:16] + "...")

        hashes = next_level
        level += 1

    return hashes[0]


# STEP 3: Create four transactions
transactions = [
    "Alice -> Bob Rp100.000",
    "Bob -> Charlie Rp50.000",
    "Charlie -> David Rp20.000",
    "David -> Eve Rp10.000"
]


print("=== ORIGINAL TRANSACTIONS ===")

for i, tx in enumerate(transactions):
    print(f"TX{i+1}: {tx}")


# STEP 4: Calculate original Merkle Root
print("\n=== ORIGINAL MERKLE TREE ===")

original_root = calculate_merkle_root(transactions)

print("\nOriginal Merkle Root:")
print(original_root)


# STEP 5: Simulate tampering
print("\n=== TAMPERING TRANSACTION 3 ===")

transactions[2] = "Charlie -> David Rp900.000"

print("TX3 modified:")
print(transactions[2])


# STEP 6: Calculate new Merkle Root
print("\n=== NEW MERKLE TREE ===")

new_root = calculate_merkle_root(transactions)

print("\nNew Merkle Root:")
print(new_root)


# STEP 7: Compare Merkle Roots
print("\n=== MERKLE ROOT VERIFICATION ===")

if original_root == new_root:
    print("VALID: Merkle Root unchanged!")
else:
    print("INVALID: Merkle Root changed!")
    print("Transaction data has been modified!")
