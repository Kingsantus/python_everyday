# love calculator
print("The Love calculator is calculating your score...")
name = input("What is your name? ")
name1 = input("What is your prospective partner name? ")

combine_name = name + name1
lower_name = combine_name.lower()
t = lower_name.count('t')
r = lower_name.count('r')
u = lower_name.count('u')
e = lower_name.count('e')

first_digit = t + r + u + e
l = lower_name.count('l')
o = lower_name.count('o')
v = lower_name.count('v')
e = lower_name.count('e')

second_digit = l + o + v + e

# first_digit = str(first_digit)
# second_digit = str(second_digit)
# lovescore = first_digit + second_digit
# lovescore = int(lovescore)

lovescore = int(str(first_digit) + str(second_digit))

if lovescore < 10 or lovescore > 90:
    print(f'Your score is {lovescore}, you go together like coke and mentos')
elif lovescore >= 40 and lovescore <= 50:
    print(f'Your score is {lovescore}, you are alright together')
else:
    print(f'Your score is {lovescore}')