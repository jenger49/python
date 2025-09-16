"""
 This task will help you practice working with 
 lists, user input, and basic calculations
"""

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps = [] # empty list
total = 0
for day in days:
    in_steps = int(input(f"How many steps did you take on {day}? "))
    steps.append(in_steps)

for my_step in steps:
    print(my_step)
    total = total + my_step
    print(f"Total Steps: {total}")

print(f"Average Steps: {total / len(steps): .2f}")