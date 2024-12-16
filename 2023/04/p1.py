import sys

with open(sys.argv[1], "r") as f:
    lines = f.read().split("\n")

total = 0

for i, line in enumerate(lines):
    card_str, draw_str = line.split(":")
    winnings, i_have = [x.strip() for x in draw_str.split("|")]
    winnings = [int(x) for x in winnings.split()]
    i_have = [int(x) for x in i_have.split()]
    pp = 0
    for x in i_have:
        pp += 1 if x in winnings else 0
    card_value = int(2 ** (pp - 1))
    total += card_value

print(total)
