import sys
import re
from collections import *
from itertools import *
from heapq import *
import math
from rich import print

sys.setrecursionlimit(2000)

def count(it):
    return sum(1 for _ in it)

# Read the input from input.txt file
with open('/Users/abidshakir/Advent-of-Code/2024/DAY 15/input.txt', 'r') as file:
    inp = file.read()

parts = inp.split("\n\n")
lines = parts[0].split("\n")

def expand(c):
    if c == "O":
        return "[]"
    elif c == "@":
        return "@."
    else:
        return c + c

# Expand lines
lines = ["".join(expand(c) for c in l) for l in lines]
print("\n".join(lines))
m = len(lines)
n = len(lines[0])

# Create the grid (defaultdict of defaultdicts)
grid = defaultdict(
    lambda: defaultdict(lambda: "!"),
    {i: defaultdict(lambda: "!", {j: line[j] for j in range(len(line))}) for i, line in enumerate(lines)}
)

# Directions and character to direction map
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
chardirs = {"<": 1, ">": 0, "^": 2, "v": 3}

result = 0

# Check move function
def check_move(d, i, j, already_checked):
    if (i, j) in already_checked:
        return already_checked[(i, j)]
    already_checked[(i, j)] = True
    if grid[i][j] == "#":
        already_checked[(i, j)] = False
    elif grid[i][j] == ".":
        already_checked[(i, j)] = True
    elif grid[i][j] == "@":
        already_checked[(i, j)] = check_move(d, i + d[0], j + d[1], already_checked)
    elif grid[i][j] == "[":
        already_checked[(i, j)] = check_move(d, i + d[0], j + d[1], already_checked) and check_move(d, i, j + 1, already_checked)
    elif grid[i][j] == "]":
        already_checked[(i, j)] = check_move(d, i + d[0], j + d[1], already_checked) and check_move(d, i, j - 1, already_checked)
    return already_checked[(i, j)]

# Commit move function
def commit_move(d, i, j, already_committed):
    if (i, j) in already_committed:
        return
    already_committed.add((i, j))
    if grid[i][j] == "#":
        return
    elif grid[i][j] == ".":
        return
    elif grid[i][j] == "[":
        commit_move(d, i + d[0], j + d[1], already_committed)
        commit_move(d, i, j + 1, already_committed)
        grid[i + d[0]][j + d[1]] = grid[i][j]
        grid[i][j] = "."
    elif grid[i][j] == "]":
        commit_move(d, i + d[0], j + d[1], already_committed)
        commit_move(d, i, j - 1, already_committed)
        grid[i + d[0]][j + d[1]] = grid[i][j]
        grid[i][j] = "."
    elif grid[i][j] == "@":
        commit_move(d, i + d[0], j + d[1], already_committed)
        grid[i + d[0]][j + d[1]] = grid[i][j]
        grid[i][j] = "."

# Find the initial robot position
robot_pos = (0, 0)
for i in range(m):
    for j in range(n):
        if grid[i][j] == "@":
            robot_pos = (i, j)

# Process the directions from the second part of the input
for dirchar in parts[1]:
    if dirchar == "\n":
        continue
    d = dirs[chardirs[dirchar]]
    if check_move(d, robot_pos[0], robot_pos[1], {}):
        commit_move(d, robot_pos[0], robot_pos[1], set())
        robot_pos = (robot_pos[0] + d[0], robot_pos[1] + d[1])

# Print the updated grid and calculate the result
for i in range(m):
    row = ""
    for j in range(n):
        row += grid[i][j]
        if grid[i][j] == "[":
            offset = 0
            #if j > n - j - 1:
            #    offset = 1
            result += 100 * i + j + offset
    print(row)

print(result)
