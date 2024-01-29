import math

def clean_monkeys_data(monkeys):
    global clean_monkeys
    for monkey in monkeys:
        monkey_data = {
            'number': monkey[0].split()[1][:-1],
            'items': [int(x) for x in monkey[1].split(":")[1].strip().split(",")]
        }

        # Parse the operation
        operation_parts = monkey[2].split("=")[1].strip().split()
        operator = operation_parts[1]
        operation_number = operation_parts[2] if operation_parts[2] != "old" else "old"
        if operation_number != "old":
            operation_number = int(operation_number)
        monkey_data['operation'] = (operator, operation_number)

        monkey_data['test'] = int(monkey[3].split("by ")[1])
        monkey_data['true_test'] = int(monkey[4].split("monkey ")[1])
        monkey_data['false_test'] = int(monkey[5].split("monkey ")[1])
        monkey_data['inspect_count'] = 0  # Initialize inspect count

        clean_monkeys.append(monkey_data)


def monkey_inspect(clean_monkeys):
    for round in range(10000):
        for monkey in clean_monkeys:
            current_items = monkey['items'].copy()
            for item in current_items:
                monkey['inspect_count'] += 1  # Increment inspect count

                operator, operation_number = monkey['operation']

                # Perform the operation
                if operator == "+":
                    worry_level = item + operation_number
                elif operator == "*":
                    worry_level = item * (operation_number if operation_number != "old" else item)

                worry_level %= common_multiple()

                # Decide which monkey to pass to based on the test
                if worry_level % monkey['test'] == 0:
                    target_monkey = monkey['true_test']
                else:
                    target_monkey = monkey['false_test']

                worry_level = worry_level % common_multiple()

                # Find the target monkey and append the worry level
                for target in clean_monkeys:
                    if target['number'] == str(target_monkey):
                        target['items'].append(worry_level)
                        break

                monkey['items'].remove(item)

def common_multiple():
    numbers = []
    for mnky in clean_monkeys:
        numbers.append(mnky['test'])

    result = math.lcm(*numbers)
    return result


clean_monkeys = []
monkeys = []
with open("input.txt", "r") as data:
    monkey = []
    for line in data:
        if line.strip():
            monkey.append(line.strip())
        else:
            if monkey:
                monkeys.append(monkey)
                monkey = []
    if monkey:
        monkeys.append(monkey)


clean_monkeys_data(monkeys)
monkey_inspect(clean_monkeys)

# Print the results
inspect_times = []
for monkey in clean_monkeys:
    inspect_times.append(monkey['inspect_count'])

inspect_times.sort(reverse=True)
print(inspect_times[0] * inspect_times[1])
