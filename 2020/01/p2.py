import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# Append new line at end of input:
# lines[-1] += "\n"

values = list([int(value) for value in lines])
sum_to_find = 2020
# print(values)
found = False
for i, a in enumerate(values):
    for j, b in enumerate(values[i+1:]):
        for k, c in enumerate(values[j+1:]):
            if a + b + c == sum_to_find:
                found = True
                u = a
                v = b
                w = c
                break

if found:
    print(u, v, w, u*v*w)
else:
    print("not found")