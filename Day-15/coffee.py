menu = {
    "espresso": {
        "ingredients": {
        "water": 50,
        "coffee": 18},
        "cost": 1.5    
    },
    "latte": {
        "ingredients": {
        "water": 200,
        "milk": 150,
        "coffee": 24},
        "cost": 2.5    
    },
    "cappuccino": {
        "ingredients": {
        "water": 250,
        "milk": 100,
        "coffee": 24},
        "cost": 3.0    
    }
}

earning = 0

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 300
}

def is_resource_sufficient(order_ingredients):
    """Return True if order will be processed and False if not"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Return the total coin put by the user"""
    print("Please insert coins.")
    total = int(input("How many quaters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True if money put is equal to choice made"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} for your change.")
        global earning
        earning += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money returned")
        return False

def make_coffee(drink_name, order_ingredients):
    """create a coffee and deduct from the resource ingrident"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!!!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${earning}")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])

            
        