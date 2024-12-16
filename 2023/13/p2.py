import sys

with open(sys.argv[1], "r") as f:
    data = f.read()

patterns = data.split("\n\n")


def detect_sym(rows):
    for i in range(1, len(rows)):
        before = rows[:i]
        after = rows[i:]

        before = before[::-1]

        # Count the number of mismatches character by character and line by line
        s = sum(
            sum(0 if a == b else 1 for a, b in zip(row_x, row_y))
            for row_x, row_y in zip(before, after)
        )

        # If there's strictly 1 mismatch then we are at the reflecting row
        if s == 1:
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
