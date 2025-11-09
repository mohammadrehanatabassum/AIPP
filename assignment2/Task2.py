def is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome (case- and punctuation-insensitive)."""
    if text is None:
        return False
    s = ''.join(ch.lower() for ch in text if ch.isalnum())
    return s == s[::-1]

if __name__ == "__main__":
    t = input("Enter text to check palindrome: ").strip()
    print(is_palindrome(t))