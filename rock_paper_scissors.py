import random 
player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins <2: #loop to end after two won matches
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices) #makes random choice

  print("Let's play rock, paper, scissors! Game ends with a score of 2.")

  player_choice = input(f"What do you choose? ").lower()
  
  print(f"Computer chose: " +computer_choice)

#first conditional statement for outcome possibilities
  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
      winner = "Player"
  elif player_choice == computer_choice:
      winner = "Tie"
  else:
      winner = "Computer"
  print(f"The winner of the match is " + winner)
#second conditional statement for match resolution
  if winner == "Player":
      print("Congrats! You won!")
      player_wins += 1 #keeps the score
  elif winner == "Computer":
        print("Sorry! Computer won!")
        computer_wins += 1 #keeps the score
  else:
      print("It's a tie!")

  print(f"Current Score is Player: {player_wins}, Computer: {computer_wins}")
#third conditional statement for game resolution
if player_wins > computer_wins:
    print("Congratulations! You won the game!")
else:
    print("Sorry! Computer won the game!")