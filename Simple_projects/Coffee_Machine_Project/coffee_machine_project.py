from menu import menu, resources


# TODO 1. Print report of all coffee machine resources
def report():
    generated_report = (
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    return generated_report


# TODO 2. Check resources sufficient to make drink order
def check_sufficient(type_of_coffee):
    enough_ingredients = True
    if resources['water'] > menu[type_of_coffee]['ingredients']['water'] and resources['milk'] > \
            menu[type_of_coffee]['ingredients']['milk'] and resources['coffee'] > menu[type_of_coffee]['ingredients'][
        'coffee']:
        resources['water'] -= menu[type_of_coffee]['ingredients']['water']
        resources['milk'] -= menu[type_of_coffee]['ingredients']['milk']
        resources['coffee'] -= menu[type_of_coffee]['ingredients']['coffee']
    elif resources['water'] < menu[type_of_coffee]['ingredients']['water'] or resources['milk'] < \
            menu[type_of_coffee]['ingredients']['milk'] or resources['coffee'] > menu[type_of_coffee]['ingredients'][
        'coffee']:
        if resources['water'] < menu[type_of_coffee]['ingredients']['water']:
            print("Sorry there is not enough water.")
            enough_ingredients = False
        elif resources['milk'] < menu[type_of_coffee]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            enough_ingredients = False
        elif resources['coffee'] < menu[type_of_coffee]['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            enough_ingredients = False
    return enough_ingredients


# TODO 3. Process coins
def coins_process():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money = round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)
    print(money)
    return money


# TODO 4. Check if transaction can be completed

def successful_transaction(type_of_coffee):
    money = coins_process()
    if money < menu[type_of_coffee]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    elif money >= menu[type_of_coffee]['cost']:
        change = round(money - menu[type_of_coffee]['cost'], 2)
        resources['money'] += menu[type_of_coffee]['cost']
        print(f"Here is ${change} in change.")
        print(f"Here is your {type_of_coffee}, Enjoy!")


# TODO 5. Make a coffee

def make_coffee():
    making_coffee = True
    while making_coffee == True:
        decision = input("What would you like ? (espresso/latte/cappuccino): ")
        if decision == "report":
            print(report())
        elif decision == "espresso" or decision == "latte" or decision == "cappuccino":
            type_of_coffee = decision
            if check_sufficient(type_of_coffee=type_of_coffee) == True:
                successful_transaction(type_of_coffee=type_of_coffee)

        # TODO 6. Turning off coffee machine
        elif decision == "off":
            making_coffee = False
            print("Turning off...")
        else:
            print("Incorrect input!")


make_coffee()
