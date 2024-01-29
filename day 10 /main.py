x = 1
cycle = 1
total_signal_strength = 0
def check_signal_strength():
    global cycle, total_signal_strength

    if cycle in (20, 60, 100, 140, 180, 220):
        signal = cycle * x
        print(cycle, x, signal)
        total_signal_strength += signal


def execute(command):
    global x, cycle

    check_signal_strength()
    cycle += 1

    if command[0] == "addx":
        check_signal_strength()
        cycle += 1

        value = int(command[1])
        x += value


with open("input.txt", "r") as data:
    for row in data:
        command = row.strip().split(" ")
        execute(command)

print(total_signal_strength)