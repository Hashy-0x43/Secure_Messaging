from cryptography.fernet import Fernet

key_file = input("Key File: ")
encrypted_file = input("Encrypted File: ")
output_file = input("Output File: ")

encrypted = open(encrypted_file,"rb")
data = encrypted.read()
encrypted.close()

key_file = open(key_file,"rb")
key = key_file.read()
key_file.close()

f = Fernet(key)
decrypted = f.decrypt(data)

file = open(output_file,"wb")
file.write(decrypted)
file.close()