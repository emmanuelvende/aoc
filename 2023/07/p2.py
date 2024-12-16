import sys
import functools

with open(sys.argv[1], "r") as f:
    lines = f.read().split("\n")


C = "J23456789TQKA"

FIVE = 7
FOUR = 6
FULL = 5
THRE = 4
TWOP = 3
ONEP = 2
CARD = 1


def eval(h):
    d = {}
    for c in h:
        d[c] = h.count(c)
    u = sorted(list(d.values()))
    j = d.get("J", 0)
    if u == [5]:
        return FIVE
    if u == [1, 4]:
        if j:
            return FIVE
        return FOUR
    if u == [2, 3]:
        if j:
            return FIVE
        return FULL
    if u == [1, 1, 3]:
        if j:
            return FOUR
        return THRE
    if u == [1, 2, 2]:
        if j:
            if j == 2:
                return FOUR
            if j == 1:
                return FULL
        return TWOP
    if u == [1, 1, 1, 2]:
        if j:
            return THRE
        return ONEP
    if u == [1, 1, 1, 1, 1]:
        if j:
            return ONEP
        else:
            return CARD
    assert(False)


def discr(h1, h2):
    for c1, c2 in zip(h1, h2):
        diff = C.index(c1) - C.index(c2)
        if diff == 0:
            continue
        else:
            # print(f"{diff=}")
            return diff


def compare_hands(h1, h2):
    # print(h1, h2)
    e1, e2 = (eval(x) for x in (h1, h2))
    # print(e1, e2)
    if e1 == e2:
        return discr(h1, h2)
    else:
        return e1 - e2


# h1, h2 = "T55J5", "KTJJT"
# print(compare_hands(h1, h2))

# u = ["T55J5", "KTJJT", "QQQJA", "JJJJA"]
# u.sort(key=functools.cmp_to_key(compare_hands))
# print(u)
# exit()


def compare_hb(hb1, hb2):
    return compare_hands(hb1[0], hb2[0])


D = []
for line in lines:
    u = line.split()
    D.append((u[0], int(u[1])))

D.sort(key=functools.cmp_to_key(compare_hb))
S = 0
for i in range(len(D)):
    j = i + 1
    S += j * D[i][1]

print(S)
