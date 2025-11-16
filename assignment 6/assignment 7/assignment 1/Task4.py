import sys
#!/usr/bin/env python3
# Recursive and iterative factorial implementations.
# Reads a non-negative integer from the user and prints both results.

def factorial_recursive(n):                       #using recursion
    # Recursive factorial: n! = n * (n-1)! with 0! = 1
    if n < 0:
        raise ValueError("factorial undefined for negative values")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):                         #using iteration
    # Iterative factorial using a loop
    if n < 0:
        raise ValueError("factorial undefined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        s = input("Enter a non-negative integer: ").strip()
        n = int(s)
        if n < 0:
            print("Error: please enter a non-negative integer.")
            sys.exit(1)
    except ValueError:
        print("Error: invalid integer input.")
        sys.exit(1)

    # Compute and display results
    try:
        print("Recursive:", factorial_recursive(n))
    except RecursionError:
        print("Recursive: recursion depth exceeded for", n)
    print("Iterative:", factorial_iterative(n))

