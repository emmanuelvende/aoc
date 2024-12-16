import sys
s = open(sys.argv[1], "r").read()
u, d = 0, 0
for c in s:
    if c == "(":
        u += 1
    else:
        d += 1

r = u - d
print(r)
