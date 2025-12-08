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
            return False  # already in same circuit, no merge
        # Union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def main():
    # Use the given absolute path
    file_path = "/Users/abidshakir/Advent-of-Code/2025/Day 08/input.txt"
    points = read_points(file_path)
    n = len(points)

    if n <= 1:
        # Trivial case: no connection needed
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

    dsu = DSU(n)
    components = n

    # Process pairs in order until all points are in one circuit
    for _, i, j in pairs:
        merged = dsu.union(i, j)
        if merged:
            components -= 1
            # When components becomes 1, this is the last connection needed
            if components == 1:
                x1 = points[i][0]
                x2 = points[j][0]
                result = x1 * x2
                print(result)
                return

    # Fallback: if somehow not all connected (shouldn't happen with full graph)
    print(0)


if __name__ == "__main__":
    main()
