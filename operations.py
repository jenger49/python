"""
Develop a program to manage ticket sales for an event.
"""
# List of available seats
available_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Display available seats 
print("Available seats:", available_seats)
# Prompt the customer to select a seat
while True:
    select = int(input("Please select an available seat by entering its number: "))
    # Remove the selected seat from the list of available seats
    if select == 0:
        print("Thank you for using our ticketing system. Goodbye!")
        break
    if select not in available_seats:
        print("Invalid selection. Please try again.")
    if select in available_seats:
        available_seats.remove(select)
    print("Updated list of available seats:", available_seats)
    if len(available_seats) == 0:
        print("All seats are sold out. Thank you!")
        break