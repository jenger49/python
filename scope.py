"""
Create a BMI calculator that takes a user's weight and height, calculates their BMI, 
and categorizes it as underweight, normal weight, overweight, or obese.
Global Variables:
Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254 m).
Main Function:
Prompt the user for their weight in pounds and height in inches.
Convert the inputs to metric units using global conversion constants.
Calculate BMI using the formula bmi = weight / (height * height).
Determine the BMI category based on standard ranges.
Display the BMI value and category.
Commenting:
Include comments to explain key parts of the code.
"""
# Conversion constants
lb_to_kg = 0.453592
in_to_m = 0.0254

# Prompt the user for weight and height

weight_lb = float(input("Enter you weight in pounds: "))
height_in = float(input("Enter your height in inches: "))
    
# Convert weight to kilograms and height to meters
weight_kg = weight_lb * lb_to_kg
height_m = height_in * in_to_m
    # Calculate BMI
bmi = (weight_kg / (height_m * height_m)) 
    # Determine BMI category
if bmi < 18.5:
        category = "Underweight"
elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
elif 25 <= bmi < 29.9:
        category = "Overweight"
elif 30 <= bmi < 34.9:
        category = "Obesity class 1 (Moderate)"
elif 35 <= bmi < 49.9:
        category = "Obesity class 2 (Severe)"
else:
        category = "Obesity class 3 (Very severe)"
# Display the BMI value and category
print(f"Your BMI is: {bmi:.2f})")
print(f"You are in the {category} category.")