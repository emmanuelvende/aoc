import re
import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# print(lines)

x = 0
for line in lines:
    nb_str = re.sub("\D", "", line)
    nb_str = nb_str[0] + nb_str[-1]
    x += int(nb_str)

print(x)
