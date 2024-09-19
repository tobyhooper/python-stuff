import random

def rockpaperscissors(userinput):
    ranint = random.randint(1, 3)

    if ranint == 1:
       cpu = "rock"
    if ranint == 2:
        cpu = "paper"
    if ranint == 3:
        cpu = "scissors"

    if userinput == cpu:
        return "draw"

    if userinput == "rock":
        if cpu == "paper":
            return "lose"
    if userinput == "paper":
        if cpu == "scissors":
            return "lose"
    if userinput == "scissors":
        if cpu == "rock":
            return "lose"
    
    return "win"

# Add error handling for user input
while True:
    gameinput = input("Play your move. (rock/paper/scissors) ").lower()
    if gameinput in ["rock", "paper", "scissors"]:
        break
    else:
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

gameresult = rockpaperscissors(gameinput)

#output result
if gameresult == "win":
    print("You win!")

if gameresult == "lose":
    print("You lost.")

if gameresult == "draw":
    print("It's a draw.")