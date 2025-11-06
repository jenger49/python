"""
Your task is to design and implement a class in a programming language. This class will represent a person and hold personal data.
Assignment Steps:

Class Creation: Design a class named Person with the following data: name, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of
 data. These methods allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class. Use one instance for
 your made-up information and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance. Ensure the 
output is formatted and easy to read. You need to print out all the data for each.
 You can create a method that prints everything or call each get function one at a time.
"""
# Define the Person class
class Person:
    # Initialize the class with name, address, age, and phone number
    def __init__(self, name, address, age, phone_number):
        self._name = name 
        self._address = address
        self._age = age 
        self._phone_number = phone_number
    
    # Accessor methods
    # getter for name
    def get_name(self):
        return self._name
    # getter for address
    def get_address(self):
        return self._address
    # getter for age
    def get_age(self):
        return self._age
    # getter for phone number
    def get_phone_number(self):
        return self._phone_number
    
    # Method to display all information
    def display_information(self):
        print(f"Name: {self.get_name()}")
        print(f"Address: {self.get_address()}")
        print(f"Age: {self.get_age()}")
        print(f"Phone Number: {self.get_phone_number()}")
    
    # Create instances of the Person class
person1 = Person("John Smith", "123 Maple Rd", 30, "123-456-7890")
person2 = Person("Jane Doe", "432 Main St", 67, "098-765-4321")
person3 = Person("Mike Williams", "789 Wilson St", 41, "432-9870-4356")

    # Display information
person1.display_information()
person2.display_information()
person3.display_information()

