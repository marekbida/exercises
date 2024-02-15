"""
This program assigns a grade based on the marks entered by the user, 
using multiple elif statements for exclusive ranges of marks.
"""

# Grading system based on marks
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is {grade}.")
