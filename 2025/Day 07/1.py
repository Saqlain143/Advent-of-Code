from collections import deque

def count_splits(grid):
    """
    grid: list[list[str]] representing the manifold.
    Returns the number of times tachyon beams are split.
    """
    h = len(grid)
    w = len(grid[0])

    # Find starting position S
    start_row = start_col = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
                break
        if start_row is not None:
            break

    if start_row is None:
        raise ValueError("No starting point 'S' found in the grid.")

    # BFS over *beam positions* with merging:
    # If a beam has already passed through a cell, another beam arriving
    # at the same cell acts identically, so we don't process it again.
    queue = deque()
    visited = set()

    queue.append((start_row, start_col))
    visited.add((start_row, start_col))

    splits = 0

    while queue:
        r, c = queue.popleft()

        # Move one step downward
        nr = r + 1
        if nr >= h:
            # Beam leaves the manifold
            continue

        # Check what is directly below
        if grid[nr][c] == '^':
            # Beam encounters a splitter: it stops and splits
            splits += 1

            # New beams from immediate left and right of the splitter (same row nr)
            for nc in (c - 1, c + 1):
                if 0 <= nc < w:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        else:
            # Empty space: beam just continues downward
            if (nr, c) not in visited:
                visited.add((nr, c))
                queue.append((nr, c))

    return splits


def main():
    # Replace this path if needed; per your instructions:
    input_path = "/Users/abidshakir/Advent-of-Code/2025/Day 07/input.txt"

    with open(input_path, "r", encoding="utf-8") as f:
        # Strip only newline; keep dots, carets, and S exactly
        lines = [line.rstrip("\n") for line in f if line.strip() != ""]

    # Build grid as list of lists of characters
    grid = [list(row) for row in lines]

    result = count_splits(grid)
    print(result)


if __name__ == "__main__":
    main()
