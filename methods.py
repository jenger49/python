"""
Objective: Understand and implement a class with specific attributes and methods and explore Python's special methods and functions.

Task Description:
Create the Pet Class:
Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
Implement get and set methods for each of these attributes.
Add a method called print_details that prints the details of the pet.
Create Instances:
Create three objects of the Pet class with different kinds, breeds, and names.

Call the print_details method for each object that you created

Demonstrate a Special Method or Function:
Choose three of the following and demonstrate its use with the Pet class instances:

__name__: Display the name of the class.
type(): Show the class used to instantiate a pet object.
__module__: Return the module name in which the Pet class is defined.
__bases__: Display the base classes of the Pet class (if any).
isinstance(): Check if an instance is of the Pet class.
"""

# Define the pet class
class Pet:
    def __init__(self, kind, breed, name):
        self._kind = kind
        self._breed = breed
        self._name = name

    # Accessor methods
    def get_kind(self):
        return self._kind
    def get_breed(self):
        return self._breed
    def get_name(self):
        return self._name
    
    # Mutator methods
    def set_kind(self, kind):
        self._kind = kind
    def set_breed(self, breed):
        self._breed = breed
    def set_name(self, name):
        self._name = name

    # Print details
    def print_details(self):
        print(f'Pet Details:\nKind: {self.get_kind()}\nBreed: {self.get_breed()}\nName: {self.get_name()}\n')

    # Create instances

pet1 = Pet("Dog", "Golden Retriever", "Buddy")
pet2 = Pet("Cat", "Siamese", "Ginny")
pet3 = Pet("Bird", "Parrot", "Chance")

# Call print details
pet1.print_details()
pet2.print_details()
pet3.print_details()

# Demonstrate special methods or functions
print(f'Class Name: {Pet.__name__}')
print(f'Class Type: {type(pet1)}')
print(f'Module Name: {Pet.__module__}')

