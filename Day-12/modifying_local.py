"""Modifyng Global Scope"""

enemies = 2

def increase_enemies():
    # without += you cannot modifyng the global scope
    # it not good to modify the global scope from the local
    # to achieve this use return keyword
    #enemies += 2
    #print(f"enemies inside function: {enemies}")
    return enemies + 1
    # using return you can define the change where ever you want it, instead of overiding the global scope anytime

enemies1 = increase_enemies()
print(f"enemies outside function: {enemies}")
print(f"enemies outside function: {enemies1}")