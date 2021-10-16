from art import logo


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operations = {"+": add, "-": sub, "*": mul, "/": div}



def calculator():
    print(logo)
    num1 = float(input("Enter 1st number:\n"))
    for key in operations:
        print(key)
    should_continue = True
    while should_continue:
        op = input("select the operator\n")
        num2 = float(input("Enter 2nd number:\n"))
        ops = operations[op]
        result = ops(num1, num2)
        print(f"{num1} {op} {num2} = {result}")
        if input(
                "type 'y' to continue calculating with result, else type 'n' to start with new calculations.").lower() == 'y':
            num1 = result
        else:
            should_continue = False
            calculator()


calculator()
