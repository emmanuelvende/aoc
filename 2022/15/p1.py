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


all_x = [x[0] for x in sensors + beacons]
most_left = min(all_x) - max(distances)
most_right = max(all_x) + max(distances)

print(most_left, most_right)

y = 2e6

counter = 0
for x in range(most_left, most_right):
    if x % 1e5 == 0:
        print(x)
    if not is_possible(x, y) and not (x, y) in beacons:
        counter += 1

print(counter)
