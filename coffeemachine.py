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


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return round(total, 2)


def coffee_machine():
    keep_running = True
    money = 0
    while keep_running:
        coffee = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee == "off":
            return
        elif coffee == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        elif coffee in MENU:
            enough_ingredients = True
            for ingredient in MENU[coffee]['ingredients']:
                if MENU[coffee]['ingredients'][ingredient] > resources[ingredient]:
                    print(f"Sorry there is not enough {ingredient}.")
                    enough_ingredients = False
            if enough_ingredients:
                coins = insert_coins()
                enough_coins = True
                if coins < MENU[coffee]['cost']:
                    print("Sorry that's not enough money. Money refunded.")
                    enough_coins = False
                if enough_coins:
                    change = round(coins - MENU[coffee]['cost'], 2)
                    money += MENU[coffee]['cost']
                    if change > 0:
                        print(f"Here is ${change} dollars in change.")
                    for ingredient in MENU[coffee]['ingredients']:
                        resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]
                    print(f'Here is your {coffee}. Enjoy!')
        else:
            print("Invalid input.")


coffee_machine()



