import os, base64

def gen_api_key(byte_length=8):
    random_bytes = os.urandom(byte_length)
    return base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=')

print(gen_api_key())