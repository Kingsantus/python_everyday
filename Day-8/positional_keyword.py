# function with more than one input
def greet_with(name,location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}")

greet_with("Kingsantus", "Anambra") #positional argument
# positional argument def my_function(a,b)  my_function("hello", "World")
# keyword argument def my_function(a,b)  myfunction(b='hello', a='world')
greet_with(location='Anambra', name='Kingsantus') #keyword argument 