# using randomization to get information from the list
# get input from the user
# join the str and convert it to list each alphabet an item in the list
# start random.randint with 0 and end with the len of the user input
# the value of the randomization will produce the printed value
import random

names_string = input("please type in names of your friends with a comma e.g., Adam, eve? ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_to_pay = names[random_choice]
print(person_to_pay + " is going to buy the meal today!")
