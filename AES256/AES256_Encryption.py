#example of using cryptography to implement AES 256 bit encryption

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from pathlib import Path
from base64 import b64decode, b64encode
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
backend = default_backend()



# Key is stored separately, IV is first 16 digits of whatever you encrypt
def create_key():
    key = ChaCha20Poly1305.generate_key()

    with open(Path("C:/Users/tkaake/Desktop/enc_key.txt"), "w+") as key_file:
        key = b64encode(key).decode('utf-8')
        key_file.write(key)


def encrypt():
    with open(Path("C:/Users/tkaake/Desktop/enc_key.txt"), "r") as key_file:
        key = key_file.read()

        key = b64decode(key.encode('utf-8'))

    message = input("Please enter a file to encrypt: ")
    with open(Path(message), "r+b") as file_to_enc:
        data_to_enc = str(file_to_enc.read())

        iv = os.urandom(16)  # initialization vector

        cipher = Cipher(algorithms.AES(key), modes.OFB(iv),
                        backend=backend) # chose output feedback (OFB) mode to avoid having to pad data
        encryptor = cipher.encryptor()

        ct = encryptor.update(bytes(data_to_enc, 'utf-8')) + encryptor.finalize()
        # iv = b64encode(iv).decode('utf-8')  # b64encoded IV decoded as utf-8
        file_to_enc.truncate(0)
        file_to_enc.seek(0)
        file_to_enc.write(iv)
        file_to_enc.write(ct)

def decrypt():
    with open(Path("C:/Users/tkaake/Desktop/enc_key.txt"), "r") as key_file:
        key = key_file.read()
        key = b64decode(key.encode('utf-8'))

    message = input("Please enter a file to decrypt: ")
    with open(Path(message), "r+b") as file_to_dec:
        data_to_dec = file_to_dec.read()
        iv = data_to_dec[0:16]

        cipher = Cipher(algorithms.AES(key), modes.OFB(iv),
                        backend=backend)  # chose output feedback (OFB) mode to avoid having to pad data
        decryptor = cipher.decryptor()
        ct = decryptor.update(data_to_dec[16:]) + decryptor.finalize()
        file_to_dec.seek(0)
        file_to_dec.truncate(0)
        file_to_dec.seek(0)
    with open(Path(message), "r+") as file_to_write:

        file_to_write.write(ct.decode()[2:-1])

