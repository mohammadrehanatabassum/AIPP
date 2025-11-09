def sum_odd_even(numbers):
    """
    Calculate the sum of odd and even numbers in a list.
    
    Args:
        numbers: A list of integers
    
    Returns:
        A tuple containing (sum_of_odd, sum_of_even)
    
    Example:
        >>> sum_odd_even([1, 2, 3, 4, 5])
        (9, 6)  # Odd: 1+3+5=9, Even: 2+4=6
    """
    sum_odd = 0
    sum_even = 0
    
    for num in numbers:
        if num % 2 == 0:  # Even number
            sum_even += num
        else:  # Odd number
            sum_odd += num
    
    return sum_odd, sum_even


# Alternative implementation using list comprehension
def sum_odd_even_comprehension(numbers):
    """
    Calculate the sum of odd and even numbers using list comprehension.
    
    Args:
        numbers: A list of integers
    
    Returns:
        A tuple containing (sum_of_odd, sum_of_even)
    """
    sum_odd = sum(x for x in numbers if x % 2 != 0)
    sum_even = sum(x for x in numbers if x % 2 == 0)
    
    return sum_odd, sum_even


# Main program with user input
if __name__ == "__main__":
    print("Sum of Odd and Even Numbers Calculator")
    print("=" * 50)
    
    # Get user input for numbers
    user_input = input("Enter numbers separated by spaces or commas: ")
    
    # Clean and parse the input
    # Replace commas with spaces and split
    numbers_str = user_input.replace(',', ' ').split()
    
    try:
        # Convert to list of integers
        numbers = [int(x) for x in numbers_str]
        
        # Calculate sums
        sum_odd, sum_even = sum_odd_even(numbers)
        
        # Display results
        print(f"\nNumbers entered: {numbers}")
        print(f"Odd numbers: {[x for x in numbers if x % 2 != 0]}")
        print(f"Even numbers: {[x for x in numbers if x % 2 == 0]}")
        print(f"\nSum of odd numbers: {sum_odd}")
        print(f"Sum of even numbers: {sum_even}")
        print(f"Total sum: {sum_odd + sum_even}")
        
    except ValueError:
        print("Error: Please enter valid integers separated by spaces or commas.")





