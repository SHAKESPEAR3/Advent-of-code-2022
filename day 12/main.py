from collections import deque

def is_valid_move(x, y, rows, cols, grid_map, visited, current_value):
    # A move is valid if it's within the grid bounds, the cell has not been visited,
    # and the value of the cell is at most one greater than the current value.
    return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid_map[x][y] <= current_value + 1

def bfs_shortest_path(start, goal, grid_map):
    rows, cols = len(grid_map), len(grid_map[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, 0)])  # Queue to manage the BFS, storing position and distance

    while queue:
        (x, y), dist = queue.popleft()  # Pop the next position and its distance from the queue
        if (x, y) == goal:
            return dist  # Return the distance if the goal is reached

        if visited[x][y]:  # Skip if already visited
            continue

        visited[x][y] = True  # Mark the cell as visited
        current_value = grid_map[x][y]  # Get the value of the current cell

        # Check all adjacent cells (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, rows, cols, grid_map, visited, current_value):
                queue.append(((nx, ny), dist + 1))  # Add valid moves to the queue

    return -1  # Return -1 if the goal is not reachable

def letter_to_number(letter):
    if letter == 'S':
        return -1  # Start position
    elif letter == 'E':
        return 26  # Goal position
    else:
        return ord(letter) - ord('a')  # Convert other letters to numbers

def find_position(grid_map, value_to_find):
    # Find the position (row, column) of a given value in the grid map
    for i, row in enumerate(grid_map):
        for j, value in enumerate(row):
            if value == value_to_find:
                return (i, j)  # Return the position when found

# Read the grid map from the file and convert each letter to its corresponding number
grid_map = []
with open("input.txt", "r") as map:
    for row in map:
        row = list(row.strip())
        grid_row = [letter_to_number(letter) for letter in row]
        grid_map.append(grid_row)

# Find the starting and goal positions in the grid map
start = find_position(grid_map, -1)
goal = find_position(grid_map, 26)


shortest_path_length = bfs_shortest_path(start, goal, grid_map)
print(shortest_path_length)
