import re

with open("in.txt", "r") as f:
    lines = f.read()


def scan(s):
    muls = list(m for m in re.finditer(r"mul\(\d+,\d+\)", s))
    doess = list(m for m in re.finditer(r"do\(\)", s))
    donts = list(m for m in re.finditer(r"don't\(\)", s))
    tokens = muls + doess + donts
    tokens.sort(key=lambda x: x.span()[0])
    result = 0
    enabled = True
    for token in tokens:
        word = token.group()
        if word.startswith("mul") and enabled:
            nn = re.findall("\d+", word)
            result += int(nn[0]) * int(nn[1])
        elif word.startswith("do()"):
            enabled = True
        elif word.startswith("don't()"):
            enabled = False
    print(result)

scan(lines)
