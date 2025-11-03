"""
Hangman Start - Week 10 Strings Demo

This program begins a simple version of Hangman. You will finish it by:
- Adding a list to keep track of guessed letters
- Checking if the letter was already guessed BEFORE checking if it is in the word
- Changing the word list to 15 words on a subject of your choice
- Display how many incorrect guesses they have left 
"""

# get random
import random

# available words
WORD_LIST = ["TIGER", "ELEPHANT", "GIRAFFE", "ALLIGATOR", "CROCODILE", "PENGUIN", "KANGAROO", 
"DOLPHIN", "CHEETAH", "LEOPARD", "ZEBRA", "TURTLE", "RACCOON", "HORSE", "FLAMINGO"]

max_wrong = 5

# main game function
def game(answer, display):
    wrong = 0
    right = 0
    guessed_letters = []
    max_wrong = 5

    print("Welcome to Hangman!")
    print("You will guess letters until you guess the animal")
    print("If you have 5 wrong guesses you will lose!")

    while True:
        # display letter spots
        for item in display:
            print(item, end=" ")
        
        # show guessed letters and guesses remaining
        print("\nGuessed letters:", " ".join(guessed_letters))
        print("Guesses remaining:", max_wrong - wrong)

        # get input from user
        print("\n\n")
        guess = input("Please enter a letter: ").upper()

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        else:
            guessed_letters.append(guess)

        bad_guess = True
        for i in range(len(answer)):
            if guess == answer[i]:
                display[i] = guess
                right += 1
                bad_guess = False

        if bad_guess:
            print("Wrong!")
            wrong += 1
            if wrong > 5:
                print("You Lose!")
                print("The correct word was:", answer)
                break

        if right == len(answer):
            print("You Win!")
            print("The word was:", answer)
            break


def main():
    answer = random.choice(WORD_LIST)
    display = ["_"] * len(answer)
    game(answer, display)


main()
