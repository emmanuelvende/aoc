import sys
import pyperclip
import re


def pr(x):
    print(x)
    pyperclip.copy(x)


s = open(sys.argv[1], "r").read()

m = re.findall("-?\d+\.?\d*", s)
r = sum((int(x) for x in m))
pr(r)
