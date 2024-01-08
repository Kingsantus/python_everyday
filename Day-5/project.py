"""Python Password Generator"""
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
str_add = int(input("How many letters would you like in your password?\n"))
sym_add = int(input("How many symbols would you like?\n"))
num_add = int(input("How many number would you like?\n"))

# easy method
password = ""
for n in range(1, str_add + 1):
    password += random.choice(letters)

for n in range(1, sym_add + 1):
    password += random.choice(symbols)

for n in range(1, num_add + 1):
    password += random.choice(numbers)

print(password)

# hard level
password_list = []
for n in range(1, str_add + 1):
    password_list += random.choice(letters)

for n in range(1, sym_add + 1):
    password_list += random.choice(symbols)

for n in range(1, num_add + 1):
    password_list.append(random.choice(numbers))

#print(password_list)
random.shuffle(password_list)
#print(password_list)

new_password = ""
for char in password_list:
    new_password += char

print(new_password)