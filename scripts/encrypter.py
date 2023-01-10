from cryptography.fernet import Fernet
import pathlib


def encrypt(key: bytes, file):
    """Detects if 'file' is actually a file or if it's a text
    then encrypts it and is returning the path to the file or
    the text in bytes like encrypted utf-8 format"""
    fernet = Fernet(key)

    if not pathlib.Path(f"{file}").is_file():
        return fernet.encrypt(file.encode())

    with open(file, 'rb') as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(file, 'wb') as f:
        f.write(encrypted)

    return pathlib.Path(file)


def decrypt(key: bytes, file):
    """Detects if 'file' is actually a file or if it's a text
    then decrypts it and is returning the path to the file or
    the text in utf-8 format"""
    fernet = Fernet(key)

    if not pathlib.Path(f"{file}").is_file():
        return fernet.decrypt(file).decode()

    with open(file, 'rb') as f:
        data = f.read()

    decrypted = fernet.decrypt(data)

    with open(file, 'wb') as f:
        f.write(decrypted)

    return pathlib.Path(file)


def gen_key() -> bytes:
    """generates one key and saves it to the key.txt file, also returns it"""
    key = Fernet.generate_key()
    with open("key.txt", "wb") as f:
        f.write(key)
    return key
