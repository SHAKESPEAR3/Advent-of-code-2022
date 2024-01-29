head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
tail = 10*[[0,0]]
tail_positions = set()  # Set to store unique tail positions


def is_head_tail_adjacent(n):
    global head_x, head_y, x, tail_y
    # Check if the head and tail are more than 1 unit apart.
    if n < len(tail):
        return abs(tail[n-1][0] - tail[n][0]) > 1 or abs(tail[n-1][1] - tail[n][1]) > 1


def move_tail():
    global tail_x, tail_y, head_x, head_y, tail_positions

    # Move tail only if head and tail are not adjacent
    for n in range(1, len(tail)):
        if is_head_tail_adjacent(n):
            # The tail segment moves towards the previous segment's position
            tail_x, tail_y = tail[n]

            # Move horizontally closer if needed
            if tail[n - 1][0] > tail_x:
                tail_x += 1
            elif tail[n - 1][0] < tail_x:
                tail_x -= 1

            # Move vertically closer if needed
            if tail[n - 1][1] > tail_y:
                tail_y += 1
            elif tail[n - 1][1] < tail_y:
                tail_y -= 1

            # Update the segment's position
            tail[n] = [tail_x, tail_y]

            if n == len(tail) - 1:
                tail_positions.add((tail_x, tail_y))


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

        if tail:
            tail[0] = [head_x, head_y]
        else:
            tail.append([head_x, head_y])

        move_tail()  # Move tail after the head moves


# Read movements from file and execute
with open("input.txt", "r") as rows:
    for row in rows:
        movement = row.strip().replace(" ", "")
        direction = movement[0]
        steps = int(movement[1:])
        move_head(direction, steps)

# Add 1 for the initial 0:0 position
print(f"total {len(tail_positions) + 1}")

