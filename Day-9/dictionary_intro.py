"""Dictionary"""
# Dictionary helps us to group things that are related together
# it has key on the left hand side and value on the right hand side
# dictionary = {key: value} or {'Bug':'hello we have issue, 'loop':'iterating data','function':'stored block of code'}

programming_dict = {
    'Bug': 'An error',
    'loop': 'Iteration'
}

# retriving an item from a dictionary
# the information in the dictionary is identified as a key
# programming_dict['Bug']
#print(programming_dict['Bug'])

# adding an item into a dictionary
# name_dictionary['new_item'] = 'new value'
programming_dict['function'] = 'Block of code stored together'

#create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# call an existing dictionary and assign it to an empty dict
wipe_dict = {}

#edit an item in a dictionary
#programming_dict['Bug'] = 'error in code'
#print(programming_dict)

# iterating over a dictionary
# to get the only the keys
# for i in programming_dict:
#     print(i)
# this will print only the key value 
# to get the values and key
for key in programming_dict:
    print(key)
    print(programming_dict[key])