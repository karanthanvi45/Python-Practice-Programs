# Write a Python program to solve quadratic equation.
# The standard form of a quadratic equation is:
# 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0
# where
# a, b and c are real numbers and
# 𝑎≠0
# The solutions of this quadratic equation is given by:
# (−𝑏 ± (𝑏2 − 4𝑎𝑐)1/2)/(2𝑎)

import math
a= float(input("enter coefficient a: "))
b= float(input("enter coefficient b: "))
c= float(input("enter coefficient c: "))

discrminant = b**2 - 4*a*c
if discrminant > 0:
    root1 = (-b + math.sqrt(discrminant))/(2*a)
    root2 = (-b - math.sqrt(discrminant))/(2*a)
    print((f"Root 1: {root1}"))
    print((f"Root 2: {root2}"))
elif discrminant == 0:
    root = -b/(2*a)
    print(f"Root: {root}")
else:
    real_part = -b/(2*a)
    imaginary_part = math.sqrt(abs(discrminant))/(2*a)
    print(f"Root 1: {real_part}+ {imaginary_part}i")
    print(f"Root 2: {real_part}- {imaginary_part}i")