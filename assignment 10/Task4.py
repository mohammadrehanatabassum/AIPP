def calculate_total(scores):
    total = 0
    for s in scores:
        total += s
    return total


def find_highest(scores):
    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s
    return highest


def find_lowest(scores):
    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s
    return lowest


def process_scores(scores):
    total = calculate_total(scores)
    avg = total / len(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


# ---- User Input ----
raw_input_scores = input("Enter scores separated by spaces: ")
scores = [float(x) for x in raw_input_scores.split()]

# ---- Process Scores ----
process_scores(scores)

