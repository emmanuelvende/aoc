with open("in.txt", "r") as f:
    lines = f.read().split("\n")

u = list(list(map(int, line.split())) for line in lines)
u1, u2 = list(x[0] for x in u), list(x[1] for x in u)

u1.sort()
u2.sort()

result = 0
for i, x in enumerate(u1):
    y = u2[i]
    dist = abs(x - y)
    result += dist

print(result)
