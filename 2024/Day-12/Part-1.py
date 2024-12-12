def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def get_neighbors(x, y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def dfs(x, y, plant_type, grid, visited, rows, cols):
    stack = [(x, y)]
    visited[x][y] = True
    area = 0
    perimeter = 0
    
    while stack:
        cx, cy = stack.pop()
        area += 1
        local_perimeter = 0
        
        for nx, ny in get_neighbors(cx, cy):
            if is_valid(nx, ny, rows, cols):
                if grid[nx][ny] == plant_type and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                elif grid[nx][ny] != plant_type:
                    local_perimeter += 1
            else:
                local_perimeter += 1
        
        perimeter += local_perimeter
    
    return area, perimeter

def calculate_total_cost(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    total_cost = 0
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                plant_type = grid[i][j]
                area, perimeter = dfs(i, j, plant_type, grid, visited, rows, cols)
                total_cost += area * perimeter
    
    return total_cost

def main():
    file_path = '/Users/abidshakir/Advent-of-Code/2024/Day-12/input.txt'
    grid = read_input(file_path)
    total_cost = calculate_total_cost(grid)
    print(total_cost)

if __name__ == '__main__':
    main()
