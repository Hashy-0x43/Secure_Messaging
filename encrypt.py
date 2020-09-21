from cryptography.fernet import Fernet

key_file = input("Key File: ")
encrypted_file = input("New Encrypted File: ")
message = input("Message: ")

message = message.encode()

key_file = open(key_file,"rb")
key = key_file.read()
key_file.close()

f = Fernet(key)
encrypted = f.encrypt(message)

file = open(encrypted_file,"wb")
file.write(encrypted)
file.close()