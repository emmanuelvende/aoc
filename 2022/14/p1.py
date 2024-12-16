import sys
import math


def sign_(x):
    return int(math.copysign(1, x))


def add_tuple(a, b):
    return tuple([a[i] + b[i] for i in range(len(a))])


def draw_(rocks, start_xy, end_xy):
    s = ""
    for y in range(start_xy[1], end_xy[1]):
        for x in range(start_xy[0], end_xy[0]):
            s += "#" if (x, y) in rocks else "."
        s += "\n"
    print(s)


def compute_floor(rocks):
    return max([coord[1] for coord in rocks])


rocks_ = set()


class RockPath:
    def __init__(self) -> None:
        self.edges = set()
        self.last_edge = None

    def add_edge(self, coord):
        if self.last_edge == None:
            self.edges.add(coord)
        else:
            last = self.last_edge
            du = [coord[i] - last[i] for i in range(len(coord))]
            dx, dy = du
            for i in range(abs(dx)):
                x_inc = (i + 1) * sign_(dx)
                self.edges.add((last[0] + x_inc, last[1]))
            for j in range(abs(dy)):
                y_inc = (j + 1) * sign_(dy)
                self.edges.add((last[0], last[1] + y_inc))
        self.last_edge = coord

    def add_to(self, rocks):
        for edge in self.edges:
            rocks.add(edge)


with open(sys.argv[1], "r") as f:
    input_ = f.read()

paths = input_.split("\n")

for path in paths:
    edges = path.split(" -> ")
    rock_path = RockPath()
    for edge in edges:
        coord = eval(edge)
        rock_path.add_edge(coord)
    rock_path.add_to(rocks_)

# print(rocks_)
# draw_(rocks_, (493, 0), (504, 10))
# draw_(rocks_, (0, 0), (1000, 500))

floor_level_ = compute_floor(rocks_)
# print(floor_level_)

sands_ = set()


def fall(floor_level, rocks, sands):
    sand_pos = (500, 0)
    resting = False
    while not resting and sand_pos[1] <= floor_level:
        new_sand_pos = add_tuple(sand_pos, (0, 1))
        if new_sand_pos not in rocks and new_sand_pos not in sands:
            sand_pos = new_sand_pos
        else:
            new_sand_pos = add_tuple(sand_pos, (-1, 1))
            if new_sand_pos not in rocks and new_sand_pos not in sands:
                sand_pos = new_sand_pos
            else:
                new_sand_pos = add_tuple(sand_pos, (1, 1))
                if new_sand_pos not in rocks and new_sand_pos not in sands:
                    sand_pos = new_sand_pos
                else:
                    resting = True
                    sands.add(sand_pos)
    return resting


unit = 0
while fall(floor_level_, rocks_, sands_):
    unit += 1

print(unit)
