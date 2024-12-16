import sys

with open(sys.argv[1], "r") as f:
    data = f.read()

seeds, *blocks = data.split("\n\n")
# print(blocks)

seeds = list(int(x) for x in seeds.split(":")[1].split())

# print(seeds)


def is_true_interval(u):
    return u[1] > u[0]


def compute_new_ranges(transfo_ranges, the_ranges):
    transformed_ranges = []
    for dst, src_start, length in transfo_ranges:
        src_end = src_start + length
        new_ranges = []
        while the_ranges:
            start, end = the_ranges.pop()
            # [start                                           end]
            #           [src_start           src_end]
            # [ before ][      intermediate         ][   after    ]
            before = start, min(src_start, end)
            intermediate = max(start, src_start), min(src_end, end)
            after = max(start, src_end), end
            if is_true_interval(before):
                new_ranges.append(before)
            if is_true_interval(intermediate):
                a, b = intermediate
                transformed_ranges.append((a - src_start + dst, b - src_start + dst))
            if is_true_interval(after):
                new_ranges.append(after)
        the_ranges = new_ranges
    result = transformed_ranges + the_ranges
    # print(result)
    return result


minimas = []
for start_seed, range_seed in [
    (seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)
]:
    # print(start_seed, range_seed)
    the_ranges = [(start_seed, start_seed + range_seed)]
    for block in blocks:
        transfo_ranges = []
        for line in block.splitlines()[1:]:
            transfo_ranges.append([int(x) for x in line.split()])
        the_ranges = compute_new_ranges(transfo_ranges, the_ranges)
        # print(the_ranges)
    minimas.append(min(the_ranges)[0])

print(min(minimas))
