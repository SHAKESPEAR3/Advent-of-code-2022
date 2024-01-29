interior_trees = 0


def is_tree_visible(forrest, tree, row, column):
    global interior_trees

    # ROWS
    left = [int(num) for num in forrest[row][:column] if num.isdigit()]
    right = [int(num) for num in forrest[row][column + 1:] if num.isdigit()]
    # Check if all trees to its left and right are smaller
    check_left = all(num < tree for num in left)
    check_right = all(num < tree for num in right)
    if check_left or check_right:
        interior_trees += 1

    else:
        # COLUMNS
        above = [int(forrest[i][column]) for i in range(row) if forrest[i][column].isdigit()]
        below = [int(forrest[i][column]) for i in range(row + 1, len(forrest)) if forrest[i][column].isdigit()]
        # A tree is visible if all trees above and below are smaller
        check_above = all(num < tree for num in above)
        check_below = all(num < tree for num in below)
        if check_above or check_below:
            interior_trees += 1

def find_all_interior_trees(forrest):
    # Trees that are not on the edge
    for row in range(1, len(forrest) -1):
        for column in range(1, len(forrest[row]) - 1):
            tree = int(forrest[row][column])
            is_tree_visible(forrest, tree, row, column)

def calculate_trees_on_edge(forest):
    width = len(forest[0])
    height = len(forest)
    trees_on_edge = 2 * (height + width) - 4

    return trees_on_edge

forrest = []
with open("input.txt", "r") as rows:
    for row in rows:
        new_forrest = list(row.strip())
        forrest.append(new_forrest)

find_all_interior_trees(forrest)
trees_on_edge = calculate_trees_on_edge(forrest)
total_visible_trees = trees_on_edge + interior_trees
print(total_visible_trees)