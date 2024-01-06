# nested if/else
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoster!!!")
    age = int(input("Please provide your age? "))
    if age <= 12:
        print("You will pay $5")
    elif age <= 18:
        print("You will pay $7")        
    else:
        print("You will pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")