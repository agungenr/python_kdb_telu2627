
import hashlib
import json


# STEP 1: Define a Block
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = {
            "index": self.index,
            "data": self.data,
            "previous_hash": self.previous_hash
        }

        block_string = json.dumps(
            block_data, sort_keys=True
        )

        return hashlib.sha256(
            block_string.encode()
        ).hexdigest()


# STEP 2: Create Blockchain
block1 = Block(
    1, "Alice -> Bob Rp100.000", "0"
)

block2 = Block(
    2, "Bob -> Charlie Rp50.000", block1.hash
)

block3 = Block(
    3, "Charlie -> David Rp20.000", block2.hash
)

chain = [block1, block2, block3]


# STEP 3: Validate Blockchain
def is_chain_valid(chain):
    for i, block in enumerate(chain):

        # Check whether stored hash matches data
        if block.hash != block.compute_hash():
            print(f"Block {block.index}: Hash mismatch!")
            return False

        # Check connection with previous block
        if i > 0:
            previous = chain[i - 1]

            if block.previous_hash != previous.hash:
                print(
                    f"Block {block.index}: "
                    "Previous hash mismatch!"
                )
                return False

    return True


# STEP 4: Display Blockchain
print("=== BLOCKCHAIN CREATED ===")

for block in chain:
    print(f"\nBlock {block.index}")
    print(f"Data          : {block.data}")
    print(f"Previous Hash : {block.previous_hash[:16]}...")
    print(f"Hash          : {block.hash[:16]}...")


# STEP 5: Validate Original Blockchain
print("\n=== VALIDATING BLOCKCHAIN ===")

if is_chain_valid(chain):
    print("Blockchain is VALID!")
else:
    print("Blockchain is INVALID!")


# STEP 6: Simulate Tampering
print("\n=== TAMPERING BLOCK 2 ===")

chain[1].data = "Bob -> Charlie Rp900.000"

# Simulate an attacker recalculating Block 2 hash
chain[1].hash = chain[1].compute_hash()

print("Block 2 transaction modified!")
print("New Block 2 Hash:", chain[1].hash[:16] + "...")


# STEP 7: Validate Again
print("\n=== VALIDATING AFTER TAMPERING ===")

if is_chain_valid(chain):
    print("Blockchain is VALID!")
else:
    print("Blockchain is INVALID!")
