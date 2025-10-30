"""
Objective: Write a Python program that handles exceptions related to list operations. Your program will start with a predefined list of the top ten performing artists of all time and will include functionality to modify this list based on user input.
Modify Artist List: Write a function to replace an artist in the top_artists list. The function should ask the user for an index and a new artist name. Ensure your function catches and handles ValueError for invalid number conversion and IndexError for out-of-range indices.
General Error Handling: Modify your function to catch both ValueError and IndexError using a single except block. Provide a general error message like "An input error occurred."
"""

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    
    print("Top 10 Performing Artists of All Time:")
    print(top_artists)
    
    try:
            index = int(input("Enter the index of the artist to replace (0-9): "))
            new_artist = input("Enter the new artist name: ")
            top_artists[index] = new_artist
            print("Updated artist list:")
            print(top_artists)
        
    except ValueError:
            print(f"An error occurred. Please enter a valid index (0-9).")
    except IndexError:
            print(f"An error occurred. Please enter a valid artist name.")
            

main()

