# creating a program to change plaintext to Ciphertext using ceaser cipher algorithm.
alphabets = 'abcdefghijklmnopqrstuvwxyz'

pos_letters = len(alphabets)
def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = alphabets.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= pos_letters:
                    new_index -= pos_letters
                ciphertext += alphabets[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = alphabets.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0 :
                    new_index += pos_letters
                plaintext += alphabets[new_index]
    return plaintext

print()
print("CEASAR CIPHER PROGRAM ")
print()

print("Do you want to encrypt or decrypt?")
user_input = input('e/d:').lower()
print()

if user_input == 'e':
    print('ENCRYPTION IS SELECTED')
    print()
    key = int(input('Enter the key between 1 to 26 :'))
    text = input('Enter the text to encrypt:')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')
    
elif user_input == 'd':
    print('DECRYPTION IS SELECTED')
    print()
    key = int(input('Enter the key between 1 to 26 :'))
    text = input('Enter the text to decrypt:')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')