import sys
import pyperclip
import itertools


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

nodes = set()
D = {}

for line in L:
    left, dist = line.split("=")
    dist = int(dist)
    src, _, dst = left.split()
    if src not in D:
        D[src] = {}
    D[src][dst] = dist
    if dst not in D:
        D[dst] = {}
    D[dst][src] = dist
    nodes.add(src)
    nodes.add(dst)


P = list(itertools.permutations(nodes))
r = 0
for p in P:
    r0 = 0
    for i, n in enumerate(p[:-1]):
        m = p[i + 1]
        r0 += D[n][m]
    if r0 > r:
        r = r0

pr(r)
