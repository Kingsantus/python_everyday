# Randomization
# using random() to produce random numbers
# random.randint(a,b)  it a fuction in random that display ransom number from point a to point b. it only produce one number between a and b
# random.random() this print random floating number between 0.0 to 1.0 not including 1 

import random
#import my_module

randon_integer = random.randint(1, 10)
random_float = random.random()
# creating random float to be more than 1
multiple_random = randon_integer * random_float

print(randon_integer)
print(random_float)
print(multiple_random)
#print(my_module.pi)