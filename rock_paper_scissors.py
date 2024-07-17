import random
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
print("Let's play rock, paper, scissors")

player_choice = input(f"What do you choose? ").lower()
print(f"Computer chose: " +computer_choice)

if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
elif player_choice == computer_choice:
    winner = "Tie"
else:
    winner = "Computer"
print(f"The winner of the game is " + winner)

if winner == "Player":
    print("Congratulations! You won!")
elif winner == "Computer":
    print("Sorry! Computer won!")
else:
    print("It's a tie!")