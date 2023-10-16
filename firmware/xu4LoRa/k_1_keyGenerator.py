import os
import binascii

# Number of keys you want to generate
numOfKeys = 5  # Change this to the desired number of keys

keys = []

for _ in range(numOfKeys):
    # Generate a random 16-byte key
    key = os.urandom(16)

    # Convert the key to a hexadecimal string
    hex_key = binascii.hexlify(key).decode('utf-8').upper()

    keys.append(hex_key)

# Now 'keys' contains the generated Application Keys
for i, key in enumerate(keys):
    print(f"Generated Application Key {i + 1}: {key}")

with open("generatedKeys.txt", 'w') as output:
    for row in keys:
        output.write(str(row) + '\n')