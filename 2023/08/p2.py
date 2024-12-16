import sys
import math

with open(sys.argv[1], "r") as f:
    data = f.read()

I, all_nodes = data.split("\n\n")
# print(I)
nodes = all_nodes.split("\n")

D = {}
for node in nodes:
    u = node.split("=")
    # print(u)
    l, r = [x.strip() for x in u[1].split(",")]
    l = l[1:]
    r = r[:-1]
    D[u[0].strip()] = (l, r)

# print(D)

ghosts = list(filter(lambda x: x.endswith("A"), D.keys()))
print(ghosts)


i = 0
d_nb_steps_per_ghost = {}
each_ghost_has_eached_at_least_once = False
while not each_ghost_has_eached_at_least_once:
    for ghost_index in range(len(ghosts)):
        m = I[i % len(I)]
        pos = ghosts[ghost_index]
        pos = D[pos][0 if m == "L" else 1]
        ghosts[ghost_index] = pos
        if pos.endswith("Z") and not ghost_index in d_nb_steps_per_ghost.keys():
            d_nb_steps_per_ghost[ghost_index] = i + 1
    each_ghost_has_eached_at_least_once = len(d_nb_steps_per_ghost) == len(ghosts)
    i += 1

print(d_nb_steps_per_ghost)
v = list(d_nb_steps_per_ghost.values())
# print(v)
print(math.lcm(*v))
