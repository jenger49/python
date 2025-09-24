"""
Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.
"""
# User inputs five names
names_input = input("Enter five names separated by commas: ")
names = names_input.split(",")

# Sorted list 
swapped = True
while swapped:
    swapped = False
    for i in range(len(names)-1):
        if names[i] > names[i+1]:
            names[i], names[i+1] = names[i+1], names[i]
            swapped = True # mark that a swap occurred
# Reverse the list
reversed_names = names[:]
reversed_names.reverse()
# Print the sorted and reversed lists
print("Sorted names:", names)
print("Reversed names:", reversed_names)