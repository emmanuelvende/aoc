import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


D = open(sys.argv[1], "r").read().split(",")

D = list(map(lambda x: x.strip(), D))

# print(D)

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


pos = 0, 0
to = N
for instr in D:
    cmd = instr[0]
    n = int(instr[1:])
    to = compute_direction(to, cmd)
    mov = mul(to, n)
    pos = add(pos, mov)


pr(sum([abs(x) for x in pos]))
