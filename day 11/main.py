def clean_monkeys_data(monkeys):
    global clean_monkeys
    for monkey in monkeys:
        # Extract and format basic monkey data
        monkey_data = {
            'number': monkey[0].split()[1][:-1],  # Monkey's identifier
            'items': [int(x) for x in monkey[1].split(":")[1].strip().split(",")]  # Starting items
        }

        # Parse and store the operation for each monkey
        operation_parts = monkey[2].split("=")[1].strip().split()
        operator = operation_parts[1]  # Operation type (+ or *)
        operation_number = int(operation_parts[2]) if operation_parts[2] != "old" else "old"
        monkey_data['operation'] = (operator, operation_number)

        # Extract and store test and target monkeys for true/false outcomes
        monkey_data['test'] = int(monkey[3].split("by ")[1])
        monkey_data['true_test'] = int(monkey[4].split("monkey ")[1])
        monkey_data['false_test'] = int(monkey[5].split("monkey ")[1])

        # Initialize inspection count for each monkey
        monkey_data['inspect_count'] = 0

        # Append formatted data to the global list
        clean_monkeys.append(monkey_data)


def monkey_inspect(clean_monkeys):
    for round in range(10000):
        # Iterate through each monkey for inspection
        for monkey in clean_monkeys:
            # Create a copy of current items to avoid modifying the list during iteration
            current_items = monkey['items'].copy()

            # Inspect each item in the monkey's possession
            for item in current_items:
                # Increment the inspection counter
                monkey['inspect_count'] += 1

                # Perform the specified operation on the item
                operator, operation_number = monkey['operation']
                if operator == "+":
                    worry_level = item + operation_number
                elif operator == "*":
                    worry_level = item * (operation_number if operation_number != "old" else item)
                worry_level //= 3

                # Determine the target monkey based on the divisibility test
                target_monkey = monkey['true_test'] if worry_level % monkey['test'] == 0 else monkey['false_test']

                # Find the target monkey and pass the worry level
                for target in clean_monkeys:
                    if target['number'] == str(target_monkey):
                        target['items'].append(worry_level)
                        break

                # Remove the inspected item from the current monkey's list
                monkey['items'].remove(item)


# Read and process input data
clean_monkeys = []
monkeys = []
with open("input.txt", "r") as data:
    monkey = []
    # Read each line and group them into individual monkeys' data
    for line in data:
        if line.strip():
            monkey.append(line.strip())
        else:
            if monkey:
                monkeys.append(monkey)
                monkey = []
    if monkey:
        monkeys.append(monkey)

# Clean and inspect monkey data
clean_monkeys_data(monkeys)
monkey_inspect(clean_monkeys)

# Calculate and print the product of the two highest inspection counts
inspect_times = [monkey['inspect_count'] for monkey in clean_monkeys]
inspect_times.sort(reverse=True)
result = inspect_times[0] * inspect_times[1]
print(result)
