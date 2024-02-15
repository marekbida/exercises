# Nested for loops to print a 3x3 grid
for row in range(1, 4): # Outer loop
    for col in range(1, 4): # Inner loop
        print(f"({row},{col})", end=" ") # Print the current cell and stay on the same line
    print()  # New line after each row
