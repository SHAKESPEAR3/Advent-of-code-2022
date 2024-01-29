import ast
from functools import cmp_to_key


# Custom comparison function for sorting
def compare_elements(left, right):
    # Convert integers to single-element lists if one element is an integer and the other is a list
    if isinstance(left, int) and isinstance(right, list):
        left = [left]
    elif isinstance(right, int) and isinstance(left, list):
        right = [right]

    # Compare integers
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (left < right)  # Return -1, 0, or 1 based on comparison

    # Compare lists
    if isinstance(left, list) and isinstance(right, list):
        min_length = min(len(left), len(right))   # To avoid index errors
        for i in range(min_length):
            result = compare_elements(left[i], right[i])
            if result != 0:
                return result
        # If lists are of different lengths
        return (len(left) > len(right)) - (len(left) < len(right))

    return 0  # Return 0 if types are not integers or lists


# Function to sort pairs using the custom comparison function
def sort_pairs(pairs):
    # Use 'cmp_to_key' to convert the comparison function for use with 'sorted'
    return sorted(pairs, key=cmp_to_key(compare_elements))


# Read pairs from a file and convert them into Python lists
pairs = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            pairs.append(ast.literal_eval(line))  # Parse string to Python list
    # Add decoder keys
    pairs.append([[2]])
    pairs.append([[6]])

# Sort the pairs
sorted_pairs = sort_pairs(pairs)

# Find the index positions of specific lists in the sorted order and calculate their product
index_product = (sorted_pairs.index([[2]]) + 1) * (sorted_pairs.index([[6]]) + 1)

# Print the result
print(index_product)
