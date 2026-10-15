alphabets = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        shifted_position = alphabets.index(letter) - shift
        decrypted_letter = alphabets[shifted_position]
        decrypted_text += decrypted_letter

    print(decrypted_text)

decrypt("uqwtcx", 2)