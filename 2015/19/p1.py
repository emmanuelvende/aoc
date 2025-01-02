import sys
import pyperclip
import re


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

MOLECULE = L[-1]

D = []
for line in L[:-2]:
    lf, rg = line.split("=>")
    lf, rg = lf.strip(), rg.strip()
    D.append((lf, rg))


def sub(s, pattern, what):
    u = []
    for m in re.finditer(pattern, s):
        u.append(s[: m.start()] + what + s[m.end() :])
    return u


R = set()
for pattern, what in D:
    for molecule in sub(MOLECULE, pattern, what):
        R.add(molecule)

pr(len(R))
