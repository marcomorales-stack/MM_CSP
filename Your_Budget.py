# MM, Your_Bugdet
while True:
    try:
        income = float(input("What is your monthly income"))
        break
    except:
        print("Thats not a number")

   
while True:
    try:
        income = float(input("What is your monthly rent/mortgage"))
        break
    except:
        print("Thats not a number")

   
while True:
    try:
        income = float(input("What is your monthly utilities"))
        break
    except:
        print("Thats not a number")

   
while True:
    try:
        income = float(input("What is your monthly groceries"))
        break
    except:
        print("Thats not a number")

    
while True:
    try:
        income = float(input("What is your monthly transportation"))
        break
    except:
        print("Thats not a number")
        income = float(input("What is your monthly income: $"))

        rent_percent = rent / income * 100
        utilities_percent = utilities / income * 100
        groceries_percent = groceries / income * 100
        transportation_percent = transportation / income * 100
        savings_percent = savings / income * 100

        spending = income - rent - utilities - groceries - transportation - savings
print("Your rent is $", round(rent, 2), "and that is", round(rent_percent), "% of your income.")
print("Your utilities are $", round(utilities, 2), "and that is", round(utilities_percent), "% of your income.")
print("Your groceries are $", round(groceries, 2), "and that is", round(groceries_percent), "% of your income.")
