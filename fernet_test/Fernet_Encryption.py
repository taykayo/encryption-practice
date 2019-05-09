#this encrypts data input by user using Fernet symmetric encrypton
#using 128-bit AES in CBC mode and PKCS7 padding,
#with HMAC using SHA256 for authentication
#must pip install cryptography

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
message = input("Please enter message to encrypt: ")
token = f.encrypt(bytes(message, 'utf-8'))
print(token)
print(f.decrypt(token))
