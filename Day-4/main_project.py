# ROCK, PAPER, SCISSORS game!!!
# Rock wins against scissors.
# Scissors wins against paper
# Paper wins against rock

import random

Rock = """"
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
rock
"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
paper
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
scissors
"""

choices = [Rock,Paper,Scissors]

print("Welcome to the Game!!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0,2)
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number and you lose. You lose")
else:
    print("You choose:")
    print(choices[user_choice])
    print("Computer Choose:")
    print(choices[computer_choice])

    if computer_choice == user_choice:
        print("Play Again")
    elif user_choice == Rock and computer_choice == Scissors:
        print("You Win")
    elif computer_choice == Rock and user_choice == Scissors:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You Win")

# if choices[computer_choice]  == 0 and choices[user_choice] == 1:
#     print("You lose")
# elif user_choice == 1 and computer_choice == 2:
#     print("You win")
# elif user_choice == 2 and computer_choice == 0:
#     print("You win")
# elif computer_choice == 0 and user_choice == 1:
#     print("You win")
# elif computer_choice == 1 and user_choice == 2:
#     print("You win")
# elif computer_choice == 2 and user_choice == 0:
#     print("You win")
# elif computer_choice == user_choice:
#     print("Play Again")
# else:
#     print("You lose, input not vaild")
