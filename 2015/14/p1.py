import sys
import pyperclip
import itertools
import copy


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

D = {}

for line in L:
    u = line.split()
    name, speed, f_time, r_time = u[0], int(u[3]), int(u[6]), int(u[13])
    D[name] = (speed, f_time, r_time)


SCORES = {}


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


for reindeer in D.keys():
    SCORES[reindeer] = compute_distance(reindeer, 2503)

pr(max(SCORES.values()))
