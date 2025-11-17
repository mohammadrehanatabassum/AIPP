def grade(score):
    thresholds = {
        90: "A",
        80: "B",
        70: "C",
        60: "D"
    }

    for limit, grade_letter in thresholds.items():
        if score >= limit:
            return grade_letter
    return "F"


# Enable user input
try:
    user_score = float(input("Enter the score: "))
    print("Grade:", grade(user_score))
except ValueError:
    print("Invalid input! Please enter a numeric score.")
