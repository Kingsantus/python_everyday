from random import randint, choice
from game import game

score = 0
def format_data(account):
    """Format the account into printable format"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    print(f'{name}, a {description}, from {country}')

def check_answer(guess, a_follower, b_follower):
    """Takes the user guess and follower counts and returns if they got it right"""
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'

game_should_continue = True
option_b = choice(game)

while game_should_continue:
    option_a = option_b
    option_b = choice(game)

    if option_a == option_b:
        option_b = choice(game)

    print(f"Compare A: {format_data(option_a)}.")
    print(f"Against B: {format_data(option_b)}.")


    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = option_a['follower_count']
    b_follower_count = option_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong! Final Score: {score}")
        