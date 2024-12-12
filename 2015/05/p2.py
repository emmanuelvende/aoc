import sys
import re
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")


def cond2(s):
    m = re.search(r"(\w)\w\1", s)
    return bool(m)


def cond1(s):
    m = re.search(r"(\w\w)\w*\1", s)
    return bool(m)


counter = 0
for s in L:
    nice = cond1(s) and cond2(s)
    if nice:
        counter += 1

pr(counter)
