#Soluzione non ottimizzata
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def encrypt(text, shift):
    encrypted_word = ""
    for letter in text:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                if len(alphabet) + i + shift <= len(alphabet):
                    encrypted_word += alphabet[i + shift]
                else:
                    differenza = (shift+i) - len(alphabet)
                    encrypted_word += alphabet[differenza]
                    
    return encrypted_word
        

def decrypt(text, shift):
    decrypted_word = ""
    for letter in text:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                decrypted_word += alphabet[i - shift]
    return decrypted_word


print(art.logo)

def loop():
    end = False
    while not end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or type 'e' for exit :\n").lower()
        
        if direction == "encode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            print("Encrypted: " + str(encrypt(text, shift)))
        elif direction =="decode":
            tx2 = input("Type your message for decrypt:\n").lower()
            key = int(input("Type the shift number:\n"))
            print("Decrypted: " + str(decrypt(tx2, key)))
        elif direction == "e":
            print("Siamo usciti!")
            end = True

loop()