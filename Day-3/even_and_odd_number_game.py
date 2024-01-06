# which number do you want to check
# % modular remainder
print("Check if any number is even or odd number")
number = int(input("Input your number "))
if number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")