import re
import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


W, H = len(lines[0]), len(lines)
map_of_chars = "".join(lines)


def get_char(col, row):
    i = row * W + col
    return map_of_chars[i]


def get_adjacents_positions(c, r):
    pp = []
    for p in (
        (c - 1, r - 1),
        (c, r - 1),
        (c + 1, r - 1),
        (c - 1, r),
        (c + 1, r),
        (c - 1, r + 1),
        (c, r + 1),
        (c + 1, r + 1),
    ):
        if 0 <= p[0] < W and 0 <= p[1] < H:
            pp.append(p)
    return pp


def is_to_count(positions):
    countable = False
    for p in positions:
        for adj_pos in get_adjacents_positions(*p):
            c = get_char(*adj_pos)
            countable = countable or (not (c.isdigit() or c == "."))
    return countable


nbs_to_count = []
for row, line in enumerate(lines):
    for m in re.finditer("\d+", line):
        positions = []
        for c in range(m.start(), m.end()):
            positions.append((c, row))
        if is_to_count(positions):
            nb = int(m.group())
            nbs_to_count.append(nb)

print(sum(nbs_to_count))
