# nested loop game
# the program interpret the Body Mass Index (BMI) based on a User's weight and height
# and combined
# or one can be right
height = float(input("Enter your height in meters e.g., 1.55? "))
weight = int(input("Enter your weight in kilograms e.g., 72? "))
bmi = weight / (height ** 2)
bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are Underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obessed")
else:
    print(f"Your BMI is {bmi}, you are clinical obessed")
