# MM, Fixing user inputs

while True:
    color = input("Tell me a color: ").strip().lower().capitalize()
    if color.isnumeric():
            print("That is a number not a color")
    elif " " in color:
            print("I said one word.")
    else:
        break

print(f"We painted the walls {color}!")