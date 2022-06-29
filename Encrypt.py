from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PasswordHasher import password_hashing
from Credentials import password, file


def encrypt(file: str, key=None):
    # AES256 encryption: 32 bytes key
    if isinstance(key, bytes) and len(key) == 32:
        pass
    else:
        key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_GCM)
    file_data = open(file, "rb")
    data = file_data.read()
    file_data.close()
    file_out = open(file, "wb")
    cipherdata, tag = cipher.encrypt_and_digest(data)
    [file_out.write(x) for x in (cipher.nonce, cipherdata, tag)]
    file_out.close()


try:
    t = open(file)
    t.close()
except FileNotFoundError:
    raise FileNotFoundError
else:
    key = password_hashing(password)
    encrypt(file, key=key)
