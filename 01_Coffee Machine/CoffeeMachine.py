# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Coffee Machine Project >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# Concepts Utilized: 

# Project: Coffee Machine
# Concept Utilized: lists, dictionaries, global variables, functions

# create menu using dictionary
menu = {
        "espresso": {"ingredients": {"water": 50, "coffee": 18,}, "cost": 1.5},

        "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24, }, "cost": 2.5},

        "cappucino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24, }, "cost": 3.0}
       }

profit = 0
resources = {"water": 300, "milk": 200, "coffee": 100,}

# the machine should check if it is loaded with the resources for the order
def is_resource_sufficient(order_ingredients):
    """returns True when order can be made, else returns false"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there isn't enough {item}")
            return False
    return True

# check how much coin is inserted
def process_coins():
    """returns total calculated from the coins inserted in the machine"""
    print("Please insert the coins.")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# check for successful transaction
def is_transaction_successful(money_received, drink_cost):
    """returns True when payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Refund Initiated.")
        return False
    
# make drink and deduct from the total resources
def make_coffee(drink_name, order_ingredients):
    """deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Have a good time!")

# take user input and make coffee
is_on = True

while is_on:
    choice = input("What wold you like? (Espresso / Latte / Cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])