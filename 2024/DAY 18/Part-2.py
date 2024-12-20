import heapq
from collections import deque
from rich import print

def read_input(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")
    return [tuple(map(int, line.split(","))) for line in data]

def simulate_falling_bytes_incrementally(corrupted_positions, grid_size=(70, 70)):
    grid = [["." for _ in range(grid_size[0] + 1)] for _ in range(grid_size[1] + 1)]
    for i, (x, y) in enumerate(corrupted_positions):
        grid[y][x] = "#"
        if not is_path_possible(grid):
            return x, y
    return None

def is_path_possible(grid):
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([start])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= end[0] and 0 <= ny <= end[1] and grid[ny][nx] == "." and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return False

def main():
    file_path = "/Users/abidshakir/Advent-of-Code/2024/DAY 18/input.txt"
    corrupted_positions = read_input(file_path)

    # Find the first byte that blocks the path
    blocking_byte = simulate_falling_bytes_incrementally(corrupted_positions)

    if blocking_byte:
        print(f"Answer No. 2: {blocking_byte[0]},{blocking_byte[1]}")
    else:
        print("Path remains open")

if __name__ == "__main__":
    main()