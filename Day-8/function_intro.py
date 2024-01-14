"""Function"""
# handy way of taking a complex set of instruction and packaging them together inside a block of code that has a name given to it and when we need all of the lines of code that packaged inside the function all we have to do is to call the function by typing the name with a parenthesis "name_of_function()"
#function that
# create a function called greet()
# Write 3 print statements inside the function
# Call the greet() function and run your code

def greet():
    print("Hello World!")
    print("Welcome to functions")
    print("Python is fun!!")

greet()

# can give our variable something in other to ensure the function is run other things
# eg def greet(name)
# this is a function that allows an input

def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How do you do {name}")

greet_with_name("Kingsantus")

# name = parameter
# the value of the parameter is argument
