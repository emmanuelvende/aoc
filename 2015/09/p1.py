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
    left, dist = line.split('=')
    dist = int(dist)
    src, _, dst = left.split()
    if src not in D:
        D[src] = {}
    D[src][dst] = dist
    nodes.add(src)
    nodes.add(dst)

print(nodes)
print(D)


P = list(itertools.permutations(nodes))
print(len(P))