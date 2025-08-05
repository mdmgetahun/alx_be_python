def safe_divide(numerator, denominator):
    
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return numerator / denominator

def main():

    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = safe_divide(numerator, denominator)
        print(f"The result of the division is {result}")
    except ValueError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.") 
main()
    