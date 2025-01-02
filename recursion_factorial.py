import sys

sys.setrecursionlimit(1_000_000)


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


pr(recf(1000))
