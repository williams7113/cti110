# Scott Williams
# 7/7/2025
# P4LAB2
# Using loops within Python to create a multiplication table


#Use an outer 'while loop' to determine if the program repeats

run_again = "yes"
while run_again != "no":
    #Get integer from user
    user_num = int(input("Enter an integer: "))

    #Specify that no negative numbers can be used in this loop
    if user_num >= 0:
        #Use a for loop to create a multiplication table from 1-12
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        #Set an else statement to provide feedback if a negative value is input
        print("This program does not handle negative values")
    #Set input for repeating the program.  End if "no" is input
    run_again = input("Would you like to run the program again? Type 'no' to end. ")
        
    
#Loop has broken.  User entered "no".  Confirm termination of program

print("Program has ended.")
