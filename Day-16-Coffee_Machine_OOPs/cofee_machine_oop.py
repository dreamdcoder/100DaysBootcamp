from menu import MENU, resources

profit = 0

def process_coins():
    """Returns total cash"""
    # 1 quarter equals 0.25 = 1/4 dollar
    # 1 dime equals 0.1 = 1/10 dollar
    # 1 nickel equals 0.05 = 1/20 dollar
    # 1 penny equals 0.01 = 1/100 dollar
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    total_cash = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total_cash

def format_resource(water,milk,coffee,money):
    print(f"water:{water}ml\nmilk:{milk}ml\ncoffee:{coffee}g\nmoney:${money}")


def check_resources(drink):
    """ returns required resources for coffee"""
    for item in drink:
        if drink[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def is_transaction_success(total_cash,price):
    global profit
    if total_cash < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = total_cash - price
        print(f"Here is ${change} in change.")
        profit += price
        return True


def make_coffee(drink_name,drink):
    for item in drink:
        resources[item] -= drink[item]
    print(f"Here is your {drink_name} ☕.Enjoy!")

def dispense():
    is_on = True
    while is_on:
        current_water = resources["water"]
        current_milk = resources["milk"]
        current_coffee = resources["coffee"]
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'report':
            format_resource(current_water,current_milk,current_coffee,profit)
        elif choice == 'off':
             is_on = False
        else:
            price = MENU[choice]["cost"]
            order_ingredients =MENU[choice]["ingredients"]
            if check_resources(order_ingredients):
                print(f"That would be ${price}.Please insert coins.")
                total_cash = process_coins()
                if is_transaction_success(total_cash,price):
                     make_coffee(choice,order_ingredients)

if __name__ == "__main__":
    dispense()