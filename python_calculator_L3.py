# this upgraded version of the calculator no longer relies on Python’s eval() function
# ensuring safe calculation
def add(a, b):  # user-defined function
    return (a+b)


def substract(a, b):
    return (a-b)


def multiply(a, b):
    return (a*b)


def devision(a, b):
    return (a/b)


while True:
    try:
        expression = input(
            # removing all the spaces
            "Enter a expression or type(exit,quit): ").replace(" ", "")
        if expression in ("exit", "quit"):
            break

        if "+" in expression:  # checks if there is "+" operator in the expression
            # converts that part of the expression into a string
            string = expression.split("+")
            # converts the string into floting point datatype
            numbers = [float(p) for p in string]
            # takes the first number (index 0) from the floting point datatype
            result = numbers[0]
            # continues taking numbers from floting point datatype and srores it in i
            for i in numbers[1:]:
                result = add(result, i)  # adds all the number one by one

        elif "-" in expression:

            string = expression.split("-")
            numbers = [float(p) for p in string]
            result = numbers[0]
            for i in numbers[1:]:
                result = substract(result, i)

        elif "*" in expression:
            string = expression.split("*")
            numbers = [float(p) for p in string]
            result = numbers[0]
            for i in numbers[1:]:
                result = multiply(result, i)
        elif "/" in expression:
            string = expression.split("/")
            numbers = [float(p) for p in string]
            result = numbers[0]
            for i in numbers[1:]:
                result = devision(result, i)
        else:
            print("enter the the correct expression :")
        print(f"Result : {result}")
    except ZeroDivisionError:  # indicates devision by 0 error
        print("Error: Division by zero")

    except ValueError:  # indicates the error in input value
        print("Error: Invalid numbers")

    choice = input("Do you want to continue (y/n)? ").lower()
    if choice != "y":
        break
