import ast

def compare_elements(left, right):
    # If one element is an integer and the other is a list, convert the integer to a list
    if isinstance(left, int) and isinstance(right, list):
        left = [left]
    elif isinstance(right, int) and isinstance(left, list):
        right = [right]

    # If both elements are integers, compare their values
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1  # Left is smaller = correct order
        elif left > right:
            return 0  # Left is larger = incorrect order
        else:
            return "continue"   # Elements are equal = continue comparison

    # If both elements are lists, compare their elements recursively
    if isinstance(left, list) and isinstance(right, list):
        min_length = min(len(left), len(right))     # To avoid index errors
        for i in range(min_length):
            result = compare_elements(left[i], right[i])
            if result != "continue":
                return result  # Return the result if elements are not equal

        # Compare the length of the lists if elements are equal
        if len(left) < len(right):
            return 1  # Left list is shorter = correct order
        elif len(left) > len(right):
            return 0  # Left list is longer = incorrect order
        else:
            return "continue"  # Lists are of equal length = continue comparison

    return "error"

def process_pairs(pairs):
    global pair_index, indexes_total

    for i in range(0, len(pairs), 2):
        # Evaluate the string representation of the list
        list1 = ast.literal_eval(pairs[i])
        list2 = ast.literal_eval(pairs[i + 1])

        # Compare the two lists and accumulate the index if they are in the correct order
        if compare_elements(list1, list2) == 1:
            indexes_total += pair_index

        pair_index += 1  # Increment the pair index


indexes_total = 0
pair_index = 1
pairs = []
# Read the pairs from a file and store them in a list
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:  # Ignore empty lines
            pairs.append(line)


process_pairs(pairs)
print(indexes_total)
