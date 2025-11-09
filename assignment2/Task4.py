def sum_of_squares(numbers):
    """
    Calculate the sum of squares of a list of numbers.
    
    Args:
        numbers: A list of numbers (int or float)
    
    Returns:
        The sum of squares of all numbers in the list
    
    Example:
        >>> sum_of_squares([1, 2, 3])
        14  # 1² + 2² + 3² = 1 + 4 + 9 = 14
    """
    return sum(x ** 2 for x in numbers)


# Alternative function for sum of squares from 1 to n
def sum_of_squares_range(n):
    """
    Calculate the sum of squares from 1 to n.
    
    Args:
        n: An integer representing the upper limit
    
    Returns:
        The sum of squares: 1² + 2² + ... + n²
    
    Example:
        >>> sum_of_squares_range(3)
        14  # 1² + 2² + 3² = 1 + 4 + 9 = 14
    """
    return sum(i ** 2 for i in range(1, n + 1))


# Example usage with user input
if __name__ == "__main__":
    print("Sum of Squares Calculator")
    print("=" * 40)
    
    # Get user input for numbers
    user_input = input("Enter numbers separated by spaces or commas: ")
    
    # Clean and parse the input
    # Replace commas with spaces and split
    numbers_str = user_input.replace(',', ' ').split()
    
    try:
        # Convert to list of floats (handles both int and float)
        numbers = [float(x) for x in numbers_str]
        
        # Calculate sum of squares
        result = sum_of_squares(numbers)
        
        print(f"\nNumbers entered: {numbers}")
        print(f"Sum of squares = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers separated by spaces or commas.")

