
while True:
    try:
        expression = input(
            "Enter a expression or type(exit,quit): ").lower()
        if expression in ("exit", "quit"):
            break
        result = eval(expression)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error:not divisible by 0")
    except (SyntaxError, TypeError):
        print("invalid expression")
    choice = input("do u want to continue the calculation(y/n) :").lower()
    if choice != "y":
        break
