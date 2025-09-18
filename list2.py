"""
Create a list representing 20 seats, numbered 1 to 20.
Display the list of available seats to the customer.
Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
Remove the selected seat from the list of available seats and display the updated list.
If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
Ensure the program gracefully handles all scenarios and is user-friendly.
"""

# List of available seats
available_seats = ["1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20"]
print("Available Seats", available_seats)
selection = 0
while selection >= 0 and selection < 20:
    selection = int(input("Please select a seat by entering its number: "))
    if selection < 1 or selection > 20:
        print(f"{selection} is invalid")
        
available_seats.remove(selection)



