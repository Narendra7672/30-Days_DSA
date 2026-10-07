# Number of Islands:
def numberOfIslands(grid):
    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    dier = [(1,0),(-1,0),(0,1),(0,-1)] # up,down,right,left
    def bfs(r,c):
        queue = [(r,c)]
        grid[r][c] = '0'
        while queue:
            x,y = queue.pop(0)
            for dx ,dy in dier:
                nx,ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    queue.append((nx,ny))
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                bfs(i,j)
    return count
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
res = numberOfIslands(grid)
print(res) 

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
res1 = numberOfIslands(grid)
print(res1) 
