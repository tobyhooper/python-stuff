import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

while True:
    n_terms = input("Enter the number of terms: ")
    try:
        n_terms = int(n_terms)
        if n_terms <= 0:
            print("Please enter a positive integer")
        else:
            start_time = time.time()  # Start the timer
            print("Fibonacci sequence:")
            for i in range(n_terms):
                print(fibonacci(i))
            end_time = time.time()  # End the timer
            elapsed_time = (end_time - start_time)
            if elapsed_time < 1:
                elapsed_time = elapsed_time * 1000
                print(f"Time taken: {elapsed_time:.2f} milliseconds. (2 d.p.)")
            else:
                print(f"Time taken: {elapsed_time:.2f} seconds. (2 d.p.)")
            break
    except ValueError:
        print("Please enter a valid integer")
