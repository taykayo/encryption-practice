#example of using cryptography to implement AES 256 bit encryption

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16) #initialization vector
#chose output feedback (OFB) mode to avoid having to pad data
cipher = Cipher(algorithms.AES(key), modes.OFB(iv), backend = backend)
encryptor = cipher.encryptor()
message = input("Please enter a message to be encrypted: ")
ct = encryptor.update(bytes(message, 'utf-8')) + encryptor.finalize()
print(ct) #prints encrypted text
decryptor = cipher.decryptor()
print(decryptor.update(ct) + decryptor.finalize()) #prints decrypted text
