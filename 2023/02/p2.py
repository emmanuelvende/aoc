import re
import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

R, G, B = 12, 13, 14

possible_games_ids = []
powers = []
for i, line in enumerate(lines):
    game, draws = line.split(":")
    maxr, maxg, maxb = 0, 0, 0
    for draw in draws.split(";"):
        r, g, b = 0, 0, 0
        for x in draw.strip().split(","):
            x = x.strip()
            if x.endswith("red"):
                r += int(x.split()[0])
            if x.endswith("green"):
                g += int(x.split()[0])
            if x.endswith("blue"):
                b += int(x.split()[0])
        if r > maxr:
            maxr = r
        if g > maxg:
            maxg = g
        if b > maxb:
            maxb = b
    powers.append(maxr * maxg * maxb)

print(sum(powers))
