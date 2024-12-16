import sys

with open(sys.argv[1], "r") as f:
    data = f.read()

patterns = data.split("\n\n")


def detect_sym(rows):
    for i in range(1, len(rows)):
        before = rows[:i]
        after = rows[i:]

        before = before[::-1]

        before = before[: len(after)]
        after = after[: len(before)]

        if after == before:
            return i


total = 0
for i, pattern in enumerate(patterns):
    rows = pattern.split("\n")
    sym = detect_sym(rows)
    if sym:
        total += sym * 100
    else:
        sym = detect_sym(list(zip(*rows)))
        total += sym

print(total)
