"""FizzBuzz code challenge"""
# if a number is divisible by 3 print Fizz
# if a number is divisible by 5 print Buzz
# if a number is divisible by 3 and divisible by 5 print FizzBuzz
# print other number as number

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)