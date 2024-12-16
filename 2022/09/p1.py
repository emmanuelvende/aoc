import sys


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# Append new line at end of input:
lines[-1] += "\n"

# convention : move = (delta_row, delta_col)


def parse_line_to_move(text):
    direction = text[0]
    quantity = int(text[2:])
    MOVES = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    return MOVES[direction], quantity


def compute_new_head_pos(head, move):
    return tuple(head[i] + move[i] for i in range(2))


def compute_new_tail_pos_from_head(head, tail):
    drow, dcol = (head[i] - tail[i] for i in range(2))
    if abs(drow) <= 1 and abs(dcol) <= 1:
        new_tail = tail
    elif abs(drow) >= 2 and abs(dcol) >= 2:
        new_tail_row = head[0] - 1 if drow > 0 else head[0] + 1
        new_tail_col = head[1] - 1 if dcol > 0 else head[1] + 1
        new_tail = new_tail_row, new_tail_col
    elif abs(drow) >= 2:
        new_tail_row = head[0] - 1 if drow > 0 else head[0] + 1
        new_tail_col = head[1]
        new_tail = new_tail_row, new_tail_col
    elif abs(dcol) >= 2:
        new_tail_row = head[0]
        new_tail_col = head[1] - 1 if dcol > 0 else head[1] + 1
        new_tail = new_tail_row, new_tail_col
    return new_tail
    

head = (0, 0)
tail = (0, 0)
tail_positions = set()
tail_positions.add(tail)
for line in lines:
    u, n = parse_line_to_move(line[:-1])
    for _ in range(n):
        head = compute_new_head_pos(head, u)
        tail = compute_new_tail_pos_from_head(head, tail)
        tail_positions.add(tail)
print(len(tail_positions))