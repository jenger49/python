"""
Accept a numeric grade from the user and display a 
letter grade. The  grading scale is  90 - 100: A, 
80-89: B, 70-79:C, 60-69:D, Below 60: F
Check to see if the number given is between 0 and 100. 
"""

# Input numeric grade
grade = int(input("Enter the numeric grade: "))

# Convert input to find the letter grade
if grade >= 90 and grade <= 100:
    print("The letter grade is: A")
elif grade >= 80 and grade < 90:
    print("The letter grade is: B")
elif grade >= 70 and grade < 80:
    print("The letter grade is: C")
elif grade >= 60 and grade < 70:
    print("The letter grade is: D")
elif grade >= 0 and grade < 60:
    print("The letter grade is: F")