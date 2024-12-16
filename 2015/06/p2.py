import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


LEDS = [[0 for c in range(1000)] for l in range(1000)]


def f(start_pos, end_pos, val=None):
    c_s, l_s = start_pos
    c_e, l_e = end_pos
    for l in range(l_s, l_e + 1):
        for c in range(c_s, c_e + 1):
            v = LEDS[l][c]
            w = v + val
            LEDS[l][c] = 0 if w < 0 else w


CMDS = open(sys.argv[1], "r").read().split("\n")
for cmd in CMDS:
    tokens = cmd.split()
    start_token = tokens[-3]
    end_token = tokens[-1]
    start_pos = tuple(int(x) for x in start_token.split(","))
    end_pos = tuple(int(x) for x in end_token.split(","))
    if cmd.startswith("toggle"):
        f(start_pos, end_pos, val=2)
    elif cmd.startswith("turn on"):
        f(start_pos, end_pos, val=1)
    elif cmd.startswith("turn off"):
        f(start_pos, end_pos, val=-1)

res = 0
for l in range(1000):
    for c in range(1000):
        res += LEDS[l][c]

pr(res)
