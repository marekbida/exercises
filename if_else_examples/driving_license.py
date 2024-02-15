"""
This example uses nested if statements to first check if a person is of legal driving age,
and then within that block, it checks if the person has a driving license.
"""

# Nested if statements to check multiple conditions
age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ").lower()

if age >= 18:
    if has_license == "yes":
        print("You can drive.")
    else:
        print("You are old enough but need a driving license to drive.")
else:
    print("You are not old enough to drive.")
