# choice your own choices
print("Your mission to Tresure Island.")
choice = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if choice == 'left':
    choice1 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice1 == 'wait':
        choice2 = input('You arrived at the unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which color do you choose?\n').lower()
        if choice2 == 'yellow':
            print("You found the treasure! You Win!")
        elif choice2 == 'blue':
            print("You entered a room of beast. Game over")
        elif choice2 == 'red':
            print("It's a room full of fire. Game over")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game over")
else:
    print("You fell into a hole. Game over")
