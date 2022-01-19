import random

print("What is your choice: rock, paper or scissors ?")

userchice = input()

choices = ["rock", "paper", "scissors"]
randomNr = random.randint(0, 2)
choicePc = choices[randomNr]

print("You chose: " + userchice)
print("The PC chose: " + choicePc)

win = (userchice == "rock" and choicePc == "scissors") \
    or (userchice == "paper" and choicePc == "rock") \
    or (userchice == "scissors" and choicePc == "paper") \


if userchice not in choices:
    print("invalid choice")
else:
    if userchice == choicePc:
        print("It's a draw!")
    elif userchice != choicePc:
        if win == True:
            print("You won!")
        else:
            print("You lost!")
