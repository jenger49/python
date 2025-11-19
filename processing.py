"""
Read each line in a loop
Strip newline and convert to float
Add to running total
Count the lines
Format and print each number
Print the total, count, and average
Use a main() function
Use try and except for errors
"""

# define main function
def main():
    try:
        # initialize variables
        total = 0.0
        count = 0
        # open the file 
        with open("sales_totals.txt") as file:
            # read each line in the file
            for line in file:
                # strip newline and convert to float
                number = float(line.strip())
                # add to running total
                total += number
                # increment line count
                count += 1
                # format and print each number 
                print(f"{number:.2f}")
                
        # calculate average
        average = total / count if count > 0 else 0
            
        # print total, count, and average
        print(f"Total: {total:.2f}")
        print(f"Count: {count}")
        print(f"Average: {average:.2f}")
        
    except FileNotFoundError:
        print("Error: The file was not found.")
    except ValueError:
        print("Error: Could not convert data to a float.")
main()
