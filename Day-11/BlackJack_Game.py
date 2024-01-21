"""Black Jack"""
# the rule of the game is the highest number not > 21 between the player and computer
# the game is over when the player quit playing, their card and computer cards will be counted together
# the kings and queen is counted 10
# the spade A is counted 11 or 1 depending

############ BlackJack Project################
# Difficulty Normal: Use all Hints below to complete the project
# Difficulty Hard: Use only Hint 1, 2, 3 to complete the project
# Difficulty Extra Hard: only use Hints 1 & 2 to complete the project
# Difficulty expert: Only use Hint 1 to complete the project

############ Our Blackjack House Rules ###################
## The deck is unlimited in size
## There are no jokers
## The Jack/Queen/King all count as 10
## The Ace can be count as 11 or 1
## Use the following list as the deck of cards:
# card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10]
## The cards in the list have equal probability of being drawn
## Cards are not removed from the deck as they are drawn

############### Hints ########################
# Hint 1: Go to this website and try out the BlackJack game:
#   https://game.washingtonpost.com/games/blackjack/
# then try out the completed BlackJack project here:
#   https://blackjack-final.app.brewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   https://listmoz.com/view/6h34DJpvJ8FVRlZfjvxF
# then try to create your own flowchart for the program

# Hint 3: Download and read this flow chart I've created
#   hrrps://drive.google.com/uc/?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random caed.
# 11 is the Ace
# card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10]
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_scores(user_score, computer_score):
    """CompareScore function compare the score of user and computer"""
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponent has BlackJack"
    elif user_score == 0:
        return "You win with a BlackJack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f' Your cards: {user_cards}, current score: {user_score}')
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    play_game()