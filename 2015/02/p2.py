import pyperclip


def pr(s):
    print(s)
    pyperclip.copy(s)


import sys


def ribbon(l, w, h):
    return l * w * h + min(2 * (l + w), 2 * (l + h), 2 * (w + h))


lines = open(sys.argv[1], "r").read().split("\n")
r = 0
for line in lines:
    u = list(int(x) for x in line.split("x"))
    r += ribbon(*u)

pr(r)
