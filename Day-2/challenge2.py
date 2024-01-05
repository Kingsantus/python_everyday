# manually printing out the week left to any one
# one year is 56 weeks
# 90 years is 90 * 56
#user ages added
#user age * 56 
# 90 years weeks - user age weeks
# ptint the remaining

# one_year = 52
# expected_age = 90
# expected_age_week = 90 * 52
# age = input("Type in your age? ")
# age = int(age)
# age_week = age * one_year
# expected_age_remaining = expected_age_week - age_week
# print(f"You have {expected_age_remaining} weeks left")

age = input()
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} left.")