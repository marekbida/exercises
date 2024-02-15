# Using else with for loops to handle the case when the loop completes without a break statement being executed
numbers = [1, 3, 5, 7] # A list of numbers
search_for = 8
for num in numbers: # Loop through each number in the list
    if num == search_for: # Check if the current number is the one we are looking for
        print("Found!")
        break
else:  # Executed because no break occurs in the loop
    print("Not found!")
