num1 = float(input("Enter value of num1: "))
num2 = float(input("Enter value of num2: "))

operator = input("Operation (+, -, *, /): ")

print(num1, operator, num2)

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero!")
    case _:
        print("Invalid operator")
