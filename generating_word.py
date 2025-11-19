"""
Use a generator function with the yield statement in Python to generate all possible two-letter combinations from a given set of characters.
Background:
Generators in Python are a powerful tool for creating iterators in a memory-efficient way. The yield statement is used to produce a sequence of values over time, pausing the function execution between each one.
Task:
Create a Python program that uses a generator function to produce all possible two-letter combinations from a given list of characters. For example, if the list is ['a', 'b', 'c'], the program should generate 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'.
Instructions:
Define a generator function two_letter_combinations that takes a list of characters as an argument.
Use nested loops within the generator function to iterate over the list of characters. In each iteration, concatenate two characters and use the yield statement to yield the two-letter combination.
In the main method, call the generator function with a list of characters and iterate over the generator to print each combination. Create an original  5-letter list.
Include comments in your code to explain the logic behind the generator function and the use of the yield statement.
"""

# Define the generator function
def two_letter_combinations(characters):
    # Iterate over each character for the first position
    for first_char in characters:
        # Iterate over each character for the second position
        for second_char in characters:
            # Concatenate the two characters and yield the combinations
            yield first_char + second_char

# Main method to test the generator function
def main():
    # Define a list of characters
    characters = ['a', 'b', 'c', 'd', 'e']
    # Call the generator function and iterate over the results
    for combination in two_letter_combinations(characters):
        print(combination)
    
    # Call main function
main()


