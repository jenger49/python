"""
Create a program named personal_diary.py.
Ask the user for date, time, and a diary entry.
Append the entry to diary.txt (do not overwrite).
Separate each entry with a blank line for readability.
Run your program at least three times to confirm new entries are saved properly.
"""
# Diary entry function
def write_diary_entry():
    # Get date, time, and diary entry from user
    date = input("Enter the date (YYYY-MM-DD): ")
    time = input("Enter the time (HH:MM): ")
    entry = input("Enter your diary entry: ")
    # Open diary.txt in append mode
    with open("diary.txt", "a") as diary_file:
        # Write the entry to the file
        diary_file.write(F"Date: {date}\n")

        diary_file.write(F'Time: {time}\n')
        
        diary_file.write(F'Entry: {entry}\n\n')
        print("Diary entry saved.")
# Diary entry main function
def main():
    write_diary_entry()

# Call main function
main()
            
                         