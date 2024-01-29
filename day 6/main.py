def find_mark(code):
    mark = code[:15]

    for letter in code[15:]:
        if len(mark[-14:]) == len(set(mark[-14:])):
            print(len(mark))
            break
        else:
            mark += letter

with open("input.txt", "r") as line:
    code = line.readline()
    find_mark(code)