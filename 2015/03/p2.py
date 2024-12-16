import pyperclip


def pr(s):
    print(s)
    pyperclip.copy(s)


import sys

L = open(sys.argv[1], "r").read()


visits = []
presents = {}
c, r = 0, 0
cB, rB = 0, 0
visits.append((c, r))
visits.append((cB, rB))
for i, ch in enumerate(L):
    if i % 2 == 0:
        if ch == ">":
            c += 1
        elif ch == "<":
            c += -1
        elif ch == "^":
            r += -1
        elif ch == "v":
            r += 1
        visits.append((c, r))
    else:
        if ch == ">":
            cB += 1
        elif ch == "<":
            cB += -1
        elif ch == "^":
            rB += -1
        elif ch == "v":
            rB += 1
        visits.append((cB, rB))


luckies = 0
seen = set()
for house in visits:
    if house not in seen:
        luckies += 1
        seen.add(house)

pr(luckies)
