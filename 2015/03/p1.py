import pyperclip


def pr(s):
    print(s)
    pyperclip.copy(s)


import sys

L = open(sys.argv[1], "r").read()


visits = []
presents = {}
c, r = 0, 0
visits.append((c, r))
for ch in L:
    if ch == ">":
        c += 1
    elif ch == "<":
        c += -1
    elif ch == "^":
        r += -1
    elif ch == "v":
        r += 1
    visits.append((c, r))

luckies = 0
seen = set()
for house in visits:
    if house not in seen:
        luckies += 1
        seen.add(house)

pr(luckies)