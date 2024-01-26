"""Higher or Lower Game"""
# trying to become better but I have come to accept failure as my friend
from random import randint
from game import game

option_a = randint(0,len(game)-1)
option_b = randint(0,len(game)-1)

while option_a == option_b:
    option_b = randint(0,len(game)-1)

print(f"Compare A: {game[option_a]['name']}, {game[option_a]['description']}, {game[option_a]['country']}")
print(f"Against B: {game[option_b]['name']}, {game[option_b]['description']}, {game[option_b]['country']}")

A = game[option_a]['follower_count']
B = game[option_b]['follower_count']

pick_option = input("Who has more followers? Type 'A' or 'B': ").upper()

count = 0

def option(pick_option):
    if pick_option == 'A':
        if A > B:
            print("You won")
            count += 1
        elif A < B:
            print("You Lose")
        elif A == B:
            print("You try again")
    elif pick_option == 'B':
        if B > A:
            print("You won")
            count += 1
        elif B < A:
            print("You Lose")
        elif B == A:
            print("You try again")
    else:
        print("Pick a side")
    return count

print(count)