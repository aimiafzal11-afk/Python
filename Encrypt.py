import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

#ENCRYPTION
plain_text = input("Enter message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += (keys[index])

print(f"Plain Text: {plain_text}")
print(f"Encrypted Text: {cipher_text}")

#DECRYPTION
cipher_text = input("\nEnter message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += (chars[index])

print(f"Encrypted Text: {cipher_text}")
print(f"Plain Text: {plain_text}")
