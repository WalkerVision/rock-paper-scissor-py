import random

choices = ["Rock", "Paper", "scissor"]

while True:
    player = input("Rock Paper Scissor Enter your choice ")

    if player in choices:
        break
    else:
        print("Invalid choice. Please enter Rock Paper Scissor")



computer = random.choice(choices)
print(f"computer choice : {computer}")