# Simple Calculator

"""
Ask for 2 numbers as input from user and perform addition, subtraction, division, and
multiplication
"""

# User Input
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

# Addition
addNum = num1 + num2
print("\nAddition: ", addNum)

# Subtraction
subNum = num1 - num2
print("Subtraction:", subNum)

# Division
divNum = num1 / num2
print("Division:", divNum)

# Floor Division
divFloorNum = num1 // num2
print("Floor Division:", divFloorNum)

# Multiplication
mulNum = num1 * num2
print("Multiplication:", mulNum)

# Power
powNum = num1 ** num2
print("Power :", powNum)

print("\nNOTE: THE SAME WORKS FOR FLOATS AS WELL :)")


