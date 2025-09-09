"""
Write a Python program that uses if-else statements and:
Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward and user-friendly.
"""

# User inputs age
age = int(input("How old are you? "))

# Check if the user is old enough to drive
if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")

# Check if the user is old enough to vote
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

# Check if the user is old enough to buy alcohol
if age >= 21:
    print("You can buy alcohol legally.")
else:
    print("You cannot buy alcohol legally.")

# Check if the user is eligible for a senior discount
if age >= 60:
    print("You are eligible for a senior discount.")
else:
    print("You are not eligible for a senior discount.")