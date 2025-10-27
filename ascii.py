""" 
Start Your Python Script:
Open your Python environment and start a new script.
Use a main() function to organize your code.
Prompt for User Input:
Ask the user to enter a single character using input().
Validate the Input:
Ensure the user enters precisely one character.
Use len() to check input length.
Convert to ASCII Value:
Use the built-in function ord() to get the ASCII value.
Display the Result:
Print the ASCII value to the user.
Reverse Lookup:
Prompt the user to enter an ASCII value.
Ensure that the value is between 32 and 127.
Use a try-except block to handle invalid inputs.
Use the built-in function chr() to get the corresponding character.
"""

def main(): 
    # Prompt for user input
    char = input("Please enter a single character: ")
    while len(char) != 1:
        print("I'm sorry, I can only work with single characters.")
        char = input("Please enter a single character: ")
        
    # Convert to ASCII value
    ascii_value = ord(char)
    print(f"The ascii value of {char} is {ascii_value}")
    
    try:  
        ascii_input = int(input("Please enter a ASCII value between 32 and 127: "))
        if 32 <= ascii_input <= 127:
            result_char = chr(ascii_input)
            print(f"The character for ASCII value {ascii_input} is {result_char}")
        else: 
            print("The value is out of range. Please enter a value between 32 and 127.")
    except ValueError:
        print("Invalid input. Please enter a number between 32 and 127.")

# Call the main function
main()