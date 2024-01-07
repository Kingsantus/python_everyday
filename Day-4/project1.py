import random
# Take user input
user_input = input("Enter a string: ")

# Remove specified characters and convert to lowercase
filtered_input = ''.join(char.lower() for char in user_input if char.isalpha())

# Convert the filtered string to an array of individual letters
name_array = list(filtered_input)

name_length = len(name_array)

random_output = random.randint(0, name_length - 1)

# Display the result
print(name_array[random_output])
