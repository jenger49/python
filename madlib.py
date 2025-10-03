"""
Develop a Python-based Madlib based on a song of your choice. 
The program should collect at least 8 different pieces of information 
from the user and incorporate them into the song using named arguments. The goal is to practice using
functions, user input, and string manipulation in Python.
Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.
Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.
Write the Function:
Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
Use f-strings to incorporate these parameters into the song's lyrics.
Ensure the function prints the customized song lyrics.
Collect User Input:
Write code to collect user input for each of the 8 variables.
Use clear and descriptive prompts to guide the user.
Call the Function:
Call the custom_song function with the user inputs as named arguments.
Ensure the order of arguments matches the parameters in your function definition.
"""
def song(color, place, noun, noun2, person, adjective, place2, verb, noun3, verb2, verb3, verb4):
    print("\n\n")
    print(f"The snow glows {color} on the {place} tonight")
    print(f"Not a {noun} to be seen")
    print(f"A {noun2} of isolation")
    print(f"And it looks like I'm the {person}")
    print(f"The wind is {adjective} like this swirling storm inside")
    print(f"Couldn't keep it in, {place2} knows I tried")
    print(f"Don't let them in, don't let them {verb}")
    print(f"Be the good {noun3} you always have to be")
    print(f"Well, now they know")
    print(f"Let it {verb3}, let it {verb4}")

input_color = input("Enter a color: ")
input_place = input("Enter a place: ")
input_noun = input("Enter a noun: ")
input_noun2 = input("Enter another noun: ")
input_person = input("Enter any person: ")
input_adjective = input("Enter an adjective: ")
input_place2 = input("Enter another place: ")
input_verb = input("Enter a verb: ")
input_noun3 = input("Enter another noun: ")
input_verb2 = input("Enter another verb: ")
input_verb3 = input("Enter another verb: ")
input_verb4 = input("Enter another verb: ")

song(color=input_color, place=input_place, noun=input_noun, noun2=input_noun2, person=input_person, adjective=input_adjective, place2=input_place2, verb=input_verb, noun3=input_noun3, verb2=input_verb2, verb3=input_verb3, verb4=input_verb4)
