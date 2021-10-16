from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
menu_object = Menu()
coffee_maker_object = CoffeeMaker()
money_machine_object = MoneyMachine()
while is_on:
    options = menu_object.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == 'report':
        coffee_maker_object.report()
        money_machine_object.report()
    elif choice == 'off':
        is_on = False
    else:
        drink = menu_object.find_drink(choice)
        if 'MenuItem' in str(type(drink)):
            if coffee_maker_object.is_resource_sufficient(drink=drink):
                if money_machine_object.make_payment(drink.cost):
                    coffee_maker_object.make_coffee(drink)

