# Scott Williams
# 6/30/2025
# P3LAB
# Using Python IF statements to perform numerical calculations with money


#Get amount of money from user
change = float(input("Enter an amount of money: $"))

#Convert the money into an integer, rounded
change = round(change * 100)

if change == 0:
    print("No change")

#Determine how many dollars are present
num_dollars = change // 100
change = change - (num_dollars * 100)

#Determine how many quarters are present
num_quarters = change // 25
change = change - (num_quarters * 25)

#Determine how many dimes are present
num_dimes = change // 10
change = change - (num_dimes * 10)

#Determine how many nickels are present
num_nickels = change // 5
change = change - (num_nickels * 5)

#Determine how many pennies are present
num_pennies = change

#if/else statement for dollars
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

#if/else statement for quarters     
if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")

#if/else statement for dimes
if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

#if/else statement for nickels
if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
    else:
        print(f"{num_nickels} Nickels")

#if/else statement for pennies
if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")

