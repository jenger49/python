"""
Define a Pet Class:
Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type.
Set a default value for pet_type as "Dog".
Implement getter and setter methods for all properties.
Include a class variable vet_name set to the name of your veterinary office.
Add a method display_pet_info to print all details of the pet and owner.
Create Pet Objects:
Instantiate at least three pet objects with different details.
Show the use of setter methods for at least one pet object.
Implement Property Existence Check:
Write a function check_property that uses hasattr() to verify if a property exists in a pet object.
Display Information:
Use display_pet_info to print details for each pet.
Show three examples of check_property being used on various properties and pets.
show two examples of display_pet_info on different instances of pet that you create
"""
# Define pet class
class Pet: 
    # Class variable
    vet_name = "Meow, Woof & Everything In Between Veterinary Clinic"
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Instance variables
        self._owner_first_name = owner_first_name
        self._owner_last_name = owner_last_name
        self._pet_id = pet_id
        self._pet_name = pet_name
        self._pet_type = pet_type

        # Getter methods
    def get_owner_first_name(self):
        return self._owner_first_name
    def get_owner_last_name(self):
        return self._owner_last_name 
    def get_pet_id(self):
        return self._pet_id
    def get_pet_name(self):
        return self._pet_name
    def get_pet_type(self):
        return self._pet_type
        
        # Setter methods
    def set_owner_first_name(self, owner_first_name):
        self._owner_first_name = owner_first_name 
    def set_owner_last_name(self, owner_last_name):
        self._owner_last_name = owner_last_name
    def set_pet_id(self, pet_id):
        self._pet_id = pet_id
    def set_pet_name(self, pet_name):
        self._pet_name = pet_name
    def set_pet_type(self, pet_type):
        self._pet_type = pet_type
        # Method to display pet information
    def display_pet_info(self):
        print(f"Owner First Name: {self._owner_first_name}")
        print(f"Owner Last Name: {self._owner_last_name}")
        print(f"Pet ID: {self._pet_id}")
        print(f"Pet Name: {self._pet_name}")
        print(f"Pet Type: {self._pet_type}")
# Create pet objects
pet1 = Pet("Michael", "Smith", 123, "Bud", "Dog")
pet2 = Pet("Olivia", "Johnson", 456, "Winter", "Cat")
pet3 = Pet("Emma", "Williams", 789, "Max", "Turtle")

# Use setter method
pet1.set_pet_name("Buddy")
    

# Function to check property
def check_property(pet, property_name):
    return hasattr(pet, property_name)

# Display pet information
pet1.display_pet_info()
pet2.display_pet_info()

# Check properties
print(check_property(pet1, '_pet_name'))
print(check_property(pet2, '_owner_first_name'))
print(check_property(pet3, '_pet_color'))




