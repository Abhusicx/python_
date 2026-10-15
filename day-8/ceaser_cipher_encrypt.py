alphabets = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift): 
    encrypted_text = "" 
    for letter in text: 
        shifted_position = alphabets.index(letter) + shift
        shifted_position %= len(alphabets)
        shifted_letter = alphabets[shifted_position]
        encrypted_text += shifted_letter
    
    print(encrypted_text)

encrypt("sourav", 2)



    