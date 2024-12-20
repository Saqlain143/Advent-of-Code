import heapq
from collections import deque
from rich import print

def read_input(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")
    return [tuple(map(int, line.split(","))) for line in data]

def simulate_falling_bytes(corrupted_positions, grid_size=(70, 70), byte_limit=1024):
    grid = [["." for _ in range(grid_size[0] + 1)] for _ in range(grid_size[1] + 1)]
    for i, (x, y) in enumerate(corrupted_positions):
        if i >= byte_limit:
            break
        grid[y][x] = "#"
    return grid

def find_shortest_path(grid):
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Priority queue for A* algorithm
    queue = [(0, start)]  # (cost, position)
    visited = set()

    while queue:
        cost, (x, y) = heapq.heappop(queue)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        # If we reach the destination, return the cost
        if (x, y) == end:
            return cost

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= end[0] and 0 <= ny <= end[1] and grid[ny][nx] == "." and (nx, ny) not in visited:
                heapq.heappush(queue, (cost + 1, (nx, ny)))

    return -1  # Return -1 if there's no path

def main():
    file_path = "/Users/abidshakir/Advent-of-Code/2024/DAY 18/input.txt"
    corrupted_positions = read_input(file_path)

    # Simulate the falling bytes
    grid = simulate_falling_bytes(corrupted_positions)

    # Find the shortest path
    min_steps = find_shortest_path(grid)

    print("The minimum number of steps to reach the exit:")
    print(f"Answer No. 1: {min_steps}")

if __name__ == "__main__":
    main()
