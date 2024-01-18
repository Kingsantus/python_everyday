"""A program that grade the student scores"""
student_scores = {
    'Harry': 81,
    'Ron': 78,
    'Hermione': 99,
    'Draco': 74,
    'Nevile': 62,
}

# create an empty dictionary called student grade
student_grades = {}

# Write your code below to add the grade to student
for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grades[key] = 'Outstanding'
    elif score > 80:
        student_grades[key] = 'Exceeds Expectation'
    elif score > 70:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'

    # if student_scores[key] <= 70:
    #     student_grades[key] = 'Fail'
    # elif student_scores[key] >= 71 and student_scores[key] <= 80:
    #     student_grades[key] = 'Acceptable'
    # elif student_scores[key] >= 81 and student_scores[key] <= 90:
    #     student_grades[key] = 'Exceeds Expectation'
    # elif student_scores[key] >= 91 and student_scores[key] <= 100:
    #     student_grades[key] = 'outstanding'
    #student_grade += student_scores[key]


print(student_grades)