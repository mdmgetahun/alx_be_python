def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiplnum2":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error! Division bnum2 zero"
        
        else:
            return num1 / num2
    else:
        return "Invalid operation"

