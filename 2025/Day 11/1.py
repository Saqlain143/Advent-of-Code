from __future__ import annotations
from typing import Dict, List
import os

# Read input from the same directory as this script
INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def parse_graph(path: str) -> Dict[str, List[str]]:
    """
    Parse the input file into an adjacency list for a directed graph.
    Each line has the form:
        node: child1 child2 child3
    """
    graph: Dict[str, List[str]] = {}

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Split "aaa: you hhh" → "aaa", "you hhh"
            left, right = line.split(":", 1)
            node = left.strip()
            # Right side might be empty or have multiple targets
            targets = right.strip()
            if targets:
                neighbors = targets.split()
            else:
                neighbors = []

            graph[node] = neighbors

    return graph


def count_paths(graph: Dict[str, List[str]], start: str, end: str) -> int:
    """
    Count the number of distinct paths from `start` to `end` in a directed graph.
    Assumes there are no cycles on any path from `start` that would lead to infinite paths.
    If a cycle is detected in the recursion stack, an exception is raised.
    """
    memo: Dict[str, int] = {}
    in_stack: set[str] = set()

    def dfs(node: str) -> int:
        if node == end:
            return 1

        if node in memo:
            return memo[node]

        if node in in_stack:
            # Cycle detected along a path from `start`.
            # For this puzzle, the graph is expected to be acyclic on relevant paths.
            raise ValueError(f"Cycle detected involving node '{node}'")

        in_stack.add(node)
        total = 0
        for nei in graph.get(node, []):
            total += dfs(nei)
        in_stack.remove(node)

        memo[node] = total
        return total

    return dfs(start)


def main() -> None:
    graph = parse_graph(INPUT_PATH)

    # If "you" is not present at all, there are no paths.
    if "you" not in graph:
        print(0)
        return

    paths = count_paths(graph, "you", "out")
    print(paths)


if __name__ == "__main__":
    main()
