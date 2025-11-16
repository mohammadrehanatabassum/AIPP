# Find largest number in a list (two simple implementations)

from typing import Iterable, TypeVar

T = TypeVar("T")

def find_max(nums: Iterable[T]) -> T:
    """
    Return the largest element from nums using a single-pass algorithm.
    Raises ValueError if nums is empty or contains no elements.
    """
    it = iter(nums)
    try:
        max_val = next(it)
    except StopIteration:
        raise ValueError("find_max() arg is an empty iterable")
    for x in it:
        if x > max_val:
            max_val = x
    return max_val

def find_max_builtin(nums: Iterable[T]) -> T:
    """
    Return the largest element using Python's built-in max().
    Raises ValueError for empty iterables (same behavior as built-in).
    """
    return max(nums)

if __name__ == "__main__":
    s = input("Enter numbers separated by spaces (or press Enter to exit): ").strip()
    if s:
        try:
            nums = [float(x) if "." in x or "e" in x.lower() else int(x) for x in s.split()]
            print("Manual find_max ->", find_max(nums))
            print("Built-in max     ->", find_max_builtin(nums))
        except Exception as e:
            print("Error parsing input or comparing values:", e)