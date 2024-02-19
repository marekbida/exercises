# Nested while loops to create a multiplication table
import time

time.sleep(10)

i = 1

while i <= 5:
    j = 1
    while j <= 5: 
        # Print the product of i and j followed by a tab character (\t)
        print(f"{i} * {j} = {i * j}", end='\t') 
        j += 1 
    print()  # New line after each row
    i += 1
