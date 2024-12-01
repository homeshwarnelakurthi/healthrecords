from Crypto.Cipher import AES
import base64

def pad_data(data):
    block_size = AES.block_size
    padding_length = block_size - len(data) % block_size
    padding = chr(padding_length) * padding_length
    return data + padding

