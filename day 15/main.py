def save_no_beacon_zone(grid, sensor_x,  sensor_y, distance, target_row):
    # Initialize the half_width variable for adjusting the search area
    half_width = 0

    # Loop through the y-axis within the specified distance from the sensor
    for y in range(sensor_y - distance, sensor_y + distance + 1):
        # If the current y-coordinate matches the target row
        if y == target_row:
            # Loop through the x-axis within the adjusted width from the sensor
            for x in range(sensor_x - half_width, sensor_x + half_width + 1):
                # Add the x-coordinate to the grid representing the no-beacon zone
                grid.add(x)

        # Adjust half_width based on the y-coordinate position relative to the sensor
        if y < sensor_y:
            half_width += 1
        else:
            half_width -= 1


def solve(target_row):
    # Initialize sets to track overlapping coordinates
    not_beacon = set()
    devices_on_target_row = set()

    with open("input.txt", 'r') as data:
        for line in data:
            # Extract sensor and beacon coordinates from the line
            sensor_x = int(line.strip().split("at x=")[1].split(", y=")[0])
            sensor_y = int(line.strip().split(", y=")[1].split(":")[0])
            beacon_x = int(line.strip().split("is at x=")[1].split(", y=")[0])
            beacon_y = int(line.strip().split("beacon")[1].split(", y=")[1])

            # Check if the sensor or beacon is on the target row
            if sensor_y == target_row:
                devices_on_target_row.add(sensor_x)
            if beacon_y == target_row:
                devices_on_target_row.add(beacon_x)

            # Calculate Manhattan distance between sensor and beacon
            manhattan_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

            # Check if the target row is within the range of the Manhattan distance
            if target_row in range(sensor_y - manhattan_distance, sensor_y + manhattan_distance):
                # Save the no-beacon zone for the current line
                save_no_beacon_zone(not_beacon, sensor_x, sensor_y, manhattan_distance, target_row)

        # Print the number of coordinates in the no-beacon zone after removing device overlaps
        print(len(not_beacon - devices_on_target_row))


# Call the solve function with the specified y_index
solve(2000000)
