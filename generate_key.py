import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "password" # This password along with the salt will be used to generate a key.
password = password_provided.encode()
salt = # Use os.urandom() to generate a salt and paste the exact output here.
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

file = open("key.txt","wb")
file.write(key)
file.close()