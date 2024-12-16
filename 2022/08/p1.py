import sys


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# Append new line at end of input:
lines[-1] += "\n"

rows = []
for line in lines:
    input_line = line[:-1]
    row = [int(x) for x in input_line]
    rows.append(row)
a = len(rows)


def is_visible(x, first_trees, edge):
    if len(first_trees) == 0:
        return x > edge
    else:
        return x > edge and max(first_trees) < x


def get_column_from_up(rows, col):
    return [row[col] for row in rows]


def get_column_from_down(rows, col):
    column = [row[col] for row in rows]
    return list(reversed(column))


def get_row_from_left(rows, row):
    return rows[row]


def get_row_from_right(rows, row):
    return list(reversed(rows[row]))


# print("=== TEST === get_column_from_up")
# for i in range(a):
#     print(f"{i=} --> {get_column_from_up(rows, col=i)=}")

# print("=== TEST === get_column_from_down")
# for i in range(a):
#     print(f"{i=} --> {get_column_from_down(rows, col=i)=}")

# print("=== TEST === get_row_from_left")
# for i in range(a):
#     print(f"{i=} --> {get_row_from_left(rows, row=i)=}")

# print("=== TEST === get_row_from_right")
# for i in range(a):
#     print(f"{i=} --> {get_row_from_right(rows, row=i)=}")


def compute_visible_trees(trees):
    ranks = []

    for i, x in enumerate(trees[1:]):
        if x > max(trees[: i + 1]):
            ranks.append(i + 1)
    return ranks


def detect_from_top(rows, col_index):
    trees = get_column_from_up(rows, col_index)
    return compute_visible_trees(trees)


def detect_from_down(rows, col_index):
    trees = get_column_from_down(rows, col_index)
    return compute_visible_trees(trees)


def detect_from_left(rows, row_index):
    trees = get_row_from_left(rows, row_index)
    return compute_visible_trees(trees)


def detect_from_right(rows, row_index):
    trees = get_row_from_right(rows, row_index)
    return compute_visible_trees(trees)


nb_edge_trees = 4 * (a - 1)


detected_trees = set()

for i in range(a):
    detected_trees.add((i, 0))
    detected_trees.add((i, a - 1))
    detected_trees.add((0, i))
    detected_trees.add((a - 1, i))
print(f"nb of edge trees : {len(detected_trees)}")


for col_index in range(a):
    ranks = detect_from_top(rows, col_index)

    for rank in ranks:
        col, row = col_index, rank
        detected_trees.add((col, row))


for col_index in range(a):
    ranks = detect_from_down(rows, col_index)

    for rank in ranks:
        col, row = col_index, a - 1 - rank
        detected_trees.add((col, row))


for row_index in range(a):
    ranks = detect_from_right(rows, row_index)
    for rank in ranks:
        col, row = a - 1 - rank, row_index
        detected_trees.add((col, row))


for row_index in range(a):
    ranks = detect_from_left(rows, row_index)
    for rank in ranks:
        col, row = rank, row_index
        detected_trees.add((col, row))


print(f"{len(detected_trees)=}")
