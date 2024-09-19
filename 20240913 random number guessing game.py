import random

highest_int = int(input("Enter the highest number the random number could be: "))

random_int = random.randint(1, highest_int)

guess1 = int(input("Enter your first guess: "))

if random_int == guess1:
    print(f"Your guess, {random_int}, was correct. Good guess!\nGuessed 1st attempt.")
else:
    guess2 = int(input("That was incorrect.\nEnter your second guess: "))
    if random_int == guess2:
        print(f"Your guess, {random_int}, was correct. Good guess!\nGuessed 2nd attempt.")
    else:
        guess3 = int(input("That was incorrect.\nEnter your final guess: "))
        if random_int == guess3:
            print(f"Your guess, {random_int}, was correct. Good guess!\nGuessed 3rd attempt.")
        else:
            print(f"Used all attempts.\nThe correct number was {random_int}.\nThanks for playing!")