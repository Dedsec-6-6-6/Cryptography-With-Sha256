import hashlib

def hash_text_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def verify_hash(text, expected_hash):
    calculated_hash = hash_text_sha256(text)
    return calculated_hash == expected_hash
