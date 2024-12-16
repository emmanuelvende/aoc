import sys

with open(sys.argv[1], "r") as f:
    lines = f.read().split("\n")

cards = []
for i, line in enumerate(lines):
    card_str, draw_str = line.split(":")
    winnings, i_have = [x.strip() for x in draw_str.split("|")]
    winnings = [int(x) for x in winnings.split()]
    i_have = [int(x) for x in i_have.split()]
    pp = 0
    for x in i_have:
        pp += 1 if x in winnings else 0
    cards.append(pp)

d = {}
for i, card in enumerate(cards):
    d[i] = 1

for i, card in enumerate(cards):
    for j in range(card):
        d[i + j + 1] += d[i]

total = 0
for k, v in d.items():
    total += v

print(total)
