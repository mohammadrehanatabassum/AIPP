def print_multiples_for(number):
    """Print first 10 multiples using for loop."""
    print(f"First 10 multiples of {number} (for loop):")
    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")


def print_multiples_while(number):
    """Print first 10 multiples using while loop."""
    print(f"First 10 multiples of {number} (while loop):")
    i = 1
    while i <= 10:
        print(f"{number} × {i} = {number * i}")
        i += 1


def print_multiples_list_comp(number):
    """Print first 10 multiples using list comprehension."""
    print(f"First 10 multiples of {number} (list comprehension):")
    multiples = [number * i for i in range(1, 11)]
    for i, mult in enumerate(multiples, 1):
        print(f"{number} × {i} = {mult}")


def print_multiples_for_else(number):
    """Print first 10 multiples using for-else loop."""
    print(f"First 10 multiples of {number} (for-else loop):")
    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")
    else:
        print("Completed printing all multiples!")


# Main program
if __name__ == "__main__":
    print("=" * 50)
    num = int(input("Enter a number: "))
    print()
    
    print_multiples_for(num)
    print()
    print_multiples_while(num)
    print()
    print_multiples_list_comp(num)
    print()
    print_multiples_for_else(num)
    
    print("\n" + "=" * 50)
    print("CODE ANALYSIS")
    print("=" * 50)
    print("""
    1. FOR LOOP:
       - Uses range(1, 11) for fixed 10 iterations
       - Most Pythonic and readable approach
       - Best for known iteration count
       - Time: O(1), Space: O(1)
    
    2. WHILE LOOP:
       - Uses counter variable with condition (i <= 10)
       - More flexible for variable conditions
       - Requires manual counter increment
       - Time: O(1), Space: O(1)
    
    3. LIST COMPREHENSION:
       - Creates list first, then iterates to print
       - Functional programming style
       - Uses enumerate() for indexing
       - Time: O(1), Space: O(1) - stores 10 values
    
    4. FOR-ELSE LOOP:
       - Standard for loop with else clause
       - Else executes after loop completes normally
       - Useful for confirmation messages
       - Time: O(1), Space: O(1)
    
    COMPARISON:
    ✓ For loop: Best for fixed iterations (recommended)
    ✓ While loop: Best for variable/conditional iterations
    ✓ List comprehension: Best when you need the list
    ✓ For-else: Best when you need post-loop actions
    
    All methods produce identical output with O(1) complexity.
    """)
