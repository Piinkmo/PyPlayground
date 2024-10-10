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
    "money": 0
}

def print_report():
    '''Print the current resource storages.'''
    for key, value in resources.items():
        print(f"{key.capitalize()}: {value}ml" if key != "money" else f"Money: ${value}")

def is_resource_sufficient(drink):
    '''Check if there are enough resources to make the selected drink.'''
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if ingredient in resources and resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    '''Ask user to insert coins.'''
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)

def check_transaction(drink, money_inserted):
    cost = MENU[drink]["cost"]
    if money_inserted >= cost:
        resources["money"] += cost
        change = round(money_inserted - cost, 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {drink}. Enjoy!")


def main():

    while True:
        choice =input("What would you like? (espresso/latte/cappuccino) or you can simply turn 'off' machine: ").lower()
        if choice == "off":
            break
        elif choice == "report":
            print_report()
        elif choice in MENU:
            if is_resource_sufficient(choice):
                money_inserted = process_coins()
                if check_transaction(choice, money_inserted):
                    make_coffee(choice)
        else:
            print("Invalid selection. Please choose again.")


if __name__ == "__main__":
    main()




