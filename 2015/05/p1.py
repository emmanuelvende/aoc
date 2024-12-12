import sys
import re
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")


def al3v(s):
    """at least 3 vowels"""
    m = re.findall(r"[aeiou]", s)
    if m:
        return len(m) >= 3
    return False


def aloltiar(s):
    """at least one letter twince in a row"""
    m = re.search(r"(\w)\1", s)
    return bool(m)


counter = 0
for s in L:
    nice = (
        not any(("ab" in s, "cd" in s, "pq" in s, "xy" in s))
        and al3v(s)
        and aloltiar(s)
    )
    if nice:
        counter += 1

pr(counter)
