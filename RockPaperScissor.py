import random

options = ("rock", "paper", "scissors")
running = True

while running:
    comp = random.choice(options)
    player = ""
    while player not in options:       
        player = input("Choose rock, paper or scissor: ").lower()

    print(f"Player: {player}")
    print(f"Computer: {comp}")

    if comp == player:
        print("IT'S A TIE!")
    elif player == "rock" and comp == "scissors":
        print("YOU WIN!")
    elif player == "paper" and comp == "rock":
        print("YOU WIN!")
    elif player == "scissors" and comp == "paper":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

    play_again = input("Want to play again?(y/n): ").lower()
    if not play_again == "y":
        running = False




