"""
Write a short interactive Python program of your choice that uses try and except to catch and respond to at least two specific exceptions. Your program should:

Include a main() function.
Use try and except to catch specific errors like ValueError or ZeroDivisionError.
Provide helpful messages when errors occur
build a number guessing game
"""
import random

def main():
    random_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    while True:
        try:
            guess = int(input("Please enter your guess, between 1 and 100: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Your guess is out of range. Please try again.")
                continue
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again,")
            else:
                print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
                break
        except ValueError: 
            print("Invalid input. Please enter a valid number between 1 and 100.")
        
main()