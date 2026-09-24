# MM, 7th, loops
import random

count = 1

while count <= 10:
    print(count)
    count += 1

ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break
    print("Duck. . . .")
    ducks += 1 #ducks = ducks + 1
print("GOOSE!!!!")

# Complex Data Type = holds other data in it
siblings =["Charlize, Jimena, Miranda, Cami"]
print(siblings{2})