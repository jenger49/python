"""
Enhance a basic Python program by implementing try and except statements to handle 
errors in user input, focusing on data type errors.
Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
Identify Potential Errors: Consider errors that might occur with non-numeric input.
Add Exception Handling: Implement try and except blocks to catch a ValueError. Handle
 incorrect data types with an error message.
Test Your Code: Ensure the exception handling works correctly with various inputs.
"""
# Starting code

# Simple Python program to calculate the square of a number
def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

square_number()
    