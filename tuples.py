"""
 Imagine you're planning the classes for a programming certificate. You need to list out six classes. Here's what you need to do:
Create a tuple named programming_classes with these classes: 'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'.
Write a program that uses a for loop to print each class in the tuple.
Use the len function to print how many courses are in the tuple.
Make sure to use a main function for this program.
"""
def main():
    # Create a tuple named programming_classes
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')
    # Use a for loop to print each class in the tuple
    for course in programming_classes:
        print(course)
    # Use the len function to print how many courses are in the tuple
    print(f"Total number of courses: {len(programming_classes)}")
# Call the main function
main()