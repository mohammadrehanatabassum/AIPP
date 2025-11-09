# ================================================================
# Prompt given to AI:
# "Write a Python function fib_recursive(n) that returns the nth Fibonacci number using recursion.
#  - Use 0-based indexing: fib(0)=0, fib(1)=1.
#  - Validate input (n must be a non-negative integer).
#  - Add a clear docstring and detailed inline comments.
#  - Also generate a short explanation document (module docstring) that describes base cases, recursion,
#    examples, and time/space complexity. Provide a small interactive example."
# ================================================================

"""
📘 Fibonacci Recursion Module (Transparency Task)

This module demonstrates two recursive approaches to calculate Fibonacci numbers:
1️⃣ fib_recursive(n) – a simple pure-recursive method (educational, but slow)
2️⃣ fib_memo(n) – a recursive method with memoization (optimized version)

🔹 Definition (0-based indexing):
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2) for n ≥ 2
    

🔹 Base Cases:
    These stop the recursion — when n is 0 or 1.

🔹 Time & Space Complexity:
    • fib_recursive → Exponential time O(φⁿ), φ ≈ 1.618, space O(n)
    • fib_memo → Linear time O(n), space O(n)

🔹 Example Outputs:
    fib_recursive(5) → 5
    fib_memo(10) → 55
"""

from functools import lru_cache


def fib_recursive(n: int) -> int:
    """
    Return the nth Fibonacci number using pure recursion (0-based indexing).

    Parameters:
        n (int): Non-negative integer index in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is not an integer or is negative.
    """

    # --- Step 1: Input validation ---
    # Ensure the input is an integer.
    if not isinstance(n, int):
        raise ValueError("n must be an integer.")
    
    # Ensure n is non-negative since Fibonacci is undefined for negative indices.
    if n < 0:
        raise ValueError("n must be non-negative.")

    # --- Step 2: Base cases ---
    # These are the stopping points for recursion.
    # If n == 0 → return 0 (first Fibonacci number)
    # If n == 1 → return 1 (second Fibonacci number)
    if n == 0:
        return 0
    if n == 1:
        return 1

    # --- Step 3: Recursive step ---
    # For any n ≥ 2:
    # Fibonacci of n = Fibonacci of (n-1) + Fibonacci of (n-2)
    # This step calls the same function twice with smaller arguments.
    # It continues until reaching the base cases (n == 0 or 1).
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@lru_cache(maxsize=None)  # Built-in caching to avoid recomputation
def fib_memo(n: int) -> int:
    """
    Optimized Fibonacci using recursion + memoization.
    Results are cached to prevent recalculating the same values.
    """
    
    # Input validation (same as before)
    if not isinstance(n, int):
        raise ValueError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")

    # Base cases (identical logic)
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive step, but now results are automatically stored
    # in cache by lru_cache(), making it much faster.
    return fib_memo(n - 1) + fib_memo(n - 2)


# ================================================================
# Interactive Demonstration Section
# ================================================================
if __name__ == "__main__":
    # Display the top-level documentation (acts as explanation)
    print(__doc__)

    try:
        # Ask user for input (optional)
        user_input = input(
            "\nEnter a non-negative integer n to compute fib(n) "
            "(or press Enter to see sample examples): "
        ).strip()

        # If user presses Enter, show some predefined examples
        if not user_input:
            examples = [0, 1, 5, 10]
            print("\n--- Sample Fibonacci Computations ---")
            
            # Loop through sample values and print both implementations
            for e in examples:
                # Show result using pure recursion
                print(f"fib_recursive({e}) = {fib_recursive(e)}    (pure recursion)")
                # Show result using memoized recursion
                print(f"fib_memo({e})      = {fib_memo(e)}        (memoized recursion)")
        else:
            # Convert user input to integer
            n = int(user_input)

            # Print results for both methods
            print(f"\nfib_recursive({n}) = {fib_recursive(n)}")
            print(f"fib_memo({n})      = {fib_memo(n)}")

    except Exception as exc:
        # Handle any errors gracefully
        print("Error:", exc)
