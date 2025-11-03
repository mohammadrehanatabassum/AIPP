# Few-shot examples to show the desired format:
# Example 1: Input: "John Doe"        -> Output: "Doe, John"
# Example 2: Input: "jane mary smith" -> Output: "Smith, Jane Mary"
# Example 3: Input: "Plato"           -> Output: "Plato"

def format_name(full_name: str) -> str:
    """Format a full name as 'Last, First' (keep given+middle together)."""
    s = full_name.replace(",", " ").strip()  # handle comma input
    if not s:
        return ""
    parts = [p for p in s.split() if p]
    if len(parts) == 1:
        return parts[0].title()
    last = parts[-1].title()
    first = " ".join(p.title() for p in parts[:-1])
    return f"{last}, {first}"


if __name__ == "__main__":
    print("Few-shot examples:")
    print('  "John Doe"        ->', format_name("John Doe"))
    print('  "jane mary smith" ->', format_name("jane mary smith"))
    print('  "Plato"           ->', format_name("Plato"))
    user = input("Enter a full name to format: ").strip()
    if user:
        print(format_name(user))
    else:
        print("No input provided.")
