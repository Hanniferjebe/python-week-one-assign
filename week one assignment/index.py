def calculate(num1, num2, operation):
    if operation == "+":    
        return num1 + num2
    elif operation == "-": 
        return num1 - num2
    elif operation == "*":  
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid operation"
    return

num1 = float(input("enter the first number: "))

operation = input("enter the operation (+, -, *, /): ")

num2 = float(input("enter the second number: "))
result = calculate(num1, num2, operation)

print(f"result: {result}")