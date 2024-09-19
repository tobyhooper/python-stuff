#Python 3.9
#For rev.2 - add an error message for when anything other than an integer is entered
#          - add support for floats

print("This program takes a number and determines whether or not it is a prime number.")
#Function that determines if input is prime or not, returning True or False.
def is_prime(n):

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Please enter a number: "))
result = is_prime(number)

#Prints result.
if result == True:
    print(f"The number {number:,} is a prime number.")

elif result == False:
    print(f"The number {number:,} is not a prime number.")