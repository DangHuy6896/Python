from data_day15 import MENU
from data_day15 import resources

money = 0
def coffee_machine():
    global money
    n = True
    while n:
        type_coffee = input("What would you like? (espresso/latte/capuccino): ").lower()
        if type_coffee == "report":
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
        elif type_coffee == "espresso" or type_coffee == "latte" or type_coffee == "cappuccino":
            print("Please insert coins.")
            quarter = int(input("How many quarters? "))
            dime = int(input("How many dimes? "))
            nickle = int(input("How many nickles? "))
            pennie = int(input("How many pennies? "))
            ctm_m = round(quarter/4 + dime/10 + nickle/20 + pennie/100, 2)
            if ctm_m >= MENU[type_coffee]['cost']:
                if type_coffee == "espresso":
                    if MENU['espresso']['ingredients']['water'] > resources['water']:
                        print("Sorry there is not enough water.")
                    elif MENU['espresso']['ingredients']['coffee'] > resources['coffee']:
                        print("Sorry there is not enough coffee.")
                    else:
                        money = MENU[type_coffee]['cost']
                        change = ctm_m - MENU[type_coffee]['cost']
                        resources['water'] -= MENU['espresso']['ingredients']['water']
                        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                        print(f"Here is ${change} in change")
                        print("Here is your latte ☕ Enjoy!")
                else:
                    if MENU[type_coffee]['ingredients']['water'] > resources['water']:
                        print("Sorry there is not enough water.")
                    elif MENU[type_coffee]['ingredients']['milk'] > resources['milk']:
                        print("Sorry there is not enough milk.")
                    elif MENU[type_coffee]['ingredients']['coffee'] > resources['coffee']:
                        print("Sorry there is not enough coffee.")
                    else:
                        money = MENU[type_coffee]['cost']
                        change = ctm_m - MENU[type_coffee]['cost']
                        resources['water'] -= MENU[type_coffee]['ingredients']['water']
                        resources['milk'] -= MENU[type_coffee]['ingredients']['milk']
                        resources['coffee'] -= MENU[type_coffee]['ingredients']['coffee']
                        print(f"Here is ${change} in change")
                        print("Here is your latte ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif type_coffee == "off":
            n = False
        else:
            coffee_machine()

coffee_machine()