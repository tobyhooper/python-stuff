#Python 3.9

print("This program takes a number and determines whether or not it is a prime number.")
#Function that determines if input is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        user_input = input("Please enter a number: ")
        # Attempt to convert input to a float and check if it's an integer
        try:
            number = float(user_input)
            if number.is_integer():
                number = int(number)
                result = is_prime(number)
                if result:
                    print(f"The number {number} is a prime number.")
                else:
                    print(f"The number {number} is not a prime number.")
            else:
                print("The number is a decimal and cannot be a prime number.")
        except ValueError:
            # If conversion to float fails, it might be a non-numeric string or boolean
            if user_input.lower() in ["true", "false"]:
                print("Booleans are not a valid input. Please try again.")
            else:
                print("Invalid input. Please enter a valid integer.")

        break  # Exit loop if successful
    except ValueError:
        print("Fatal error. Please try again.")