# MM, strings

# strings +> any saved inside of quotaion

name = input("What is your name: ").strip().capitalize

age = input('How old are you: ')
print(type(age))

# Concatenation => puts two strings directlynext to each other
print(age+age)
print(name + " " + "LaRose")

#
sentence = " The quick brown fox jumped over the lazy dog."
print(sentence)
print(sentence.replace("doge," "monkey"))
print(len(name)) #<= gets the lenght of a string
print(f"Tour name is {name} that is {len(name)} letters long. Your first initial is{name[0]}")