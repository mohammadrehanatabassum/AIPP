# Task #4: Sum of First N Numbers Using Loops
# --------------------------------------------

def sum_to_n_for(n):
    """Calculate the sum of first n numbers using a FOR loop."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_to_n_while(n):
    """Calculate the sum of first n numbers using a WHILE loop."""
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


# Main Program
if __name__ == "__main__":
    print("=" * 50)
    print("PROGRAM: SUM OF FIRST N NATURAL NUMBERS")
    print("=" * 50)

    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Please enter a number greater than zero.")
        else:
            # Using FOR loop
            sum_for = sum_to_n_for(n)
            print(f"\nSum of first {n} numbers using FOR loop: {sum_for}")

            # Using WHILE loop
            sum_while = sum_to_n_while(n)
            print(f"Sum of first {n} numbers using WHILE loop: {sum_while}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

    # Code Analysis Section
    print("\n" + "=" * 50)
    print("CODE ANALYSIS")
    print("=" * 50)
    print("""
    1. FUNCTION: sum_to_n_for(n)
       - Uses a FOR loop from 1 to n.
       - Adds each number to a variable 'total'.
       - Returns the total sum.

    2. FUNCTION: sum_to_n_while(n)
       - Uses a WHILE loop with a counter variable 'i'.
       - Continues adding until i > n.
       - Returns the total sum.

    3. INPUT HANDLING:
       - Accepts integer input from the user.
       - Checks for invalid or negative input.

    4. CODE QUALITY:
       ✓ Clear and readable
       ✓ Demonstrates both FOR and WHILE control structures
       ✓ Matches expected output format
    """)



