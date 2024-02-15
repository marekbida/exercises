"""
This example checks if a number entered by the user is within the range of 10 to 20, 
inclusive, using the and operator to combine two conditions.
"""

# Checking if a number is within a certain range
number = int(input("Enter a number: "))

if number >= 10 and number <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not in the range of 10 to 20.")