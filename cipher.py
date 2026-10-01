# MM, 7th, Cipher


encrypt = input("Would you like to (E)ncrypt or (D)ecrypt a message? ")
message = input("Enter your message: ")
amount = input("Enter a shift amount: ")

for letter in message:
    if letter.isalpha():
        letter = ord(letter)
        print(letter)
        letter += amount
        print(letter)
        