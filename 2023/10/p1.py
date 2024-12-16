import sys
from operator import add

with open(sys.argv[1], "r") as f:
    lines = f.read().split("\n")

WIDTH, H = len(lines[0]), len(lines)

M = "".join(l for l in lines)


def get_char(col, row):
    return M[row * WIDTH + col]


# print(c(1, 1), c(3, 3), c(2, 3), c(1, 3))

N = (0, -1)
S = (0, 1)
W = (-1, 0)
E = (1, 0)
# (col, row)
MOVES = {"|": (N, S), "-": (W, E), "L": (N, E), "J": (N, W), "7": (W, S), "F": (E, S)}

# MOVES["S"] = MOVES["F"]  # test1.txt
# MOVES["S"] = MOVES["F"]  # test2.txt
MOVES["S"] = MOVES["|"]  # input.txt

# print(MOVES)
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == "S":
            start = (col, row)
            break


# print(start)


def compute_neighbours(pos):
    c = get_char(*pos)
    # print(c)
    neighbours = []
    for move in MOVES[c]:
        neighbours.append(tuple(map(add, pos, move)))
    return neighbours


# print(compute_neighbours)

visited = set()


# def dfs(visited, pos):  # pos := (col, row)
#     if pos not in visited:
#         visited.add(pos)
#         neighbours = compute_neighbours(pos)
#         # print(neighbours)
#         for neighbour in neighbours:
#             dfs(visited, neighbour)


def bfs(visited, pos):
    queue = []
    visited.add(pos)
    queue.append(pos)
    while queue:
        s = queue.pop(0)
        for n in compute_neighbours(s):
            if n not in visited:
                visited.add(n)
                queue.append(n)


bfs(visited, start)

print(len(visited) // 2)
