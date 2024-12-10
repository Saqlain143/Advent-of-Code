from collections import deque
from rich import print

def read_map(file_path):
    """Reads the map from a file and returns it as a 2D grid of integers."""
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def is_valid_move(x, y, rows, cols):
    """Checks if a move is within the bounds of the grid."""
    return 0 <= x < rows and 0 <= y < cols

def bfs(start_x, start_y, grid):
    """Performs BFS to count how many 9s are reachable from a given trailhead."""
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    reachable_9s = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        if grid[x][y] == 9:
            reachable_9s += 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, rows, cols) and not visited[nx][ny]:
                if grid[nx][ny] == grid[x][y] + 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    return reachable_9s

def count_distinct_trails(start_x, start_y, grid):
    """Performs DFS to count the number of distinct trails leading to a 9 from a given trailhead."""
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        if grid[x][y] == 9:
            return 1
        
        visited[x][y] = True
        total_trails = 0
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, rows, cols) and not visited[nx][ny]:
                if grid[nx][ny] == grid[x][y] + 1:
                    total_trails += dfs(nx, ny)
        
        visited[x][y] = False  # Unmark to allow other paths to start here
        return total_trails
    
    return dfs(start_x, start_y)

def find_trailheads(grid):
    """Finds all positions in the grid that have a value of 0 (trailheads)."""
    trailheads = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def main():
    """Main function to read the grid, calculate total score and total rating, and display the results."""
    file_path = '/Users/abidshakir/Advent-of-Code/2024/Day-10/input.txt'
    grid = read_map(file_path)
    
    trailheads = find_trailheads(grid)
    total_score = 0
    total_rating = 0
    
    for trailhead in trailheads:
        x, y = trailhead
        total_score += bfs(x, y, grid)
        total_rating += count_distinct_trails(x, y, grid)
    
    print(f'Total score of all trailheads: {total_score}')
    print(f'Total rating of all trailheads: {total_rating}')

if __name__ == "__main__":
    main()
