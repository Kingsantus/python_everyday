"""Guessing Game"""
# patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

comp_guess = random.randint(1,101)

easy = 10
hard = 5

def user_guess():
    global easy
    if comp_guess < choice:
        print("Too high")
    elif comp_guess > choice:
        print("Too low.")
    elif choice == comp_guess:
        print("You guessed it")
        return is_game_over == True
    
    return easy - 1
def user_guess_hard():
    global hard
    if comp_guess < choice:
        print("Too high")
    elif comp_guess > choice:
        print("Too low.")
    elif choice == comp_guess:
        print("You guessed it")
        return is_game_over == True
    
    return hard - 1

is_game_over = False
while not is_game_over:
    if level == 'easy':
        print(f"You have {easy} attempts remaining to guess the number.")
        choice = int(input("Make a guess: "))
        easy = user_guess()
    elif level == 'hard':
        print(f"You have {hard} attempts remaining to guess the number.")
        choice = int(input("Make a guess: "))
        hard = user_guess_hard()
    

    if easy == 0:
        print("Game over. You're out of attempts.")
        is_game_over = True
    if hard == 0:
        print("Game over. You're out of attempts.")
        is_game_over = True