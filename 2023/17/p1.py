import sys

# import functools

with open(sys.argv[1], "r") as f:
    lines = f.read().split("\n")

grid = [[int(char) for char in row] for row in lines]
# print(grid)


directions = "NSWE"
moves = "LRS"


def get_neighbours(G, node, d):  # node := (row, col)
    row, col = node
    if d == "N":
        
