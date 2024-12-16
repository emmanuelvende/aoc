import pyperclip


def pr(s):
    print(s)
    pyperclip.copy(s)


import sys

s = open(sys.argv[1], "r").read()


pos = 0
for i, c in enumerate(s):
    if c == "(":
        pos += 1
    else:
        pos -= 1
    if pos == -1:
        break

pr(i + 1)
