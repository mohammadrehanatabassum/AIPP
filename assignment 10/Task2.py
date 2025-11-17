def find_common(a, b):
    return [x for x in a if x in b]

# ---- User Input ----
a = input("Enter first list elements separated by space: ").split()
b = input("Enter second list elements separated by space: ").split()

# ---- Find Common ----
common = find_common(a, b)

print("Common elements:", common)
