import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


D = open(sys.argv[1], "r").read().split(",")

D = list(map(lambda x: x.strip(), D))


N, E, W, S = (-1, 0), (0, 1), (0, -1), (1, 0)


def compute_direction(current, cmd):
    return {
        N: {"L": W, "R": E},
        E: {"L": N, "R": S},
        W: {"L": S, "R": N},
        S: {"L": E, "R": W},
    }[current][cmd]


def add(u, v):
    return u[0] + v[0], u[1] + v[1]


def mul(u, n):
    return n * u[0], n * u[1]


def travel_to_pos(src, mov):
    """
    Returns all positions from src to add(src, mov)
    """
    u = []
    if mov[0] == 0:  # E or W
        n = mov[1]
        sign = n // abs(n)
        for i in range(abs(n)):
            u.append(add(src, mul((0, sign), i + 1)))
    else:
        n = mov[0]
        sign = n // abs(n)
        for i in range(abs(n)):
            u.append(add(src, mul((sign, 0), i + 1)))
    return u


pos = 0, 0
to_direction = N
positions = []
for instr in D:
    cmd = instr[0]
    n = int(instr[1:])
    to_direction = compute_direction(to_direction, cmd)
    mov = mul(to_direction, n)

    new_positions = travel_to_pos(pos, mov)
    already_visited = False
    for np in new_positions:
        pos = np
        if pos in positions:
            already_visited = True
            break
        else:
            positions.append(pos)
    if already_visited:
        break

pr(sum([abs(x) for x in pos]))
