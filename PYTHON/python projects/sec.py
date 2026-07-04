import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()
random.shuffle(key)
#print(f"chars: {chars}")
#print(f"key: {key}")

"""
# ENCRYPT
plain_text = input("Enter a message to encypt: ")
cipher_text = ""

for letters in plain_text:
    index = chars.index(letters)
    cipher_text += key[index]
    
print(f"original message : {plain_text}")
print(f"encypted message : {cipher_text}")
"""

# DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letters in cipher_text:
    index = key.index(letters)
    plain_text += chars[index]
    
print(f"encrypted message : {cipher_text}")
print(f"original message : {plain_text}")