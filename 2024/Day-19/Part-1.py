from collections import defaultdict
import os
from rich import print

def can_form_design(patterns, design):
    """
    Function to determine if a design can be formed using the given patterns.
    """
    pattern_set = set(patterns)

    # Dynamic Programming to determine if the design can be formed
    dp = [False] * (len(design) + 1)
    dp[0] = True  # Base case: an empty design can always be formed

    for i in range(1, len(design) + 1):
        for j in range(i):
            if dp[j] and design[j:i] in pattern_set:
                dp[i] = True
                break

    return dp[len(design)]

# File path to the input file
file_path = "/Users/abidshakir/Advent-of-Code/2024/Day-19/input.txt"

# Read input from the file
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        lines = f.read().strip().split("\n")
else:
    raise FileNotFoundError(f"File not found at {file_path}")

# Parse the input
patterns = lines[0].split(", ")

# Separate the designs
if "" in lines:
    designs_index = lines.index("") + 1
else:
    raise ValueError("Input format error: Missing blank line separating patterns and designs.")

designs = lines[designs_index:]

# Check each design and count the number of possible designs
possible_count = 0

for design in designs:
    if can_form_design(patterns, design):
        possible_count += 1

# Output the result
print(f"Number of possible designs: {possible_count}")