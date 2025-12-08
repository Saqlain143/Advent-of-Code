import math
from collections import Counter

def read_points(file_path):
    points = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x_str, y_str, z_str = line.split(",")
            x, y, z = int(x_str), int(y_str), int(z_str)
            points.append((x, y, z))
    return points


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        # Path compression
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  # no change
        # Union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def main():
    # Use the path you specified
    file_path = "/Users/abidshakir/Advent-of-Code/2025/Day 08/input.txt"
    points = read_points(file_path)
    n = len(points)

    if n == 0:
        print(0)
        return

    # Build all unique pairs with squared distance
    pairs = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d2 = dx * dx + dy * dy + dz * dz  # squared distance
            pairs.append((d2, i, j))

    # Sort by distance ascending
    pairs.sort(key=lambda t: t[0])

    NUM_CONNECTIONS = 1000
    max_connections = min(NUM_CONNECTIONS, len(pairs))

    dsu = DSU(n)

    # Process the 1000 (or fewer) shortest pairs
    for k in range(max_connections):
        _, i, j = pairs[k]
        dsu.union(i, j)  # if they are already in the same circuit, nothing changes

    # Count circuit sizes
    comp_counts = Counter()
    for i in range(n):
        root = dsu.find(i)
        comp_counts[root] = dsu.size[root]

    # Get the sizes of all circuits
    sizes = sorted(comp_counts.values(), reverse=True)

    if len(sizes) == 0:
        print(0)
        return
    elif len(sizes) == 1:
        result = sizes[0]
    elif len(sizes) == 2:
        result = sizes[0] * sizes[1]
    else:
        result = sizes[0] * sizes[1] * sizes[2]

    print(result)


if __name__ == "__main__":
    main()
