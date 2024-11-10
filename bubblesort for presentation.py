import random # for generating random numbers
import time # for time measurement
import sys # for int max size
import pandas as pd # for the results table

def bubble_sort(lst): # Bubble sort function
    length = len(lst)
    for i in range(length - 1):  # Limit passes to length - 1
        swapped = False  # Track whether any swap happens
        for j in range(1, length - i):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]  # Swap
                swapped = True
        if not swapped:  # If no swap happened, the list is already sorted
            break
    return lst

sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000] # List of sizes
results = [] # List to store the results

for size in sizes: # for each size
    print(f'- Sorting {size} numbers, please wait...\n')
    lst = [random.randint(0, sys.maxsize) for _ in range(size)] # Generate a list of random numbers
    start_time = time.time() # Start time measurement
    sorted_lst = bubble_sort(lst) # Sort the list
    end_time = time.time() # End time measurement
    elapsed_time = end_time - start_time # Calculate the elapsed time
    results.append({'Size': size, 'Time (seconds)': elapsed_time}) # Store the result

# Create a DataFrame
df = pd.DataFrame(results)

# Display the table
print(f'Results:\n\n{df}')
