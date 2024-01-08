"""A program that print the highest number in a list of number"""
# accept highest score
# convert to int list
# give highest number nothing
# any number greater than highest number is = highest number
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_number = 0
for number in student_scores:
    if number > highest_number:
        highest_number = number
print(f"The highest score in the class is: {highest_number}")