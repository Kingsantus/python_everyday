"""Local and Global Scope"""
# Global scope can be used any where, it a variable defined outside the function. it not within another function
enemies = 1

def increase_enemies():
    # Local scope can only be utilized in the function. Local scope only exist within function. local scope is a variable created inside a function
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# the concept Global and Local is not only for function, it applies anything you named NameSpace. 