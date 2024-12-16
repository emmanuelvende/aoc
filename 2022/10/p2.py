import sys


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# Append new line at end of input:
lines[-1] += "\n"

NTH_TIMES_TO_CONSIDER = [20, 60, 100, 140, 180, 220]
NB_COLS = 40
NB_ROWS = 6


class Device:
    def __init__(self):
        self.time = 0
        self.x = 1
        self.signal_strength = 0
        self.screen = [[" " for _ in range(NB_COLS)] for _ in range(NB_ROWS)]

    def tick(self):
        pixel_row = self.time // NB_COLS
        pixel_col = self.time % NB_COLS
        self.screen[pixel_row][pixel_col] = "#" if abs(self.x - pixel_col) <= 1 else "."

        self.time += 1
        if self.time in NTH_TIMES_TO_CONSIDER:
            self.signal_strength += self.time * self.x

    def display(self):
        for row in range(NB_ROWS):
            print("".join(self.screen[row]))


device = Device()

for line in lines:
    args = line[:-1].split()
    if len(args) == 1:
        op = args[0]
    else:
        op, val = args[0], int(args[1])
    if op == "noop":
        device.tick()
    elif op == "addx":
        device.tick()
        device.tick()
        device.x += val

print(device.signal_strength)
device.display()
