# writing a virtual coin game
import random

coin = random.randint(0,1)
coin1 = random.randint(0,1)

if (coin == 1) and (coin1 == 1):
    print(f"coin 1 is Heads, coin 2 is Heads. You Win!!")
elif  (coin == 0) and (coin1 == 0):
    print(f"coin 1 is Tails, coin 2 is Tails. You Win!!")
else:
    print("Please try again!!!")