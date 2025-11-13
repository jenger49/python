"""
Assignment Part 1: Defining Classes
File 1: Write an Employee class with the following attributes:

Employee name
Employee number
Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:

Shift number (integer: 1 for day, 2 for night)
Hourly pay rate
Implement accessor and mutator methods (getters and setters) for each class.

Assignment Part 2: Implementing and Testing
 

Part 2: Write a script to:

Create an instance of ProductionWorker.
Prompt the user for each attribute's data.
Store and then display the data using the object's methods.
"""

# define employee class
class employee: 
    # initialize attributes
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number

    # accessor and mutator methods
    def get_employee_name(self):
        return self.employee_name
    def set_employee_name(self, employee_name):
        self.employee_name = employee_name
    def get_employee_number(self):
        return self.employee_number
    def set_employee_number(self, employee_number):
        self.employee_number = employee_number

class ProductionWorker(employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
            super().__init__(employee_name, employee_number)
            self.shift_number = shift_number
            self.hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
            return self.shift_number
    def set_shift_number(self, shift_number):
            self.shift_number = shift_number
    def get_hourly_pay_rate(self):
            return self.hourly_pay_rate
    def set_hourly_pay_rate(self, hourly_pay_rate):
            self.hourly_pay_rate = hourly_pay_rate       

# define main function
def main():
    # get employee info from user
    employee_name = input("Enter Employee Name: ")
    employee_number = input("Enter Employee Number: ")
    emp = employee(employee_name, employee_number)
    shift_number = int(input("Enter Shift Number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Enter Hourly Pay Rate: "))

    # print details of employee
    print("Details of Employee:")

    print(f"Name: {emp.get_employee_name()}")
    print(f"Employee Number: {emp.get_employee_number()}")
    print(f"Shift Number: {shift_number}")
    print(f"Hourly Pay Rate: {hourly_pay_rate}")

# recall main function
main()
