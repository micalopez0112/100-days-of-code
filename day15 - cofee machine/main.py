MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

ingredients = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
    """Prints a report of all resources."""
    print(f"Water: {ingredients['water']}ml")
    print(f"Milk: {ingredients['milk']}ml")
    print(f"Coffee: {ingredients['coffee']}g")

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def is_payment_successful(payment, drink_cost):
    """Returns True when payment is accepted, False if insufficient."""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit 
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources."""
    for item in order_ingredients:
        ingredients[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_payment_successful(payment, drink["cost"]):
               make_coffee(choice, drink["ingredients"])


