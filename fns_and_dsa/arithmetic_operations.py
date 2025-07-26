def perform_operation(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "substract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        if y == 0:
            return "Error! Division by zero"
        
        else:
            return x / y
    else:
        return "Invalid operation"

