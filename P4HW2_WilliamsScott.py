# Scott Williams
# 7/7/2025
# P4HW2
# Using a Python sentinel to improve previous assignment

#Set initial variables to store inputs if multiple employees are entered
total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

# Loop parameters
run_again = "any"
while run_again != "Done":
    # Input Employee Information
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    # Set conditions to end the loop
    if employee_name == "Done":
        break
    run_again = employee_name
    # Employee pay inputs
    hours_worked = float(input("Enter number of hours worked: "))
    base_rate = float(input("Enter employee's pay rate: "))

    # Set Remaining Variables for hourly calculations
    overtime_hours = hours_worked - 40
    base_hours = 40

    # Determine Overtime, if any, and regular/overtime pay via if/else statements
    if hours_worked > 40:
        overtime_pay = overtime_hours * base_rate * 1.5
        regular_pay = base_hours * base_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * base_rate
    
    

    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Display results

    print()
    print(f"Employee name:    {employee_name}")
    print()
    print(f"{'Hours Worked':<18}{'Pay Rate':<18}{'OverTime':<18}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay':<18}")
    print("------------------------------------------------------------------------------------------------------")
    print(f"{hours_worked:<18.2f}${base_rate:<17.2f}{overtime_hours:<18.2f}${overtime_pay:<17.2f}${regular_pay:<17.2f}${gross_pay:<17.2f}")
    print()
    print()

    # Add data to variables
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    

#Results of all employees entered
print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

