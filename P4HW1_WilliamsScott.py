# Scott Williams
# 7/7/2025
# P4HW1
# Using loops to improve on previous assignments

#Have user input the number of scores to be entered
num_scores = int(input("How many scores do you want to enter? "))
print()

#Provide list for scores to be entered into
score_list = []

#Create for loop using the number of scores entered as the range
for i in range(num_scores):  
    
        score_input = float(input(f"Enter score #{i + 1}: "))
        #Embed while loop in case a score is <0 or >100
        while score_input < 0 or score_input > 100:
                print()
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
                score_input = int(input(f"Enter score #{i + 1} Again: "))
       
        #Add valid scores to the list
        score_list.append(score_input)


low = min(score_list)



# Display the results with proper formatting
print()
print()
print("------------Results------------")
print(f"{"Lowest Grade":<15}: {low:.1f}")
#Perform Calculations after removing lowest entry
score_list.remove(low)
sum_grades = sum(score_list)
avg = sum_grades / len(score_list)
print(f"{"Modified List":<15}: {score_list}")
print(f"{"Scores Average":<15}: {avg:.2f}")
# Determine letter grade for average
if avg >= 90:
    print(f"{"Your grade is":<15}: A")
elif avg >= 80:
    print(f"{"Your grade is":<15}: B")
elif avg >= 70:
    print(f"{"Your grade is":<15}: C")
elif avg >= 60:
    print(f"{"Your grade is":<15}: D")
else:
    print(f"{"Your grade is":<15}: F")
print("--------------------------------------")

