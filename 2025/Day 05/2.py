# Advent of Code 2025 - Day 05, Part 2 style problem
# Count how many ingredient IDs are considered fresh by the union of all ranges.

def read_ranges(file_path: str):
    """
    Reads the input file and returns a list of (start, end) tuples
    representing the fresh ingredient ranges.
    Only the first section (before the blank line) is used.
    """
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f]

    # Find blank line that separates ranges and available IDs
    try:
        blank_index = lines.index("")
    except ValueError:
        # If there is no blank line, treat all lines as ranges
        blank_index = len(lines)

    range_lines = lines[:blank_index]

    ranges = []
    for line in range_lines:
        if not line:
            continue
        parts = line.split("-")
        if len(parts) != 2:
            continue  # skip malformed lines if any
        start, end = map(int, parts)
        if start > end:
            start, end = end, start  # normalize if reversed
        ranges.append((start, end))

    return ranges


def merge_ranges(ranges):
    """
    Given a list of (start, end) ranges, merge overlapping or adjacent ranges.
    Returns a list of merged (start, end) tuples.
    """
    if not ranges:
        return []

    # Sort by start, then end
    ranges.sort()
    merged = [list(ranges[0])]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # overlapping or directly adjacent
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return [tuple(r) for r in merged]


def count_fresh_ids(merged_ranges):
    """
    Given merged non-overlapping ranges, count how many integer IDs they cover.
    Each range is inclusive.
    """
    total = 0
    for start, end in merged_ranges:
        total += (end - start + 1)
    return total


def main():
    # Use your specific input path
    file_path = "/Users/abidshakir/Advent-of-Code/2025/Day 05/input.txt"

    ranges = read_ranges(file_path)
    merged_ranges = merge_ranges(ranges)
    result = count_fresh_ids(merged_ranges)

    # Print the result to the terminal
    print(result)


if __name__ == "__main__":
    main()
