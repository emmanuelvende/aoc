import sys
from itertools import combinations

with open(sys.argv[1], "r") as f:
    data = f.read()

G = [line for line in data.split("\n")]


def print_g(g):
    for row in g:
        print(row)


def expand_lines(g):
    h = []
    for line in g:
        h.append(line)
        if not "#" in line:
            h.append(line)
    return h


def transpose(g):
    return ["".join([c for c in line]) for line in zip(*g)]


G = expand_lines(G)

G = transpose(expand_lines(transpose(G)))


LOCS = []  # (col, row)
for row, line in enumerate(G):
    for col, char in enumerate(line):
        if char == "#":
            LOCS.append((col, row))

# for i, g in enumerate(LOCS, start=1):
#     print(i, g)

# 1 (4, 0)
# 2 (9, 1)
# 3 (0, 2)
# 4 (8, 5)
# 5 (1, 6)
# 6 (12, 7)
# 7 (9, 10)
# 8 (0, 11)
# 9 (5, 11)


def dist(a, b):
    h = abs(b[1] - a[1])
    w = abs(b[0] - a[0])
    return h + w


# for k, l in ((5, 9), (1, 7), (3, 6), (8, 9)):
#     i = k - 1
#     j = l - 1
#     print((k, l), dist(LOCS[i], LOCS[j]))

length = 0
for a, b in combinations(LOCS, 2):
    length += dist(a, b)
print(length)

# print(len(list(combinations(LOCS, 2))))