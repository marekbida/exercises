# In this exercise, you are tasked to create a Python program that simulates a game of "Higher or Lower". 
# The computer will generate a random number between 1 and 100. The player will then guess a number. 
# If the guess is too high or too low, the computer will indicate this. 
# The game will continue until the player guesses correctly.

# Write a program that generates a random number between 1 and 100 and stores it as the "target number".
# The program should then continuously prompt the user for their guess.
# If the guess is lower than the target number, the program should print "Higher!".
# If the guess is higher than the target number, the program should print "Lower!".
# If the guess is equal to the target number, the program should print "Congratulations! You've found the number!" and terminate.

# Pseudocode

# 1. Generate a random number using 'random' module
import random

target_number = random.randint(1, 100)

# 2. Variable guessed_correctly set to False
guessed_correctly = False

# 3. Start while loop and ask user the number
while not guessed_correctly:
    user_input = input("Guess a number between 1 and 100: ")

    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Provide number, not a string!")
        continue

# 4. Inside while loop, check if the number is higher, lower or equal
    if user_input < target_number:
        print("Higher!")
    elif user_input > target_number:
        print("Lower!")
    else:
        print("Amazing! You've found the number!")
        guessed_correctly = True
        print("It's the end of the loop!")
# 5. If the guess is lower than the target number, the program should print "Higher!".
# 6. If the guess is higher than the target number, the program should print "Lower!".
# 7. If the guess is equal to the target number, the program should print "Congratulations! You've found the number!" and terminate.

