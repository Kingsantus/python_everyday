# Average Hight of the student
student_height = input().split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
total_height = 0
for height in student_height:
    total_height += height
print(f"Total height = {total_height}")
# len function done manually
total_student = 0
for student in student_height:
    total_student += 1
print(f"Number of student = {total_student}")
average = round(total_height / total_student, 2)
print(f"Average height = {average}")