from random import randint

EASY_LEVEL_TURNS = 10
MEDUIM_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Check answer against guess, and return the number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy', 'meduim' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'meduim':
        return MEDUIM_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return 

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    answer = randint(1,101)
    turns = set_difficulty()
    if turns == None:
        return print("Please choose a level between easy or meduim or hard")
    

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You 've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")

game()