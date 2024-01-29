current_directory = ""
file_system = {"/": {}}
last_command_was_ls = False
total_sizes = 0
def add_item_to_system(riadok, current_directory):
    global file_system
    parts = current_directory.strip("/").split("/")
    current_location = file_system["/"]  # Start from the root directory

    # Navigate to the current directory in file_system
    for part in parts:
        if part:
            current_location = current_location.setdefault(part, {})

    if riadok.startswith("dir "):
        dir_name = riadok[4:]
        current_location[dir_name] = current_location.get(dir_name, {})
    else:
        file = riadok.split()
        file_size = int(file[0])
        file_name = file[1]
        current_location[file_name] = file_size


def move_level_up(current_directory):
    # Split the path into parts
    parts = current_directory.strip("/").split("/")

    # Remove the last part to move one level up
    if len(parts) > 1:
        # More than one level deep
        new_path = "/".join(parts[:-1])
    else:
        # Already at the top level or only one level deep
        new_path = "/"
    return new_path

def execute_command(riadok):
    global current_directory

    command = riadok[2:4]
    if command == "cd":
        directory = riadok[5:]
        if directory == "..":
            # Move one level up
            current_directory = move_level_up(current_directory)
        elif directory == "/":
            # Go to the root directory
            current_directory = "/"
        else:
            # Move down into a specific directory
            if current_directory == "/":
                # If at root, don't add an extra '/'
                current_directory += directory
            else:
                # Otherwise, add '/' before appending the directory
                current_directory += "/" + directory
        return False
    elif command == "ls":
        return True

with open("input.txt", "r") as data:
    for line in data:
        riadok = line.strip()
        if riadok.startswith("$"):
            last_command_was_ls = execute_command(riadok)
        elif last_command_was_ls:
            add_item_to_system(riadok, current_directory)


def calculate_directory_size(directory):
    total_size = 0
    for item, content in directory.items():
        if isinstance(content, dict):
            # It's a subdirectory, so calculate its size recursively
            subdirectory_size = calculate_directory_size(content)
            total_size += subdirectory_size
            # Check size of each subdirectory against the threshold
            if subdirectory_size <= 100000:
                global total_sizes
                total_sizes += subdirectory_size
        else:
            # It's a file, so add its size
            total_size += content
    return total_size

# Reset total_sizes to 0
total_sizes = 0

# Calculate the total size for each directory in file_system
for dir_name, contents in file_system.items():
    if isinstance(contents, dict):
        size = calculate_directory_size(contents)
        # Check size of top-level directory against the threshold
        if size <= 100000:
            total_sizes += size

print("Total size of all directories smaller than 100k:", total_sizes)


