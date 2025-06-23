 # Scott Williams
 # 6/21/2025
 # P2HW2
 # Utilizing list functions within Python

 
# Prompt the user to input grades for all module tests
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store the input grades into a list with a descriptive name
module_grades_list = [module1, module2, module3, module4, module5, module6]

# Grade calculations
lowest_grade = min(module_grades_list)
highest_grade = max(module_grades_list)
sum_grades = sum(module_grades_list)
average_grade = sum_grades / len(module_grades_list)

# Display the results with proper formatting
print()
print("------------Results------------")
print(f"{"Lowest Grade:":<25}{lowest_grade}")
print(f"{"Highest Grade:":<25}{highest_grade}")
print(f"{"Sum of Grades:":<25}{sum_grades}")
print(f"{"Average:":<25}{average_grade:.2f}")
print("--------------------------------------")
