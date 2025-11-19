from typing import Any, List, Optional

def linear_search(arr: List[Any], target: Any) -> Optional[int]:
    """
    Search for a target value in a list using linear search.

    Returns index if found, None otherwise.
    """
    if not isinstance(arr, list):
        raise TypeError("First argument must be a list")

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None


def linear_search_all(arr: List[Any], target: Any) -> List[int]:
    """
    Search for all occurrences of a target in the list.

    Returns a list of indices.
    """
    if not isinstance(arr, list):
        raise TypeError("First argument must be a list")

    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


if __name__ == "__main__":
    print("Linear Search Operations")
    print("=" * 50)

    arr = []  # initialize before menu starts

    while True:
        print("\nOptions:")
        print("1. Create/Enter a list")
        print("2. Search for first occurrence")
        print("3. Search for all occurrences")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            arr_input = input("Enter list elements separated by space: ").split()
            arr = []

            for item in arr_input:
                # convert to int when possible
                try:
                    arr.append(int(item))
                except ValueError:
                    arr.append(item)

            print(f"List created: {arr}")

        elif choice == "2":
            if not arr:
                print("No list created yet. Please enter a list first.")
                continue

            target_input = input("Enter value to search: ")

            try:
                target = int(target_input)
            except ValueError:
                target = target_input

            result = linear_search(arr, target)

            if result is not None:
                print(f"Element '{target}' found at index: {result}")
            else:
                print(f"Element '{target}' NOT found")

        elif choice == "3":
            if not arr:
                print("No list created yet. Please enter a list first.")
                continue

            target_input = input("Enter value to search: ")

            try:
                target = int(target_input)
            except ValueError:
                target = target_input

            results = linear_search_all(arr, target)

            if results:
                print(f"Element '{target}' found at indices: {results}")
            else:
                print(f"Element '{target}' NOT found")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid input. Please enter a number between 1–4.")
