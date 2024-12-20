import functools
from math import log10
from rich import print

day = "11"

# Memoized recursive function to compute the number of stones after 'generations' blinks
@functools.cache
def num_stones(stone, generations):
    if generations == 0:
        return 1
    if stone == 0:
        return num_stones(1, generations - 1)
    
    num_digits = int(log10(stone)) + 1
    
    # Rule 1: If the stone has an even number of digits, split it
    if num_digits % 2 == 0:
        # Split into left and right halves
        half_length = num_digits // 2
        left = stone // (10 ** half_length)
        right = stone % (10 ** half_length)
        return num_stones(left, generations - 1) + num_stones(right, generations - 1)
    
    # Rule 2: If the stone has an odd number of digits, multiply by 2024
    else:
        return num_stones(stone * 2024, generations - 1)

# Assuming tokenedlines is a function to split the input data
def tokenedlines(day):
    # Simulate the behavior of `tokenedlines` which should read and split the input for Day 11
    with open('/Users/abidshakir/Advent-of-Code/2024/DAY 11/input.txt', 'r') as file:
        return [line.split() for line in file.readlines()]

# Read the input data
stones = tokenedlines(day)[0]

# Compute and print the results for 25 and 75 blinks
print(f"Part One: {sum([num_stones(int(stone), 25) for stone in stones])}")  # Part A: After 25 blinks
print(f"Part Two: {sum([num_stones(int(stone), 75) for stone in stones])}")  # Part B: After 75 blinks
