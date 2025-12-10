from typing import List, Tuple
import re
import pulp


# -----------------------------
# Proper parser for AoC Day 10
# -----------------------------
def read_input(path: str) -> List[List[str]]:
    machines = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Capture: [pattern]  (buttons...)  {jolts}
            pattern = re.findall(r"\[([.#]+)\]", line)[0]
            buttons = re.findall(r"\(([^()]*)\)", line)
            jolts = re.findall(r"\{([^}]*)\}", line)[0]

            # Create a unified structure similar to user's original input format
            arr = []
            arr.append(f"[{pattern}]")
            for b in buttons:
                arr.append(f"({b})")
            arr.append(f"{{{jolts}}}")

            machines.append(arr)

    return machines


# -----------------------------
# PART 1 - Minimum presses (XOR lights)
# -----------------------------
def calc_min_op(machine: List[str]) -> int:
    pattern = machine[0][1:-1]

    # Convert pattern like .##.# → target bitmask
    target = int(''.join(['1' if c == '#' else '0' for c in pattern[::-1]]), 2)

    seen = {0: 0}

    # Loop over button definitions (skip first and last which is {jolts})
    for btn in machine[1:-1]:
        digits = tuple(map(int, btn[1:-1].split(','))) if btn[1:-1] else ()
        state = 0
        for d in digits:
            state |= (1 << d)

        # XOR BFS-expansion in bitmask space
        for s, step in list(seen.items()):
            new_state = s ^ state
            if new_state not in seen or seen[new_state] > step + 1:
                seen[new_state] = step + 1

    return seen.get(target, -1)


def solve1(data: List[List[str]]) -> int:
    return sum(calc_min_op(line) for line in data)


# -----------------------------
# PART 2 - ILP solution (Joltage increments)
# -----------------------------
def solve_ilp(machine: List[str]) -> int:
    # Extract joltage targets
    target = tuple(map(int, machine[-1][1:-1].split(',')))

    # Extract button -> list of counters
    buttons = []
    for btn in machine[1:-1]:
        if btn[1:-1].strip() == "":
            buttons.append(())
            continue
        buttons.append(tuple(map(int, btn[1:-1].split(','))))

    m = len(target)   # counters
    n = len(buttons)  # buttons

    prob = pulp.LpProblem("MinButtonPress", pulp.LpMinimize)

    # integer variables for each button
    x = [pulp.LpVariable(f"x_{i}", cat="Integer", lowBound=0) for i in range(n)]

    # Objective -> minimize total presses
    prob += pulp.lpSum(x)

    # For each counter: sum(button presses affecting this counter) = target value
    for i in range(m):
        prob += (pulp.lpSum(x[j] for j in range(n) if i in buttons[j]) == target[i])

    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if status != pulp.LpStatusOptimal:
        return -1

    return sum(int(pulp.value(var)) for var in x)


def solve2(data: List[List[str]]) -> int:
    return sum(solve_ilp(machine) for machine in data)


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    input_path = "/Users/abidshakir/Advent-of-Code/2025/Day 10/input.txt"

    input_data = read_input(input_path)

    print("Part 1 (indicator lights):")
    res1 = solve1(input_data)
    print(res1)

    print("Part 2 (joltage ILP):")
    res2 = solve2(input_data)
    print(res2)
