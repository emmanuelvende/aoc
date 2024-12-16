import re
import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# print(lines)

# lines = [line.strip() for line in lines]

patterns = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
x = 0

for k, line in enumerate(lines):
    nb_str = ""
    for i, c in enumerate(line):
        if c.isdigit():
            nb_str += c
        for j, p in enumerate(patterns):
            if line[i:].startswith(p):
                nb_str += f"{j+1}"
    x += int(nb_str[0] + nb_str[-1])
print(x)
