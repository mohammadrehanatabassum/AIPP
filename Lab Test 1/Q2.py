
def summarize_transactions(amounts):
    """Summarize total deposits, withdrawals, and net balance.

    Args:
        amounts (list[float]): Monetary values where positive numbers
            represent deposits and negative numbers represent withdrawals.

    Returns:
        dict: Dictionary with keys:
            - 'deposits' (float): Sum of all positive values.
            - 'withdrawals' (float): Sum of absolute values of negatives.
            - 'net' (float): Deposits minus withdrawals.

    Raises:
        TypeError: If any value in amounts is not numeric.
    """
    if any(not isinstance(value, (int, float)) for value in amounts):
        raise TypeError("All transaction values must be numeric.")

    # Keep running totals for each category so the loop only processes once.
    total_deposits = 0.0
    total_withdrawals = 0.0

    for value in amounts:
        # Positive values are deposits.
        if value >= 0:
            total_deposits += value
        else:
            # Store withdrawals as positive numbers for readability.
            total_withdrawals += abs(value)

    # Net balance is deposits minus withdrawals.
    net_balance = total_deposits - total_withdrawals

    return {
        "deposits": total_deposits,
        "withdrawals": total_withdrawals,
        "net": net_balance,
    }


# AI-generated docstring (from a helper tool) for comparison purposes.
def summarize_transactions_ai(amounts):
    """
    Returns total deposits, total withdrawals, and net value from the list.

    Args:
        amounts (list): Transaction amounts where positive numbers are
            deposits and negatives are withdrawals.

    Returns:
        dict: {'deposits': float, 'withdrawals': float, 'net': float}
    """
    return summarize_transactions(amounts)


def compare_docstrings():
    """Print differences between manual and AI-generated documentation."""

    print("=" * 60)
    print("Manual Docstring")
    print("=" * 60)
    print(summarize_transactions.__doc__)

    print("\n" + "=" * 60)
    print("AI-Generated Docstring")
    print("=" * 60)
    print(summarize_transactions_ai.__doc__)

    print("\n" + "=" * 60)
    print("Analysis")
    print("=" * 60)
    print(
        "Manual docstring offers detailed descriptions, type hints, and "
        "explicit error behavior, improving clarity. The AI version is concise "
        "but omits the TypeError information and lacks guidance on how values "
        "are transformed (e.g., absolute withdrawals). Manual comments inside "
        "the function also explain why each step exists, which the AI "
        "description cannot infer. Together, this shows manual documentation "
        "remains more complete, while AI docs are useful as a quick starting "
        "point."
    )


if __name__ == "__main__":
    sample = [1200.0, -200.0, 450.0, -50.0, 30.0]
    summary = summarize_transactions(sample)
    print("Summary:", summary)
    compare_docstrings()

