import sys
import pyperclip
import itertools


def pr(x):
    print(x)
    pyperclip.copy(x)


L = open(sys.argv[1], "r").read().split("\n")

D = []

for line in L:
    ingr, props = line.split(":")
    props = props.split(",")
    properties = []
    for prop in props:
        u = prop.split()
        p = int(u[1])
        properties.append(p)
    D.append(properties)


def cookie(teaspoons):
    t = teaspoons

    calories = 0
    for index_ingr in range(len(D)):
        calories += D[index_ingr][4] * t[index_ingr]

    if calories != 500:
        return 0

    params = []
    for index_param in range(len(D[0]) - 1):
        score = 0
        for index_ingr in range(len(D)):
            score += D[index_ingr][index_param] * t[index_ingr]
        score = 0 if score < 0 else score
        params.append(score)

    total_score = 1
    for param in params:
        total_score *= param
    return total_score


N = 100
P = []
for i in range(N + 1):
    for j in range(N + 1):
        if i + j > N:
            break
        for k in range(N + 1):
            if i + j + k > N:
                break
            for l in range(N + 1):
                if i + j + k + l > N:
                    break
                if i + j + k + l == N:
                    P.append((i, j, k, l))

r = 0
for p in P:
    x = cookie(p)
    if x > r:
        r = x

pr(r)
