"""Calculator"""

def add(a,b):
    """Add two number
    Param:
        a: x
        b: y
        return x+y"""
    return a + b
def sub(a,b):
    """Subtract two number
    Param:
        a: x
        b: y
        return x-y"""
    return a - b
def mul(a,b):
    """Multiply two number
    Param:
        a: x
        b: y
        return x*y"""
    return a * b
def div(a,b):
    """div two number
    Param:
        a: x
        b: y
        return x/y"""
    return a / b

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}



continue_calculation = False

while not continue_calculation:
    a = int(input("What's the first number?: "))
    for key in operators:
        print(key)
    operator = input("Pick an operator: ")
    b = int(input("What's the next number?: "))
    calculation_func = operators[operator]
    answer = calculation_func(a,b)
    print(f"{a} {operator} {b} = {answer}")
    continue_again = input("Type 'y' to continue with 10.0, or 'n' to start a new calculation: ")
    if continue_again == 'n':
        continue_calculation = False
    else:
        operator = input("Pick an operator: ")
        c = int(input("What's the next number?: "))
        calculation_func = operators[operator]
        answer =  calculation_func(answer,c)
        print(f"{a} {operator} {b} = {answer}")

