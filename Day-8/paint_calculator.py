"""Paint calculator"""
import math
def paint_calculator(height, width, coverage):
    number_of_cans = round((height * width) / coverage)
    roundup_result = math.ceil(number_of_cans)
    print(f"You 'll need {roundup_result} cans 0f paint")

#paint_calculator()

height = int(input("Type the height of the wall  "))
width = int(input("Type the width of the wall  "))
coverage = 5
paint_calculator(height=height, width=width, coverage=coverage)