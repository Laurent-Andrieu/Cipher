import hashlib


def password_hashing(passwd: str):
    # 32 bytes Key hash from password of any length
    try:
        passwd = passwd.encode('utf-8')
    except Exception:
        raise Exception
    else:
        pwd_hash = hashlib.sha256(passwd)
    return pwd_hash.digest()
