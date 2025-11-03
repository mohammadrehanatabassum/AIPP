def count_vowels(s: str) -> int:
    """Return the number of vowels (a,e,i,o,u) in s, case-insensitive."""
    if s is None:
        return 0
    vowels = set("aeiou")
    return sum(1 for ch in s.lower() if ch in vowels)

# Test cases / output
print(count_vowels("hello"))   # Expected: 2
print(count_vowels("Sky"))     # Expected: 1
print(count_vowels("AEIOU"))   # Expected: 5
print(count_vowels(""))        # Expected: 0

# User input
user = input("Enter a string: ")
print("Vowel count:", count_vowels(user))