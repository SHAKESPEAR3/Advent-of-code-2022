position = -1
register_x = 1
CRT_image = []


def check_timing():
    global position, register_x, CRT_image

    # Reset position at the start of a new line
    if len(CRT_image) % 40 == 0:
        position = 0

    # Determine whether to add a dot or a hash based on the distance from register_x
    if abs(position - register_x) > 1:
        CRT_image.append(".")
    else:
        CRT_image.append("#")


def execute(command):
    global register_x, position, CRT_image

    # Process commands
    if command[0] == "addx":
        # Extract the value
        value = int(command[1])
        # Update position twice
        position += 1
        check_timing()
        position += 1
        check_timing()
        # Update register_x based on the command value
        register_x += value

    elif command[0] == "noop":
        # Increment position for noop command
        position += 1
        check_timing()


def print_crt_image(crt_image):
    # Convert the CRT_image list to a single string
    crt_image_str = ''.join(crt_image)
    # Split the string into lines of 40 characters each
    lines = [crt_image_str[i:i + 40] for i in range(0, len(crt_image_str), 40)]
    # Print each of the first 6 lines
    for line in lines[:6]:
        print(line)


# Read commands from file and execute them
with open("input.txt", "r") as data:
    for row in data:
        command = row.strip().split(" ")
        execute(command)


print_crt_image(CRT_image)