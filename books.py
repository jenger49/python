"""
In this assignment, you will create a Python program that collects book titles from a user. Your program should use a while loop to prompt the user to enter a total of 10 book titles. Follow these steps to complete your assignment:

Set Up the Main Function: Write your program inside a main function. This is where your while loop will be implemented.
Collect Book Titles: Use a while loop to ask the customer to enter 10 book titles. Store these titles in a list.
Ensure proper capitalization: Use the title function to ensure that the first letter is capitalized before storing it in the list.
Create a Sorted List: Once all titles are collected, save them to a new list named books_sorted. This list should contain the titles in alphabetical order.
Display the Titles: Use a for loop to print each title from the sorted list on a separate line.
Test Your Program: Ensure your program runs correctly and meets all the requirements.
"""
def main():
    books = ['Wonder', 'The Great Gatsby', 'To Kill a Mockingbird', 'The Catcher in the Rye', 'Brave New World', 'Lord of the Flies', 'Charlottes Web', 'The Hobbit', 'A Wrinkle in Time', 'The Giving Tree']
    books_sorted = sorted(books)
    for book in books_sorted:
        print(book)

# Call the main function
main()