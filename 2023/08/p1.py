import sys
import re
with open(sys.argv[1], "r") as f:
    data = f.read()

I, all_nodes = data.split("\n\n")
print(I)
nodes = all_nodes.split("\n")

D = {}
for node in nodes:
    u = node.split('=')
    # print(u)
    l, r = [x.strip() for x in u[1].split(",")]
    l = l[1:]
    r = r[:-1]
    D[u[0].strip()] = (l, r)

# print(D)

i = 0
pos = "AAA"
while not pos == "ZZZ":
    m = I[i % len(I)]
    pos = D[pos][0 if m == 'L' else 1]
    i += 1

print(i)