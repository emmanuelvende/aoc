import re


def move(n, a, b):
    """
    Elements are now moved by group.
    a and b aren't modifed in place => return them :)
    """
    x = a[:n]
    a = a[n:]
    b = x + b
    return a, b


def get_command_parameters(s):
    """
    Apply regex to command line "move n from a to b" and returns n, a, b
    """
    m = re.search(r"move (?P<n>\d+) from (?P<a>\d+) to (?P<b>\d+)", s)
    return int(m.group("n")), int(m.group("a")), int(m.group("b"))


def analyze_input_file(filename):
    """
    Analyze input.txt and return the list of crates lines and the list of commands lines
    """
    with open(filename) as f:
        lines = f.readlines()

    empty_line_index = lines.index("\n")
    crates_lines = lines[:empty_line_index]
    commands_lines = lines[empty_line_index+1:]
    return crates_lines, commands_lines


def initialize_crates(crates_lines):
    """
    Each column of crates is represented by a list
    Returns a list of 9 lists
    """
    # Remove the last line containing the columns numbers:
    crates_lines = crates_lines[:-1]

    CHARS_COL_INDEXES = list(range(1, 34, 4))

    crates = [[] for _ in range(9)]

    for crate_line in crates_lines:
        for index_crate, col_index in enumerate(CHARS_COL_INDEXES):
            char = crate_line[col_index]
            if char != " ":
                crates[index_crate].append(crate_line[col_index])
    return crates


def apply_command(command_line):
    """
    Notice that now, "move" function does not modify in place lists anymore.
    """
    n, a, b = get_command_parameters(command_line)
    crates[a - 1], crates[b - 1] = move(n, crates[a - 1], crates[b - 1])


crates_lines, commands_lines = analyze_input_file("input.txt")
crates = initialize_crates(crates_lines)
# print("START")
# for crate in crates:
#     print(crate)

for command_line in commands_lines:
    apply_command(command_line)

# print("END")
# for crate in crates:
#     print(crate)

answer = ""
for crate in crates:
    answer += crate[0]
print(answer)
