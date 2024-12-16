import sys

# PRINT = 1
PRINT = 0


def print_(x, end="\n"):
    if PRINT:
        print(x, end=end)


def compare_order(a, b):
    """
    -1 if left < right  (good)
    0 if left == right  (draw)
    1 if left > right   (bad)
    """
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return 0
        else:
            return (a - b) // abs(a - b)
    elif isinstance(a, list) and isinstance(b, list):
        u, v = len(a), len(b)
        i = 0
        while i < u and i < v:
            r = compare_order(a[i], b[i])
            if r == 1 or r == -1:
                return r
            i += 1
        if i == u and i < v:
            return -1
        elif i == v and i < u:
            return 1
        else:
            return 0
    elif isinstance(a, int) and isinstance(b, list):
        return compare_order([a], b)
    else:
        return compare_order(a, [b])


with open(sys.argv[1], "r") as f:
    input_ = f.read()

pairs = input_.split("\n\n")
analysis_results = []  # list of (u, v, value)

for pair in pairs:
    u, v = pair.split("\n")
    u, v = eval(u), eval(v)
    comp = compare_order(u, v)
    print_(f"{u=}, {v=}, {comp=}")
    analysis_results.append((u, v, comp))

indices_sum = 0
for i, r in enumerate(analysis_results):
    indices_sum += i + 1 if r[2] == -1 else 0

print(indices_sum)
