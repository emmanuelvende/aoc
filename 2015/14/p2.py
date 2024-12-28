import sys
import pyperclip


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

D = {}

for line in L:
    u = line.split()
    name, speed, f_time, r_time = u[0], int(u[3]), int(u[6]), int(u[13])
    D[name] = (speed, f_time, r_time)


def compute_distance(reindeer, t):
    speed, fly, rest = D[reindeer]
    n = t // (fly + rest)
    if n * (fly + rest) == t:
        return n * fly * speed
    else:
        dt = t - n * (fly + rest)
        if dt >= fly:
            return (n + 1) * fly * speed
        else:
            return (n * fly + dt) * speed


SCORES = {}
for reindeer in D.keys():
    SCORES[reindeer] = 0

for duration in range(1, 2504):
    DISTANCES = {}
    for reindeer in D.keys():
        DISTANCES[reindeer] = compute_distance(reindeer, duration)
    farest = max(DISTANCES.values())
    for reindeer in D.keys():
        if DISTANCES[reindeer] == farest:
            SCORES[reindeer] += 1

pr(max(SCORES.values()))
