import sys
import functools

PRINT = 1
# PRINT = 0


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

packets = []
for pair in pairs:
    u, v = pair.split("\n")
    u, v = eval(u), eval(v)
    packets += [u, v]

packets.append([[2]])
packets.append([[6]])

print_(packets)

packets.sort(key=functools.cmp_to_key(compare_order))

index_1 = packets.index([[2]]) + 1
index_2 = packets.index([[6]]) + 1

print(index_1 * index_2)
