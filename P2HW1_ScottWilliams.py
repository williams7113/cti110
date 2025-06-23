 # Scott Williams
 # 6/21/2025
 # P2HW1
 # To edit and enhance a previous submission with new tools

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
print(f"{"Location:":<25}{dest}")
print(f"{"Initial Budget:":<25}${ini_bud:.2f}")
print(f"{"Fuel:":<25}${gas:.2f}")
print(f"{"Accomodation:":<25}${hotel:.2f}")
print(f"{"Food:":<25}${food:.2f}")
print("-----------------------------------")
print()
print(f"{"Remaining Balance:":<25}${final:.2f}")
