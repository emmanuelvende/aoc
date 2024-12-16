"""
Implementation using a double ended queue to store the visitable positions.

Classical BSF problem (https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)
"""

import sys
import collections

with open(sys.argv[1], "r") as f:
    input_ = f.read()


MAP = input_.split("\n")
# print(the_map)
H = len(MAP)
W = len(MAP[0])
print(f"{H=}, {W=}")

# All positions in map are (r, c)


def find_char(char):
    for r, row in enumerate(MAP):
        c = row.find(char)
        if c != -1:
            break
    return r, c


START_POS = find_char("S")
END_POS = find_char("E")

print(f"{START_POS=}, {END_POS=}")

# DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1), ".": (0, 0)}
DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def get_altitude(pos):
    if pos == START_POS:
        return ord("a")
    elif pos == END_POS:
        return ord("z")
    else:
        return ord(MAP[pos[0]][pos[1]])


def move(pos_, mov):
    return tuple([pos_[i] + mov[i] for i in range(2)])


def is_in_map(pos_):
    return 0 <= pos_[0] < H and 0 <= pos_[1] < W


# print(f"{is_in_map((0, 0))=}")


def can_move_from_pos_in_direction(pos_, dir_):
    """dir_ and pos are (x, y)"""
    new_pos = move(pos_, dir_)
    yes_i_can = is_in_map(new_pos) and get_altitude(new_pos) - get_altitude(pos_) <= 1
    return yes_i_can


positions_and_ranks = (
    collections.deque()
)  # double ended queue of (position, rank) tuples

for r in range(H):
    for c in range(W):
        pos = r, c
        if get_altitude(pos) == ord("a"):
            positions_and_ranks.append((pos, 0))


def compute_best_path():
    visited_positions = set()
    while positions_and_ranks:
        # print(f"{positions_and_ranks=}")
        pos, rank = positions_and_ranks.popleft()
        if pos in visited_positions:
            # print(f"{pos=} has been visited")
            continue
        # else:
        #     print(f"new position to visit : {pos=}")
        visited_positions.add(pos)
        if pos == END_POS:
            return rank
        for direction in DIRS.values():
            if can_move_from_pos_in_direction(pos, direction):
                new_pos = move(pos, direction)
                positions_and_ranks.append((new_pos, rank + 1))


print(compute_best_path())
