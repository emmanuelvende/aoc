import sys
import re

with open(sys.argv[1], "r") as f:
    input_ = f.read()

lines = input_.split("\n")


def get_info(line):
    m = re.search(
        r"Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)",
        line,
    )
    return tuple([int(m.group(x)) for x in ("sx", "sy", "bx", "by")])


def manhattan(a, b):
    return sum([abs(a[i] - b[i]) for i in range(len(a))])


# s = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15"
# print(get_info(s))

sensors = list()
beacons = list()
distances = list()

for line in lines:
    sx, sy, bx, by = get_info(line)
    sensor = sx, sy
    sensors.append(sensor)
    beacon = bx, by
    beacons.append(beacon)
    distance = manhattan(sensor, beacon)
    distances.append(distance)

# print(sensors, beacons, distances)


def is_possible(x, y):
    for i, sensor in enumerate(sensors):
        if manhattan((x, y), sensor) <= distances[i]:
            return False
    return True


def compute_all_positions_at_distance(a, d):
    p = set()
    x, y = a
    for i in range(d + 1):
        j = d - i
        p.add((x + i, y + j))
        p.add((x + i, y - j))
        p.add((x - i, y + j))
        p.add((x - i, y - j))
    return p


# p_ = compute_all_positions_at_distance((10, 10), 5)
# print(p_)
# s = ""
# for y in range(20):
#     for x in range(20):
#         s += "+" if (x, y) == (10, 10) else "*" if (x, y) in p_ else "."
#     s += "\n"
# print(s)


# maxi = 20
maxi = 4000000
stop = False
nb_sensors = len(sensors)
for i, sensor in enumerate(sensors):
    print(f"sensor {sensor} {i+1} of {nb_sensors}...")
    d = distances[i]
    positions = compute_all_positions_at_distance(sensor, d + 1)
    nb_positions = len(positions)
    print(f"{nb_positions=}")
    for k, p in enumerate(positions):
        if k % 1e5 == 0:
            print(f"position {k+1} out of {nb_positions}...")
        x, y = p
        if not (0 <= x <= maxi and 0 <= y <= maxi):
            continue
        if is_possible(x, y):
            print(f"FOUND : {x * 4000000 + y}")
            stop = True
            break
    if stop:
        break
