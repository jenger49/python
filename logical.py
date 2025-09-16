"""
In this exercise, you will practice using logical
operators (and, or, not) in Python. Your task is
to create a program that prompts the user for 
two integer inputs and then demonstrate the use 
of these operators.
"""

# user inputs integer values
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# Implement six different logical comparisons using the input integers. Include two examples for each of the following operators: and, or, not
if num1 > 0 and num2 > 0:
    print("Both numbers are greater than zero: True")
elif num1 < 0 and num2 < 0:
    print("Both number are greater than zero: False")
if num1 > 100 and num2 > 100:
    print("Both numbers are greater than 100: True")
elif num1 < 100 and num2 < 100:
    print("Both numbers are greater than 100: False")

# Using or logical comparisons
if num1 % 2 == 0 or num2 % 2 == 0:
    print("Either number is even? True")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Either number is even? False")
if num1 < 100 or num2 < 100:
    print("Either number is less than 100? True")
elif num1 > 100 or num2 > 100:
    print("Either number is less than 100? False")

# Using not logical comparisons
if num1 != num2:
    print("The numbers are not equal: True")
elif num1 == num2:
    print("The numbers are not equal: False")
if num1 != 0:
    print("The first number is not zero: True")
elif num1 == 0:
    print("The first number is not zero: False")