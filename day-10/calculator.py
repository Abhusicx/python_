def calculate(number1, number2, operation):
    if(operation=="-"):
        return number1 - number2
    elif(operation=="*"):
        return number1 * number2
    elif(operation=="+"):
        return number1 + number2
    elif(operation=="/"):
        return number1 / number2
    else:
        return "invalid operation"

while True : 
    number1 = float(input("Enter a number: "))
    operation = input("""
    Select an operation you like to perform : 
    -
    *
    +
    /
    """)
    number2 = float(input("Enter a number: "))

    result = calculate(number1, number2, operation)
    print(f"your result {result}")

    choice = input("would you like to continue? answer in yes/no. \n")

    if (choice == "no"):
        print("thanks! goodbye for now we'll meet soon.")
        break


