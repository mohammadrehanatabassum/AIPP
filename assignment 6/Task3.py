def classify_age_nested(age):
    """Classify age groups using nested if-elif-else."""
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        if age < 30:
            return "Young Adult"
        elif age < 50:
            return "Adult"
        else:
            return "Middle-aged Adult"
    else:
        return "Senior"


def classify_age_simple(age):
    """Classify age groups using simple if-elif-else."""
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 30:
        return "Young Adult"
    elif age < 50:
        return "Adult"
    elif age < 65:
        return "Middle-aged Adult"
    else:
        return "Senior"


def classify_age_ternary(age):
    """Classify age groups using ternary operators."""
    if age < 0:
        return "Invalid age"
    return ("Child" if age < 13 else
            "Teenager" if age < 20 else
            "Young Adult" if age < 30 else
            "Adult" if age < 50 else
            "Middle-aged Adult" if age < 65 else
            "Senior")


# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("AGE GROUP CLASSIFICATION")
    print("=" * 50)
    
    test_ages = [5, 15, 25, 40, 55, 70]
    
    print("\n1. Nested if-elif-else:")
    for age in test_ages:
        print(f"Age {age:3d}: {classify_age_nested(age)}")
    
    print("\n2. Simple if-elif-else:")
    for age in test_ages:
        print(f"Age {age:3d}: {classify_age_simple(age)}")
    
    print("\n3. Ternary Operators:")
    for age in test_ages:
        print(f"Age {age:3d}: {classify_age_ternary(age)}")
    
    # User input
    print("\n" + "=" * 50)
    try:
        age = int(input("Enter your age: "))
        print(f"Your age group: {classify_age_nested(age)}")
    except ValueError:
        print("Error: Please enter a valid integer.")
    
    print("\n" + "=" * 50)
    print("CODE ANALYSIS")
    print("=" * 50)
    print("""
    1. NESTED IF-ELIF-ELSE:
       - Uses nested conditions (if inside elif)
       - Hierarchical structure
       - Time: O(1), Space: O(1)
       - Readability: Moderate
    
    2. SIMPLE IF-ELIF-ELSE:
       - Linear chain, no nesting
       - Sequential evaluation
       - Time: O(1), Space: O(1)
       - Readability: Good (recommended)
    
    3. TERNARY OPERATORS:
       - Chained conditional expressions
       - Most concise
       - Time: O(1), Space: O(1)
       - Readability: Poor (too compact)
    
    All methods produce same output with O(1) complexity.
    Simple if-elif-else is most readable and maintainable.
    """)
