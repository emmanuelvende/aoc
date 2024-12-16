import sys

with open(sys.argv[1], "r") as f:
    lines = f.read().split("\n")


def compute_diffs(u):
    v = []
    for i in range(len(u) - 1):
        v.append(u[i + 1] - u[i])
    return v


def all_zeros(u):
    for x in u:
        if x != 0:
            return False
    return True


def compute_number_to_add(u):
    if all_zeros(u):
        return 0
    v = compute_diffs(u)
    return u[-1] + compute_number_to_add(v)




# s = "0 3 6 9 12 15"
# u = [int(x.strip()) for x in s.split()]
# print(u)
# u = compute_diffs(u)
# print(u)
# print(all_zeros(u))
# u = compute_diffs(u)
# print(u)
# print(all_zeros(u))
# print(compute_number_to_add(u))

numbers = []
for line in lines:
    u = [int(x.strip()) for x in line.split()]
    numbers.append(compute_number_to_add(u))

print(sum(numbers))