import sys

with open(sys.argv[1], "r") as f:
    lines = f.read().split("\n")


C = "23456789TJQKA"


def eval(h):
    d = {}
    for c in h:
        d[c] = h.count(c)
    u = sorted(list(d.values()))
    if max(u) == 5:
        return 7
    if max(u) == 4:
        return 6
    if u[0] == 2 and u[1] == 3:
        return 5
    if max(u) == 3:
        return 4
    if u[-1] == u[-2] == 2:
        return 3
    if max(u) == 2:
        return 2
    return 1


def discr(h1, h2):
    for c1, c2 in zip(h1, h2):
        diff = C.index(c1) - C.index(c2)
        if diff == 0:
            continue
        else:
            return diff


def compare_hands(h1, h2):
    e1, e2 = (eval(x) for x in (h1, h2))
    if e1 == e2:
        return discr(h1, h2)
    else:
        return e1 - e2


# h1, h2 = "T55J5", "KTJJT"
# print(compare_hands(h1, h2))


def compare_hb(hb1, hb2):
    return compare_hands(hb1[0], hb2[0])


D = []
for line in lines:
    u = line.split()
    D.append((u[0], int(u[1])))

import functools

D.sort(key=functools.cmp_to_key(compare_hb))
S = 0
for i in range(len(D)):
    j = i + 1
    S += j * D[i][1]

print(S)
