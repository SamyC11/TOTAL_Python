name=input("What's your name?: ")

sales=int(input("How many sales have you done ?:"))

commission=round(sales*13/100,3)

print(f"Congratulation {name}, your commission is {commission} dollars")