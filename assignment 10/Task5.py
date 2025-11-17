def divide_numbers(a, b):
    """
    Divide two numbers with safe error handling.

    This function attempts to divide `a` by `b` and uses a try-except block
    to prevent crashes when invalid operations occur (e.g., division by zero).
    
    Parameters:
        a (float or int): The numerator.
        b (float or int): The denominator.
    
    Returns:
        float: The result of the division if successful.
        None: Returned when an error occurs.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both inputs must be numbers.")

# --- Enable user input ---
try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    result = divide_numbers(num1, num2)

    if result is not None:
        print("Result:", result)
except ValueError:
    print("Invalid input! Please enter numeric values.")

