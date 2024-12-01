import hashlib

def generate_hash(data):
    hash_object = hashlib.sha256(data.encode('utf-8'))
    return hash_object.hexdigest()

