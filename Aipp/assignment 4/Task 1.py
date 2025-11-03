def is_leap_year(year: int) -> bool:
    """
    Return True if year is a leap year, else False.
    Rule: divisible by 4, except years divisible by 100 unless divisible by 400.
    """
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    return year % 400 == 0

if __name__ == "__main__":
    prompt = (
        "Zero-shot prompt: provide a year (integer) and this program will tell you\n"
        "whether it's a leap year.\nEnter year: "
    )
    user_input = input(prompt)
    try:
        y = int(user_input.strip())
    except ValueError:
        print("Invalid input: please enter an integer year.")
    else:
        if is_leap_year(y):
            print(f"{y} is a leap year.")
        else:
            print(f"{y} is not a leap year.")