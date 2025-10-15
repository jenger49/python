"""
In this assignment, you will create a Python program that generates 
a random number between 1 and 100. Your program should allow the user to guess the number, 
and provide feedback on how close their guess is to the actual number.
Import the random module and use it to generate a random number between 1 and 100.
Write a while loop that allows the user to enter a guess for the number.
Inside the loop, use the abs() function to calculate the absolute difference between the guess and the actual number.
Provide feedback based on the computed difference (e.g., "Very Hot" for close guesses).
The loop should continue until the user guesses the correct number.
"""
import random

# define the main function
def main():
        number = random.randint(1,100)
        guess = -1

        # loop until the user guesses the correct number
        while guess != number:
            try:
                guess = int(input("Enter your guess between 1 and 100: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value between 1 and 100.")
                difference = abs(guess - number)

            # check if the guess is within the valid range
            if guess < 1 or guess > 100:
                    print("The number is out of range. Please enter a number between 1 and 100.")

            # calculate the difference
            difference = abs(guess - number)


            if difference == 0:
                print("Congratulations! You guessed the correct number.")
            elif difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("Cold")
# Call the main function
main()
