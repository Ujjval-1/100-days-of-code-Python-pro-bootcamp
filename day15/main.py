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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit=0

def sufficient_ing(order_ing):
    for item in order_ing:
        if order_ing[item]>resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins")

    total= int(input("Enter quarters: ")) *0.25
    total+=int(input("Enter dimes: ")) * 0.10
    total+=int(input("Enter nickles: ")) * 0.05
    total+=int(input("Enter pennies: ")) * 0.01
    return total

def tran_success(drink_price,user_amount):
    if user_amount<drink_price:
        print("Sorry, that's not enough money. Money refunded")
        return False
    else:
        amt = round(user_amount - drink_price, 2)
        print(f"Here is ${amt} for change")
        global profit
        profit+=drink_price
        return True

def making_coffee(order_ing, drink_name):
    for ing in order_ing:
        resources[ing]-=order_ing[ing]
    print(f"Here is your {drink_name} ☕, Enjoy!")


def coffee_machine():
    should_continue = True
    while should_continue:
        user_input= input("What would you like? (espresso/ latte/ cappuccino): ")
        if user_input=="off":
            should_continue=False
        elif user_input=='report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            if sufficient_ing(MENU[user_input]['ingredients']):
                payment = process_coins()
                if tran_success(MENU[user_input]['cost'], payment):
                    making_coffee(MENU[user_input]['ingredients'], user_input)

coffee_machine()



