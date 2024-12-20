from collections import defaultdict

# Function to read the grid from input.txt file
def get_problem_lines(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Initialize the grid using defaultdict
m = defaultdict(lambda: '.')

# Replace 'input.txt' with the actual path to your file
filename = '/Users/abidshakir/Advent-of-Code/2024/DAY 04/input.txt'

# Read the grid from the file
for i, line in enumerate(get_problem_lines(filename)):
    for j, c in enumerate(line):
        m[(i, j)] = c

# List of all positions in the grid
k = list(m.keys())

# Part 1: Count "XMAS" in all 8 directions
ans = 0
directions = [
    (0, 1), (0, -1),  # Horizontal: Right, Left
    (1, 0), (-1, 0),  # Vertical: Down, Up
    (1, 1), (1, -1),  # Diagonal: Down-Right, Down-Left
    (-1, 1), (-1, -1) # Diagonal: Up-Right, Up-Left
]

# Search for the word "XMAS"
for d in directions:
    for s in k:
        if m[s] == 'X' and m[(s[0] + d[0], s[1] + d[1])] == 'M' and \
           m[(s[0] + 2 * d[0], s[1] + 2 * d[1])] == 'A' and \
           m[(s[0] + 3 * d[0], s[1] + 3 * d[1])] == 'S':
            ans += 1

print(f"part 1: {ans}")

# Part 2: Count "X-MAS" pattern
ans = 0
for s in k:
    if m[s] == 'A' and \
            ((m[(s[0] - 1, s[1] - 1)] == 'M' and m[(s[0] + 1, s[1] + 1)] == 'S') or
             (m[(s[0] - 1, s[1] - 1)] == 'S' and m[(s[0] + 1, s[1] + 1)] == 'M')) and \
            ((m[(s[0] - 1, s[1] + 1)] == 'M' and m[(s[0] + 1, s[1] - 1)] == 'S') or
             (m[(s[0] - 1, s[1] + 1)] == 'S' and m[(s[0] + 1, s[1] - 1)] == 'M')):
        ans += 1

print(f"part 2: {ans}")