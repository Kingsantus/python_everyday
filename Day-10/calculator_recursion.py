"""A function that call itself"""
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

def calculator():
    a = float(input("What's the first number?: "))
    for key in operators:
        print(key)
    should_continue = True
    while should_continue:
        operator = input("Pick an operator: ")
        b = float(input("What's the next number?: "))
        calculation_func = operators[operator]
        answer = calculation_func(a,b)
        print(f"{a} {operator} {b} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}: ") == 'y':
            a = answer
        else:
            should_continue = False
            calculator()

calculator()