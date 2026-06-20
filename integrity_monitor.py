import hashlib
import time

def get_file_hash(filename):
    # Reads a file and outputs its unique SHA-256 fingerprint
    hasher = hashlib.sha256()
    with open(filename, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

target = "important_data.txt"
# Save original state
original_hash = get_file_hash(target)

print("Monitoring file integrity...")
while True:
    current_hash = get_file_hash(target)
    if current_hash != original_hash:
        print("⚠️ ALERT: File was modified or tampered with!")
        break
    time.sleep(5)
