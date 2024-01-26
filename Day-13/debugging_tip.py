"""Debugging"""
# tip 1 Describe the problem 
# try to understand the code 
# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("You got it")
# my_function()

# tip 2 Reproduce the bug
# from random import randint
# dice_imgs = ['1','2','3','4','5','6']
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])

# tip 3 Play computer 
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Genz.")

# tip 4 Fix the error
"""When the editor is giving error try to debug it immediately"""
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# tip 5 Print is your friend
"""Print out every step to see where the issues lye"""
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# tip 6 Use a Debugger
# you use python tool debugger
# you can use breakpoint to identify where it happen
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# mutate([1,2,3,5,8,13])

# tip 7 Take a break

# tip 8 Ask a friend

# tip 9 run your code often

# tip 10 ask the question on stack over flow, or just check stack over flow questions asked