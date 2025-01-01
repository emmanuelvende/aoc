import sys
import pyperclip
import copy

def pr(x):
    print(x)
    pyperclip.copy(x)


G = open(sys.argv[1], "r").read().split("\n")

# for line in G:
#     print(line)


def nb_on(l, c, grid):
    poss = [
        (c - 1, l - 1),
        (c, l - 1),
        (c + 1, l - 1),
        (c - 1, l),
        (c + 1, l),
        (c - 1, l + 1),
        (c, l + 1),
        (c + 1, l + 1),
    ]
    nb = 0
    for col, lin in poss:
        if 0 <= lin <= len(grid) - 1 and 0 <= col <= len(grid[0]) - 1:
            character = grid[lin][col]
            if character == "#":
                nb += 1
    return nb


def compute_next_grid(grid):
    newgrid = []
    for l, line in enumerate(grid):
        newline = ""
        for c, x in enumerate(line):
            n = nb_on(l, c, grid)
            if x == "#":
                if 2 <= n <= 3:
                    newline += "#"
                else:
                    newline += "."
            else:
                if n == 3:
                    newline += "#"
                else:
                    newline += "."
        newgrid.append(newline)

    return newgrid

def count_on(grid):
    nb = 0
    for line in grid:
        for char in line:
            nb += 1 if char == "#" else 0
    return nb

# print()
N = copy.deepcopy(G)
for i in range(100):
    N = compute_next_grid(N)

# for line in N:
#     print(line)

r = count_on(N)

pr(r)
