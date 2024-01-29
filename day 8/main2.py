# Initialize the variable to keep track of the highest scenic score
highest_score = 0

# Function to find the viewing distance in a given direction
def find_viewing_distance(direction, forrest, row, column, tree):
    distance = 0  # Initialize distance counter

    # Check the 'up' direction
    if direction == "up":
        if row == 0:  # If the tree is on the top edge, no distance to calculate
            return 0
        else:
            # Iterate through rows above the tree
            for i in range(row - 1, -1, -1):
                if forrest[i][column].isdigit():  # Check if it's a tree (digit)
                    distance += 1  # Increment the distance
                    # If the tree above is equal or larger, stop counting
                    if int(forrest[i][column]) >= tree:
                        break

    # Check the 'down' direction
    elif direction == "down":
        if row == len(forrest) - 1:  # Tree is on the bottom edge
            return 0
        else:
            # Iterate through rows below the tree
            for i in range(row + 1, len(forrest)):
                if forrest[i][column].isdigit():  # Check if it's a tree (digit)
                    distance += 1
                    # If the tree below is equal or larger, stop counting
                    if int(forrest[i][column]) >= tree:
                        break

    # Check the 'left' direction
    elif direction == "left":
        if column == 0:  # Tree is on the left edge
            return 0
        else:
            # Iterate through columns to the left of the tree
            for i in range(column - 1, -1, -1):
                if forrest[row][i].isdigit():  # Check if it's a tree (digit)
                    distance += 1
                    # If the tree on the left is equal or larger, stop counting
                    if int(forrest[row][i]) >= tree:
                        break

    # Check the 'right' direction
    elif direction == "right":
        if column == len(forrest[row]) - 1:  # Tree is on the right edge
            return 0
        else:
            # Iterate through columns to the right of the tree
            for i in range(column + 1, len(forrest[row])):
                if forrest[row][i].isdigit():  # Check if it's a tree (digit)
                    distance += 1
                    # If the tree on the right is equal or larger, stop counting
                    if int(forrest[row][i]) >= tree:
                        break

    # Return the calculated viewing distance
    return distance

# Function to calculate the scenic score for each tree in the forrest
def calculate_scenic_score(forrest):
    global highest_score  # Refer to the global highest_score variable

    # Iterate over each tree in the forrest
    for row in range(len(forrest)):
        for column in range(len(forrest[row])):
            tree = int(forrest[row][column])  # Convert the tree symbol to an integer

            # Calculate viewing distances in all four directions
            up_score = find_viewing_distance("up", forrest, row, column, tree)
            down_score = find_viewing_distance("down", forrest, row, column, tree)
            left_score = find_viewing_distance("left", forrest, row, column, tree)
            right_score = find_viewing_distance("right", forrest, row, column, tree)

            # Calculate the scenic score as the product of the viewing distances
            scenic_score = up_score * down_score * left_score * right_score

            # Update the highest score if the current scenic score is greater
            if scenic_score > highest_score:
                highest_score = scenic_score

    # Return the highest scenic score found
    return highest_score

# Reading the forrest structure from the input file
forrest = []
with open("input.txt", "r") as rows:
    for row in rows:
        new_forrest = list(row.strip())  # Convert each row to a list of tree symbols
        forrest.append(new_forrest)  # Append the converted row to the forrest

# Calculate the highest scenic score in the forrest
highest_score = calculate_scenic_score(forrest)
print(highest_score)
