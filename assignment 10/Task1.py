def discount(price, category):
    rules = {
        "student": (1000, 0.90, 0.95),  # (limit, above-limit rate, below-limit rate)
        "other":   (2000, 0.85, 1.00)
    }

    limit, above_rate, below_rate = rules.get(category, rules["other"])

    if price > limit:
        return price * above_rate
    else:
        return price * below_rate


# ---- User Input ----
price = float(input("Enter the price: "))
category = input("Enter category (student/other): ").lower()

# ---- Output ----
print("Final price after discount:", discount(price, category))

