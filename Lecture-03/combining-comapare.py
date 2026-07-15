age = int(input("age: "))
income = int(input("income: "))

if age <= 18 and age <= 65 and income > 30000:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")