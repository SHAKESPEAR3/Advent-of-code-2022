from collections import deque

def is_valid_move(x, y, rows, cols, grid_map, visited, current_value):
    # A move is valid if it's within the grid bounds, the cell has not been visited,
    # and the value of the cell is at most one greater than the current value.
    return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid_map[x][y] <= current_value + 1

def bfs_shortest_path(starts, goal, grid_map):
    # BFS function modified to accept multiple starting points
    rows, cols = len(grid_map), len(grid_map[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, 0) for start in starts])  # Initialize the queue with all starting points

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == goal:
            return dist  # Return the distance when the goal is reached

        if visited[x][y]:
            continue

        visited[x][y] = True
        current_value = grid_map[x][y]

        # Check all four directions (up, down, left, right) for valid moves
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, rows, cols, grid_map, visited, current_value):
                queue.append(((nx, ny), dist + 1))

    return -1  # Return -1 if the goal is not reachable

def letter_to_number(letter):
    if letter == 'S':
        return -1  # Start position
    elif letter == 'E':
        return 26  # Goal position
    else:
        return ord(letter) - ord('a')  # Convert other letters to numbers


def find_positions(grid_map, value_to_find, type):
    positions = []
    for i, row in enumerate(grid_map):
        for j, value in enumerate(row):
            if type == "goal" and value == value_to_find:
                return (i, j)  # Return the position immediately for goal
            elif type == "start" and value <= value_to_find:
                positions.append((i, j))  # Collect all start positions

    return positions if type == "start" else None


# Read the grid map from the file and convert each letter to its corresponding number
grid_map = []
with open("input.txt", "r") as map:
    for row in map:
        row = list(row.strip())
        grid_row = [letter_to_number(letter) for letter in row]
        grid_map.append(grid_row)

# Find the starting and goal positions in the grid map
starts = find_positions(grid_map, 0, "start")
goal = find_positions(grid_map, 26, "goal")


shortest_path_length = bfs_shortest_path(starts, goal, grid_map)
print(shortest_path_length)
