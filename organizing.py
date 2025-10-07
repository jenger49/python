"""
Write a Python program using a recursive function to calculate the factorial of a number. A recursive function is a function that calls itself to solve a problem.
Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
In your factorial function, first define the base case: n == 1 or n == 0, where the factorial is 1.
For the recursive step, return n * factorial(n-1) if n > 1.
Prompt the user for a non-negative integer and call factorial, printing the result.
"""
# Defining a function named factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
# Prompt the user for a non-negative integer
def main():
    number = int(input("Enter a non-negative integer: "))
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")
# Call the main function
main()
