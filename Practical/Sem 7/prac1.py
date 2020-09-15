  #def encripted(string,shift):
alphabets = 'abcdefghijklmnopqrstuvwxyz'
string_input = input("enter your orignal text :")
key = int(input("enter your shift key :"))

n = len(string_input)

string_input = ""

for i in range(n):
        character = string_input[i]
        print(character)
        location = alphabets.find(character)
        new_location = (location + key) %26
        string_input += alphabets[new_location]

        print(string_input)


