import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

SUES = []

for line in L:
    t = line.split(":")
    sue = int(t[0].split()[-1])

    right = "".join(t[1:])
    params = right.split(",")
    things = {}
    for param in params:
        what, howmany = param.split()
        things[what] = int(howmany)

    SUES.append(things)



GOOD_SUE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

REF = {}
for k in GOOD_SUE:
    REF[k] = "good"


def check_sue(sue):
    ref = {}
    for k in GOOD_SUE.keys():
        p = sue.get(k)
        if p == None:
            ref[k] = "good"
        else:
            ref[k] = "good" if GOOD_SUE[k] == sue[k] else "bad"
    return ref == REF


POSSIBLES = []
for index, sue in enumerate(SUES):
    if check_sue(sue):
        POSSIBLES.append(index + 1)

assert len(POSSIBLES) == 1
pr(POSSIBLES[0])
