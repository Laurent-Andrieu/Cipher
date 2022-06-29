from Crypto.Cipher import AES
from PasswordHasher import password_hashing
from Credentials import password, file


def decrypt(file: str, key: bytes):
    file_data = open(file, "rb")
    data = file_data.read()
    file_data.close()
    # Lecture des données
    nonce, cipher_data, tag = data[:16], data[16: -16], data[-16:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    try:
        unencryped_data = cipher.decrypt_and_verify(cipher_data, tag)
    except ValueError:
        print("Encrypted data or key is incorrect")
    else:
        file_out = open(file, "wb")
        file_out.write(unencryped_data)
        return unencryped_data


try:
    t = open(file)
    t.close()
except FileNotFoundError:
    raise FileNotFoundError
else:
    key = password_hashing(password)
    data = decrypt(file, key)
    print(data)
