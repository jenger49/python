"""
Write a Python function named calculate_interest that computes and returns simple interest based on given parameters. (Note - you will call the function from the main() function, main is required!
Define the function calculate_interest with appropriate parameters.
In main request the three parameters from the user, then pass them as variable.
Apply the formula to calculate the simple interest.
Return the calculated interest.
Print the result using an f-string
"""
# define calculate_interest function
def calculate_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# define the main function    

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time in years: "))

# define interest
interest = calculate_interest(principal, rate, time)
    
# print the result    
print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")

