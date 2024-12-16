def does_contain(a, b):
    """
    a : (i, j)
    b : (k, l)

    Return: does a contains b ?
    """

    def _contains(i, j, k, l):
        return k <= i and j <= l

    return _contains(*a, *b)


def does_overlap(a, b):
    """
    a : (i, j)
    b : (k, l)

    Return: does b overlap on a at starting or ending of the zone ?
    """

    def _overlaps(i, j, k, l):
        return (k <= i and i <= l and l <= k) or (i <= k and k <= j and j <= l)

    return _overlaps(*a, *b)


def convert(zone_str):
    bornes_str = zone_str.split("-")
    return [int(x) for x in bornes_str]


with open("input.txt", "r") as f:
    lines = f.readlines()

# Fix the input (last line does not contain newline char)
lines[-1] += "\n"

total = 0
for line in lines:
    zone_a, zone_b = [convert(x) for x in line[:-1].split(",")]
    contains = does_contain(zone_a, zone_b) or does_contain(zone_b, zone_a)
    overlaps = does_overlap(zone_a, zone_b) or does_overlap(zone_b, zone_a)
    # print(f"{line=} --> {zone_a=} {zone_b=} --> {contains=} | {overlaps=}")
    if contains or overlaps:
        total += 1

print(total)
