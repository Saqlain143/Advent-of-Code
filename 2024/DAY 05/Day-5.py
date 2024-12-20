import sys
from collections import defaultdict, Counter, deque
import pyperclip as pc

def pr(s):
    print(s)
    pc.copy(s)

# Set the recursion limit for deep recursion scenarios
sys.setrecursionlimit(10**6)

# Input file path (hardcoded to 'input.txt')
infile = '/Users/abidshakir/Advent-of-Code/2024/DAY 05/input.txt'

# Initialize part 1 and part 2 counters
p1 = 0
p2 = 0

# Read the contents of the input file
D = open(infile).read().strip()

# E[x] is the set of pages that must come before x
# ER[x] is the set of pages that must come after x
E = defaultdict(set)
ER = defaultdict(set)

# Split input into edges and queries sections
edges, queries = D.split('\n\n')

# Process the edges (rules between pages)
for line in edges.split('\n'):
    x, y = line.split('|')
    x, y = int(x), int(y)
    E[y].add(x)  # y depends on x (x must come before y)
    ER[x].add(y) # x must come before y

# Process the queries (the sequences of pages in each update)
for query in queries.split('\n'):
    vs = [int(x) for x in query.split(',')]
    
    # Ensure the number of pages in the query is odd
    assert len(vs) % 2 == 1
    
    ok = True
    
    # Check if the sequence of pages respects the rules
    for i, x in enumerate(vs):
        for j, y in enumerate(vs):
            if i < j and y in E[x]:
                ok = False
    
    # If valid, add the middle page number to part 1
    if ok:
        p1 += vs[len(vs)//2]
    else:
        # Otherwise, determine the correct order of pages
        good = []
        Q = deque([])
        D = {v: len(E[v] & set(vs)) for v in vs}
        
        # Initialize queue with pages that have no prerequisites
        for v in vs:
            if D[v] == 0:
                Q.append(v)
        
        # Perform topological sort using Kahn's algorithm
        while Q:
            x = Q.popleft()
            good.append(x)
            for y in ER[x]:
                if y in D:
                    D[y] -= 1
                    if D[y] == 0:
                        Q.append(y)
        
        # Add the middle page number of the correctly ordered pages to part 2
        p2 += good[len(good)//2]

# Print and copy the results to clipboard
pr(p1)
pr(p2)