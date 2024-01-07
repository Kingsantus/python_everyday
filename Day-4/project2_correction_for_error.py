line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")

letter = position[0].lower()
abc = ['a', 'b', 'c']

if letter not in abc or len(position) != 2 or not position[1].isdigit():
    print("Invalid input. Please provide a valid position (e.g., a1, b2, c3).")
else:
    letter_index = abc.index(letter)
    number_index = int(position[1]) - 1
    map[number_index][letter_index] = "X"

    print(f"{line1}\n{line2}\n{line3}")
