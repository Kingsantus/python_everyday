# multiple if condition
# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do C

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
    else:
        bill = 12
        print("Adult tickets is $12")
    photo = input("Do you want a photo taken? Y or N. ")
    if (photo == "Y") or (photo == "y"):
        bill += 3
    print(f'your bill is {bill}') 
else:
    print("Sorry, you have to grow taller before you can ride.")