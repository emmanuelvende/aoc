import sys
import pyperclip
import itertools


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

D = {}

for s in L:
    t = s.split()
    a, sign, score, b = t[0], t[2], int(t[3]), t[-1][:-1]
    sign = 1 if sign == "gain" else -1
    if a in D:
        D[a][b] = sign * score
    else:
        D[a] = {b: sign * score}

possibles = itertools.permutations(D.keys())

E = {}
for scenario in possibles:
    current_score = 0
    for i, person in enumerate(scenario[:-1]):
        a = person
        b = scenario[i + 1]
        current_score += D[a][b] + D[b][a]
    a = scenario[-1]
    b = scenario[0]
    current_score += D[a][b] + D[b][a]
    E[scenario] = current_score

r = max(E.values())
pr(r)
