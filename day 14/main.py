def draw_rocks():
    global grid, rows, columns

    for row_list, col_list in zip(rows, columns):
        for i in range(len(row_list) - 1):
            r_start, r_end = sorted([row_list[i], row_list[i + 1]])
            c_start, c_end = sorted([col_list[i], col_list[i + 1]])

            print(f"Drawing from ({r_start}, {c_start}) to ({r_end}, {c_end})")

            if r_start < len(grid) and c_end < len(grid[0]):
                if r_start == r_end:  # Horizontal line
                    for c in range(c_start, c_end + 1):
                        grid[r_start][c] = "#"
                elif c_start == c_end:  # Vertical line
                    for r in range(r_start, r_end + 1):
                        if r < len(grid):
                            grid[r][c_start] = "#"
            else:
                print(f"Skipping out-of-bound coordinates.")


    for row in grid:
        print(''.join(row))


def draw_grid():
    global grid

    width = get_width()
    height = get_height()

    # Create a grid
    grid = [width * ["."] for _ in range(height)]

    # Print the grid
    for row in grid:
        print(''.join(row))
    print("_________")

    draw_rocks()


def get_rows_and_columns():
    global rows, columns
    rows = []  # Will store column data
    columns = []  # Will store row data

    for row in range(len(data)):
        column_data = []  # This will actually hold row data
        for item in range(len(data[row])):
            column_data.append(int(data[row][item].split(",")[0]))
        columns.append(column_data)

    for row in range(len(data)):
        row_data = []  # This will actually hold column data
        for item in range(len(data[row])):
            row_data.append(int(data[row][item].split(",")[1]))
        rows.append(row_data)


def get_width():
    width_min = 0
    width_max = max(max(map(int, sublist)) for sublist in rows)

    print(width_min, width_max)
    width = width_max - width_min + 1
    return width


def get_height():
    height_min = min(min(map(int, sublist)) for sublist in columns)
    height_max = max(max(map(int, sublist)) for sublist in columns)

    print(height_min, height_max)

    height = height_max - height_min + 1
    return height


def adjust_columns():
    global columns
    width_min = min(min(map(int, sublist)) for sublist in columns)
    adjusted_columns = [[x - width_min for x in column] for column in columns]
    return adjusted_columns


grid = []
rows = []
columns = []
data = []
with open("input.txt", "r") as lines:
    for line in lines:
        data.append(line.strip().split(" -> "))


get_rows_and_columns()
columns = adjust_columns()
print(f"rows{rows}, columns{columns}")
draw_grid()
