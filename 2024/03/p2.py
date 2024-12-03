import re

with open("in.txt", "r") as f:
    lines = f.read()


muls = list(m for m in re.finditer(r"mul\(\d+,\d+\)", lines))
doess = list(m for m in re.finditer(r"do\(\)", lines))
donts = list(m for m in re.finditer(r"don't\(\)", lines))
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
