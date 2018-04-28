"""
This program determine the winner between the player and the computer on playing the game of RPS
"""
import random
options=["ROCK","PAPER","SCISSORS"]
message={"tie":"Yawn it's tie!",
         "won":"Yay you won!",
         "lost":"Aww you lost!",
        }
def decide_winner(user_choice,computer_choice):
  print(("The choice of the user is %s")%(user_choice))
  print(("The choice of the computer is %s")%(computer_choice))
  if user_choice==computer_choice:
    print (message["tie"])
  elif user_choice==options[0] and computer_choice==options[2]:
    print(message["won"])
  elif user_choice==options[1] and computer_choice==options[0]:
    print(message["won"])
  elif user_choice==options[2] and computer_choice==options[1]:
    print(message["won"])
  else:
    print(message["lost"])
  return
def play_RPS():
  user_choice=input("Enter Rock, Paper or Scissors: ")
  user_choice=user_choice.upper()
  computer_choice=options[random.randint(0,2)]
  decide_winner(user_choice,computer_choice)
play_RPS()

