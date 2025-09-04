"""
Create a Python application that allows users to input their total 
budget and the amount spent in various categories. The program will
 then calculate and display the percentage of the total budget each 
 category represents.
"""

net_monthly_income = float(input("Please enter your net monthly income: "))

housing = float(input("Please enter your rent or mortgage: "))

utilities = float(input("Please enter how much you spend on utilities: "))

groceries = float(input("Please enter how much you spent on grocieries: "))

transportation= float(input("Please enter how much you spend on transportation: "))
                      
health_care = float(input("Please enter how much you spend on health care: "))
                    
personal_care = float(input("Please enter how much you spent on personal care: "))

clothing = float(input("Please enter how much you spent on clothing: "))

debt = float(input("Please enter the amount of debt you have: "))

# category percentages
print(f"Housing: {housing / net_monthly_income :.2%}")
print(f"Utilities: {utilities / net_monthly_income :.2%}")
print(f"Groceries: {groceries / net_monthly_income :.2%}:")
print(f"Transportation: {transportation / net_monthly_income :.2%}")
print(f"Health Care{health_care / net_monthly_income :.2%}")
print(f"Personal Care{personal_care / net_monthly_income :.2%}")
print(f"Clothing{clothing / net_monthly_income :.2%}")
print(f"Debt{debt / net_monthly_income :.2%}")

# total spent
total = housing + utilities + groceries + transportation + health_care + personal_care + clothing + debt
print(f"Total: $  {total:.2f}")

# amount left

remainder = net_monthly_income - total
print(f"Remainder: $ {remainder:.2f}")