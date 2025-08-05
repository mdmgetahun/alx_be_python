# def safe_divide(numerator, denominator):
    
#     if denominator == 0:
#         raise ZeroDivisionError("Denominator cannot be zero.")
#     return float(numerator) / float(denominator)

# def main():

#     try:
         
#         numerator = float(numerator)
#         denominator = float(denominator)

#         if denominator == 0:
#                 raise ZeroDivisionError("Denominator cannot be zero.")
         
#         result = safe_divide(numerator, denominator)

#         return float(numerator) / float(denominator)

#         numerator = float(input("Enter the numerator: "))
#         denominator = float(input("Enter the denominator: "))
#         print(f"The result of the division is {result}")
#     except ValueError:
#         print("Error: Please enter numeric values only.")
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero.") 

# if __name__ == "__main__":
#     main()
    
def safe_divide(numerator, denominator):
    """
    Perform division after converting inputs to float.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator cannot be zero.")
    except ValueError:
        raise ValueError("Invalid numeric input.")
    
def main():
    try:
        numerator = input("Enter the numerator: ")
        denominator = input("Enter the denominator: ")
        result = safe_divide(numerator, denominator)
        print(result)
    except ZeroDivisionError as e:
        print(e)
        print("Error: Cannot divide by zero.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()