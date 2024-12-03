with open("in.txt", "r") as f:
    lines = f.read().split("\n")


u = list(list(map(int, line.split())) for line in lines)
u1, u2 = list(x[0] for x in u), list(x[1] for x in u)

result = 0
for x in u1:
    n = u2.count(x)
    result += n * x

print(result)
