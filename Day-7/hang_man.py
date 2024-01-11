"""Hang Man"""
hang_man = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ \n"""
stages = ["""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= """, """
  +---+
  |   |
  O   |
 /|\\ |
 /    |
      |
========= """, """
  +---+
  |   |
  O   |
 /|\\ |
      |
      |
========= """, """
  +---+
  |   |
  O   |
 /|   |
      |
      |
========= """, """
  +---+
  |   |
  O   |
  |   |
      |
      |
========= """, """
  +---+
  |   |
  O   |
      |
      |
      |
========= """, """
  +---+
  |   |
      |
      |
      |
      |
========="""]

print(hang_man)
word_list = ["ardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)
lives = 6
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_game = False
while not end_game:
    user_guess = input("Guess a letter that might be in the hidden word\n").lower()
    if user_guess in display:
        print(f"You've already guessed {user_guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter
    if letter not in user_guess:
        print(f"You guessed {user_guess}, that's not in the word you lose a life")
        lives -= 1

        if lives == 0:
            end_game = True
            print("You Lose")

        print(f"{''.join(display)}")

    if "_" not in display:
        end_game = True
        print("You win.")

    print(stages[lives])