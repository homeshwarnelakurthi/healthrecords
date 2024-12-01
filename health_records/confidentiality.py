from Crypto.Cipher import AES
import base64

def pad_data(data):
    block_size = AES.block_size
    padding_length = block_size - len(data) % block_size
    padding = chr(padding_length) * padding_length
    return data + padding

def unpad_data(data):
    padding_length = ord(data[-1])
    return data[:-padding_length]

def encrypt_data(data, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    padded_data = pad_data(data)
    encrypted_data = cipher.encrypt(padded_data.encode('utf-8'))
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_data(encrypted_data, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decoded_data = base64.b64decode(encrypted_data)
    decrypted_data = cipher.decrypt(decoded_data).decode('utf-8')
    return unpad_data(decrypted_data)
