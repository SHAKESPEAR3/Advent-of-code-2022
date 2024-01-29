head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
tail_positions = set()  # Set to store unique tail positions


def is_head_tail_adjacent():
    global head_x, head_y, x, tail_y
    # Check if the head and tail are more than 1 unit apart.
    return abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1



def move_tail(direction):
    global tail_x, tail_y, head_x, head_y, tail_positions

    head_tail_distance = is_head_tail_adjacent()
    # Move tail only if head and tail are not adjacent
    if head_tail_distance == 1:
        if direction == "R":
            tail_x = head_x - 1
        elif direction == "L":
            tail_x = head_x + 1
        elif direction == "U":
            tail_y = head_y - 1
        elif direction == "D":
            tail_y = head_y + 1

        position = (tail_x, tail_y)
        tail_positions.add(position)


def move_head(direction, steps):
    global head_x, head_y

    for i in range(steps):
        # Update head position based on direction
        if direction == "R":
            head_x += 1
        elif direction == "L":
            head_x -= 1
        elif direction == "U":
            head_y += 1
        elif direction == "D":
            head_y -= 1

        move_tail(direction)  # Move tail after the head moves
        print(f"head {head_x}:{head_y} tail {tail_x}:{tail_y}")


# Read movements from file and execute
with open("input.txt", "r") as rows:
    for row in rows:
        movement = row.strip().replace(" ", "")
        direction = movement[0]
        steps = int(movement[1:])
        move_head(direction, steps)

# Add 1 for the initial 0:0 position
print(f"total {len(tail_positions) + 1}")
