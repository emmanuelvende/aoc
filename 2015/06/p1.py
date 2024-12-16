import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


LEDS = [[0 for c in range(1000)] for l in range(1000)]


def manage_leds(start_pos, end_pos, val=None):
    c_start, l_start = start_pos
    c_end, l_end = end_pos
    for l in range(l_start, l_end + 1):
        for c in range(c_start, c_end + 1):
            if val == None:
                v = LEDS[l][c]
                LEDS[l][c] = 0 if v == 1 else 1
            else:
                LEDS[l][c] = val


CMDS = open(sys.argv[1], "r").read().split("\n")
for cmd in CMDS:
    tokens = cmd.split()
    start_token = tokens[-3]
    end_token = tokens[-1]
    start_pos = tuple(int(x) for x in start_token.split(","))
    end_pos = tuple(int(x) for x in end_token.split(","))
    if cmd.startswith("toggle"):
        manage_leds(start_pos, end_pos)
    elif cmd.startswith("turn on"):
        manage_leds(start_pos, end_pos, val=1)
    elif cmd.startswith("turn off"):
        manage_leds(start_pos, end_pos, val=0)

res = 0
for l in range(1000):
    for c in range(1000):
        if LEDS[l][c] == 1:
            res += 1

pr(res)
