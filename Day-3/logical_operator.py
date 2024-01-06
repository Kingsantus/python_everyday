# multiple condition
# if condition1 & condition2 & condition3:
#     do this
# else:
#     do this

# logical operators
# A and B both have to be true before it execute
# C or D only one need to be true
# not E when none is true


print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoster!!!")
    age = int(input("Please provide your age? "))
    if age <= 12:
        bill = 5
        print("Children tickets is $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets is $7")
    elif (age >= 45) and (age <= 55):
        bill += 0
        print("Midlife don't have to pay")       
    else:
        bill = 12
        print("Adult tickets is $12")
    photo = input("Do you want a photo taken? Y or N. ")
    if (photo == "Y") or (photo == "y"):
        bill += 3
    print(f'your bill is {bill}') 
else:
    print("Sorry, you have to grow taller before you can ride.")