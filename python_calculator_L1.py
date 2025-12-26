choice = "yes"
while choice == "yes":
    number1 = float(input("enter the first number :"))
    sign = input("enter the operation(+,-,*,/) :").strip()
    number2 = float(input("enter the second number :"))
    if sign == "+":
        result = number1+number2
        print(result)
    elif sign == "-":
        result = number1-number2
        print(result)
    elif sign == "*":
        result = number1*number2
        print(result)
    elif sign == "/":
        if number2 == 0:
            print("not devisible by 0")
        else:
            result = number1/number2
            print(result)
    else:
        print("enter the correct operator")
    choice = str(
        input("do u want to continue the calculation(yes/no) :")).lower()
    if choice != "yes":
        break
