# Scott Williams
# 6/30/2025
# P3HW1
# Using Python if/else statements to determine wages, including overtime


# Input Employee Information
employee_name = input("Enter employee's name: ")
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

print("-----------------------------------------")
print(f"Employee name:    {employee_name}")
print()
print(f"{'Hours Worked':<18}{'Pay Rate':<18}{'OverTime':<18}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay':<18}")
print("------------------------------------------------------------------------------------------------")
print(f"{hours_worked:<18.2f}${base_rate:<17.2f}{overtime_hours:<18.2f}${overtime_pay:<17.2f}${regular_pay:<17.2f}${gross_pay:<17.2f}")
