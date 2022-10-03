import random

def get_choices():
      player_choice = input("Enter a choice (Rock, Paper, scissors): ")
      option = ["rock", "paper", "scissors"]
      computer_choice = random.choice(option)
      choices = {"player": player_choice, "computer": computer_choice}
      return choices

def check_win(player, computer):
      print(f"You chose {player} and Computer chose {computer}")
      if player == computer:
            return("It's a tie!")
      elif player == "rock":
            if computer == "scissors":
                  return("Rock smashes scissors! You win!")
            else:
                  return("Paper cover rock! You lose.")
      elif player == "paper":
            if computer == "rock":
                  return("Paper cover rock! You win!")
            else:
                  return("Scissors cuts paper! You lose.")
      elif player == "scissors":
            if computer == "rock":
                  return("Scissors cuts paper! You win!")
            else:
                  return("Rock smashes scissors! You lose.")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)