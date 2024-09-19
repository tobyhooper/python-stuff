def bubblesort(lst):
    total = len(lst)
    for i in range(total):
        for j in range(0, total-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

total_vals = int(input("How many numbers?: "))
values = []

for i in range(total_vals):
    while True:
        try:
            value = float(input(f"Enter value {i+1}: "))  # Convert input to float
            values.append(value)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

sorted_values = bubblesort(values)

# Format the output
formatted_values = ', '.join(f'{int(val)}' if val.is_integer() else f'{val}' for val in sorted_values)

print(f"Sorted values are: {formatted_values}")