"""
This example checks if a year is a leap year by combining conditions with and 
and or logical operators, considering the special cases for years divisible by 100 and 400.
"""

# Check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")