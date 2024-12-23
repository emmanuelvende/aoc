import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

r = 0
for line in L:
    s = line[1:-1].encode().decode("unicode_escape")
    r += len(line) - len(s)

pr(r)
