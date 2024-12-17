import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


sys.setrecursionlimit(1_000_000)

L = open(sys.argv[1], "r").read().split("\n")

VALS = {}

def recf(x):
    if x in VALS:
        return VALS[x]
    else:
        if x == 0:
            return 1
        else:
            v = x * recf(x - 1)
            VALS[x] = v
            return v

VALS2 = {0:1}

def recf2(x):
    if x in VALS:
        return VALS[x]
    else:
        v = x * recf(x - 1)
        VALS[x] = v
        return v


pr(recf(1000))
pr(recf2(1000))
