"""
This program checks if the input day is either Saturday or Sunday to determine if it's a weekend, using the or operator.
"""

# Checking if the day is a weekend
day = input("Enter the day of the week: ").lower()

if day == "saturday" or day == "sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")
