import re
from collections import deque


def solve_by_subset(target, button_masks):
    """
    Solve using subset enumeration over buttons (works best when number of buttons is small).
    Each button is either pressed 0 or 1 time (mod 2), so we just try all subsets and
    keep the one with minimal number of presses whose combined effect equals target.
    """
    m = len(button_masks)
    size = 1 << m

    # combined[s] = XOR of all buttons included in subset 's'
    combined = [0] * size
    # if target is 0, pressing nothing is already a solution with cost 0
    best = 0 if target == 0 else None

    for s in range(1, size):
        lsb = s & -s  # least significant bit
        idx = lsb.bit_length() - 1  # which button index
        combined[s] = combined[s ^ lsb] ^ button_masks[idx]

        if combined[s] == target:
            presses = s.bit_count()
            if best is None or presses < best:
                best = presses

    return best


def solve_by_bfs(target, button_masks, n_lights):
    """
    BFS over light configurations. State = bitmask of current lights.
    Start from all-off (0), each edge = press one button (toggle its mask).
    First time we reach target state gives minimal number of presses.
    """
    if target == 0:
        return 0

    max_state = 1 << n_lights
    dist = [-1] * max_state
    q = deque([0])
    dist[0] = 0

    while q:
        state = q.popleft()
        d = dist[state]

        for bm in button_masks:
            ns = state ^ bm
            if dist[ns] == -1:
                dist[ns] = d + 1
                if ns == target:
                    return d + 1
                q.append(ns)

    # If here, target is unreachable (shouldn't happen for valid puzzles).
    return None


def min_presses_for_machine(pattern, button_masks):
    """
    Given pattern string like '.##.#' and list of button bitmasks,
    return minimal number of presses to reach pattern from all-off.
    """
    # Build target bitmask: bit i = 1 if light i should be '#'
    target = 0
    for i, ch in enumerate(pattern):
        if ch == '#':
            target |= 1 << i

    if target == 0:
        return 0

    if not button_masks:
        return None

    m = len(button_masks)
    n = len(pattern)

    # Heuristic: if number of buttons is small, subset enumeration is cheap.
    # Otherwise, if lights are few, BFS on states is better.
    # This should be more than enough for typical Advent of Code constraints.
    if m <= 22 and m <= n:
        ans = solve_by_subset(target, button_masks)
        if ans is not None:
            return ans

    # Fallback / alternative: BFS over light configurations
    ans = solve_by_bfs(target, button_masks, n)
    return ans


def parse_machine_line(line):
    """
    Parse one line of input:
    [.##.] (3) (1,3) (2) ... {jolts...}

    Returns (pattern_string, [button_masks])
    """
    line = line.strip()
    if not line:
        return None

    # Ignore joltage part in {...}
    left = line.split('{', 1)[0].strip()

    # Extract indicator pattern [ .#... ]
    m = re.search(r'\[([.#]+)\]', left)
    if not m:
        return None
    pattern = m.group(1)

    # Extract all button definitions inside parentheses
    after = left[m.end():]
    button_strs = re.findall(r'\(([^()]*)\)', after)

    button_masks = []
    for bs in button_strs:
        bs = bs.strip()
        if not bs:
            continue
        indices = [x for x in bs.split(',') if x.strip() != '']
        mask = 0
        for idx_s in indices:
            idx = int(idx_s)
            mask |= 1 << idx
        button_masks.append(mask)

    return pattern, button_masks


def main():
    # Use your absolute path as requested
    input_path = "/Users/abidshakir/Advent-of-Code/2025/Day 10/input.txt"

    total_presses = 0

    with open(input_path, "r") as f:
        for line in f:
            parsed = parse_machine_line(line)
            if parsed is None:
                continue
            pattern, button_masks = parsed
            presses = min_presses_for_machine(pattern, button_masks)
            if presses is None:
                raise RuntimeError(f"Machine configuration unreachable for line: {line.strip()}")
            total_presses += presses

    # Print final answer in terminal
    print(total_presses)


if __name__ == "__main__":
    main()
