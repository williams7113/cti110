# Scott Williams
# 7/14/2025
# P5LAB
# Using Python functions to improve previous assignment


import random


def disperse_change(change):
    
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
    


def main():
    #Function logic

    #Generate the amount owed via provided randomization code
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    #Create variable to represent payment put into machine
    money_in = float(input("How much cash will you put in the self-checkout? "))

    #Calculate change owed to customer
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    #Call the disperse_change function
    print()
    disperse_change(change)


#Call the main function
main()




