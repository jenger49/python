"""
Write a Python program that includes two functions - one to calculate the area of a square and another for the area of a circle.
"""

# Square and circle functions will accept two variables, calculate, and display the area of a square and circle
def square(side):
    area = side * side
    print(f"The area of the square is: {area: ,.2f}")


def circle(radius):
    area = radius * 3.14
    print(f"The area of the circle is: {area: ,.2f}")


square(8)
circle(13)