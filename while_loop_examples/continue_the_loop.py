# Skipping even numbers and printing odd numbers until 10
num = 0
while num < 10: # Loop until num is less than 10
    num += 1 # Increment num by 1
    if num % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(num)
