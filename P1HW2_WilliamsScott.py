# Scott Williams
# 6/13/2025
# P1HW2
# Description:  Use python to perform travel expense calculations using variables/input/print

print("This program calculates and displays travel expenses")
print()

# Ask the user how much money their budget consists of.
ini_bud = int(input("Enter Budget: "))
print()

# Ask the user where their destination is.
dest = input("Enter your travel destination: ")
print()

# Inquire as to how much money on fuel will be spent.
gas = int(input("How much do you think you will spend on gas? "))
print()

# Inquire as to the estimated cost of accomodation stays.
hotel = int(input("Approximately, how much will you need for accomodations/hotel? "))
print()

# Inquire as to how much the user will spend on meals.
food = int(input("Last, how much do you need for food? "))

# Perform calculation representing the (Initial Budget) minus (all costs).
final = ini_bud-gas-hotel-food

print()
print("----------Travel Expenses----------")
print("Location:", dest)
print("Initial Budget:", ini_bud)
print()
print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food)
print()
print("Remaining Balance:", final)
