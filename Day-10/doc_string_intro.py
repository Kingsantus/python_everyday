"""Doc String"""
# a method to write documentation when writing our code
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name.
    Params:
        f_name: accept first name
        l_name: accept last name
        return: both first and last name"""
    if f_name == '' or l_name == '':
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

format_name()