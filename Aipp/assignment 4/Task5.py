def count_lines(filename: str) -> int:
    """
    Count number of lines in a text file.
    Returns -1 if file cannot be opened.
    """
    try:
        with open(filename, 'r') as f:
            return sum(1 for _ in f)
    except:
        return -1

if __name__ == "__main__":
    # Few-shot examples
    print("Few-shot examples:")
    print("Example 1: sample.txt contains:")
    print("hello\nworld\ngoodbye")
    print("count_lines('sample.txt') -> 3")
    
    print("\nExample 2: empty.txt contains:")
    print("<empty file>")
    print("count_lines('empty.txt') -> 0")
    
    print("\nExample 3: missing.txt:")
    print("<file does not exist>")
    print("count_lines('missing.txt') -> -1")

    # Get user input
    filename = input("\nEnter text file name to count lines: ")
    result = count_lines(filename)
    if result >= 0:
        print(f"Number of lines: {result}")
    else:
        print("Error: Could not open file")