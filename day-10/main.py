from art import logo


def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def divid(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Enter a second number different of 0"


def multiplication(n1, n2):
    return n1 * n2


operations = {
    "-": subtraction,
    "+": addition,
    "*": multiplication,
    '/': divid
}


print(logo)

num1 = float(input("What's the first number?: "))


for key in operations:
    print(key)

operation_symbol = input("Pick an operation from the line above: ")

num2 = float(input("What's the next number?: "))

function = operations[operation_symbol]

result = function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {result}")


is_continue = True


while is_continue == True:
    choice = input(
        "Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")

    if choice == 'y':
        operation_symbol = input("Pick an operator: ")
        fun = operations[operation_symbol]

        num = int(input("What's the next number?: "))
        previous_result = result
        result = fun(result, num)

        print(f"{previous_result} {operation_symbol} {num} = {result}")
    else:
        is_continue = False
