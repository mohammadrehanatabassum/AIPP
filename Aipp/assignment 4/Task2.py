def cm_to_inches(cm: float) -> float:
    """Convert centimeters to inches. 1 inch = 2.54 cm."""
    return cm / 2.54

if __name__ == "__main__":
    # One-shot example shown to the user, then prompt for input (one-shot prompting)
    one_shot_example = "One-shot example: Input: 10  -> Output: 3.9370"
    prompt = f"{one_shot_example}\nOne-shot prompt: enter centimeters (numeric): "
    user_input = input(prompt)
    try:
        cm_value = float(user_input.strip())
    except ValueError:
        print("Invalid input: please enter a numeric value for centimeters.")
    else:
        inches = cm_to_inches(cm_value)
        print(f"{cm_value} cm = {inches:.4f} inches")