import pyperclip


def pr(s):
    print(s)
    pyperclip.copy(s)


import sys


def area(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, l * h, w * h)


lines = open(sys.argv[1], "r").read().split("\n")
a = 0
for line in lines:
    u = list(int(x) for x in line.split("x"))
    a += area(*u)

pr(a)
