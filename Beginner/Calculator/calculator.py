# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# function = operations["+"]
# print(function(2, 3))


def calculator():
    num1 = float(input("What is your first number? \n"))
    for operation in operations:
        print(operation)
    should_continue = True

    while should_continue == True:
        operation_symbol = input("Pick an operation: \n")
        num2 = float(input("What's the next number? \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        new_operation = input(f"Type 'y' to continue calculting with {answer}, or type 'n' to start a new calculation. Type 'end' if you want end your opeations:\n")
        if new_operation == 'y':
            num1 = answer
        elif new_operation == 'n':
            should_continue = False
            calculator()
        elif new_operation == 'end':
            should_continue = False
            print("Thanks for using our calculator!")
        else:
            print("Type 'y', 'n' or 'end'!")

calculator()