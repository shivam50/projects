alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    cipher = ""

    for letter in text:
        if letter in alphabet:
            indx = alphabet.index(letter)
            new_letter = alphabet[indx + shift]
            cipher += new_letter
    
    return cipher
  
def decrypt(text, shift):
    cipher = ""

    for letter in text:
        if letter in alphabet:
            indx = alphabet.index(letter)
            new_letter = alphabet[indx - shift]
            cipher += new_letter

    return cipher

if direction == "encode" :
    encoded_message = encrypt(text, shift)
    print(f"The encoded text is {encoded_message}")
elif direction == "decode" :
    decoded_message = decrypt(text, shift)
    print(f"The decoded text is {decoded_message}")
    



    