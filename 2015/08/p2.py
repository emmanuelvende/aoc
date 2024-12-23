import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

r = 0
for line in L:
    count = 0
    for x in line[1:-1]:
        if x == "\\" or x == '"':
            count += 2
        else:
            count += 1
    count += 4  # beginning and ending '"' characters
    s = line[1:-1]
    r += count - len(s)

pr(r)
