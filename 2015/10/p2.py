import pyperclip
import sys


def pr(x):
    print(x)
    pyperclip.copy(x)


s = open(sys.argv[1], "r").read()


def compute(s):
    ns = ""
    p = s[0]
    c = 1
    for x in s[1:]:
        if x == p:
            c += 1
        else:
            ns += f"{c}{p}"
            p = x
            c = 1
    ns += f"{c}{p}"
    return ns


for i in range(50):
    s = compute(s)


pr(len(s))
