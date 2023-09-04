def encrypt(plaintext, shift):  #plaintext is the text to be encrypted and shift is the nuer of positions to shift each character
    ciphertext = ""             # empty string stores encrypted text
    for char in plaintext:
        if char.isalpha():          #looping over each char in plaintext str to see if current char is a letter using isalpha() method
            # Shift each alphabetic character by the specified shift value
            if char.islower():       #checks if char is lowercase using islower() method
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))    #if lowercase, it's shifted using ASCII values of 'a' and 'A' as references
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))    #chr()func converts an ASCII value to its corresponding character
        else:
            # Keep non-alphabetic characters unchanged
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Shift each alphabetic character back by the specified shift value 
            if char.islower():
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            # Keep non-alphabetic characters unchanged
            plaintext += char
    return plaintext


# Example usage
plaintext = "Hello, World!"
shift = 3

encrypted_text = encrypt(plaintext, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)

