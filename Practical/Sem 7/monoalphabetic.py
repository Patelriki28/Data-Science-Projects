


monoalpha_cipher = {
   'a': 'm','b': 'n','c': 'b','d': 'v', 'e': 'c','f': 'x','g': 'z','h': 'a','i': 's',
   'j': 'd','k': 'f','l': 'g','m': 'h','n': 'j','o': 'k','p': 'l','q': 'p','r': 'o',
   's': 'i','t': 'u','u': 'y','v': 't','w': 'r', 'x': 'e','y': 'w','z': 'q',' ': ' ',
}

def inverse_monoalpha_cipher(monoalpha_cipher):
   inverse_monoalpha = {}
   for key, value in monoalpha_cipher.items():
      inverse_monoalpha[value] = key
   return inverse_monoalpha

inversmonoalpha = inverse_monoalpha_cipher(monoalpha_cipher)

def encryption(string):
    cipher = ""
    for char in string:
        if char.isupper():
            cipher = (cipher + monoalpha_cipher[char.lower()]).upper()
        elif char.islower():
            cipher = cipher + monoalpha_cipher[char]
        elif char.isnumeric():
            cipher = cipher + char
        elif char == " ":
            cipher = cipher + char


    return cipher

def decryption(string):

    decipher = ""
    for char in string:
        if char.isupper():
            decipher = (decipher + inversmonoalpha[char.lower()]).upper()
        elif char.islower():
            decipher = decipher + inversmonoalpha[char]
        elif char.isnumeric():
            decipher = decipher + char
        elif char == " ":
            decipher = decipher + char

    return decipher

print("which operation you want to do?")
print("1.Encryption: 2.Decryption:")
inputvalue = int(input("Enter the Choice : "))
if inputvalue == 1:
    text = input("Enter text : ")
    print("encrypted text is : ",encryption(text))

else:
    text = input("Enter encrypted text ")
    print("decrypted text is : ", decryption(text))