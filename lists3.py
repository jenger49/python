"""
Create a Python script to track heart rate readings and calculate the average heart rate.
Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
Use a loop to prompt the user for heart rate (in BPM) at each time slot.
Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
Calculate the average heart rate and display it.
"""
# Define time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

total = 0

heart_rates = []
# Get heart rate readings from the user
for slot in time_slots:
    rate = int(input(f"Enter your heart rate (in BPM) in the {slot}: "))
    heart_rates.append([slot, rate])
    total += rate
# Calculate average heart rate
average = total / len(time_slots)
print(f"Your average heart rate is: {average} BPM")