import pyperclip
import sys
import itertools


def pr(x):
    print(x)
    pyperclip.copy(x)


s = open(sys.argv[1], "r").read()


def rule1(s):
    triplets = [chr(i) + chr(i + 1) + chr(i + 2) for i in range(97, 97 + 26 - 2)]
    triplets = filter(lambda x: not any((y in x for y in "iol")), triplets)
    return any((t in s for t in triplets))


def rule3(s):
    pairs = [2 * chr(i) for i in range(97, 97 + 26)]
    pairs = list(
        itertools.filterfalse(lambda x: x == "ii" or x == "oo" or x == "ll", pairs)
    )
    condition = False
    for p in pairs:
        if p in s:
            qairs = list(
                itertools.filterfalse(
                    lambda x: x == "ii" or x == "oo" or x == "ll", pairs
                )
            )
            qairs.remove(p)
            for q in qairs:
                if q in s:
                    condition = True
                    break
            if condition:
                break
    return condition


def is_valid(pwd):
    return rule1(pwd) and rule3(pwd)


D = {}


def compute_next(s):
    if s in D:
        return D[s]
    c = s[-1]
    if c != "z":
        if c in "iol":
            r = s[:-1] + chr(ord(c) + 2)
        else:
            r = s[:-1] + chr(ord(c) + 1)
    else:
        r = compute_next(s[:-1]) + "a"
    D[s] = r
    return r


while True:
    s = compute_next(s)
    if is_valid(s):
        break

pr(s)
