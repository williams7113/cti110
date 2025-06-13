 # Scott Williams
 # 6/13/2025
 # P1HW1
 # Description: Use python to perform basic math, using input and print functions.
 
print("-----Calculating Exponents----")
print()
print()
CE_base = int(input("Enter an integer as the base value: "))
CE_exp = int(input("Enter an integer as the exponent: "))
CE_end = CE_base**CE_exp
print()
print()
print(CE_base, "raised to the power of", CE_exp, "is", CE_end, "!!")
print()
print()
print("-----Addition and Subtraction----")
print()
print()
arith_base = int(input("Enter a starting integer: "))
arith_add = int(input("Enter an integer to add: "))
arith_subtract = int(input("Enter an integer to subtract: "))
arith_end = arith_base+arith_add-arith_subtract
print()
print()
print(arith_base, "+", arith_add, "-", arith_subtract, "is equal to", arith_end)
