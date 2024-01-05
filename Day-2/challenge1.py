# Ist Input enter your hight in meters e.g: 1.65
height = input("Please provide your height in meters e.g: 1.65? ")
height = float(height)
#2nd input enter your weight in kilograms e.g 72
weight = input("Please provide your weight in KG e.g: 72? ")
weight = int(weight)

bmi = weight / (height ** 2)
bmi = int(bmi)
print(bmi)
