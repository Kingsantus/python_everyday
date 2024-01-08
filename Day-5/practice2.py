"""Program that add all the even number in range provided by user"""
# collect input from user
# turn it into int
# create total = 0
# create for loop where input is b of range(a,b)
# condition if loop is divided by 2 reminder 0 add to total
# print total
target = int(input("Enter a number between 0 and 1000\n"))
total1 = 0
total = 0
for n in range(2, target + 1, 2):
    total1 += n
for n in range(0,target + 1):
    if n % 2 == 0:
        total += n
print(f"The sum of the even number is: {total}")
print(f"The sum of the even number, is: {total}")