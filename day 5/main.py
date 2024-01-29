storage = []
storage_created = 0
storage_moved = 0


def make_storage(line):
    #Replace first empty space
    line.replace(" ", "", 1)
    #Check if line is part of storage
    if line != "" and "1" not in line:
        for char in range(len(line)):
            # check if the char is not empty and add it to correct storage
            if line[char] != " ":
                index = int(char-char/2)
                add_to_sublist(storage, index, line[char])
        return 0
    else:
        return 1

def add_to_sublist(storage, index, element):
    # Extend the list with empty sublists if necessary
    while len(storage) <= index:
        storage.append([])

    # Add the element to the specified sublist
    storage[index].append(element)



with open("input.txt", "r") as lines:
    for line in lines:
        # Clean Lines
        line = line.rstrip().replace("[", " ").replace("]", " ").replace("   ", " ")
        # Create a storage
        if storage_created == 0:
            storage_created = make_storage(line)
        #Get the number what to move where
        elif "move" in line:
            print(storage)
            numbers = line.split()
            amount = int(numbers[1])
            move_from = int(numbers[3])
            move_to = int(numbers[5])


            #Move the elements (for part 2: change 0 in the last in for i
            for i in range(amount):
                # [move_from-1] to adjust to 0 index
                element = storage[move_from-1].pop(0)
                storage[move_to-1].insert(0, element)




    print(''.join(storage[i][0] for i in range(len(storage)) if storage[i]))
