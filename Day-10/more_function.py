"""More Function"""
# first simple function
# def my_function():
#     do this
#     then do this
#     finally do this

# second type of functions, functions with input
# def my_function(something):
#     do this with something
#     then do this 
#     finally do this

# third type of function is function with outputs
# def my_function():
#     result = 3 * 2
#     return result   #return returns the output

def my_function():
    result = 4 * 5
    return result

output = my_function()

#print(output)

def format_name(a,b):
    first_name = a.capitalize()
    last_name = b.capitalize()
    return f'{first_name} {last_name}'

first = input('Add your first name ')
last = input('Add your last name ')

output = format_name(a=first, b=last)
#print(output)

# correction
# using title() instead of capitalized

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

output = format_name(f_name=first, l_name=last)

print(output)