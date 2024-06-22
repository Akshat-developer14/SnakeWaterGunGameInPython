import random

"""
1 for snake
-1 for water
0 for gun
"""
# Generate a random number from the set {-1, 0, 1}
random_number = random.choice([-1, 0, 1])
computer = random_number
youstr = input("Enter your choice from the following\n( Snake, Water, Gun ): ")
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr.lower()]

print(f"You choose {reverseDict[you]} and computer choose {reverseDict[computer]}")

if computer == you:
    print(f"Its a draw...!\nBoth choose {youstr}")
else:
    if computer == -1 and you == 1:
        print("You win as snake drinks water")
    elif computer == -1 and you == 0:
        print("You lose as water sinks gun")
    elif computer == 1 and you == 0:
        print("You win as gun kills snake")
    elif computer == 1 and you == -1:
        print("You lose as snake drinks water")
    elif computer == 0 and you == -1:
        print("You win as water sinks gun")
    elif computer == 0 and you == 1:
        print("You lose as gun kills snake")
    else:
        print("Something went wrong...!")
