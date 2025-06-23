# Scott Williams
# 6/21/2025
# P2LAB2
# Using Dictionaries

#Create Dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}


#Get Keys

keys = cars.keys()
print(keys)
print()

#Get a car model from user input
car_name = input("Enter a vehicle to see it's mpg: ")
print()

#Get mpg for input car
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} mpg.")
print()

#Get travel distance from user input
distance = float(input(f"How many miles will you drive the {car_name}? "))
print()

#Calculate amount of gas needed to travel a certain distance
gas_needed = distance / car_mpg

print(f"{gas_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {distance} miles.")
