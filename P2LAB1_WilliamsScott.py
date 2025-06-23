# Scott Williams
# 6/21/2025
# P2LAB1_WilliamsScott
# Perform Basic Mathematical Calculations Involving a Circle

import math
#Get radius of circle from input
radius = float(input("What is the radius of the circle? "))
print()

#Equations to perform calculations on given radius
circum = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#Results of calculations
print(f"The diameter of the circle is {diam:.1f}")
print()
print(f"The circumference of the circle is {circum:.2f}")
print()
print(f"The area of the circle is {area:.3f}")
