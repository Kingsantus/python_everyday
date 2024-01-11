"""Hang Man"""
# start game
# generate a random word
# Generate as many blanks as the letters in word
# Ask the user to guess a letter
# is the guessed letter in the word {if yes (replace the blank with the letter)} {if no (lose a life)}
# if yes check are all the blank filled {if no repeat from ask a user} if yes game over}
# if no from guess {check have they run out of lives {if yes game over {if no go back to guess}}}

# start game 
# get a word in a list
# check the lenght of the word
# use _ to represent the word
# use while loop to show if input is equal to lenght
# ask the user to add an input
# convert to lower number
# check if the number is in the word list
# if yes replace display the letter in position of the word
# if no show nothing
# loop again
# until complete
# the time for the game should give at least two extra life 

# step 1
stages = ["""\
  +---+
  |   |
      |
      |
      |
      |
=========""",
 """
  +---+
  |   |
  O   |
      |
      |
      |
========= """,
 """
  +---+
  |   |
  O   |
  |   |
      |
      |
========= """,
 """
  +---+
  |   |
  O   |
 /|   |
      |
      |
========= """,
 """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= """,
 """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= """,
 """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= """]

word_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)
print(chosen_word)
# TODO-4 - Create a variable called 'lives' to keep track of the number of lives left'
# set 'lives' to equal to 6
lives = 6
# TODO-1.1 - Create am empty list called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# so if the chosen_word was "apple", display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

# TODO-3.4 - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_game = False
while not end_game:
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-2.1 - Loop through each position in the chosen_word;
# if the letter in the display at that position.
# e.g If the user guessed "p" and the chosen word was "apple", then display should be ["_","p","p","_","_"].
    user_guess = input("Guess a letter that might be in the hidden word\n").lower()
# TODO-3 - Check if the letter the user guessed (guess) is the one of the letters in the chosen_word.
# TODO-3.1 - Print "display" and you see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter
    if letter not in user_guess:
        lives -= 1

        if lives == 0:
            end_game = True
            print("You Lose")

# TODO-4.1 - If guess is not a letter in the chosen_word,
# then reduce 'lives' by 1 .
# If lives goes down to 0 then the game should stop and it should print "You lose"

# Join all the elements in the list and turn it into a string
        print(f"{''.join(display)}")

    #check id user has got all letters
    if "_" not in display:
        end_game = True
        print("You win.")

    #TODO-4.5 - Print the Ascill art from stages that corresponds to the current number of 'lives' the user has remaining
    print(stages[lives])
    

