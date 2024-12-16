def compute_priority(letter):
    if letter.upper() == letter:
        return ord(letter) - 38
    else:
        return ord(letter) - 96


with open("input.txt", "r") as f:
    lines = f.readlines()

N = 3
lists_of_3_lines = [lines[n : n + N] for n in range(0, len(lines), N)]


def find_badge(line_a, line_b, line_c):
    item = ""
    for x in line_a:
        if (x in line_b) and (x in line_c):
            item = x
            break
    return item


total = 0
for list_of_3_lines in lists_of_3_lines:
    badge = find_badge(*list_of_3_lines)
    score = compute_priority(badge)
    total += score

print(total)
