from collections import Counter

def find_outside_range(sensor_x, sensor_y, manhattan_distance):
    half_width = 0
    coords_to_add = set()
    outline_coords = []

    for y in range(sensor_y - manhattan_distance - 1, sensor_y + manhattan_distance + 2):
        coords_to_add.update((x, y) for x in [sensor_x - half_width, sensor_x + half_width] if 0 < x <= 4000000 and 0 < y <= 4000000)

        if y < sensor_y:
            half_width += 1
        else:
            half_width -= 1

    outline_coords.extend(coords_to_add)
    print(sensor_x, sensor_y)
    return outline_coords

outline_coords = []
devices_coords = []

with open("input.txt", 'r') as data:
    for line in data:
        # Extract sensor and beacon coordinates from the line
        sensor_x = int(line.strip().split("at x=")[1].split(", y=")[0])
        sensor_y = int(line.strip().split(", y=")[1].split(":")[0])
        beacon_x = int(line.strip().split("is at x=")[1].split(", y=")[0])
        beacon_y = int(line.strip().split("beacon")[1].split(", y=")[1])

        devices_coords.append([sensor_x, sensor_y])
        devices_coords.append([beacon_x, beacon_y])

        manhattan_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        outline_coords.extend(find_outside_range(sensor_x, sensor_y, manhattan_distance))

# Flatten the list of coordinates
flat_coordinates = [tuple(coord) for coord in outline_coords]

# Use Counter to count occurrences of each coordinate
coord_counter = Counter(flat_coordinates)

# Find the most common coordinate
if coord_counter:
    most_common_coordinate = coord_counter.most_common(1)[0][0]
    print("Most common coordinate:", most_common_coordinate[0])

print(most_common_coordinate[0] * 4000000 + most_common_coordinate[1])


