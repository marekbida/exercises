"""
In this program:

- The if statement checks if the user's age is 18 or older to be eligible to vote.
- The elif statement provides an additional condition to catch invalid input (negative age).
- The else statement covers the scenario where the user is under 18 and not eligible to vote.
"""


# Ask the user for their age
age = int(input("Enter your age: "))

# Check if the user is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
elif age < 0:
    print("Error: Age cannot be negative.")
else:
    print("You are not eligible to vote yet.")
