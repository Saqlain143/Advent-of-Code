import sys
import re
from collections import defaultdict, Counter

# Set recursion limit if needed
sys.setrecursionlimit(10**6)

# Define the file path directly
infile = '/Users/abidshakir/Advent-of-Code/2024/DAY 03/input.txt'

# Read the content of the input file
D = open(infile).read().strip()

# Initialize variables
p1 = 0
p2 = 0
enabled = True

# Process the input data
for i in range(len(D)):
    # Check for 'do()' and enable future mul instructions
    if D[i:].startswith('do()'):
        enabled = True
    # Check for "don't()" and disable future mul instructions
    if D[i:].startswith("don't()"):
        enabled = False

    # Find mul instructions using regex
    instr = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', D[i:])
    
    # If a mul instruction is found, extract values and calculate results
    if instr is not None:
        x, y = int(instr.group(1)), int(instr.group(2))
        p1 += x * y  # This is the sum for all mul instructions
        if enabled:
            p2 += x * y  # This is the sum for only enabled mul instructions

print(p1)
print(p2)