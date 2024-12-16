import sys
import functools

with open(sys.argv[1], "r") as f:
    data = f.read()

lines = data.split("\n")


# print(lines)
@functools.lru_cache
def count_valid_configs(record, groups):
    # print(f"{record=}, {groups=}")
    if record == "":
        return 1 if groups == () else 0

    if groups == ():
        return 0 if "#" in record else 1

    result = 0

    if record[0] in ".?":
        result += count_valid_configs(record[1:], groups)

    if record[0] in "#?":
        n = groups[0]
        if (
            n <= len(record)
            and "." not in record[:n]
            and (n == len(record) or record[n] != "#")
        ):
            result += count_valid_configs(record[n + 1 :], groups[1:])

    return result


total = 0
for line in lines:
    record, groups = line.split()
    record = "?".join([record] * 5)
    groups = ",".join([groups] * 5)
    groups = tuple(int(x) for x in groups.split(","))
    # print(record, groups)
    total += count_valid_configs(record, groups)

print(total)
