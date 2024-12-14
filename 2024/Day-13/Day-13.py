from rich import print

OFFSET = 10000000000000  

def parse_button_line(line):

    line = line.strip()
    _, coords = line.split(":", 1)
    coords = coords.strip()
    x_part, y_part = coords.split(",")
    x_part = x_part.strip()  
    y_part = y_part.strip() 
    Ax = int(x_part[1:])  
    Ay = int(y_part[1:]) 
    return Ax, Ay

def parse_prize_line(line):
    line = line.strip()
    _, coords = line.split(":", 1)
    coords = coords.strip()
    x_part, y_part = coords.split(",")
    x_part = x_part.strip() 
    y_part = y_part.strip() 
    Px = int(x_part[2:])  
    Py = int(y_part[2:])  
    return Px, Py

def min_cost_for_prize_bruteforce(Ax, Ay, Bx, By, Px, Py, max_presses=100):
    # part 1 
    min_cost = None
    for nA in range(max_presses+1):
        for nB in range(max_presses+1):
            if Ax*nA + Bx*nB == Px and Ay*nA + By*nB == Py:
                cost = 3*nA + nB
                if min_cost is None or cost < min_cost:
                    min_cost = cost
    return min_cost

def solve_machine_cramer(Ax, Ay, Bx, By, Px, Py):

    ## part 2 cramer
    Det = Ax*By - Ay*Bx
    if Det == 0:
        return None

    nA_num = Px*By - Py*Bx
    nB_num = Ax*Py - Ay*Px

    if nA_num % Det != 0 or nB_num % Det != 0:
        return None

    nA = nA_num // Det
    nB = nB_num // Det

    if nA < 0 or nB < 0:
        return None

    cost = 3*nA + nB
    return cost

def main():

    with open("/workspaces/Advent-of-Code/2024/Day-13/input.txt", "r") as f:
        raw_lines = [line.strip() for line in f]
    lines = [line for line in raw_lines if line]  

    machines = []
    for i in range(0, len(lines), 3):
        if i+2 < len(lines):
            A_line = lines[i]
            B_line = lines[i+1]
            P_line = lines[i+2]

            Ax, Ay = parse_button_line(A_line)
            Bx, By = parse_button_line(B_line)
            Px, Py = parse_prize_line(P_line)

            machines.append((Ax, Ay, Bx, By, Px, Py))

    costs_part1 = []
    for (Ax, Ay, Bx, By, Px, Py) in machines:
        c = min_cost_for_prize_bruteforce(Ax, Ay, Bx, By, Px, Py, 100)
        if c is not None:
            costs_part1.append(c)
    max_prizes_part1 = len(costs_part1)
    total_cost_part1 = sum(costs_part1)

    costs_part2 = []
    for (Ax, Ay, Bx, By, Px, Py) in machines:
        Px_off = Px + OFFSET
        Py_off = Py + OFFSET
        c = solve_machine_cramer(Ax, Ay, Bx, By, Px_off, Py_off)
        if c is not None:
            costs_part2.append(c)
    max_prizes_part2 = len(costs_part2)
    total_cost_part2 = sum(costs_part2)

    print("Part 1 Results:")
    print(f"The most prizes you can possibly win: {max_prizes_part1}")
    print(f"The fewest tokens to spend to win all these prizes: {total_cost_part1}")

    print("\nPart 2 Results (with 10 trillion offset):")
    print(f"The most prizes you can possibly win: {max_prizes_part2}")
    print(f"The fewest tokens you would have to spend to win all these prizes: {total_cost_part2}")

main()