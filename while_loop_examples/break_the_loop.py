# Using break to exit a loop based on user input
print("Type 'exit' to stop the loop.")
while True:  # This creates an infinite loop by design
    response = input("> ")
    if response == "exit":
        break  # Exit the loop
    print(f"You typed '{response}'.") # This line is executed after the if statement

print("Bye!") # This line is executed after the loop ends