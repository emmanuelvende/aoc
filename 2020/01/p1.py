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
    for b in values[i+1:]:
        if a + b == sum_to_find:
            found = True
            u = a
            v = b
            break

if found:
    print(u, v, u*v)
else:
    print("not found")