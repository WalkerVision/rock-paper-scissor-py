import random

choices = ["Rock", "Paper", "Scissor"]

while True:  # used while loop to run game until user is done

    while True:  # used while loop to validate player input
        player = input("Rock Paper Scissor Enter your choice ")

        if player in choices:
            break
        else:
            print("Invalid choice. Please enter Rock Paper Scissor")

    computer = random.choice(choices)
    print(f"computer choice : {computer}")

    # determine the winner
    if player == computer:
        print("Its a Tie!")

    elif(player == "Rock" and computer == "Scissor") or \
        (player == "Paper" and computer == "Rock") or \
        (player == "Scissor" and computer == "Paper"):
        print("You Win!")

    else:
        print("Computer Wins!")

    play_again = input("Do you want to play again? (yes/no):")
    if play_again != "yes":
        break