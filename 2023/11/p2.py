import sys
from itertools import combinations

with open(sys.argv[1], "r") as f:
    data = f.read()

G = [line for line in data.split("\n")]


# def print_g(g):
#     for row in g:
#         print(row)


def transpose(g):
    return ["".join([c for c in line]) for line in zip(*g)]


# G = expand_lines(G)

# G = transpose(expand_lines(transpose(G)))


LOCS = []  # (col, row)
for row, line in enumerate(G):
    for col, char in enumerate(line):
        if char == "#":
            LOCS.append((col, row))


L_W = [not "#" in line for line in G]
C_W = [not "#" in line for line in transpose(G)]


def dist(a, b):
    C = 1000000
    h = abs(b[1] - a[1])
    n = len(list(filter(None, L_W[min(a[1], b[1]) : max(a[1], b[1])])))
    # h + n*(C-1)
    w = abs(b[0] - a[0])
    p = len(list(filter(None, C_W[min(a[0], b[0]) : max(a[0], b[0])])))
    # w + p*(C-1)
    return h + w + (n + p) * (C - 1)



length = 0
for a, b in combinations(LOCS, 2):
    length += dist(a, b)
print(length)

# print(len(list(combinations(LOCS, 2))))
