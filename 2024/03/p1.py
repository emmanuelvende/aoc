import re

with open("in.txt", "r") as f:
    lines = f.read()


def scan(s):
    m = re.findall(r"mul\(\d+,\d+\)", s)
    if m:
        result = 0
        for p in m:
            n = re.findall("\d+", p)
            result += int(n[0]) * int(n[1])
    print(result)


scan(lines)
