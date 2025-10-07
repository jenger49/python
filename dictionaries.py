"""
Your mission is to create a Python program
 that uses a dictionary to translate letters into the NATO Phonetic Alphabet. 
This program will ask users for a word and then spell it out using the NATO codes.
Create the NATO Phonetic Alphabet Dictionary:
Construct a dictionary in Python named NATO_ALPHABET (this is a global constant), where each key is a letter, and its value is the corresponding NATO phonetic term.
Develop the Spelling Program:
Write a function to prompt the user for a word and iterate through each letter to find and print the NATO phonetic term.
Incorporate a Main Function:
Encapsulate your logic within a main() function for organization.
Test Your Program:
Test the program with various inputs, ensuring it works as expected.
"""
# Create the NATO Phonetic Alphabet Dictionary
NATO_Alphabet = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 
    'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 
    'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 
    'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee', 'Z': 'Zulu'}
# define the main function
def main():
    # Prompt the user for a word
    word = input('Enter a word: ').upper()
    # Iterate through each letter in the word
    for letter in word:
        # Find and print the corresponding NATO term
        if letter in NATO_Alphabet:
            print(f"{letter}: {NATO_Alphabet[letter]}")
        else:
            print(f"{letter}: (not in NATO alphabet)")
# Call the main function
main()
    