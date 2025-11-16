import math

def is_prime(n: int) -> bool:
    """Return True if n is a prime number (integers only)."""
    if not isinstance(n, int):
        return False
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    s = input("Enter an integer to check primality (or press Enter to exit): ").strip()
    if s:
        try:
            num = int(s)
            print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")
        except Exception:
            print("Invalid input: please enter an integer.")

